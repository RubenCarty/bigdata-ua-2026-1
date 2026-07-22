---
---

<div style="text-align: center; padding: 15px 0; border-bottom: 3px solid #bd4804; margin-bottom: 20px;">

**<span style="font-size: 1.3em; color: #bd4804;">UNIVERSIDAD AUTÓNOMA DEL PERÚ</span>**  
**<span style="font-size: 1.1em; color: #bd4804;">FACULTAD DE INGENIERÍA Y ARQUITECTURA</span>**  
**<span style="font-size: 1.0em; color: #bd4804;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS COMPUTACIONALES</span>**

</div>

# EVALUACIÓN PARCIAL — BIG DATA

**Código: DD283 | Ciclo VIII | Semestre 2026-1**

**CÓDIGO DEL ESTUDIANTE:** 2221895373  
**NÚMERO DE CLASE:** EXAMEN PARCIAL  
**APELLIDOS Y NOMBRES:** LEON AGUILAR DALIA NANCY  
**FECHA ENTREGA:** 27 JUN 2026  
**DOCENTE:** Mg. Rubén Quispe Llacctarimay  
**Modalidad:** Implementación + Video  

---

## INSTRUCCIONES GENERALES

| Ítem | Detalle |
|------|---------|
| **Duración** | 48 horas desde que el docente comparte este documento |
| **Modalidad** | Individual — implementación real en software + video de sustentación |
| **IA permitida** | **Sí** — puedes usar ChatGPT, Claude, Gemini, GitHub Copilot para asistirte en el código. Sin embargo, debes **entender, modificar y ejecutar** lo que el sistema genere. El video evidenciará tu comprensión. |
| **Entregable** | Enlace de repositorio GitHub (PR a la rama `semana_04`) + enlace de video |
| **Herramientas obligatorias** | Databricks Community Edition · MongoDB Atlas M0 · Docker Desktop |

---

> **Sobre el uso de IA:** Usar IA para generar código es válido y profesional. Lo que se evalúa es que:
> (a) el código funcione en las herramientas indicadas con **output real visible**,
> (b) puedas **explicar verbalmente** en el video cada decisión técnica, y
> (c) hayas **adaptado el código** al caso específico de este examen, no copiado una respuesta genérica.
---

# EVALUACIÓN PARCIAL — BIG DATA
## Código: DD283 | Ciclo VIII | Semestre 2026-1

---

| **CÓDIGO DEL ESTUDIANTE:** |  2221895373 | **NÚMERO DE CLASE:** | EXAMEN PARCIAL|
|---|---|---|---|
| **APELLIDOS Y NOMBRES:** | LEON AGUILAR  DALIA NANCY | **FECHA ENTREGA:** |27 JUN 2026 |
| **DOCENTE:** | **Mg. Rubén Quispe Llacctarimay** | **Modalidad:** | **Implementación + Video** |

---
---
Link videos: https://drive.google.com/drive/folders/1u9h9lw0M3LSVGHb3U0OOIZdjrQ1CzRJr

Link repositorio: https://github.com/leondalar12-ux/yape-leon-dalia.git
---
---
## INSTRUCCIONES GENERALES

| Ítem | Detalle |
|------|---------|
| **Duración** | 48 horas desde que el docente comparte este documento |
| **Modalidad** | Individual — implementación real en software + video de sustentación |
| **IA permitida** | **Sí** — puedes usar ChatGPT, Claude, Gemini, GitHub Copilot para asistirte en el código. Sin embargo, debes **entender, modificar y ejecutar** lo que el sistema genere. El video evidenciará tu comprensión. |
| **Entregable** | Enlace de repositorio GitHub (PR a la rama `semana_04`) + enlace de video |
| **Herramientas obligatorias** | Databricks Community Edition · MongoDB Atlas M0 · Docker Desktop |

---

> **Sobre el uso de IA:** Usar IA para generar código es válido y profesional. Lo que se evalúa es que:
> (a) el código funcione en las herramientas indicadas con **output real visible**,
> (b) puedas **explicar verbalmente** en el video cada decisión técnica, y
> (c) hayas **adaptado el código** al caso específico de este examen, no copiado una respuesta genérica.

---

## CASO BASE: YAPE — Sistema de Pagos Digitales

**Yape** (BCP) es la fintech más grande de Perú:

| Indicador | Dato 2025 |
|-----------|-----------|
| Usuarios activos | 15 millones |
| Transacciones diarias | 3.2 millones |
| Comerciantes afiliados | 1.3 millones |
| TPS en hora pico | 450 transacciones/segundo |
| Historial acumulado | ~18 TB/año |
| Tipos de comercio | Bodega, restaurante, farmacia, taxi, empresa, ONG |

**Problema:** El sistema Oracle actual demora 45 segundos en cargar el historial de un usuario. El equipo de Data Engineering necesita rediseñar la arquitectura con Big Data tools. Tú eres parte de ese equipo.

---

## PARTE A — DISEÑO Y ARQUITECTURA (4 puntos)
### *Puedes usar IA generativa en esta sección — cita qué herramienta usaste*

### Diagrama 1 — Flujo de datos (arquitectura completa)

