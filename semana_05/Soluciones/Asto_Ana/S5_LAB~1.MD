# S5 — LABORATORIO EN CASA: Pipeline Spark Completo (RESUELTO)
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: PySpark + Spark SQL + Streaming simulado en Databricks Community

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha de entrega** | ______________________________________________ |
| **Tiempo estimado** | 2 horas |
| **Modalidad** | Individual |
| **Entorno** | Databricks Community Edition (principal) · Google Colab (alternativa) |

> **Nota:** el código de este documento fue completado y ejecutado localmente (PySpark 3.5.0 + Spark local) para verificar que la lógica es correcta. Los outputs mostrados son reales, no inventados. Al ejecutarlo en Databricks Community los números serán distintos (mismo `seed`, pero el orden de partición/ejecución puede variar ligeramente los `.show()` de filas individuales); las cifras agregadas (conteos, sumas, promedios) deben coincidir.

---

## OBJETIVO

Implementar un pipeline completo de procesamiento de datos masivos usando Apache Spark: desde la ingesta de datos crudos (Bronze) hasta la generación de métricas de negocio (Gold), aplicando PySpark, Spark SQL y simulando un stream en tiempo real — todo sobre un dataset de taxis en Lima.

**Competencia que desarrolla:** Procesar datos masivos con Spark aplicando transformaciones, Spark SQL y detección de patrones en streaming.

---

## SOFTWARE Y HERRAMIENTAS

### Opción A — Databricks Community (RECOMENDADA)

| Herramienta | Versión | Acceso |
|-------------|---------|--------|
| Databricks Community Edition | Spark 3.5 | community.cloud.databricks.com |
| Python | 3.11 (incluido) | Incluido en Databricks |
| PySpark | 3.5 (incluido) | Incluido en Databricks |
| matplotlib | Incluido | Incluido en Databricks |

**Verificación del entorno:**
```python
# Celda 0: verificar entorno (ejecutar primero)
print(f"Spark version: {spark.version}")
print(f"Python version: {spark.sparkContext.pythonVer}")
print("✅ Entorno listo")
```

### Opción B — Google Colab (alternativa)

```python
!pip install pyspark==3.5.0 -q
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("S5_LimaTaxis") \
    .config("spark.ui.port", "4050") \
    .getOrCreate()
print(f"✅ Spark {spark.version} listo en Colab")
```

---

## CONTEXTO DEL LABORATORIO

**Dataset:** 10,000 viajes de taxi en Lima Metropolitana (datos sintéticos basados en patrones reales de taxis por aplicativo).

**Caso de negocio:** Eres Data Engineer en **TaxiApp Perú**. El equipo de producto necesita:

1. Identificar las rutas más rentables para los conductores (Bronze → Silver → Gold)
2. Detectar conductores "estrella" (rating > 4.5, más de 20 viajes)
3. Simular un sistema de alertas en tiempo real para conductores con rating en caída

---

## PARTE 1 — EXPLORACIÓN: Carga y perfil del dataset (30 min)

### Celda 1 — Generar el dataset (ejecutar tal cual)

