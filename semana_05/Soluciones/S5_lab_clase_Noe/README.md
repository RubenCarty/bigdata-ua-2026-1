# S5 — LABORATORIO DE CLASE: Spark SQL en Acción
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: Consultas Spark SQL sobre datos de Delivery Lima

---

> **Este laboratorio se realiza DURANTE la clase bajo supervisión del docente**
> **Tiempo: 35 minutos | Individual**
> **Herramienta: Databricks Community Edition o Google Colab**

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | NOE PAREDES HILARIO |
| **Código** | 2221895643 |
| **Fecha** | 08/06/2026 |
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
# ============================================================
# CELDA 1: Dataset de pedidos PidelitoApp Lima
# Ejecutar tal cual — no modificar
# ============================================================
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

**PUNTO DE VERIFICACIÓN 1:** ¿Ves "800 pedidos cargados" con 10 columnas? → Continúa.

---

## PASO 2 — Consultas Spark SQL (20 min)

```python
# ============================================================
# CELDA 2: Consulta 1 — Top 5 restaurantes por ingresos
# SQL: SELECT restaurante, COUNT, SUM(monto), AVG(rating)
#      WHERE estado = 'entregado'
#      GROUP BY restaurante
#      ORDER BY ingresos DESC LIMIT 5
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

```python
# ============================================================
# CELDA 3: ▶ TU TURNO — Consulta 2: Demanda por hora
# COMPLETA los ___ para responder:
# "¿A qué hora del día hay más pedidos y mayor ingreso?"
# ============================================================

demanda_hora = spark.sql("""
    SELECT 
        hora,
        COUNT(*)                    AS total_pedidos,
        ROUND(SUM(___), 2)          AS ingresos_hora,
        ROUND(AVG(tiempo_entrega_min), 1) AS tiempo_prom
    FROM pedidos
    WHERE ___ = 'entregado'
    GROUP BY ___
    ORDER BY total_pedidos ___
""")

print("🕐 DEMANDA POR HORA DEL DÍA:")
demanda_hora.show(8)
```

*Pistas:*
- *`SUM(___)` → suma de `monto_soles`*
- *`WHERE ___ = 'entregado'` → el campo `estado`*
- *`GROUP BY ___` → la columna `hora`*
- *`ORDER BY total_pedidos ___` → `DESC` para ordenar de mayor a menor*

---

```python
# ============================================================
# CELDA 4: ▶ TU TURNO — Consulta 3: Repartidores eficientes
# COMPLETA el pipeline para encontrar repartidores con:
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
    WHERE estado = ___
    GROUP BY ___
    HAVING ___ > 10
       AND AVG(tiempo_entrega_min) < ___
       AND AVG(rating) > ___
    ORDER BY rating_prom DESC
""")

print("⚡ REPARTIDORES EFICIENTES (>10 pedidos, tiempo<40min, rating>4.0):")
repartidores_eficientes.show(10)
print(f"Total repartidores que cumplen los criterios: {repartidores_eficientes.count()}")
```

*Pistas:*
- *`WHERE estado = ___` → `'entregado'`*
- *`GROUP BY ___` → `id_repartidor`*
- *`HAVING ___ > 10` → `COUNT(*)`*
- *`tiempo < ___` → `40`*
- *`rating > ___` → `4.0`*

---

## PASO 3 — Pregunta de análisis final (5 min)

```python
# ============================================================
# CELDA 5: Escribe tus respuestas como comentarios Python
# ============================================================

pregunta_1 = """
¿Cuándo hay más pedidos según tu consulta (hora del día)?
¿Coincide con lo que esperabas para Lima? ¿Por qué sí o no?

# Tu respuesta:
"""
Según la consulta de demanda por hora, el pico de pedidos ocurre a las 7:00 AM,
con 55 pedidos y S/ 3,548.36 en ingresos, seguido de cerca por las 15h (51 pedidos),13h (50 pedidos) y 18h (50 pedidos).

Este resultado NO coincide del todo con lo que uno esperaría para un patrón real
de delivery en Lima. Normalmente esperaría dos picos bien marcados y separados:
uno en el almuerzo (12h-14h) y otro en la cena (19h-21h), ya que son los horarios
en que la gente pide comida a domicilio con más frecuencia (oficinas saliendo a
almorzar, familias cenando en casa). Un pico fuerte a las 7am es atípico para
delivery de restaurantes — a esa hora normalmente hay poca demanda, salvo quizás
pedidos de desayuno o café.

La explicación más probable es que el dataset es SINTÉTICO: la columna 'hora' se
generó con np.random.randint(7, 23), es decir, una distribución uniforme entre
las 7am y las 11pm. Con una distribución uniforme y un tamaño de muestra de 800
pedidos repartidos entre 16 horas posibles, es esperable que todas las horas
tengan una cantidad de pedidos similar (45-55 aprox.), y que la hora "ganadora"
sea más bien producto del azar que de un patrón de consumo real.

En un dataset real de delivery en Lima, sí esperaría ver los picos de almuerzo
y cena reflejados claramente, porque responden a hábitos de consumo reales de
la población, no a una generación aleatoria uniforme

pregunta_2 = """
Si la empresa quiere bonificar a los mejores repartidores,
¿cuál de los 3 criterios de la Consulta 3 es el más importante?
Justifica con un argumento de negocio.