```mermaid
flowchart TD
    A1[Pagos Yape\n450 TPS pico] --> B1
    A2[Comerciantes\n1.3M afiliados] --> B2
    A3[Sesiones\n15M usuarios] --> B3
    A4[Eventos fraude\nReal-time] --> B4

    B1[Delta Lake + Databricks\nPipeline Medallion] --> C1
    B2[MongoDB\nPerfiles flexibles] --> C2
    B3[Redis\nSesiones TTL 30min] --> C3
    B4[Apache Flink\nStreaming fraude] --> C4

    C1 --> D1[Bronze\nDatos crudos]
    D1 --> D2[Silver\nDatos limpios]
    D2 --> D3[Gold\nMétricas negocio]

    C2 --> E1[Equipo comercial\nReporte comerciantes]
    C3 --> E2[App Yape\nLogin rápido]
    C4 --> E3[Seguridad\nAlertas fraude]
    D3 --> E4[Power BI\nDashboard ejecutivo]

    style A1 fill:#F0997B,color:#712B13
    style A2 fill:#F0997B,color:#712B13
    style A3 fill:#F0997B,color:#712B13
    style A4 fill:#F0997B,color:#712B13
    style B1 fill:#85B7EB,color:#042C53
    style B2 fill:#5DCAA5,color:#04342C
    style B3 fill:#5DCAA5,color:#04342C
    style B4 fill:#ED93B1,color:#4B1528
    style D1 fill:#FAC775,color:#412402
    style D2 fill:#EF9F27,color:#412402
    style D3 fill:#BA7517,color:#FAEEDA
    style E4 fill:#97C459,color:#173404
```

---

### Diagrama 2 — Arquitectura por capas (Medallion)

```mermaid
flowchart LR
    subgraph FUENTES["Fuentes de datos"]
        F1[Transacciones\nYape]
        F2[Usuarios\n15M]
        F3[Comerciantes\n1.3M]
    end

    subgraph BRONZE["Bronze Layer — Datos crudos"]
        B[Parquet raw\n2000+ registros/hora]
    end

    subgraph SILVER["Silver Layer — Datos limpios"]
        S1[Filtro: solo completadas]
        S2[Categoría monto]
        S3[Hora pico]
        S4[Comisión Yape 1.5%]
    end

    subgraph GOLD["Gold Layer — Métricas negocio"]
        G1[Top 5 distritos\nvolumen]
        G2[Ingresos por hora\ncomisiones]
    end

    subgraph CONSUMO["Consumidores"]
        C1[Power BI\nDashboard]
        C2[App Yape\nHistorial]
    end

    FUENTES --> BRONZE
    BRONZE --> SILVER
    SILVER --> GOLD
    GOLD --> CONSUMO

    style BRONZE fill:#FAC775,color:#412402
    style SILVER fill:#85B7EB,color:#042C53
    style GOLD fill:#97C459,color:#173404
```

---


---

### PREGUNTA 1 — Arquitectura Big Data de Yape (4 puntos)

**1.1 (2 pts) — Tabla de arquitectura:**

Diseña la arquitectura completa de datos para Yape. Para cada componente del sistema, elige la tecnología adecuada y justifica. Puedes usar IA para explorar opciones, pero la justificación debe ser tuya.

| Componente del sistema | Tecnología elegida | Tipo BD/Herramienta | Por qué esta tecnología para Yape (2 líneas) |
|------------------------|-------------------|--------------------|--------------------------------------------|
| Core de pagos (3.2M transacciones/día, no puede perder dinero) | CockroachDB | NewSQL distribuido | Mantiene ACID en múltiples regiones y escala horizontalmente para procesar 450 TPS sin perder consistencia en transacciones financieras críticas. |
| Sesiones de login activo (15M usuarios, expira en 30 min) | Redis | In-memory store | Proporciona acceso sub-milisegundo a 15M sesiones con expiración automática TTL, ideal para gestionar tokens y sesiones de usuarios. |
| Perfil del comerciante (bodega, restaurante, taxi — atributos distintos) | MongoDB | Documental NoSQL | Esquema flexible que permite almacenar atributos variables (bodega, restaurante, taxi) sin columnas NULL, adaptándose a la diversidad de comerciantes. |
| Historial de transacciones para análisis (18 TB/año) | Delta Lake + Databricks | Data Lakehouse | Combina almacenamiento económico en la nube con capacidades ACID y procesamiento distribuido, manejando 18TB/año con queries rápidos. |
| Red de detección de fraude (ciclo A→B→C→A en < 5 min) | Apache Flink | Streaming real-time | Procesa flujos de eventos en <5 minutos con ventanas temporales, detectando patrones A→B→C→A en tiempo real. |
| Dashboard ejecutivo (top 10 distritos, actualización diaria) | Power BI / Tableau | BI Visualización | Conexión directa a datos agregados en Gold layer, actualizaciones diarias programadas con visualizaciones intuitivas. |

---

**1.2 (1 pt) — Teorema CAP:**

Para los siguientes 2 componentes de Yape, indica la combinación CAP correcta (CP, AP o CA) y explica qué propiedad sacrifica y por qué ese sacrificio es aceptable o inaceptable:

| Componente | Combinación CAP | Propiedad sacrificada | ¿Por qué ese sacrificio es correcto o incorrecto para este caso? |
|------------|----------------|----------------------|----------------------------------------------------------------|
| Core de pagos (débito/crédito de saldos) | **CP** | Disponibilidad parcial | Correcto porque la consistencia es crítica en finanzas; si hay partición, es mejor rechazar operaciones que permitir transacciones inconsistentes que afecten saldos de los usuarios. |
| Historial "mis últimas 50 transacciones" | **AP** | Consistencia fuerte | Correcto porque los usuarios aceptan ver historial con pocos segundos de retraso (eventual consistency) a cambio de disponibilidad del servicio 24/7. |

---

**1.3 (1 pt) — NewSQL:**

El equipo de Yape evalúa migrar el core de pagos a **CockroachDB** (NewSQL). Responde:

a) ¿Qué limitación de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?
    CockroachDB resuelve la limitación de escalado horizontal de Oracle al permitir agregar nodos automáticamente sin reconfiguración manual, soportando de 15M a 50M usuarios sin caídas de rendimiento.

b) ¿Por qué MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque también escala horizontalmente?
    MongoDB NO puede reemplazar a Oracle para pagos porque carece de transacciones ACID multi-documento nativas hasta versiones recientes y no ofrece garantías de atomicidad en operaciones de débito/crédito críticas.

c) ¿Qué mecanismo técnico usa CockroachDB para mantener ACID en múltiples nodos distribuidos? (1 término técnico es suficiente)
    CockroachDB utiliza el protocolo de consenso **RAFT** para mantener ACID en nodos distribuidos.

---

## PARTE B — DATABRICKS COMMUNITY EDITION (6 puntos)
### *Implementación obligatoria — evidencia en video y screenshot de outputs*

### VIDEO : 

---

### PREGUNTA 2 — Pipeline de Transacciones Yape en Databricks (6 puntos)

**Contexto:** El equipo de Data Engineering de Yape necesita un pipeline que procese el historial de transacciones diarias. Debes implementarlo en **Databricks Community Edition** usando la arquitectura medallion (Bronze → Silver → Gold).