```python
import numpy as np
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.types import *

np.random.seed(2026)
N = 10_000

distritos = [
    "Miraflores", "San Isidro", "Barranco", "Surco", "San Borja",
    "SJL",        "Comas",      "Los Olivos","Ate",   "Villa El Salvador",
    "Callao",     "Independencia","La Victoria","Pueblo Libre","Jesús María"
]
turnos   = ["mañana", "tarde", "noche", "madrugada"]
metodos  = ["efectivo", "yape",   "tarjeta",  "contra_app"]
estados  = ["completado","completado","completado","cancelado","incidente"]

data = {
    "id_viaje":      [f"TX{i:07d}" for i in range(1, N+1)],
    "fecha":         pd.date_range("2025-09-01", periods=N, freq="1h")
                        .strftime("%Y-%m-%d").tolist(),
    "turno":         np.random.choice(turnos,    N, p=[.30, .35, .25, .10]).tolist(),
    "origen":        np.random.choice(distritos, N).tolist(),
    "destino":       np.random.choice(distritos, N).tolist(),
    "distancia_km":  np.round(np.random.exponential(9, N).clip(1, 45), 2).tolist(),
    "duracion_min":  np.random.randint(5, 120, N).tolist(),
    "tarifa_soles":  np.round(np.random.uniform(7, 95, N), 2).tolist(),
    "propina_soles": np.round(np.random.choice(
                        [0, 0, 0, 2, 5, 10], N, p=[.5, .1, .1, .15, .1, .05]), 2).tolist(),
    "metodo_pago":   np.random.choice(metodos, N, p=[.25, .40, .25, .10]).tolist(),
    "id_conductor":  [f"CON{np.random.randint(1, 200):04d}" for _ in range(N)],
    "rating":        np.round(np.random.normal(4.15, 0.55, N).clip(1, 5), 1).tolist(),
    "estado":        np.random.choice(estados, N, p=[.78, .07, .03, .10, .02]).tolist(),
}

schema = StructType([
    StructField("id_viaje",     StringType()),
    StructField("fecha",        StringType()),
    StructField("turno",        StringType()),
    StructField("origen",       StringType()),
    StructField("destino",      StringType()),
    StructField("distancia_km", DoubleType()),
    StructField("duracion_min", IntegerType()),
    StructField("tarifa_soles", DoubleType()),
    StructField("propina_soles",DoubleType()),
    StructField("metodo_pago",  StringType()),
    StructField("id_conductor", StringType()),
    StructField("rating",       DoubleType()),
    StructField("estado",       StringType()),
])

records = list(zip(*data.values()))
df_bronze = spark.createDataFrame(records, schema)
df_bronze.write.mode("overwrite").parquet("/FileStore/taxi_lima/bronze/viajes")

print(f"✅ Bronze layer: {df_bronze.count():,} viajes guardados")
print(f"   Columnas: {len(df_bronze.columns)}")
df_bronze.show(5)
df_bronze.printSchema()
```

**Output real obtenido:**
```
✅ Bronze layer: 10,000 viajes guardados
   Columnas: 13
+---------+----------+---------+------------+-----------+------------+------------+------------+-------------+-----------+------------+------+----------+
| id_viaje|     fecha|    turno|      origen|    destino|distancia_km|duracion_min|tarifa_soles|propina_soles|metodo_pago|id_conductor|rating|    estado|
+---------+----------+---------+------------+-----------+------------+------------+------------+-------------+-----------+------------+------+----------+
|TX0000001|2025-09-01|   mañana|  Los Olivos|        SJL|       16.95|          59|       44.81|          0.0| contra_app|     CON0066|   4.2|completado|
|TX0000002|2025-09-01|    tarde|Pueblo Libre|Jesús María|         1.0|          54|       44.99|          0.0|       yape|     CON0155|   3.6|completado|
|TX0000003|2025-09-01|madrugada| La Victoria|   Barranco|        2.88|          44|       68.18|          0.0|    tarjeta|     CON0168|   3.9|completado|
|TX0000004|2025-09-01|   mañana|       Surco|  San Borja|       19.93|          66|       71.75|          0.0|    tarjeta|     CON0106|   3.6|completado|
|TX0000005|2025-09-01|    tarde|    Barranco|   Barranco|        9.92|          84|        17.5|          0.0|       yape|     CON0119|   4.6|completado|
+---------+----------+---------+------------+-----------+------------+------------+------------+-------------+-----------+------------+------+----------+

root
 |-- id_viaje: string (nullable = true)
 |-- fecha: string (nullable = true)
 |-- turno: string (nullable = true)
 |-- origen: string (nullable = true)
 |-- destino: string (nullable = true)
 |-- distancia_km: double (nullable = true)
 |-- duracion_min: integer (nullable = true)
 |-- tarifa_soles: double (nullable = true)
 |-- propina_soles: double (nullable = true)
 |-- metodo_pago: string (nullable = true)
 |-- id_conductor: string (nullable = true)
 |-- rating: double (nullable = true)
 |-- estado: string (nullable = true)
```

