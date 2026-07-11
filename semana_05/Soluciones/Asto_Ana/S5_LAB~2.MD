# S5 — LABORATORIO DE CLASE: Spark SQL en Acción (RESUELTO)
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: Consultas Spark SQL sobre datos de Delivery Lima

---

> **Este laboratorio se realiza DURANTE la clase bajo supervisión del docente**
> **Tiempo: 35 minutos | Individual**
> **Herramienta: Databricks Community Edition o Google Colab**

> **Nota:** el código fue completado y ejecutado localmente (PySpark 3.5.0) para validar la lógica y mostrar outputs reales, no inventados.

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha** | ______________________________________________ |
| **Herramienta** | Databricks Community / Google Colab |
| **Tiempo** | 35 minutos |

---

## ACCESO AL ENTORNO (2 minutos)

**Databricks:** community.cloud.databricks.com → tu cuenta → New Notebook → Python → nombrar `S5_Lab_Clase`

**Google Colab (si no tienes Databricks activo):**
```python
!pip install pyspark -q
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("S5Clase").getOrCreate()
print(f"✅ Spark {spark.version}")
```

---

## CONTEXTO

Eres analista de datos en **PidelitoApp**, una plataforma de delivery que compite con Rappi en Lima. El Director de Operaciones necesita en 30 minutos un reporte de los 5 mejores restaurantes del mes, las horas de mayor demanda y los repartidores más eficientes.

---

## PASO 1 — Cargar el dataset (5 min)

```python
import numpy as np
from pyspark.sql import functions as F
from pyspark.sql.types import *

np.random.seed(42)
N = 800

restaurantes = ["La Mar", "Tanta", "Astrid & Gastón", "El Hornero",
                "Bembos", "KFC Lima", "Pardos Chicken", "Sushi Pop",
                "Cevichería Isolina", "Pizza Hut Miraflores"]
distritos    = ["Miraflores","San Isidro","Barranco","Surco","San Borja",
                "Los Olivos","Ate","SJL","Callao","Villa El Salvador"]
estados      = ["entregado","entregado","entregado","cancelado","en_camino"]

pedidos = spark.createDataFrame([
    (f"PD{i:06d}",
     np.random.choice(restaurantes),
     np.random.choice(distritos),
     int(np.random.randint(7, 23)),
     float(round(np.random.uniform(18, 120), 2)),
     float(round(np.random.uniform(3, 12), 2)),
     int(np.random.randint(15, 65)),
     float(round(np.random.normal(4.2, 0.5), 1)),
     f"REP{np.random.randint(1,40):03d}",
     str(np.random.choice(estados, p=[.75,.08,.05,.10,.02])))
    for i in range(1, N+1)
], ["id_pedido","restaurante","distrito","hora","monto_soles",
    "costo_delivery","tiempo_entrega_min","rating","id_repartidor","estado"])

pedidos.createOrReplaceTempView("pedidos")
print(f"✅ {pedidos.count()} pedidos cargados")
pedidos.show(3)
```

**Output real obtenido:**
```
✅ 800 pedidos cargados
+---------+--------------+----------+----+-----------+--------------+------------------+------+-------------+---------+
|id_pedido|   restaurante|  distrito|hora|monto_soles|costo_delivery|tiempo_entrega_min|rating|id_repartidor|   estado|
+---------+--------------+----------+----+-----------+--------------+------------------+------+-------------+---------+
| PD000001|Pardos Chicken|     Surco|  19|      36.71|         10.02|                35|   4.1|       REP011|entregado|
| PD000002|        Bembos|     Surco|  14|      90.22|          3.19|                16|   4.1|       REP024|entregado|
| PD000003|      KFC Lima|San Isidro|  22|     119.21|          8.56|                36|   3.0|       REP028|cancelado|
+---------+--------------+----------+----+-----------+--------------+------------------+------+-------------+---------+
```

**PUNTO DE VERIFICACIÓN 1:** ✅ Ves "800 pedidos cargados" con 10 columnas → Continúa.

---

## PASO 2 — Consultas Spark SQL (20 min)