**Acceso:** [community.cloud.databricks.com](https://community.cloud.databricks.com) | Gratis | Sin tarjeta de crédito

---

**CELDA 1 — Generación del dataset (ya escrita, ejecutar tal cual):**

```python
# ============================================================
# CELDA 1: Dataset sintético — 2,000 transacciones Yape
# ============================================================
import numpy as np
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.types import *
np.random.seed(42)

n = 2000
distritos = ["Miraflores", "San Isidro", "SJL", "Comas", "Villa El Salvador",
             "Los Olivos", "Surco", "Ate", "Callao", "Independencia"]
tipos     = ["persona_a_persona", "persona_a_comercio", "retiro_bcp", "recarga"]
estados   = ["completada", "completada", "completada", "rechazada", "pendiente"]

data = {
    "id_transaccion": [f"YP{i:07d}" for i in range(1, n+1)],
    "fecha":          pd.date_range("2025-01-01", periods=n, freq="1h").strftime("%Y-%m-%d").tolist(),
    "hora":           [f"{h:02d}:{m:02d}" for h, m in zip(np.random.randint(0,24,n), np.random.randint(0,60,n))],
    "monto_soles":    np.round(np.random.exponential(45, n), 2).tolist(),
    "tipo":           np.random.choice(tipos, n).tolist(),
    "distrito_origen":np.random.choice(distritos, n).tolist(),
    "estado":         np.random.choice(estados, n, p=[0.75, 0.1, 0.05, 0.07, 0.03]).tolist(),
    "id_usuario":     [f"USR{np.random.randint(1000,9999)}" for _ in range(n)],
    "es_comercio":    np.random.choice([True, False], n, p=[0.4, 0.6]).tolist()
}

df_pandas = pd.DataFrame(data)
df_bronze = spark.createDataFrame(df_pandas)
df_bronze.write.mode("overwrite").parquet("/FileStore/yape/bronze/transacciones")

print(f"✅ Bronze layer: {df_bronze.count()} transacciones guardadas")
df_bronze.show(5)
```

---

**CELDA 2 — Silver layer: limpiar y enriquecer (completar los `___`):**

```python
# ============================================================
# CELDA 2: Silver — limpiar y transformar
# COMPLETA los ___ según las instrucciones en los comentarios
# ============================================================
df_bronze = spark.read.parquet("/FileStore/yape/bronze/transacciones")

df_silver = df_bronze \
    .filter(df_bronze.estado == ___) \
    .filter(df_bronze.monto_soles > ___) \
    .withColumn("categoria_monto",
        F.when(F.col("monto_soles") < 20, "micro")
         .when(F.col("monto_soles") < 100, "medio")
         .otherwise(___)) \
    .withColumn("es_hora_pico",
        F.when(F.col("hora").between("12:00", "14:00"), True)
         .when(F.col("hora").between("18:00", ___), True)
         .otherwise(False)) \
    .withColumn("comision_yape",
        F.when(F.col("tipo") == "persona_a_comercio",
               F.round(F.col("monto_soles") * ___, 2))
         .otherwise(0.0))

df_silver.write.mode("overwrite").parquet("/FileStore/yape/silver/transacciones_limpias")

print(f"✅ Silver layer: {df_silver.count()} transacciones válidas")
print(f"   Eliminadas: {df_bronze.count() - df_silver.count()} (rechazadas/pendientes/monto cero)")
df_silver.groupBy("categoria_monto").count().show()
```

*Pistas para los `___`:*
- *`estado ==` → solo transacciones "completadas"*
- *`monto_soles >` → mayor a 0*
- *`otherwise` en categoría → "alto" (más de S/100)*
- *`between` hora tarde → "22:00"*
- *`comision_yape` → Yape cobra 1.5% a comercios: `0.015`*

---

**CELDA 3 — Gold layer: métricas de negocio (completar los `___`):**

```python
# ============================================================
# CELDA 3: Gold — agregaciones para el dashboard ejecutivo
# COMPLETA los ___ 
# ============================================================
df_silver = spark.read.parquet("/FileStore/yape/silver/transacciones_limpias")
df_silver.createOrReplaceTempView("transacciones")

# Gold 1: Top 5 distritos por volumen de transacciones
gold_distritos = spark.sql("""
    SELECT 
        distrito_origen,
        COUNT(*)                          AS total_transacciones,
        ROUND(SUM(monto_soles), 2)        AS volumen_total_soles,
        ROUND(AVG(monto_soles), 2)        AS ticket_promedio,
        SUM(CASE WHEN es_comercio THEN ___ ELSE 0 END) AS transacciones_comercio
    FROM transacciones
    GROUP BY ___
    ORDER BY ___ DESC
    LIMIT 5
""")

# Gold 2: Ingresos Yape por hora del día (comisiones de comercios)
gold_comisiones = spark.sql("""
    SELECT
        SUBSTRING(hora, 1, 2)             AS hora_dia,
        COUNT(*)                          AS num_transacciones,
        ROUND(SUM(comision_yape), 2)      AS ingresos_yape_soles
    FROM transacciones
    WHERE ___
    GROUP BY SUBSTRING(hora, 1, 2)
    ORDER BY ingresos_yape_soles DESC
""")

gold_distritos.write.mode("overwrite").parquet("/FileStore/yape/gold/top_distritos")
gold_comisiones.write.mode("overwrite").parquet("/FileStore/yape/gold/ingresos_por_hora")

print("📊 TOP 5 DISTRITOS POR VOLUMEN YAPE:")
gold_distritos.show()

print("💰 INGRESOS YAPE POR HORA (comisión comercios):")
gold_comisiones.show(5)
```

*Pistas para los `___`:*
- *`SUM(CASE WHEN es_comercio THEN ___ ELSE 0 END)` → contar con `1`*
- *`GROUP BY ___` → el campo de distrito*
- *`ORDER BY ___ DESC` → el campo de total de transacciones*
- *`WHERE ___` → solo donde la comisión es mayor a 0*

---

**CELDA 4 — Visualización (ya escrita, ejecutar tal cual):**

```python
# ============================================================
# CELDA 4: Visualización — gráfico de barras con matplotlib
# ============================================================
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

gold_distritos = spark.read.parquet("/FileStore/yape/gold/top_distritos").toPandas()
gold_comisiones = spark.read.parquet("/FileStore/yape/gold/ingresos_por_hora").toPandas()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Dashboard Ejecutivo YAPE — Análisis de Transacciones", fontsize=14, fontweight='bold')

# Gráfico 1: Top 5 distritos
axes[0].barh(gold_distritos["distrito_origen"], gold_distritos["volumen_total_soles"],
             color=["#c41230","#e63950","#f47a8a","#f9b4bc","#fde8ea"])
axes[0].set_xlabel("Volumen total (S/)")
axes[0].set_title("Top 5 Distritos — Volumen de Pagos")
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"S/{x:,.0f}"))

# Gráfico 2: Ingresos Yape por hora
gold_comisiones_sorted = gold_comisiones.sort_values("hora_dia")
axes[1].plot(gold_comisiones_sorted["hora_dia"], gold_comisiones_sorted["ingresos_yape_soles"],
             marker='o', color='#c41230', linewidth=2)
axes[1].fill_between(gold_comisiones_sorted["hora_dia"], gold_comisiones_sorted["ingresos_yape_soles"],
                     alpha=0.15, color='#c41230')
axes[1].set_xlabel("Hora del día")
axes[1].set_ylabel("Comisión recaudada (S/)")
axes[1].set_title("Ingresos Yape por Hora")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("/dbfs/FileStore/yape/gold/dashboard_yape.png", dpi=150, bbox_inches='tight')
plt.show()

print("✅ Dashboard guardado en /FileStore/yape/gold/dashboard_yape.png")
```

---

**Entregable Parte B:**
- Screenshot del notebook completo con las 4 celdas ejecutadas (outputs visibles)
- En el video (P5): explicar qué hace la arquitectura Medallion y mostrar el dashboard generado

---

## PARTE C — MONGODB ATLAS (5 puntos)
### *Implementación obligatoria en Atlas M0 — evidencia en screenshot y video*

---

### PREGUNTA 3 — Base de Datos NoSQL de Comerciantes Yape en Atlas (5 puntos)

**Acceso:** [mongodb.com/atlas](https://mongodb.com/atlas) → Create free account → M0 Free Tier (AWS São Paulo)

---

**PASO 1 — Conectar a Atlas desde Google Colab o tu local (ejecutar primero):**

```python
# ============================================================
# INSTALACIÓN (en Google Colab: ejecutar con !)
# ============================================================
# !pip install pymongo dnspython -q

from pymongo import MongoClient
import json

# REEMPLAZA con tu connection string de Atlas:
# Atlas → Connect → Drivers → Python → copia el string
CONNECTION_STRING = "mongodb+srv://<usuario>:<password>@<cluster>.mongodb.net/"

client = MongoClient(CONNECTION_STRING)
db = client["yape_db"]
comerciantes = db["comerciantes"]
print("✅ Conectado a MongoDB Atlas")
print(f"   DB: {db.name} | Colección: {comerciantes.name}")
```

---

**PASO 2 — Insertar 5 comerciantes con esquemas distintos (3.1 — 2 pts):**

Inserta los siguientes 5 documentos. Observa que **cada uno tiene campos únicos** — esto es imposible en SQL sin columnas NULL masivas.

```python
# ============================================================
# INSERTAR 5 COMERCIANTES CON ESTRUCTURA FLEXIBLE
# ============================================================

lista_comerciantes = [
    {
        "ruc": "10456789012",
        "nombre_comercio": "Bodega La Esquina de Don Mario",
        "tipo": "bodega",
        "propietario": "Mario Quispe Condori",
        "distrito": "San Juan de Lurigancho",
        "departamento": "Lima",
        "calificacion": 4.2,
        "yape_activo": True,
        "monto_mensual_soles": 4500.00,
        "categorias": ["abarrotes", "bebidas", "snacks"],   # Array
        "horario": {"apertura": "06:00", "cierre": "22:00"},# Objeto anidado
        "acepta_delivery": False
        # NO tiene: carta, capacidad_mesas, num_empleados
    },
    {
        "ruc": "20512345678",
        "nombre_comercio": "Cevichería El Muelle SAC",
        "tipo": "restaurante",
        "representante_legal": "Ana Flores Rojas",
        "distrito": "Miraflores",
        "departamento": "Lima",
        "calificacion": 4.8,
        "yape_activo": True,
        "monto_mensual_soles": 28000.00,
        "carta": [                                           # Array de objetos
            {"plato": "Ceviche clásico", "precio": 28.00},
            {"plato": "Leche de tigre",  "precio": 18.00},
            {"plato": "Tiradito",        "precio": 32.00}
        ],
        "capacidad_mesas": 45,
        "num_empleados": 12,
        "horario": {"apertura": "12:00", "cierre": "17:00"},
        "acepta_delivery": True,
        "plataformas_delivery": ["Rappi", "PedidosYa"]
        # NO tiene: categorias, acepta_tarjeta_fisica
    },
    {
        "ruc": "10789012345",
        "nombre_comercio": "Farmacia San Pablo Express",
        "tipo": "farmacia",
        "propietario": "Carlos Mendoza Ríos",
        "distrito": "Los Olivos",
        "departamento": "Lima",
        "calificacion": 4.5,
        "yape_activo": True,
        "monto_mensual_soles": 12000.00,
        "productos_destacados": ["paracetamol", "ibuprofeno", "vitaminas"],
        "horario": {"apertura": "07:00", "cierre": "23:00"},
        "venta_con_receta": True,
        "codigo_digemid": "F-2023-00456",  # Campo único de farmacias
        "acepta_delivery": True
    },
    {
        "ruc": "10234567891",
        "nombre_comercio": "Taxi Express — Luis Tapia",
        "tipo": "taxi",
        "propietario": "Luis Tapia Salcedo",
        "distrito": "Callao",
        "departamento": "Lima",
        "calificacion": 4.0,
        "yape_activo": True,
        "monto_mensual_soles": 3200.00,
        "vehiculo": {                        # Objeto único de taxis
            "placa": "ABC-123",
            "modelo": "Toyota Yaris 2022",
            "capacidad": 4
        },
        "zonas_cobertura": ["Callao", "Bellavista", "La Perla", "Miraflores"],
        "acepta_delivery": False
    },
    {
        "ruc": "20987654321",
        "nombre_comercio": "Distribuidora Norte SAC",
        "tipo": "empresa",
        "representante_legal": "Patricia Luna Torres",
        "distrito": "Independencia",
        "departamento": "Lima",
        "calificacion": 3.9,
        "yape_activo": True,
        "monto_mensual_soles": 85000.00,
        "num_empleados": 45,
        "sectores": ["abarrotes", "limpieza", "bebidas"],
        "clientes_mayoristas": 230,
        "horario": {"apertura": "08:00", "cierre": "18:00"},
        "acepta_delivery": True,
        "zonas_despacho": ["Lima Norte", "Lima Centro"]
    }
]

resultado = comerciantes.insert_many(lista_comerciantes)
print(f"✅ {len(resultado.inserted_ids)} comerciantes insertados en Atlas")
for i, id_ in enumerate(resultado.inserted_ids):
    print(f"   {lista_comerciantes[i]['tipo'].upper()}: {id_}")
```

---

**PASO 3 — Queries con filtros (3.2 — 1.5 pts):**

```python
# ============================================================
# CONSULTAS CON OPERADORES MONGODB
# ============================================================

print("="*55)
print("CONSULTA 1: Comerciantes premium (calificación > 4.3 y activos)")
premium = list(comerciantes.find(
    {"calificacion": {"$gt": 4.3}, "yape_activo": True},
    {"nombre_comercio": 1, "tipo": 1, "calificacion": 1, "_id": 0}
).sort("calificacion", -1))
for c in premium:
    print(f"  ★ {c['nombre_comercio']} ({c['tipo']}) — {c['calificacion']}")

print()
print("CONSULTA 2: Comercios con delivery en Lima que facturan > S/10,000/mes")
alto_valor = list(comerciantes.find(
    {
        "acepta_delivery": True,
        "departamento": "Lima",
        "monto_mensual_soles": {"$gt": 10000}
    },
    {"nombre_comercio": 1, "monto_mensual_soles": 1, "distrito": 1, "_id": 0}
))
for c in alto_valor:
    print(f"  → {c['nombre_comercio']} ({c['distrito']}): S/{c['monto_mensual_soles']:,.0f}/mes")

print()
print("CONSULTA 3: Bodegas O farmacias (operador $in)")
bodegas_farmacias = list(comerciantes.find(
    {"tipo": {"$in": ["bodega", "farmacia"]}},
    {"nombre_comercio": 1, "tipo": 1, "_id": 0}
))
for c in bodegas_farmacias:
    print(f"  → [{c['tipo']}] {c['nombre_comercio']}")
```

---

**PASO 4 — Aggregation Pipeline (3.3 — 1.5 pts):**

```python
# ============================================================
# ▶ TU TURNO: Completa el pipeline de facturación por tipo
# Objetivo: reporte para el equipo comercial de Yape
# ============================================================

pipeline_reporte = [
    # Paso 1: Solo comerciantes activos en Lima
    {"$match": {"yape_activo": ___, "departamento": ___}},
    
    # Paso 2: Agrupar por tipo de comercio
    {"$group": {
        "_id": "$tipo",
        "total_comercios":     {"$sum": ___},
        "facturacion_total":   {"$sum": ___},
        "calificacion_prom":   {"$avg": ___},
        "con_delivery":        {"$sum": {"$cond": ["$acepta_delivery", 1, 0]}}
    }},
    
    # Paso 3: Ordenar por facturación total descendente
    {"$sort": {"facturacion_total": ___}},
    
    # Paso 4: Formatear la salida
    {"$project": {
        "tipo_comercio":    "$_id",
        "total_comercios":  1,
        "facturacion_total": 1,
        "calificacion_prom": {"$round": ["$calificacion_prom", 1]},
        "con_delivery":     1,
        "_id": 0
    }}
]

print("📊 REPORTE COMERCIAL YAPE — FACTURACIÓN POR TIPO:")
print(f"{'TIPO':<20} {'COMERCIOS':>9} {'FACTURACIÓN/MES':>16} {'RATING':>7} {'C/DELIVERY':>11}")
print("-" * 67)
for r in comerciantes.aggregate(pipeline_reporte):
    print(f"{r['tipo_comercio']:<20} {r['total_comercios']:>9} "
          f"S/{r['facturacion_total']:>13,.0f} {r['calificacion_prom']:>7} "
          f"{r['con_delivery']:>11}")
```

*Pistas para los `___`:*
- *`yape_activo: ___` → `True`*
- *`departamento: ___` → `"Lima"`*
- *`$sum: ___` para contar → `1`*
- *`$sum: ___` para sumar → `"$monto_mensual_soles"`*
- *`$avg: ___` → `"$calificacion"`*
- *`$sort: ___` → `-1` (descendente)*

---

**Entregable Parte C:**
- Screenshot de Atlas UI → Browse Collections mostrando los documentos insertados
- Screenshot del output del pipeline ejecutado en Colab/local
- En el video: mostrar Atlas Dashboard + explicar por qué el esquema flexible de MongoDB es adecuado vs. SQL para este caso

---

## PARTE D — DOCKER DESKTOP (3 puntos)
### *MongoDB local en contenedor — evidencia en video*

---

### PREGUNTA 4 — Contenerizar MongoDB con Docker Desktop (3 puntos)

**Contexto:** El equipo de desarrollo de Yape necesita un entorno local de pruebas idéntico al de Atlas. Docker permite crear ese entorno en segundos sin instalar MongoDB directamente.

**Prerrequisito:** Docker Desktop instalado y corriendo (ícono de ballena en la barra de tareas).

---

**PASO 1 — Levantar MongoDB en contenedor (4.1 — 1 pt):**

Ejecuta estos comandos en tu terminal (CMD, PowerShell o Terminal de Mac):

```bash
# 1. Descargar la imagen oficial de MongoDB
docker pull mongo:7.0

# 2. Levantar el contenedor con MongoDB
docker run -d \
  --name yape-mongo-local \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=yape2026 \
  mongo:7.0

# 3. Verificar que el contenedor está corriendo
docker ps

# Salida esperada:
# CONTAINER ID   IMAGE      COMMAND                  STATUS        PORTS                      NAMES
# abc123def456   mongo:7.0  "docker-entrypoint.s…"  Up 5 seconds  0.0.0.0:27017->27017/tcp   yape-mongo-local
```

**Verifica en Docker Desktop:** La pestaña "Containers" debe mostrar `yape-mongo-local` en estado **Running** (ícono verde).

---

**PASO 2 — Conectar Python al MongoDB local (4.2 — 1 pt):**

```python
# ============================================================
# CONECTAR A MONGODB EN DOCKER (localhost, no Atlas)
# ============================================================
from pymongo import MongoClient

# Conexión al contenedor Docker (diferente al Atlas)
client_docker = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin"
)

db_local = client_docker["yape_local"]
col_local = db_local["comerciantes_test"]

# Insertar el mismo comerciante del Paso 2 de Atlas
col_local.insert_one({
    "nombre_comercio": "Bodega Test Docker",
    "tipo": "bodega",
    "distrito": "Lima",
    "monto_mensual_soles": 1500.00,
    "yape_activo": True,
    "entorno": "docker_local"   # ← Campo que indica que es entorno local
})

# Verificar
doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
print("✅ Documento guardado en MongoDB Docker:")
print(f"   Nombre:   {doc['nombre_comercio']}")
print(f"   Entorno:  {doc['entorno']}")
print(f"   ID:       {doc['_id']}")

# Mostrar todos los documentos en la colección
print(f"\nTotal documentos en Docker: {col_local.count_documents({})}")
```

---

**PASO 3 — Diferencia entre Docker y Atlas (4.3 — 1 pt):**

Responde en el espacio de abajo (3-5 líneas):

```
a) ¿Cuándo usarías MongoDB en Docker en lugar de MongoDB Atlas para el equipo de Yape?
    Utilizaria MongoDB en Docker cuando el equipo de Yape necesita un entorno local de desarrollo y pruebas sin depender de internet, por ejemplo para testear nuevas funcionalidades sin afectar la base de datos de producción en Atlas. También cuando se requiere trabajar con  offline o en una red corporativa cerrada


b) ¿Qué ventaja tiene Atlas M0 sobre el contenedor Docker para el contexto universitario?
    Atlas M0 no requiere instalación ni configuración de servidor local, funciona desde el navegador y está disponible desde cualquier dispositivo con internet. Basado en el contexto de estudiantes universitarios es ideal porque no depende del hardware de la PC y los datos persisten automáticamente en la nube sin necesidad de volúmenes Docker.

c) ¿Qué sucede con los datos del contenedor Docker si ejecutas `docker stop yape-mongo-local` y luego `docker rm yape-mongo-local`? ¿Y con los datos de Atlas?
    Cuando se ejecuta docker stop y docker rm yape-mongo-local, todos los datos almacenados en el contenedor se pierden permanentemente porque MongoDB guarda los datos dentro del contenedor y no se configuró un volumen persistente. En cambio, los datos de Atlas permanecen seguros en la nube de MongoDB sin importar lo que pase localmente.

```

**Comandos para detener y limpiar el contenedor al terminar:**

```bash
docker stop yape-mongo-local
docker rm yape-mongo-local
```

---

**Entregable Parte D:**
- Screenshot de Docker Desktop mostrando el contenedor `yape-mongo-local` en estado **Running**
- Screenshot del output de Python conectando al contenedor
- En el video: mostrar Docker Desktop → Containers → Logs del contenedor

---

## PARTE E — VIDEO DE SUSTENTACIÓN (2 puntos)

---

### PREGUNTA 5 — Demostración en Video (2 puntos)

**Duración:** 5 a 8 minutos
**Herramienta sugerida:** Loom (loom.com — gratuito), OBS Studio (gratuito), o grabador de pantalla de Windows/Mac.

**Estructura obligatoria del video:**

| Segmento | Tiempo | Qué mostrar |
|----------|--------|-------------|
| **1. Presentación** | 20 seg | Di tu nombre, código y tema del examen |
| **2. Arquitectura** | 1 min | Explica la tabla de P1.1 — justifica 2 decisiones tecnológicas con tus propias palabras |
| **3. Databricks** | 2 min | Muestra el notebook ejecutado, el dashboard generado, explica qué hace Bronze→Silver→Gold |
| **4. MongoDB Atlas** | 2 min | Abre Atlas UI → Browse Collections → muestra los 5 documentos → muestra el output del pipeline |
| **5. Docker Desktop** | 1 min | Muestra Docker Desktop con el contenedor corriendo → el output de Python conectando |
| **6. Uso de IA** | 30 seg | Menciona qué partes te ayudó IA a resolver y qué tuviste que modificar tú |

**Enlace del video:** `https://______________________________`

---

## ENTREGABLES Y FORMA DE ENTREGA

### Estructura del PR en GitHub:

```
semana_04/Soluciones/TuNombre_TuCodigo/
│
├── P1_arquitectura.md          ← Tabla P1.1 + respuestas P1.2 y P1.3
│
├── P2_databricks_yape.ipynb    ← Notebook exportado desde Databricks (o .py)
│   o P2_databricks_yape.py
│
├── P3_mongodb_atlas.py         ← Código Python completo de las 4 partes de P3
│
├── P4_docker.py                ← Código Python del Paso 2 de Docker
│
├── screenshots/
│   ├── databricks_celda1.png   ← Output de cada celda ejecutada
│   ├── databricks_celda2.png
│   ├── databricks_celda3.png
│   ├── databricks_dashboard.png
│   ├── atlas_collections.png   ← Browse Collections en Atlas UI
│   ├── atlas_pipeline_output.png
│   └── docker_desktop.png      ← Contenedor en estado Running
│
└── README.md                   ← Enlace al video + descripción de lo implementado
```

**Rama del PR:** `semana04-solucion-TuNombre`
**Base:** `main`
**Descripción del PR:** Incluir el enlace al video en la descripción del PR.

---

## RÚBRICA DE CALIFICACIÓN

### RUBRICA — Evaluación Parcial Big Data DD283

| **DOCENTE** | Mg. Rubén Quispe Llacctarimay |
|-------------|-------------------------------|
| **Evaluación** | Parcial — Semanas 1 a 4 |
| **Herramientas** | Databricks Community · MongoDB Atlas M0 · Docker Desktop |
| **IA** | Permitida como asistente — se evalúa implementación y comprensión |

---

| ÍTEM | DESCRIPCIÓN | 100% del puntaje | 50% del puntaje | 0% |  PTS |
|------|-------------|-----------------|----------------|-----|------|
| **P1.1 — Arquitectura** | Tabla con 6 componentes, tecnología correcta y justificación | 6/6 correctos con justificación técnica específica del caso Yape | 3-5 correctos o justificaciones genéricas | < 3 correctos | **2** |
| **P1.2 — CAP Theorem** | 2 componentes con combinación correcta y explicación de sacrificio | Ambos correctos con explicación del sacrificio vinculada al caso | 1 correcto o explicación sin caso | Ambos incorrectos | **1** |
| **P1.3 — NewSQL** | 3 preguntas: limitación Oracle, por qué no MongoDB, mecanismo técnico | Raft/Paxos mencionado + limitación correcta + problema ACID de MongoDB | 2/3 correctos | 0-1 correctos | **1** |
| **P2 — Databricks: celdas 2 y 3** | Silver y Gold completados con `___` reemplazados correctamente | Output de ambas celdas visible con datos correctos en screenshot | Solo Silver correcta o Gold con errores menores | Sin output o celdas sin completar | **4** |
| **P2 — Databricks: dashboard** | Celda 4 ejecutada, gráfico generado y visible en screenshot | Gráfico con datos reales (no vacío) guardado en /FileStore | Gráfico incompleto (un solo panel) | Sin gráfico | **2** |
| **P3.1 — Atlas: inserción** | 5 documentos con estructura flexible visible en Atlas UI | 5 documentos insertados, screenshot de Atlas Browse Collections | 3-4 documentos o sin screenshot de Atlas | Sin inserción en Atlas real |  **2** |
| **P3.2 — Atlas: queries** | 3 consultas ejecutadas con output visible | Las 3 consultas con resultado correcto | 2/3 consultas correctas | Sin queries o resultados vacíos | **1.5** |
| **P3.3 — Atlas: pipeline** | Pipeline completado con los `___` reemplazados, tabla de facturación impresa | Output visible con columnas correctas y datos coherentes | Pipeline sin completar pero ejecutado con errores menores | Sin pipeline ejecutado | **1.5** |
| **P4.1 — Docker: contenedor** | `docker run` exitoso, Docker Desktop mostrando Running | Screenshot de Docker Desktop con contenedor verde | Screenshot sin estado Running claro | Sin evidencia de Docker | **1** |
| **P4.2 — Docker: Python** | Código ejecutado, documento insertado, output impreso | Output visible con nombre e ID del documento | Código correcto pero sin output | Sin conexión a Docker | **1** |
| **P4.3 — Docker: análisis** | 3 preguntas respondidas con argumentos técnicos (persistencia, casos de uso) | 2/3 con argumento técnico | Solo 1 con argumento | Sin respuesta o respuestas de 1 línea sin técnica | **1** |
| **P5 — Video** | Cubre los 6 segmentos, muestra todo funcionando, explica uso de IA | 5-6 segmentos cubiertos, demostraciones claras | 3-4 segmentos, demostraciones con cortes o sin explicación | < 3 segmentos o sin demostración real en software | **2** |
| | | | | **SUMA TOTAL** | **20** |

---

### Escala de calificación

| Puntaje | Nivel | Descripción |
|---------|-------|-------------|
| 18 – 20 | AD — Logro destacado | Implementación completa, explicación fluida, adaptaciones propias al código |
| 14 – 17 | A — Logro esperado | Implementación funcional en las 3 herramientas, comprensión demostrada en video |
| 11 – 13 | B — En proceso | Implementación parcial (2 de 3 herramientas), explicación con vacíos conceptuales |
| 0 – 10 | C — En inicio | No puede demostrar implementación o el video no corresponde al trabajo presentado |

---

### Criterio anti-copia para el video

El video es el principal mecanismo de verificación. Un estudiante que copió el código pero lo ejecutó en su máquina y puede explicarlo verbalmente **aprueba**. Un estudiante con código propio que no puede responder preguntas básicas sobre lo que implementó **puede ser evaluado con preguntas adicionales**.

*Si el video muestra capturas de pantalla de otra persona (distintas resoluciones, nombre de usuario diferente, fecha inconsistente), el examen será anulado.*

---

*Big Data DD283 | Universidad Autónoma del Perú | Evaluación Parcial | Semana 4 | 2026-1*
*Mg. Rubén Quispe Llacctarimay | Entrega: 48 horas | Puntaje: 20 pts*