---

### Celda 2 — Exploración del dataset

```python
df = spark.read.parquet("/FileStore/taxi_lima/bronze/viajes")

print("=== ESTADÍSTICAS DESCRIPTIVAS ===")
df.select("distancia_km", "duracion_min", "tarifa_soles", "propina_soles", "rating") \
  .describe() \
  .show()

print("=== DISTRIBUCIÓN POR ESTADO ===")
df.groupBy("estado").count() \
  .orderBy("count", ascending=False) \
  .withColumn("porcentaje", F.round(F.col("count") / df.count() * 100, 1)) \
  .show()

print("=== DISTRIBUCIÓN POR TURNO ===")
df.groupBy("turno").count().orderBy("count", ascending=False).show()
```

**Output real obtenido:**
```
=== ESTADÍSTICAS DESCRIPTIVAS ===
+-------+-----------------+-----------------+------------------+------------------+------------------+
|summary|     distancia_km|     duracion_min|      tarifa_soles|     propina_soles|            rating|
+-------+-----------------+-----------------+------------------+------------------+------------------+
|  count|            10000|            10000|             10000|             10000|             10000|
|   mean|8.913066000000006|          62.1447| 51.15164999999993|            1.3353| 4.140620000000004|
| stddev|8.549312780249979|33.51733735099357|25.648813154591082|2.5812284253855564|0.5196085208130163|
|    min|              1.0|                5|              7.01|               0.0|               2.1|
|    max|             45.0|              119|             94.99|              10.0|               5.0|
+-------+-----------------+-----------------+------------------+------------------+------------------+

=== DISTRIBUCIÓN POR ESTADO ===
+----------+-----+----------+
|    estado|count|porcentaje|
+----------+-----+----------+
|completado| 8767|      87.7|
| cancelado| 1017|      10.2|
| incidente|  216|       2.2|
+----------+-----+----------+

=== DISTRIBUCIÓN POR TURNO ===
+---------+-----+
|    turno|count|
+---------+-----+
|    tarde| 3526|
|   mañana| 2960|
|    noche| 2514|
|madrugada| 1000|
+---------+-----+
```

**Pregunta de reflexión 1:** ¿Qué distribución de estados encontraste? ¿Qué porcentaje de viajes terminó en "incidente"? ¿Cómo afecta esto a los ingresos netos de TaxiApp?

```python
# R1:
# El 87.7% de los viajes terminó "completado", 10.2% "cancelado" y 2.2% "incidente".
# Aunque 2.2% parece bajo, sobre 10,000 viajes son 216 casos: cada incidente implica
# costo de seguro/soporte, reembolsos y daño reputacional (rating del conductor y de
# la app), además de que ese viaje no genera comisión. Los cancelados (10.2%, 1017
# viajes) tampoco generan ingreso pero sí consumen tiempo de match del conductor
# (costo de oportunidad). En conjunto, ~12.4% de los viajes bronze no llegan a
# facturar nada, por eso el filtro de Silver (solo "completado") es clave para que
# las métricas Gold reflejen ingresos reales y no infladas por viajes fallidos.
```

---

## PARTE 2 — APLICACIÓN: Pipeline Bronze → Silver → Gold (60 min)

### Celda 3 — Silver layer: limpiar y enriquecer (COMPLETADO)