```python
# ============================================================
# CELDA 2: Consulta 1 — Top 5 restaurantes por ingresos
# ============================================================

top_restaurantes = spark.sql("""
    SELECT 
        restaurante,
        COUNT(*)                        AS total_pedidos,
        ROUND(SUM(monto_soles), 2)      AS ingresos_totales,
        ROUND(AVG(rating), 2)           AS rating_prom,
        ROUND(AVG(tiempo_entrega_min),1)AS tiempo_entrega_prom
    FROM pedidos
    WHERE estado = 'entregado'
    GROUP BY restaurante
    ORDER BY ingresos_totales DESC
    LIMIT 5
""")

print("🍽️ TOP 5 RESTAURANTES — INGRESOS DEL MES:")
top_restaurantes.show(truncate=False)
```

**Output real obtenido:**
```
🍽️ TOP 5 RESTAURANTES — INGRESOS DEL MES:
+--------------------+-------------+----------------+-----------+-------------------+
|restaurante         |total_pedidos|ingresos_totales|rating_prom|tiempo_entrega_prom|
+--------------------+-------------+----------------+-----------+-------------------+
|Tanta               |86           |6280.6          |4.28       |37.4               |
|Pardos Chicken      |85           |5702.74         |4.28       |41.6               |
|La Mar              |83           |5643.05         |4.17       |39.1               |
|Pizza Hut Miraflores|81           |5475.86         |4.24       |40.9               |
|KFC Lima            |71           |4793.57         |4.13       |38.1               |
+--------------------+-------------+----------------+-----------+-------------------+
```

```python
# ============================================================
# CELDA 3: Consulta 2 — Demanda por hora (COMPLETADO)
# "¿A qué hora del día hay más pedidos y mayor ingreso?"
# ============================================================

demanda_hora = spark.sql("""
    SELECT 
        hora,
        COUNT(*)                    AS total_pedidos,
        ROUND(SUM(monto_soles), 2)  AS ingresos_hora,
        ROUND(AVG(tiempo_entrega_min), 1) AS tiempo_prom
    FROM pedidos
    WHERE estado = 'entregado'
    GROUP BY hora
    ORDER BY total_pedidos DESC
""")

print("🕐 DEMANDA POR HORA DEL DÍA:")
demanda_hora.show(8)
```

**Output real obtenido:**
```
🕐 DEMANDA POR HORA DEL DÍA:
+----+-------------+-------------+-----------+
|hora|total_pedidos|ingresos_hora|tiempo_prom|
+----+-------------+-------------+-----------+
|   7|           55|      3548.36|       40.6|
|  15|           51|      3303.32|       42.2|
|  13|           50|       3527.5|       40.8|
|  18|           50|       3402.1|       36.7|
|  10|           48|      3399.76|       39.3|
|  19|           47|      3228.09|       39.9|
|  11|           46|      3404.92|       38.4|
|   9|           44|      3061.83|       34.1|
+----+-------------+-------------+-----------+
only showing top 8 rows
```

**Valores usados en los `___`:**
- `SUM(monto_soles)` → suma de `monto_soles`
- `WHERE estado = 'entregado'` → el campo `estado`
- `GROUP BY hora` → la columna `hora`
- `ORDER BY total_pedidos DESC` → de mayor a menor

---

```python
# ============================================================
# CELDA 4: Consulta 3 — Repartidores eficientes (COMPLETADO)
# - Más de 10 pedidos entregados
# - Tiempo promedio de entrega < 40 min
# - Rating > 4.0
# ============================================================

repartidores_eficientes = spark.sql("""
    SELECT
        id_repartidor,
        COUNT(*)                                AS pedidos_entregados,
        ROUND(AVG(tiempo_entrega_min), 1)       AS tiempo_prom,
        ROUND(AVG(rating), 2)                   AS rating_prom,
        ROUND(SUM(costo_delivery), 2)           AS ingresos_delivery
    FROM pedidos
    WHERE estado = 'entregado'
    GROUP BY id_repartidor
    HAVING COUNT(*) > 10
       AND AVG(tiempo_entrega_min) < 40
       AND AVG(rating) > 4.0
    ORDER BY rating_prom DESC
""")

print("⚡ REPARTIDORES EFICIENTES (>10 pedidos, tiempo<40min, rating>4.0):")
repartidores_eficientes.show(10)
print(f"Total repartidores que cumplen los criterios: {repartidores_eficientes.count()}")
```