# Tu respuesta:
"""
De los tres criterios usados en la Consulta 3 (más de 10 pedidos entregados,
tiempo promedio de entrega < 40 min, y rating > 4.0), el más importante para
efectos de bonificación es el RATING PROMEDIO.

Justificación de negocio:

1. El rating es la métrica que más impacta directamente en el negocio a largo
   plazo. Un cliente satisfecho no solo vuelve a pedir, sino que además
   recomienda la plataforma (boca a boca / reseñas públicas), lo cual es
   clave para que PidelitoApp compita contra Rappi. El volumen de pedidos y
   la velocidad de entrega no sirven de nada si el repartidor maltrata el
   pedido, es descortés o genera una mala experiencia: eso se traduce
   directamente en cancelaciones futuras y pérdida de clientes.

2. El rating es un indicador COMPUESTO: en la práctica, un repartidor con
   rating alto normalmente también entrega a tiempo y de forma consistente,
   porque los usuarios califican mal las entregas tardías, frías o mal
   manipuladas. Es decir, el rating ya "absorbe" parcialmente la información
   de eficiencia en tiempo, mientras que lo inverso no es cierto: un
   repartidor puede ser muy rápido (tiempo bajo) pero descuidado, y aun así
   tener mal rating.

3. El volumen de pedidos (>10) es útil solo como filtro de significancia
   estadística —para asegurarnos de que el promedio de rating y tiempo no
   esté basado en una muestra muy pequeña— pero no debería ser el criterio
   central para bonificar, porque premiar solo el volumen puede incentivar
   a los repartidores a aceptar pedidos de forma apresurada, sacrificando
   calidad de servicio.

4. El tiempo de entrega es importante operativamente, pero es más sensible a
   factores externos que el repartidor no controla del todo (tráfico,
   distancia del restaurante, clima en Lima, etc.), a diferencia del rating,
   que refleja de forma más directa el desempeño y trato del repartidor.

En conclusión, si PidelitoApp tuviera que priorizar UN solo criterio para
bonificar, el rating promedio (>4.0) es el que mejor protege la reputación
de la marca y la retención de clientes a largo plazo, que es en última
instancia lo que determina si la empresa gana o pierde frente a la
competencia como Rappi.


pregunta_3 = """
¿Por qué usamos Spark SQL y no pandas para este análisis?
Da UN argumento técnico específico.

# Tu respuesta:
"""
Usamos Spark SQL en lugar de pandas porque Spark está diseñado para
procesamiento DISTRIBUIDO: los datos se particionan y las operaciones
(GROUP BY, agregaciones, joins) se ejecutan en paralelo across múltiples
nodos/cores, mientras que pandas procesa todo en un solo proceso y
requiere que el dataset completo quepa en la memoria RAM de una sola
máquina.

Para nuestros 800 pedidos esto no se nota, porque es un dataset pequeño y
pandas sería incluso más rápido aquí (Spark tiene overhead de
inicialización del cluster/SparkSession). Pero PidelitoApp, en producción,
manejaría millones de pedidos diarios acumulados a lo largo de meses o años.
En ese escenario, pandas simplemente colapsaría por falta de memoria (un
DataFrame de pandas vive completo en RAM), mientras que Spark puede escalar
horizontalmente agregando más nodos al cluster para procesar terabytes de
datos sin cambiar una sola línea del código SQL.

En resumen: la elección de Spark SQL no es por rendimiento en este dataset
de prueba, sino por ESCALABILIDAD — es la herramienta correcta para el
volumen de datos real que una plataforma de delivery genera en producción.


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
   → Esperar respuestas (con seed=42 y N=800 deberían ser 8-12 repartidores)

2. "¿En qué hora del día concentran más pedidos?"
   → Respuesta esperada: horas 12-13 (almuerzo) y 19-21 (cena)
   → Si alguien dice otra hora: "¿Cambiaste el seed? ¿El WHERE estaba correcto?"

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
3. **Verbalmente:** dice cuál hora tiene más pedidos y por qué tiene sentido para Lima

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Laboratorio de Clase — Ejecutar durante la sesión presencial*