```python
df_bronze = spark.read.parquet("/FileStore/taxi_lima/bronze/viajes")

df_silver = (
    df_bronze
    # Filtro 1: solo viajes completados (excluir cancelados e incidentes)
    .filter(F.col("estado") == "completado")

    # Filtro 2: distancia mínima válida (> 0.5 km) y tarifa mínima (> 0)
    .filter((F.col("distancia_km") > 0.5) & (F.col("tarifa_soles") > 0))

    # Columna nueva: ingreso total del conductor (tarifa + propina)
    .withColumn("ingreso_total",
        F.round(F.col("tarifa_soles") + F.col("propina_soles"), 2))

    # Columna nueva: comisión de TaxiApp (20% de la tarifa, no de la propina)
    .withColumn("comision_taxiapp",
        F.round(F.col("tarifa_soles") * 0.20, 2))

    # Columna nueva: ingreso neto del conductor (ingreso_total - comisión)
    .withColumn("ingreso_neto_conductor",
        F.round(F.col("ingreso_total") - F.col("comision_taxiapp"), 2))

    # Columna nueva: precio por km (tarifa / distancia)
    .withColumn("precio_por_km",
        F.round(F.col("tarifa_soles") / F.col("distancia_km"), 2))

    # Columna nueva: categoría de viaje por distancia
    .withColumn("categoria_viaje",
        F.when(F.col("distancia_km") < 5,  "corto")
         .when(F.col("distancia_km") < 15, "medio")
         .otherwise("largo"))

    # Columna nueva: es viaje rentable para el conductor (ingreso_neto > S/30)
    .withColumn("es_rentable",
        F.col("ingreso_neto_conductor") > 30)
)

df_silver.write.mode("overwrite").parquet("/FileStore/taxi_lima/silver/viajes_limpios")

total_silver = df_silver.count()
total_bronze = df_bronze.count()
print(f"✅ Silver layer: {total_silver:,} viajes válidos")
print(f"   Eliminados: {total_bronze - total_silver:,} ({(total_bronze - total_silver)/total_bronze*100:.1f}%)")

df_silver.select("id_viaje", "tarifa_soles", "propina_soles",
                 "ingreso_total", "comision_taxiapp", "ingreso_neto_conductor",
                 "precio_por_km", "categoria_viaje", "es_rentable").show(5)
```

**Output real obtenido:**
```
✅ Silver layer: 8,767 viajes válidos
   Eliminados: 1,233 (12.3%)
+---------+------------+-------------+-------------+----------------+----------------------+-------------+---------------+-----------+
| id_viaje|tarifa_soles|propina_soles|ingreso_total|comision_taxiapp|ingreso_neto_conductor|precio_por_km|categoria_viaje|es_rentable|
+---------+------------+-------------+-------------+----------------+----------------------+-------------+---------------+-----------+
|TX0000001|       44.81|          0.0|        44.81|            8.96|                 35.85|         2.64|          largo|       true|
|TX0000002|       44.99|          0.0|        44.99|             9.0|                 35.99|        44.99|          corto|       true|
|TX0000003|       68.18|          0.0|        68.18|           13.64|                 54.54|        23.67|          corto|       true|
|TX0000004|       71.75|          0.0|        71.75|           14.35|                  57.4|          3.6|          largo|       true|
|TX0000005|        17.5|          0.0|         17.5|             3.5|                  14.0|         1.76|          medio|      false|
+---------+------------+-------------+-------------+----------------+----------------------+-------------+---------------+-----------+
```

**Valores usados en los `___`:**
- `estado ==` → `"completado"`
- Distancia mínima → `0.5`
- Tarifa mínima → `0`
- `ingreso_total` → `tarifa_soles + propina_soles`
- Comisión TaxiApp → `0.20` (20%)
- Categoría largo → `"largo"`
- Rentable umbral → `30`

---

### Celda 4 — Gold layer: métricas de negocio con Spark SQL (COMPLETADO)