**Output real obtenido:**
```
⚡ REPARTIDORES EFICIENTES (>10 pedidos, tiempo<40min, rating>4.0):
+-------------+------------------+-----------+-----------+-----------------+
|id_repartidor|pedidos_entregados|tiempo_prom|rating_prom|ingresos_delivery|
+-------------+------------------+-----------+-----------+-----------------+
|       REP037|                17|       39.6|       4.43|           123.73|
|       REP031|                14|       38.1|       4.39|            96.85|
|       REP022|                12|       39.8|       4.38|           107.65|
|       REP016|                14|       39.5|       4.36|            95.27|
|       REP004|                22|       38.4|        4.3|           162.79|
|       REP029|                23|       34.0|       4.29|           163.63|
|       REP014|                16|       35.3|       4.29|           120.01|
|       REP034|                17|       39.5|       4.27|            149.4|
|       REP015|                14|       37.8|       4.27|            86.35|
|       REP008|                15|       37.5|       4.26|           109.52|
+-------------+------------------+-----------+-----------+-----------------+
only showing top 10 rows

Total repartidores que cumplen los criterios: 23
```

**Valores usados en los `___`:**
- `WHERE estado = 'entregado'`
- `GROUP BY id_repartidor`
- `HAVING COUNT(*) > 10`
- `AVG(tiempo_entrega_min) < 40`
- `AVG(rating) > 4.0`

> **Nota:** el enunciado sugiere "8-12 repartidores" como referencia aproximada del docente; con la ejecución real (seed=42, N=800) el resultado correcto y verificado es **23 repartidores** que cumplen los tres criterios simultáneamente. Es un buen punto para comentar en clase: la cifra de referencia era una estimación, no un valor exacto a reproducir — lo que importa es que la lógica (WHERE antes de agrupar, HAVING después) esté bien aplicada.

---

## PASO 3 — Pregunta de análisis final (5 min)

```python
pregunta_1 = """
¿Cuándo hay más pedidos según tu consulta (hora del día)?
¿Coincide con lo que esperabas para Lima? ¿Por qué sí o no?

# Tu respuesta:
Según la consulta, la hora con más pedidos es las 7am (55 pedidos), seguida de
15h (51), 13h (50) y 18h (50). Esto NO coincide del todo con lo esperado para
Lima, donde normalmente se esperarían picos claros en horario de almuerzo
(12-14h) y cena (19-21h). La razón técnica es que la columna "hora" se generó
con np.random.randint(7, 23) — una distribución uniforme entre las 7am y las
10pm — por lo que ninguna hora tiene más probabilidad que otra de aparecer; las
pequeñas diferencias de conteo (44 a 55) son solo ruido estadístico de una
muestra de 800 filas, no un patrón real de demanda. Si el dataset quisiera
reflejar el comportamiento real de Lima, la hora debería generarse con una
distribución no uniforme (p. ej. mezcla de normales centradas en 13h y 20h),
igual que se hizo con "turno" en el lab de taxis usando probabilidades p=[...].
"""

pregunta_2 = """
Si la empresa quiere bonificar a los mejores repartidores,
¿cuál de los 3 criterios de la Consulta 3 es el más importante?
Justifica con un argumento de negocio.

# Tu respuesta:
El más importante es el rating promedio (> 4.0), porque es el único criterio
que refleja directamente la satisfacción del cliente final, que es lo que
retiene usuarios y genera repetición de compra en la app. El volumen de
pedidos (> 10) puede inflarse simplemente por estar más horas conectado, y el
tiempo de entrega (< 40 min) depende en parte de factores externos (tráfico,
distancia del restaurante) que no siempre son responsabilidad del repartidor.
Un repartidor con rating alto sostenido está haciendo bien lo que más impacta
al negocio — experiencia del cliente — independientemente de cuántos pedidos
tome o de las condiciones de tráfico de ese día.
"""

pregunta_3 = """
¿Por qué usamos Spark SQL y no pandas para este análisis?
Da UN argumento técnico específico.

# Tu respuesta:
Porque Spark distribuye el cómputo entre varios nodos/cores y procesa los datos
de forma perezosa (lazy evaluation) con un optimizador de consultas (Catalyst)
que decide el plan de ejecución más eficiente antes de correrlo; pandas carga
todo el dataset en memoria de un solo proceso y ejecuta cada operación de
inmediato. Con 800 filas la diferencia es imperceptible, pero el mismo GROUP BY
+ HAVING escala sin cambios de código a millones o miles de millones de
registros distribuidos en un clúster, mientras que pandas eventualmente se
queda sin memoria RAM de una sola máquina.
"""

print("✅ Respuestas registradas")
print(pregunta_1)
print(pregunta_2)
print(pregunta_3)
```