```python
df_silver = spark.read.parquet("/FileStore/taxi_lima/silver/viajes_limpios")
df_silver.createOrReplaceTempView("viajes")

# ── GOLD 1: Top 10 rutas más rentables ────────────────────────
gold_rutas = spark.sql("""
    SELECT 
        CONCAT(origen, ' → ', destino)     AS ruta,
        COUNT(*)                            AS total_viajes,
        ROUND(AVG(tarifa_soles), 2)         AS tarifa_promedio,
        ROUND(AVG(precio_por_km), 2)        AS precio_km_prom,
        ROUND(SUM(comision_taxiapp), 2)     AS ingresos_taxiapp
    FROM viajes
    GROUP BY origen, destino
    HAVING COUNT(*) >= 3
    ORDER BY ingresos_taxiapp DESC
    LIMIT 10
""")

# ── GOLD 2: Conductores estrella ──────────────────────────────
gold_conductores = spark.sql("""
    SELECT
        id_conductor,
        COUNT(*)                                        AS total_viajes,
        ROUND(AVG(rating), 2)                           AS rating_prom,
        ROUND(SUM(ingreso_neto_conductor), 2)           AS ingresos_netos,
        ROUND(AVG(ingreso_neto_conductor), 2)           AS ingreso_prom_viaje,
        SUM(CASE WHEN es_rentable THEN 1 ELSE 0 END)   AS viajes_rentables
    FROM viajes
    GROUP BY id_conductor
    HAVING AVG(rating) > 4.5 AND COUNT(*) > 20
    ORDER BY rating_prom DESC, ingresos_netos DESC
    LIMIT 10
""")

# ── GOLD 3: Ingresos TaxiApp por turno y método de pago ───────
gold_turno_pago = spark.sql("""
    SELECT
        turno,
        metodo_pago,
        COUNT(*)                        AS total_viajes,
        ROUND(SUM(comision_taxiapp), 2) AS ingresos_taxiapp,
        ROUND(AVG(rating), 2)           AS rating_prom
    FROM viajes
    GROUP BY turno, metodo_pago
    ORDER BY ingresos_taxiapp DESC
""")

gold_rutas.write.mode("overwrite").parquet("/FileStore/taxi_lima/gold/top_rutas")
gold_conductores.write.mode("overwrite").parquet("/FileStore/taxi_lima/gold/conductores_estrella")
gold_turno_pago.write.mode("overwrite").parquet("/FileStore/taxi_lima/gold/ingresos_turno_pago")

print("📊 TOP 10 RUTAS MÁS RENTABLES PARA TAXIAPP:")
gold_rutas.show(truncate=False)

print("\n⭐ CONDUCTORES ESTRELLA (rating > 4.5, > 20 viajes):")
gold_conductores.show()

print("\n💰 INGRESOS TAXIAPP POR TURNO Y MÉTODO DE PAGO:")
gold_turno_pago.show(20)
```

**Output real obtenido:**
```
📊 TOP 10 RUTAS MÁS RENTABLES PARA TAXIAPP:
+-----------------------------+------------+---------------+--------------+----------------+
|ruta                         |total_viajes|tarifa_promedio|precio_km_prom|ingresos_taxiapp|
+-----------------------------+------------+---------------+--------------+----------------+
|Surco → Comas                |58          |51.34          |19.9          |595.59          |
|Callao → Independencia       |55          |52.61          |18.27         |578.7           |
|La Victoria → La Victoria    |51          |54.81          |13.87         |559.12          |
|Barranco → Ate               |50          |55.37          |11.74         |553.72          |
|Villa El Salvador → Ate      |59          |46.26          |12.36         |545.8           |
|San Borja → Ate              |49          |55.09          |16.12         |539.86          |
|Pueblo Libre → Callao        |58          |46.09          |15.69         |534.62          |
|Independencia → Pueblo Libre |51          |52.11          |18.34         |531.54          |
|La Victoria → Jesús María    |51          |51.82          |16.99         |528.52          |
|La Victoria → Miraflores     |46          |56.32          |15.18         |518.17          |
+-----------------------------+------------+---------------+--------------+----------------+

⭐ CONDUCTORES ESTRELLA (rating > 4.5, > 20 viajes):
+------------+------------+-----------+--------------+------------------+----------------+
|id_conductor|total_viajes|rating_prom|ingresos_netos|ingreso_prom_viaje|viajes_rentables|
+------------+------------+-----------+--------------+------------------+----------------+
+------------+------------+-----------+--------------+------------------+----------------+
(0 filas)

💰 INGRESOS TAXIAPP POR TURNO Y MÉTODO DE PAGO:
+---------+-----------+------------+----------------+-----------+
|    turno|metodo_pago|total_viajes|ingresos_taxiapp|rating_prom|
+---------+-----------+------------+----------------+-----------+
|    tarde|       yape|        1237|        12574.99|       4.15|
|   mañana|       yape|        1052|        10428.97|       4.13|
|    noche|       yape|         850|         8550.28|       4.15|
|    tarde|    tarjeta|         768|         7845.88|       4.18|
|    tarde|   efectivo|         756|         7741.34|       4.14|
|   mañana|    tarjeta|         668|         7015.24|       4.12|
|   mañana|   efectivo|         620|         6402.34|       4.12|
|    noche|   efectivo|         600|         6306.29|       4.14|
|    noche|    tarjeta|         521|         5423.12|       4.12|
|madrugada|       yape|         349|         3629.71|       4.17|
|    tarde| contra_app|         324|         3290.23|        4.1|
|   mañana| contra_app|         262|         2811.53|       4.11|
|    noche| contra_app|         233|         2453.06|       4.16|
|madrugada|   efectivo|         219|         2233.15|       4.15|
|madrugada|    tarjeta|         217|         2216.32|       4.09|
|madrugada| contra_app|          91|           957.7|       4.17|
+---------+-----------+------------+----------------+-----------+
```

> **Nota importante:** con este `seed` la tabla de "Conductores estrella" queda **vacía (0 filas)**. Es un resultado real y correcto, no un error: cada conductor promedia ~44 viajes (8,767 viajes / ~200 conductores), y el rating por viaje se generó con `np.random.normal(4.15, 0.55)`. Al promediar 40+ observaciones alrededor de una media de 4.15, es estadísticamente muy raro que el promedio de un conductor supere 4.5 (eso requeriría ~0.63 desviaciones estándar sostenidas sobre 40 viajes). Esto es justamente lo que se le puede hacer notar al docente: el umbral `> 4.5` es exigente para esta distribución sintética; si se quisiera obtener resultados no vacíos habría que bajar el umbral (p. ej. `> 4.3`) o generar el rating por conductor (no por viaje) con más dispersión.

**Valores usados en los `___`:**
- Gold 1 — `GROUP BY origen, destino`, `HAVING COUNT(*) >= 3`
- Gold 2 — `GROUP BY id_conductor`, `HAVING AVG(rating) > 4.5 AND COUNT(*) > 20`
- Gold 3 — `GROUP BY turno, metodo_pago`

---

### Celda 5 — Visualización del dashboard

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

gold_rutas = spark.read.parquet("/FileStore/taxi_lima/gold/top_rutas").toPandas()
gold_turno = spark.read.parquet("/FileStore/taxi_lima/gold/ingresos_turno_pago").toPandas()
gold_cond  = spark.read.parquet("/FileStore/taxi_lima/gold/conductores_estrella").toPandas()

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Dashboard Ejecutivo — TaxiApp Perú | Septiembre 2025",
             fontsize=14, fontweight="bold")

axes[0].barh(gold_rutas["ruta"].str[:25],
             gold_rutas["ingresos_taxiapp"],
             color=plt.cm.Blues(np.linspace(0.4, 0.9, len(gold_rutas))))
axes[0].set_xlabel("Ingresos TaxiApp (S/)")
axes[0].set_title("Top 10 Rutas — Ingresos TaxiApp")
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"S/{x:,.0f}"))
axes[0].invert_yaxis()

turnos_order = ["mañana", "tarde", "noche", "madrugada"]
turno_pivot  = gold_turno.pivot_table(
    index="turno", columns="metodo_pago",
    values="ingresos_taxiapp", aggfunc="sum", fill_value=0
)
turno_pivot = turno_pivot.reindex([t for t in turnos_order if t in turno_pivot.index])
turno_pivot.plot(kind="bar", ax=axes[1], rot=30, colormap="Set2")
axes[1].set_title("Ingresos por Turno y Método de Pago")
axes[1].set_xlabel("Turno")
axes[1].set_ylabel("Ingresos TaxiApp (S/)")
axes[1].legend(title="Método de pago", fontsize=8)

axes[2].scatter(gold_cond["rating_prom"], gold_cond["ingresos_netos"],
                s=gold_cond["total_viajes"] * 2,
                c=gold_cond["rating_prom"], cmap="YlOrRd", alpha=0.8, edgecolors="gray")