---

## ROL DEL DOCENTE DURANTE EL LABORATORIO

### Qué observar al circular:

| Señal positiva | Señal de alerta | Acción |
|----------------|-----------------|--------|
| "800 pedidos cargados" en Celda 1 | Error de sintaxis en Celda 1 | "¿Ejecutaste primero la celda de instalación de PySpark (si es Colab)?" |
| Top 5 restaurantes con ingresos > S/1,000 | Tabla vacía en Consulta 1 | "¿El WHERE dice `'entregado'` con comillas simples? Python distingue `True` de `'True'`" |
| Los `___` de Celda 3 reemplazados correctamente | No sabe qué va en los `___` | "¿Qué columna quieres sumar para los ingresos por hora? ¿Y qué filtro garantiza que son pedidos válidos?" |
| HAVING usado correctamente (no WHERE) | Usa WHERE en lugar de HAVING para el conteo | "WHERE filtra ANTES de agrupar. HAVING filtra DESPUÉS. ¿Cuándo sabes si un repartidor tiene más de 10 pedidos — antes o después de contar?" |
| Respuestas de análisis con argumento propio | Copia respuestas de un compañero | Pedir que explique con su propio ejemplo de la app |

### Preguntas de andamiaje:

- *"¿Por qué en la Consulta 3 usamos HAVING y no WHERE para el COUNT(*) > 10?"* → HAVING opera sobre grupos ya formados; WHERE opera antes del GROUP BY
- *"Si quisieras agregar también las cancelaciones al reporte, ¿qué cambiarías en el WHERE?"* → Eliminar el filtro o agregar `OR estado = 'cancelado'`
- *"¿Qué diferencia hay entre `AVG(rating)` en el SELECT y `AVG(rating)` en el HAVING?"* → En SELECT lo muestra; en HAVING lo usa para filtrar — pueden escribirse una sola vez con alias: `SELECT AVG(rating) AS r ... HAVING r > 4.0`

### Señales de comprensión vs. no comprensión:

**Entendió:** Puede explicar *"HAVING filtra después de GROUP BY, por eso COUNT(*) funciona ahí"*

**No entendió:** Copia los `___` de otra celda sin adaptarlos / no puede decir por qué su query devuelve 0 filas

### Cierre (5 min):

```
1. "¿Cuántos encontraron más de 5 repartidores eficientes?"
   → Con seed=42 y N=800, la ejecución real da 23 repartidores.

2. "¿En qué hora del día concentran más pedidos?"
   → Con este dataset sintético (hora generada uniforme entre 7-22h) el resultado
     es prácticamente parejo (44-55 pedidos/hora); no hay un pico real de
     almuerzo/cena porque la generación de datos no lo modela.

3. Conexión con laboratorio en casa:
   "Lo que hicieron aquí en 35 minutos sobre 800 pedidos,
   en el laboratorio en casa lo harán con 10,000 viajes de taxi.
   La lógica es la misma — la escala es mayor."
```

---

## ENTREGABLE EN CLASE

El estudiante muestra al docente al finalizar los 35 minutos:

1. **Pantalla:** 5 celdas ejecutadas sin errores
2. **La tabla de repartidores eficientes** impresa en pantalla
3. **Verbalmente:** dice cuál hora tiene más pedidos y por qué tiene sentido para Lima (o explica, como en la pregunta 1, por qué el dataset sintético no reproduce el patrón esperado)

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Laboratorio de Clase — Resuelto y verificado con ejecución real (PySpark 3.5.0 local)*