for _, row in gold_cond.iterrows():
    axes[2].annotate(row["id_conductor"],
                     (row["rating_prom"], row["ingresos_netos"]),
                     fontsize=7, ha="center", va="bottom")
axes[2].set_xlabel("Rating Promedio")
axes[2].set_ylabel("Ingresos Netos (S/)")
axes[2].set_title("Conductores Estrella\n(tamaño = # viajes)")
axes[2].axvline(x=4.7, color="red", linestyle="--", alpha=0.4, label="Top tier (>4.7)")
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig("/dbfs/FileStore/taxi_lima/gold/dashboard_taxiapp.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Dashboard guardado")
```

El dashboard fue generado y ejecutado localmente a partir de las tablas Gold reales (archivo `dashboard_taxiapp.png` adjunto). El panel 3 (conductores estrella) aparece vacío porque, como se explicó arriba, ningún conductor cumple `rating > 4.5` con este `seed`.

---

## PARTE 3 — DESAFÍO: Simulación de Streaming (30 min)

### Celda 6 — Streaming simulado de alertas de conductores

```python
# En Databricks: usar rate source como simulador de viajes llegando en tiempo real
stream_source = (
    spark.readStream
    .format("rate")
    .option("rowsPerSecond", 20)   # Simula 20 nuevos viajes por segundo
    .load()
)

stream_viajes = (
    stream_source
    .withColumn("id_conductor",
        F.concat(F.lit("CON"),
                 F.lpad((F.col("value") % 200 + 1).cast("string"), 4, "0")))
    .withColumn("rating_simulado",
        F.round(
            F.when(F.col("value") % 15 == 0, F.lit(2.8))  # Cada 15 viajes: rating bajo
             .otherwise(F.lit(4.0) + (F.col("value") % 10).cast("double") / 20),
            1
        ))
    .withColumn("tarifa_simulada",
        F.round(10 + (F.col("value") % 80).cast("double"), 2))
)

alertas_stream = (
    stream_viajes
    .groupBy(
        F.window(F.col("timestamp"), "30 seconds"),
        F.col("id_conductor")
    )
    .agg(
        F.count("*").alias("viajes_ventana"),
        F.round(F.avg("rating_simulado"), 2).alias("rating_prom_ventana"),
        F.round(F.sum("tarifa_simulada"), 2).alias("facturacion_ventana")
    )
    .filter(F.col("rating_prom_ventana") < 3.5)
    .select(
        F.col("window.start").alias("inicio_ventana"),
        F.col("window.end").alias("fin_ventana"),
        F.col("id_conductor"),
        F.col("viajes_ventana"),
        F.col("rating_prom_ventana"),
        F.col("facturacion_ventana"),
        F.lit("⚠️ ALERTA: Rating bajo — revisar conductor").alias("alerta")
    )
)

query_alertas = (
    alertas_stream
    .writeStream
    .format("memory")
    .queryName("alertas_conductores")
    .outputMode("complete")
    .start()
)

import time
print("🔴 SISTEMA DE ALERTAS EN TIEMPO REAL — TaxiApp Perú")
print("   Detectando conductores con rating < 3.5 en ventana de 30 segundos...")
print("-" * 70)

for ciclo in range(4):
    time.sleep(12)
    alertas = spark.sql("""
        SELECT id_conductor, viajes_ventana, rating_prom_ventana, 
               facturacion_ventana, alerta
        FROM alertas_conductores
        ORDER BY rating_prom_ventana ASC
        LIMIT 5
    """)
    if alertas.count() > 0:
        print(f"\n[Ciclo {ciclo+1}/4 — {12*(ciclo+1)} seg]")
        alertas.show(truncate=False)
    else:
        print(f"  [Ciclo {ciclo+1}/4] Sin alertas aún...")

query_alertas.stop()
print("\n✅ Stream detenido. Sistema de alertas completado.")
```

Esta celda no tenía `___` que completar — es código dado para ejecutar tal cual. Verificado localmente con Structured Streaming (`rate` source) que la lógica corre sin errores: cada ~15 registros por conductor genera un rating simulado de 2.8, que al promediarse en la ventana de 30s con el resto de valores (~4.0-4.5) produce el patrón esperado de alertas intermitentes.

**Pregunta de reflexión 2:** ¿Qué pasaría si aumentas `rowsPerSecond` a 1000? ¿El sistema de alertas seguiría funcionando igual? ¿Cuál sería el cuello de botella en Databricks Community (1 clúster)?

```python
# R2:
# A 1000 filas/seg el volumen por ventana de 30s pasa de ~600 a ~30,000 eventos.
# La lógica de detección seguiría siendo correcta (el groupBy + filter no cambia),
# pero el rendimiento sí se degradaría. Databricks Community solo da un clúster de
# un único nodo (recursos compartidos, sin autoscaling ni workers adicionales), por
# lo que el cuello de botella sería el driver: todo el shuffle del groupBy(window,
# id_conductor) y el estado incremental de Structured Streaming (state store) se
# procesan en los mismos cores limitados. Es probable que el micro-batch empiece a
# acumular retraso (processing time > trigger interval), generando "back pressure"
# y creciente latencia entre el evento real y la alerta mostrada. En producción esto
# se resolvería con más workers/particiones y un sink más eficiente que "memory"
# (que además no es apto para producción por consumir RAM del driver).
```

**Pregunta de reflexión 3 (conexión con proyecto grupal):** ¿Tu grupo podría aplicar Structured Streaming para detectar patrones en tiempo real en su proyecto? ¿Cuál sería la ventana temporal más adecuada?

```python
# R3:
# Sí: cualquier proyecto con eventos que llegan continuamente (sensores IoT, logs de
# transacciones, clics de una app) puede beneficiarse de Structured Streaming para
# detectar anomalías apenas ocurren, en vez de esperar un batch nocturno. La ventana
# adecuada depende de qué tan rápido se necesita reaccionar versus qué tan estable
# quiere ser la métrica: ventanas cortas (10-30s) reaccionan rápido pero son ruidosas
# con pocos datos; ventanas más largas (5-15 min) suavizan el ruido pero retrasan la
# alerta. Para un caso tipo "rating de conductor en caída" o "fraude en pagos", una
# ventana deslizante (sliding window) de 5 minutos con slide de 1 minuto sería un
# buen punto intermedio: suficiente volumen para que el promedio sea confiable, y
# suficiente frecuencia de recálculo para no perder capacidad de reacción.
```

---

## ENTREGABLES

### Estructura del PR en GitHub:

```
semana_05/Soluciones/TuNombre_TuCodigo/
├── S5_lab_casa_taxiapp.ipynb       ← Notebook exportado con outputs visibles
│   o S5_lab_casa_taxiapp.py
├── screenshots/
│   ├── celda1_bronze_output.png    ← Output de la Celda 1
│   ├── celda3_silver_output.png    ← Output de la Celda 3 (tabla con nuevas columnas)
│   ├── celda4_gold_rutas.png       ← Top 10 rutas
│   ├── celda4_gold_conductores.png ← Conductores estrella
│   ├── celda5_dashboard.png        ← Los 3 gráficos del dashboard
│   └── celda6_alertas.png          ← Output del streaming con alertas
└── README.md                        ← Reflexiones 1, 2 y 3 respondidas
```

**Rama del PR:** `semana05-lab-TuNombre`

### Rúbrica básica

| Criterio | Pts |
|----------|-----|
| Celda 1: dataset generado con output visible | 10 |
| Celda 3: Silver completada con los ___ correctos y output | 25 |
| Celda 4: Gold completada con los ___ correctos, 3 tablas visibles | 30 |
| Celda 5: Dashboard con 3 gráficos guardado | 15 |
| Celda 6: Stream ejecutado al menos 2 ciclos con alertas | 15 |
| Reflexiones 1, 2 y 3 respondidas con argumento técnico | 5 |
| **TOTAL** | **100** |

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Laboratorio en casa — Databricks Community Edition — Resuelto y verificado con ejecución real (PySpark 3.5.0 local)*
