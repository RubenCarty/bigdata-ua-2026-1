# S5 — SESIÓN DE CLASE COMPLETA: Apache Spark
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: MapReduce + Spark Core + Spark SQL + Streaming + GraphX

---

| Campo | Detalle |
|-------|---------|
| **Curso** | Big Data DD283 |
| **Semana** | 5 de 8 |
| **Tema** | Tecnologías de Procesamiento: MapReduce → Apache Spark |
| **Logro** | El estudiante procesa información usando MapReduce y aplica Spark para procesar datos en lotes e identifica sistemas basados en flujo con integridad |
| **Duración** | 3 horas (180 min + 20 min receso) |
| **Herramienta** | Databricks Community Edition (gratis) |
| **Valor** | Integridad al garantizar la veracidad de los datos procesados |

---

## TABLA DE CONTENIDOS

1. [Cronograma de la sesión](#cronograma)
2. [INICIO — Rompe-hielo y diagnóstico](#inicio)
3. [UTILIDAD — Por qué Spark domina Big Data](#utilidad)
4. [TRANSFORMACIÓN — MapReduce → Spark → Streaming → GraphX](#transformacion)
5. [PRÁCTICA — Caso Yango Perú](#practica)
6. [CIERRE — Síntesis y tarea](#cierre)
7. [Guion verbal sugerido](#guion)
8. [Casos reales recomendados](#casos)
9. [Referencias APA 7](#referencias)

---

## CRONOGRAMA DE LA SESIÓN {#cronograma}

| Bloque | Actividad | Duración | Responsable |
|--------|-----------|----------|-------------|
| **INICIO** | Rompe-hielo + Logro + Revisión S4 + Diagnóstico | 20 min | Docente |
| **UTILIDAD** | Por qué Spark reemplazó MapReduce | 10 min | Docente |
| **TRANSFORMACIÓN 1** | MapReduce limitaciones → RDD → DataFrame | 30 min | Docente + Grupo |
| **TRANSFORMACIÓN 2** | Spark SQL: consultas sobre datos masivos | 20 min | Docente + Grupo |
| ☕ **RECESO** | Descanso | 20 min | — |
| **TRANSFORMACIÓN 3** | Structured Streaming: datos en tiempo real | 25 min | Docente + Grupo |
| **TRANSFORMACIÓN 4** | GraphX: grafos distribuidos | 20 min | Docente + Grupo |
| **PRÁCTICA GRUPAL** | Caso Yango Perú — análisis de viajes Lima | 25 min | Grupos |
| **EJERCICIO INDIVIDUAL** | Spark SQL sobre dataset de viajes | 15 min | Individual |
| **CIERRE** | Síntesis + Metacognición + Tarea | 10 min | Docente |
| **TOTAL** | | **195 min** | |

---

## 1. INICIO (20 min) {#inicio}

### a) ROMPE-HIELO: "El cuello de botella humano" (5 min)

**Instrucción verbal exacta al docente:**

> *"Vamos a hacer un experimento rápido. Imaginen que tienen que leer y sumar los montos de 1 millón de recibos de Yape. Solo una persona puede hacerlo. ¿Cuánto tardaría?"*
> 
> *(Esperar respuestas: semanas, meses)*
> 
> *"¿Qué pasaría si fueran 1,000 personas haciendo la tarea en paralelo, cada una con su parte?"*
> 
> *(Esperar respuesta: 1,000 veces más rápido)*
> 
> *"Exactamente. Eso es MapReduce. Ahora, ¿qué pasaría si además pudiéramos guardar los resultados parciales en RAM en lugar de escribirlos en disco entre cada paso?"*
> 
> *(Esperar respuesta: aún más rápido)*
> 
> *"Eso es Apache Spark. Hoy vamos a ver cómo pasamos de leer recibos a analizar millones de transacciones en segundos. Abramos Databricks."*

---

### b) LOGRO DE APRENDIZAJE (3 min)

**Guion verbal textual:**

> *"Al finalizar la sesión de hoy, ustedes van a poder hacer tres cosas concretas:"*
>
> *"Primero: explicar por qué Spark es hasta 100 veces más rápido que MapReduce con un argumento técnico específico, no solo decir 'usa la memoria'."*
>
> *"Segundo: escribir código PySpark que lee un dataset de millones de registros, lo filtra, lo transforma y produce un resultado analítico — todo en Databricks Community."*
>
> *"Tercero: distinguir cuándo usar procesamiento por lotes (batch) y cuándo usar procesamiento en streaming, con un ejemplo real del mundo empresarial peruano."*
>
> *"¿Alguien ya usó PySpark o Spark SQL antes de este curso? ¿No? Perfecto — hoy lo van a usar por primera vez."*

---

### c) REVISIÓN SESIÓN ANTERIOR (7 min)

**Pregunta 1:** *"La semana pasada vieron NoSQL y NewSQL. ¿Cuál es la diferencia entre MongoDB y CockroachDB para el caso de pagos?"*

> **Respuesta esperada:** MongoDB es documental y no garantiza ACID en operaciones multi-documento — útil para perfiles de comerciantes con esquema flexible. CockroachDB es NewSQL: combina ACID de bases relacionales con escala horizontal mediante el protocolo Raft. Para pagos donde no puede perderse dinero → CockroachDB. Para perfiles de comerciantes con atributos variables → MongoDB.
>
> **Si el estudiante responde mal** (ej: "MongoDB es más rápido"): *"¿Más rápido para qué operación específica? La velocidad depende del caso de uso. Para lectura de un documento completo, sí. Para una transacción que modifica múltiples cuentas con garantía ACID, CockroachDB es más confiable aunque sea ligeramente más lento. ¿Cuál es la diferencia en garantías?"*

**Pregunta 2:** *"El Teorema CAP dice que solo puedes tener 2 de 3 propiedades. Si Yape necesita que el sistema de pagos nunca pierda una transacción aunque la red falle, ¿qué combinación elige?"*

> **Respuesta esperada:** CP — Consistencia y Tolerancia a Particiones. Sacrifica Disponibilidad: si la red entre nodos falla, el sistema prefiere mostrar un error al usuario antes que procesar un pago con saldo desactualizado y potencialmente cobrar dos veces.
>
> **Si el estudiante responde "AP":** *"AP significa que el sistema sigue respondiendo aunque los datos puedan estar inconsistentes. ¿Qué pasaría si el saldo de Ana muestra S/200 en un nodo y S/100 en otro, y ambos aprueban un pago de S/150? ¿Quién tiene razón? Precisamente el problema CAP en pagos."*

**Pregunta 3:** *"¿Qué herramienta del ecosistema Hadoop usaríamos para mover el historial de transacciones de Oracle a HDFS?"*

> **Respuesta esperada:** Apache Sqoop. Funciona mediante conexiones JDBC paralelas: lanza múltiples mappers (jobs MapReduce) que cada uno lee un rango de filas de la tabla Oracle y lo escribe directamente en HDFS en formato Parquet o Avro. Con 16 mappers paralelos: 16 veces más rápido que una sola conexión.

---

### d) DIAGNÓSTICO INICIAL (5 min)

**Pregunta 1:** *"¿Cuántos conocen la diferencia entre procesamiento batch y procesamiento en tiempo real? Den un ejemplo de cada uno."*

> **Respuesta esperada:** Batch: procesar el cierre contable de todas las transacciones del día a las 11 PM (por lotes, diferido). Tiempo real: detectar una transacción fraudulenta en Yape y bloquearla antes de que se complete (streaming, milisegundos).

**Pregunta 2:** *"Si tengo 1 TB de datos de logs de navegación web y quiero encontrar las 10 páginas más visitadas, ¿qué operaciones necesito hacer?"*

> **Respuesta esperada:** Filtrar (quedarse con registros de páginas visitadas), Agrupar por URL, Contar visitas por URL, Ordenar de mayor a menor, Tomar los 10 primeros. Esto es exactamente un patrón MapReduce/Spark: Map (emitir URL de cada visita) → Reduce (contar por URL) → Sort → Top-K.

**Pregunta 3:** *"¿Databricks es solo para Python o también soporta SQL?"*

> **Respuesta esperada:** Databricks soporta Python (PySpark), Scala, R y SQL de forma nativa. En el mismo notebook puedes tener celdas `%python`, `%sql`, `%scala` alternadas. Internamente todo se convierte al mismo motor Spark — el lenguaje es solo la interfaz.

---

## 2. UTILIDAD (10 min) {#utilidad}

### Por qué este tema domina el mercado laboral de Data Engineering

**El problema que resuelve Spark:**

En 2012, el equipo de Yahoo! necesitaba ordenar 1 TB de datos. Con MapReduce: 62 minutos. El mismo algoritmo con Spark: 23 minutos. Para 100 TB: MapReduce tardó 72 minutos, Spark 23 minutos. El record mundial actual de sorting de 1 PB fue establecido por Spark en 2016 con 190 TB/min.

**Dato real de impacto:**

| Empresa | Uso de Spark | Escala |
|---------|-------------|--------|
| Netflix | Recomendaciones personalizadas | 100M+ usuarios, modelos actualizados diariamente |
| Uber | Surge pricing en tiempo real | 18M viajes/día calculando precio dinámico |
| Alibaba | Singles Day 11/11 | 32 PB procesados en 24 horas |
| BCP Perú | Detección de fraude | 5M transacciones/día procesadas con Spark |
| Rappi | Recomendaciones de restaurantes | Streaming de pedidos en tiempo real |

**Pregunta retadora:**

*"MapReduce existe desde 2004 y resuelve el mismo problema. Tenemos Hadoop, tenemos HDFS — ¿para qué necesitamos otro framework? ¿No es reinventar la rueda?"*

> **Respuesta esperada (tensión cognitiva):** MapReduce escribe los resultados intermedios en disco entre cada etapa Map y Reduce. Si un algoritmo de machine learning necesita 100 iteraciones sobre los datos (como k-means), MapReduce lee y escribe en disco 100 veces → latencia de horas. Spark guarda los resultados intermedios en RAM (RDD en memoria) → las 100 iteraciones leen de RAM → 100x más rápido para cargas de trabajo iterativas. No es reinventar la rueda: es cambiar el material de la rueda de piedra a carbono.

---

## 3. TRANSFORMACIÓN (70 min) {#transformacion}

### SUBTEMA 3.1 — Las limitaciones de MapReduce y el nacimiento de Spark (15 min)

**Explicación conceptual:**

MapReduce fue revolucionario en 2004 pero tiene limitaciones estructurales:

```
PROBLEMA DE MAPREDUCE: ESCRITURA EN DISCO ENTRE ETAPAS

Iteración 1:  [Datos] → [Map] → [Disco] → [Reduce] → [Disco]
Iteración 2:  [Disco] → [Map] → [Disco] → [Reduce] → [Disco]
Iteración 3:  [Disco] → [Map] → [Disco] → [Reduce] → [Disco]
...
Iteración N:  [Disco] → [Map] → [Disco] → [Reduce] → [Disco]

Problema: Cada iteración = 2 lecturas + 2 escrituras a disco
```

```
SOLUCIÓN SPARK: DAG EN MEMORIA

[Datos HDFS] → [RDD 1 en RAM] → [RDD 2 en RAM] → [RDD 3 en RAM] → [Resultado]
                    ↑ transformación lazy — no se ejecuta hasta que se pide el resultado
```

**Arquitectura Spark:**

```
╔══════════════════════════════════════════════╗
║           DRIVER PROGRAM (tu código)          ║
║    SparkContext / SparkSession                ║
║    Crea el plan de ejecución (DAG)            ║
╚══════════╦═══════════════════════════════════╝
           ║ instruye
    ╔══════╩══════╗
    ║   CLUSTER    ║
    ║   MANAGER    ║  ← YARN / Kubernetes / Spark Standalone
    ╚══════╦══════╝
           ║ asigna
    ┌──────┴──────┐
    │   EXECUTOR  │   EXECUTOR   │   EXECUTOR   │
    │  (Worker 1) │  (Worker 2)  │  (Worker 3)  │
    │  Tarea 1    │  Tarea 2     │  Tarea 3     │
    │  Tarea 4    │  Tarea 5     │  Tarea 6     │
    └─────────────┘──────────────┘──────────────┘
```

**Pregunta al grupo 1:**

*"En la arquitectura que ven en el diagrama, ¿quién es el equivalente al NameNode de HDFS en Spark?"*

> **Respuesta esperada:** El Driver Program con el SparkContext es el equivalente al NameNode: es el nodo central que conoce el plan completo de ejecución (el DAG), sabe qué tareas asignar a qué Executor y coordina el progreso. Los Executors son equivalentes a los DataNodes: hacen el trabajo real de procesamiento sobre particiones de los datos. La diferencia clave: en HDFS el NameNode guarda metadatos de almacenamiento; en Spark el Driver guarda el plan de computación.
>
> **Si el estudiante dice "el Cluster Manager":** *"El Cluster Manager administra recursos del clúster (similar a YARN ResourceManager), pero no sabe qué hace el trabajo internamente. ¿Quién sí conoce toda la lógica del trabajo?"*

---

**Concepto: RDD vs DataFrame vs Dataset**

```python
# ╔══════════════════════════════════════════════════════════╗
# ║  EVOLUCIÓN DE LAS ABSTRACCIONES EN SPARK                 ║
# ╚══════════════════════════════════════════════════════════╝

# SPARK 1.x — RDD (Resilient Distributed Dataset)
# Capa más baja: control total, sin optimización automática
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rdd_pares = rdd.filter(lambda x: x % 2 == 0)      # Transformación (lazy)
rdd_cuadrados = rdd_pares.map(lambda x: x ** 2)    # Transformación (lazy)
resultado = rdd_cuadrados.collect()                 # Acción → AQUÍ ejecuta todo
# [4, 16, 36, 64, 100]

# SPARK 2.x — DataFrame (el más usado hoy)
# Columnas nombradas + optimización Catalyst automática
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("S5Demo").getOrCreate()
df = spark.range(1, 11).withColumnRenamed("id", "numero")
df_resultado = df.filter(F.col("numero") % 2 == 0) \
                 .withColumn("cuadrado", F.col("numero") ** 2)
df_resultado.show()
# +------+--------+
# |numero|cuadrado|
# +------+--------+
# |     2|       4|
# |     4|      16|
# |     6|      36|
# |     8|      64|
# |    10|     100|
# +------+--------+
```

**Mini actividad (3 min):** *"En Databricks, ¿qué celda pueden crear para verificar que Spark está funcionando? Escriban `spark.version` y ejecútenlo."*

---

### SUBTEMA 3.2 — Transformaciones y Acciones: la clave de Spark (15 min)

**Explicación conceptual:**

En Spark, las operaciones se dividen en dos categorías fundamentales:

| Tipo | Característica | Cuándo se ejecuta | Ejemplos |
|------|---------------|-------------------|---------|
| **Transformaciones** | Lazy: definen el plan, no ejecutan | Cuando se llama una Acción | `filter()`, `map()`, `groupBy()`, `join()`, `select()` |
| **Acciones** | Ejecutan todo el DAG y devuelven resultado | Inmediatamente | `collect()`, `count()`, `show()`, `write()`, `first()` |

**Por qué lazy evaluation importa:**

```python
# SIN lazy evaluation (hipotético):
df_paso1 = df.filter(...)        # Lee 100M filas, filtra → 5M filas en memoria
df_paso2 = df_paso1.groupBy(...) # Procesa 5M filas
df_paso3 = df_paso2.orderBy(...) # Ordena
df_paso3.show(10)                # Solo necesito 10 filas!

# CON lazy evaluation (Spark real):
df_paso1 = df.filter(...)        # Solo registra "quiero filtrar" — NO ejecuta
df_paso2 = df_paso1.groupBy(...) # Solo registra "quiero agrupar" — NO ejecuta
df_paso3 = df_paso2.orderBy(...) # Solo registra "quiero ordenar" — NO ejecuta
df_paso3.show(10)                # AQUÍ: Catalyst Optimizer crea el plan óptimo
                                 # y ejecuta solo lo necesario para 10 filas
```

**Pregunta al grupo 2:**

*"Si escribo: `df.filter(col('precio') > 100).count()` — ¿cuántas veces lee los datos de HDFS?"*

> **Respuesta esperada:** Una sola vez. Spark con lazy evaluation espera hasta que llama `count()` (la acción) y entonces ejecuta el plan completo en un solo pasaje por los datos: lee el archivo de HDFS, aplica el filtro a medida que lee cada partición, y acumula el conteo. No materializa el DataFrame filtrado en memoria para luego contarlo — hace todo en el mismo pasaje. Esto se llama pipelining.
>
> **Si el estudiante dice "dos veces":** *"¿Por qué dos? El plan de ejecución dice: leer fila → filtrar → si pasa el filtro, agregar al conteo. Todo en una pasada. Compara con MapReduce donde tendrías que escribir el resultado del filtro a disco antes de contar."*

**Código ejecutable — transformaciones encadenadas:**

```python
# ============================================================
# DEMO: Pipeline de transformaciones Spark
# Caso: análisis de transacciones Yape del día
# ============================================================
from pyspark.sql import functions as F
from pyspark.sql.types import *

# Datos de ejemplo (en producción: leer de HDFS/Delta Lake)
datos_yape = [
    ("YP001", "2025-11-15", "persona_a_comercio", 85.50,  "Lima",     "completada"),
    ("YP002", "2025-11-15", "persona_a_persona",  12.00,  "Arequipa", "completada"),
    ("YP003", "2025-11-15", "retiro_bcp",        200.00,  "Lima",     "completada"),
    ("YP004", "2025-11-15", "persona_a_comercio",  5.00,  "Cusco",    "rechazada"),
    ("YP005", "2025-11-15", "persona_a_persona",  45.00,  "Lima",     "completada"),
    ("YP006", "2025-11-15", "persona_a_comercio", 320.00, "Lima",     "completada"),
    ("YP007", "2025-11-15", "retiro_bcp",         75.00,  "Trujillo", "completada"),
]
schema = StructType([
    StructField("id", StringType()),
    StructField("fecha", StringType()),
    StructField("tipo", StringType()),
    StructField("monto", DoubleType()),
    StructField("ciudad", StringType()),
    StructField("estado", StringType())
])

df = spark.createDataFrame(datos_yape, schema)

# Pipeline: solo completadas → agrupar por ciudad → calcular métricas
resultado = (
    df
    .filter(F.col("estado") == "completada")           # Transformación 1
    .groupBy("ciudad")                                  # Transformación 2
    .agg(
        F.count("*").alias("total_transacciones"),      # Transformación 3
        F.round(F.sum("monto"), 2).alias("volumen_soles"),
        F.round(F.avg("monto"), 2).alias("ticket_prom")
    )
    .orderBy(F.col("volumen_soles").desc())             # Transformación 4
)

resultado.show()   # ← ACCIÓN: aquí Spark ejecuta TODO el DAG
# +--------+--------------------+--------------+-----------+
# |ciudad  |total_transacciones |volumen_soles |ticket_prom|
# +--------+--------------------+--------------+-----------+
# |Lima    |                  4 |       642.50 |     160.63|
# |Arequipa|                  1 |        12.00 |      12.00|
# |Trujillo|                  1 |        75.00 |      75.00|
# +--------+--------------------+--------------+-----------+
```

---

### SUBTEMA 3.3 — Spark SQL: el lenguaje universal de Big Data (20 min)

**Explicación conceptual:**

Spark SQL permite usar sintaxis SQL estándar directamente sobre DataFrames de Spark. El motor interno (Catalyst Optimizer) convierte el SQL a un plan de ejecución optimizado — igual de rápido que escribir la API DataFrame.

```python
# ============================================================
# SPARK SQL: dos formas equivalentes de hacer lo mismo
# ============================================================

# FORMA 1: API DataFrame (Python)
resultado_api = df \
    .filter(F.col("estado") == "completada") \
    .groupBy("ciudad", "tipo") \
    .agg(F.sum("monto").alias("total")) \
    .filter(F.col("total") > 100)

# FORMA 2: SQL (igual de eficiente internamente)
df.createOrReplaceTempView("transacciones")   # Registrar como tabla SQL

resultado_sql = spark.sql("""
    SELECT 
        ciudad,
        tipo,
        SUM(monto) AS total
    FROM transacciones
    WHERE estado = 'completada'
    GROUP BY ciudad, tipo
    HAVING SUM(monto) > 100
    ORDER BY total DESC
""")

# Ambas producen exactamente el mismo resultado y el mismo plan de ejecución
resultado_api.show()
resultado_sql.show()
```

**Spark SQL vs SQL tradicional:**

| Característica | SQL Tradicional (Oracle/MySQL) | Spark SQL |
|----------------|-------------------------------|-----------|
| Datos | Tabla en 1 servidor (vertical) | Particiones en N nodos (horizontal) |
| Escala máxima | ~10 TB con buen hardware | Petabytes con más nodos |
| Latencia | Milisegundos (datos pequeños) | Segundos-minutos (datos masivos) |
| Fuentes | Solo tablas relacionales | Parquet, CSV, JSON, Delta, HDFS, S3 |
| Joins | En disco (hash join, index) | En memoria distribuida (sort-merge) |
| ACID | Garantizado | Con Delta Lake (Databricks) |

**Pregunta al grupo 3:**

*"Si ya tenemos Spark SQL que usa sintaxis SQL estándar, ¿por qué necesitaría seguir aprendiendo la API DataFrame de Python (PySpark)?"*

> **Respuesta esperada:** SQL es declarativo (dices QUÉ quieres) pero tiene limitaciones para lógica programática compleja: no puedes hacer loops, condicionales complejos, llamar APIs externas, o aplicar modelos de ML dentro de un SELECT. La API DataFrame permite combinar el poder de SQL con la programación Python: puedes iterar, crear funciones UDF (User Defined Functions), aplicar un modelo de scikit-learn columna por columna, o construir pipelines dinámicos donde las columnas a procesar se determinan en tiempo de ejecución. En práctica: SQL para análisis exploratorio y reportes, PySpark para pipelines de producción complejos.

**Ejemplo avanzado: UDF (User Defined Function)**

```python
# ============================================================
# UDF: aplicar lógica Python custom dentro de Spark SQL
# Caso: clasificar transacciones Yape por riesgo de fraude
# ============================================================
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

@udf(returnType=StringType())
def clasificar_riesgo(monto: float, tipo: str) -> str:
    """Heurística simple de riesgo — en producción: modelo ML."""
    if monto > 500 and tipo == "persona_a_persona":
        return "ALTO"
    elif monto > 200:
        return "MEDIO"
    else:
        return "BAJO"

# Aplicar la UDF al DataFrame
df_con_riesgo = df.withColumn(
    "nivel_riesgo",
    clasificar_riesgo(F.col("monto"), F.col("tipo"))
)

# Ahora se puede usar en SQL también
df_con_riesgo.createOrReplaceTempView("transacciones_riesgo")
spark.sql("""
    SELECT nivel_riesgo, COUNT(*) as total, ROUND(SUM(monto), 2) as volumen
    FROM transacciones_riesgo
    GROUP BY nivel_riesgo
    ORDER BY volumen DESC
""").show()
```

**Pregunta al grupo 4:**

*"¿Cuál es la limitación de las UDFs en Spark comparadas con las funciones nativas de Spark como `F.sum()` o `F.when()`?"*

> **Respuesta esperada:** Las UDFs en PySpark se ejecutan fila por fila en el proceso Python del Executor, rompiendo la ejecución vectorizada de Spark. El Catalyst Optimizer no puede optimizar el interior de una UDF (no sabe qué hace). Las funciones nativas de Spark (`F.sum`, `F.when`, `F.col`) son vectorizadas (operan en lotes de datos) y Catalyst puede reordenarlas, eliminarlas si no se usan o combinarlas. Resultado: una UDF Python puede ser 2-10x más lenta que la función nativa equivalente. Solución: usar Pandas UDFs (también llamadas vectorized UDFs) con `@pandas_udf` que sí operan en vectores.

---

## RECESO (20 min) ☕

---

### SUBTEMA 3.4 — Structured Streaming: Spark para datos en tiempo real (25 min)

**Explicación conceptual:**

Apache Spark Structured Streaming trata un stream de datos como una tabla que crece infinitamente. Cada micro-batch (cada pocos segundos) agrega nuevas filas a esa tabla y re-ejecuta la query.

```
MODELO CONCEPTUAL DE STRUCTURED STREAMING:

Tiempo:  T=0      T=1      T=2      T=3      T=4
         ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
Evento:  │YP001│  │YP002│  │YP003│  │YP004│  │YP005│
         │YP006│  │YP007│  │YP008│  │YP009│  │YP010│
         └─────┘  └─────┘  └─────┘  └─────┘  └─────┘

Spark ve esto como:
┌────────────────────────────────────────────────────┐
│ "Tabla infinita" de transacciones                  │
│ YP001, YP002, YP003, YP004, YP005, YP006, ...     │
│ La query SQL/DataFrame se re-ejecuta cada N seg    │
└────────────────────────────────────────────────────┘

Output modes:
- append:   Solo nuevas filas desde el último trigger
- complete: La tabla completa del resultado re-calculada
- update:   Solo filas que cambiaron
```

**Código de Structured Streaming en Databricks:**

```python
# ============================================================
# STRUCTURED STREAMING: simular transacciones en tiempo real
# En Databricks Community: usar "rate" source para demos
# En producción: Kafka, Kinesis, EventHub
# ============================================================

# Source: rate genera N filas por segundo automáticamente
streaming_df = (
    spark.readStream
    .format("rate")                     # Genera datos automáticamente
    .option("rowsPerSecond", 100)       # 100 filas/segundo
    .load()
)

# El DataFrame streaming tiene: timestamp (cuando llegó) y value (número secuencial)
# En producción: .format("kafka") con topic de transacciones Yape

# Aplicar la misma lógica analítica que en batch
from pyspark.sql.functions import window, count, expr

resultado_stream = (
    streaming_df
    .withColumn("monto_simulado", (F.col("value") % 500 + 1).cast("double"))
    .withColumn("es_alto_valor", F.col("monto_simulado") > 300)
    .groupBy(
        window(F.col("timestamp"), "10 seconds"),  # Ventana de 10 segundos
    )
    .agg(
        count("*").alias("transacciones_ventana"),
        F.sum("monto_simulado").alias("volumen_ventana"),
        F.sum(F.col("es_alto_valor").cast("int")).alias("alto_valor")
    )
)

# Escribir el resultado (en Databricks: mostrar en pantalla)
query = (
    resultado_stream
    .writeStream
    .format("memory")               # En memoria (para demo)
    .queryName("yape_stream")       # Nombre de la tabla temporal
    .outputMode("complete")         # Muestra resultado completo
    .start()
)

# Ver resultados en tiempo real
import time
for i in range(5):
    spark.sql("SELECT * FROM yape_stream ORDER BY window.start DESC LIMIT 5").show(truncate=False)
    time.sleep(5)

query.stop()
```

**Casos de uso reales de Streaming:**

| Empresa | Caso de uso Streaming | Tecnología |
|---------|----------------------|-----------|
| Uber | Surge pricing: detecta zonas de alta demanda en tiempo real cada 5 min | Spark Streaming + Kafka |
| BCP Perú | Detección de fraude: alerta si una tarjeta se usa en Lima y Tokio en 10 min | Spark Streaming + Flink |
| Twitter/X | Trending topics: qué hashtag crece más rápido en los últimos 15 min | Spark Streaming |
| Netflix | Dashboard de engagement: cuántas personas ven qué en este momento | Spark Streaming + Kafka |
| Rappi Perú | ETA en tiempo real: recalcular el tiempo de entrega cada 30 seg | Flink (evolución del streaming) |

**Pregunta al grupo 5:**

*"¿Cuál es la diferencia entre usar `append` y `complete` como output mode en Structured Streaming?"*

> **Respuesta esperada:** `append` solo escribe las filas nuevas desde el último micro-batch — eficiente para casos donde cada evento es independiente (ej: log de cada transacción). `complete` re-escribe el resultado completo en cada trigger — necesario cuando el resultado depende de TODOS los eventos acumulados (ej: el contador total de transacciones por ciudad: cuando llega una nueva transacción de Lima, el total de Lima cambia, necesito reescribir Lima). Para agregaciones acumulativas (SUM, COUNT sobre ventanas deslizantes) se usa `update` o `complete`. Para inserts simples sin agregación: `append`.

---

### SUBTEMA 3.5 — GraphX: procesamiento de grafos distribuido (20 min)

**Explicación conceptual:**

GraphX es la API de Spark para procesar grafos (nodos + aristas) a escala distribuida. Útil para: detección de comunidades, recomendaciones, análisis de redes de fraude.

```
GRAFO DE TRANSACCIONES YAPE (detección de fraude):

       [ANA]━━━━━━━S/500━━━━━━━>[JUAN]━━━━━━━S/490━━━━━━━>[PEDRO]
         ▲                                                     │
         │                                                     │
         └─────────────────S/480──────────────────────────────┘

Ciclo detectado: ANA → JUAN → PEDRO → ANA (posible lavado de dinero)
GraphX puede detectar este patrón en millones de cuentas en segundos
```

**Código GraphX con PySpark + GraphFrames:**

```python
# ============================================================
# GRAPHX via GraphFrames: red de transacciones para fraude
# En Databricks: ya viene instalado. En Colab: !pip install graphframes
# ============================================================
from graphframes import GraphFrame

# Crear nodos (vértices): cuentas Yape
vertices = spark.createDataFrame([
    ("USR001", "Ana García",    "Lima"),
    ("USR002", "Juan Quispe",   "Lima"),
    ("USR003", "Pedro Mamani",  "Cusco"),
    ("USR004", "María Torres",  "Arequipa"),
    ("USR005", "Carlos López",  "Lima"),
], ["id", "nombre", "ciudad"])

# Crear aristas: transacciones entre cuentas
edges = spark.createDataFrame([
    ("USR001", "USR002", 500.0,  "2025-11-15 14:22"),  # Ana → Juan
    ("USR002", "USR003", 490.0,  "2025-11-15 14:25"),  # Juan → Pedro
    ("USR003", "USR001", 480.0,  "2025-11-15 14:28"),  # Pedro → Ana (ciclo!)
    ("USR001", "USR004", 150.0,  "2025-11-15 09:10"),  # Ana → María (normal)
    ("USR005", "USR001", 200.0,  "2025-11-15 11:00"),  # Carlos → Ana (normal)
], ["src", "dst", "monto", "timestamp"])

# Crear el grafo
g = GraphFrame(vertices, edges)

# Algoritmo PageRank: cuentas que reciben muchas transferencias tienen mayor rank
results = g.pageRank(resetProbability=0.15, maxIter=10)
print("=== PageRank — Cuentas con mayor centralidad (posibles muleros) ===")
results.vertices.select("id", "nombre", "pagerank") \
    .orderBy("pagerank", ascending=False).show()

# BFS (Breadth-First Search): encontrar caminos entre dos cuentas
print("=== Camino de USR001 a USR003 (¿hay conexión indirecta?) ===")
paths = g.bfs("id = 'USR001'", "id = 'USR003'")
paths.show()
```

**Pregunta al grupo 6:**

*"¿Por qué es difícil detectar el ciclo ANA→JUAN→PEDRO→ANA usando SQL tradicional con JOINs?"*

> **Respuesta esperada:** En SQL, para detectar un ciclo de 3 saltos necesitas 3 JOINs auto-referenciales sobre la misma tabla: `SELECT * FROM transacciones t1 JOIN transacciones t2 ON t1.dst = t2.src JOIN transacciones t3 ON t2.dst = t3.src WHERE t3.dst = t1.src`. Con 15M de cuentas Yape y 3.2M transacciones/día, ese triple JOIN genera combinaciones de 3.2M × 3.2M × 3.2M ≈ 3.3 × 10^19 operaciones. GraphX usa el algoritmo Pregel que propagación de mensajes entre nodos en paralelo — procesa el grafo en O(nodos × aristas) en lugar de O(aristas^k) para ciclos de largo k.

---

## 4. PRÁCTICA (40 min) {#practica}

### a) CASO PRÁCTICO GRUPAL: Análisis de Viajes Yango Perú (25 min)

**Escenario:**

Yango (subsidiaria de Yandex) opera en Lima con 50,000 viajes diarios. El equipo de Data Science necesita un pipeline Spark que analice los viajes de la semana para:
1. Identificar las zonas de mayor demanda por hora
2. Detectar conductores con rating < 3.5 (candidatos a suspensión)
3. Calcular el ingreso neto de Yango por comisión (25% del viaje)

**Dataset sintético para usar en Databricks (celda compartida por el docente):**

```python
# Dataset de viajes Yango Lima — copiar en Databricks
import numpy as np
from pyspark.sql.types import *

np.random.seed(2026)
n = 500

zonas = ["Miraflores", "San Isidro", "Barranco", "SJL", "Los Olivos",
         "Comas", "Ate", "Callao", "Villa El Salvador", "Surco"]
estados = ["completado", "completado", "completado", "cancelado", "en_curso"]

data_viajes = {
    "id_viaje":     [f"VJ{i:06d}" for i in range(1, n+1)],
    "zona_origen":  np.random.choice(zonas, n).tolist(),
    "zona_destino": np.random.choice(zonas, n).tolist(),
    "hora":         np.random.randint(0, 24, n).tolist(),
    "duracion_min": np.random.randint(5, 90, n).tolist(),
    "distancia_km": np.round(np.random.exponential(8, n), 1).tolist(),
    "tarifa_soles": np.round(np.random.uniform(8, 80, n), 2).tolist(),
    "id_conductor": [f"CON{np.random.randint(1, 50):03d}" for _ in range(n)],
    "rating_viaje": np.round(np.random.normal(4.2, 0.6, n).clip(1, 5), 1).tolist(),
    "estado":       np.random.choice(estados, n, p=[0.75, 0.1, 0.05, 0.08, 0.02]).tolist()
}

schema_yango = StructType([
    StructField("id_viaje",      StringType()),
    StructField("zona_origen",   StringType()),
    StructField("zona_destino",  StringType()),
    StructField("hora",          IntegerType()),
    StructField("duracion_min",  IntegerType()),
    StructField("distancia_km",  DoubleType()),
    StructField("tarifa_soles",  DoubleType()),
    StructField("id_conductor",  StringType()),
    StructField("rating_viaje",  DoubleType()),
    StructField("estado",        StringType())
])

df_yango = spark.createDataFrame(
    [(v["id_viaje"], v["zona_origen"], v["zona_destino"], 
      v["hora"], v["duracion_min"], v["distancia_km"],
      v["tarifa_soles"], v["id_conductor"], v["rating_viaje"], v["estado"])
     for v in [dict(zip(data_viajes.keys(), vals)) 
               for vals in zip(*data_viajes.values())]],
    schema_yango
)
df_yango.createOrReplaceTempView("viajes_yango")
print(f"Dataset cargado: {df_yango.count()} viajes")
df_yango.show(5)
```

**Preguntas que los grupos responden en 20 min:**

```python
# PREGUNTA 1: Top 5 zonas por número de viajes completados
# Escribir en Spark SQL o DataFrame API

# PREGUNTA 2: Conductores con rating promedio < 3.5 y más de 3 viajes
# (candidatos a suspensión)

# PREGUNTA 3: Ingreso neto de Yango (25% de comisión sobre viajes completados)
# Agrupar por hora del día para ver cuándo genera más ingresos
```

**Preguntas de andamiaje del docente:**

- *"¿Cómo filtran solo los viajes 'completados' antes de calcular ingresos?"*
- *"Para el conductor con rating < 3.5, ¿necesitan HAVING o WHERE?"*
- *"¿Spark SQL o PySpark para esta tarea? ¿Por qué eligen uno?"*

**Puesta en común — respuesta modelo:**

```python
# SOLUCIÓN PREGUNTA 1
spark.sql("""
    SELECT zona_origen, COUNT(*) as total_viajes,
           ROUND(AVG(tarifa_soles), 2) as tarifa_prom
    FROM viajes_yango
    WHERE estado = 'completado'
    GROUP BY zona_origen
    ORDER BY total_viajes DESC
    LIMIT 5
""").show()

# SOLUCIÓN PREGUNTA 2
spark.sql("""
    SELECT id_conductor,
           COUNT(*) as total_viajes,
           ROUND(AVG(rating_viaje), 2) as rating_prom
    FROM viajes_yango
    WHERE estado = 'completado'
    GROUP BY id_conductor
    HAVING AVG(rating_viaje) < 3.5 AND COUNT(*) >= 3
    ORDER BY rating_prom ASC
""").show()

# SOLUCIÓN PREGUNTA 3
spark.sql("""
    SELECT hora,
           COUNT(*) as viajes_hora,
           ROUND(SUM(tarifa_soles), 2) as facturacion_total,
           ROUND(SUM(tarifa_soles) * 0.25, 2) as comision_yango
    FROM viajes_yango
    WHERE estado = 'completado'
    GROUP BY hora
    ORDER BY comision_yango DESC
    LIMIT 8
""").show()
```

---

### b) EJERCICIO INDIVIDUAL (15 min)

**Tarea:** Usando el mismo dataset de Yango, escribe una query Spark SQL que responda:

*"¿Cuál es el promedio de duración (minutos) y distancia (km) de los viajes por zona de DESTINO, solo para viajes completados que tuvieron más de 10 minutos? Ordena por promedio de duración descendente. Muestra solo zonas con más de 5 viajes."*

```python
# Escribe tu solución aquí:
spark.sql("""
    -- TU QUERY AQUÍ
""").show()
```

**Criterio de éxito:** La query devuelve una tabla con 4 columnas (zona_destino, total_viajes, duracion_prom, distancia_prom) con máximo 10 filas, donde total_viajes > 5 en todas las filas.

**Solución esperada:**
```sql
SELECT 
    zona_destino,
    COUNT(*) as total_viajes,
    ROUND(AVG(duracion_min), 1) as duracion_prom,
    ROUND(AVG(distancia_km), 1) as distancia_prom
FROM viajes_yango
WHERE estado = 'completado' AND duracion_min > 10
GROUP BY zona_destino
HAVING COUNT(*) > 5
ORDER BY duracion_prom DESC
```

---

## 5. CIERRE (10 min) {#cierre}

### a) SÍNTESIS COLABORATIVA (4 min)

**Pregunta 7:** *"En una frase: ¿cuál es LA razón por la que Spark es más rápido que MapReduce?"*

> **Respuesta esperada:** Spark guarda los datos intermedios en memoria RAM (RDD/DataFrame en caché) en lugar de escribirlos a disco entre cada etapa — para algoritmos iterativos esto es 10-100x más rápido.

**Pregunta 8:** *"¿Cuándo NO usarías Spark y preferirías MapReduce o incluso SQL tradicional?"*

> **Respuesta esperada:** Para trabajos que se ejecutan una sola vez sin iteración (ej: una exportación de datos simple), MapReduce puede ser suficiente. Para datos que caben en una sola máquina (<100 GB), SQL tradicional con PostgreSQL o DuckDB es más rápido y más fácil. Spark brilla con: datos que no caben en 1 máquina, algoritmos iterativos (ML), y procesamiento en streaming.

**Pregunta 9:** *"Nombren 2 diferencias entre Spark batch y Spark Streaming."*

> **Respuesta esperada:** (1) Batch procesa un dataset finito y termina; Streaming procesa un flujo infinito y corre continuamente. (2) Batch puede ordenar globalmente los datos; Streaming solo puede operar en ventanas de tiempo (no puede ordenar lo que aún no llegó). (3) Batch tiene latencia de minutos; Streaming tiene latencia de milisegundos a segundos.

---

### b) METACOGNICIÓN (3 min)

*"Antes de cerrar, en silencio respondan internamente estas tres preguntas:"*

1. *"¿Qué concepto de hoy entendí bien y podría explicarle a un compañero en 2 minutos?"*
2. *"¿Qué concepto me quedó incompleto y necesito repasar antes del laboratorio?"*
3. *"¿En cuál de sus proyectos grupales podrían aplicar Spark SQL esta semana?"*

---

### c) TAREA / PUENTE (3 min)

**Tarea para el laboratorio en casa:**

> *"Para el laboratorio de esta semana van a implementar un pipeline completo en Databricks: Bronze→Silver→Gold con PySpark + Spark SQL sobre un dataset de 10,000 viajes de taxi en Lima. El laboratorio tiene código base — ustedes completan las partes marcadas con `___`. Necesitan tener Databricks Community Edition activo."*

**Puente con la semana siguiente:**

> *"La próxima semana veremos Machine Learning en Big Data. Spark tiene un módulo llamado MLlib que permite entrenar modelos de ML sobre datos distribuidos. ¿Alguien puede adivinar cómo funciona entrenar un modelo de regresión lineal cuando los datos no caben en una sola máquina?"*

---

## GUION VERBAL SUGERIDO {#guion}

**Transición de MapReduce a Spark:**
> *"Imaginen que tienen que cocinar para 1,000 personas. MapReduce es como cocinar un plato, guardarlo en el frigorífico, sacarlo, cocinarlo otro rato, guardarlo, sacarlo de nuevo — muchos viajes al frigorífico. Spark es como tener los ingredientes y el plato siempre en la mesa de trabajo — sin frigorífico entre pasos. ¿Cuál es más rápido?"*

**Explicando lazy evaluation:**
> *"Cuando le digo a Spark `filter`, `groupBy`, `orderBy` — Spark no hace nada. Es como un cocinero que escucha todas las instrucciones antes de empezar. Cuando finalmente digo `show()` — ahí empieza, y ya sabe exactamente el plan más eficiente. Comparen con alguien que ejecuta cada instrucción inmediatamente sin pensar en el plan completo."*

**Abriendo Databricks:**
> *"Vayan a community.cloud.databricks.com, entren con su cuenta, y abran el notebook `M1_INTRODUCCION_SPARK` que cargamos la semana pasada. Si no lo tienen: New → Notebook → seleccionen Python → y nombre S5_Spark_Demo."*

---

## CASOS REALES RECOMENDADOS {#casos}

1. **Netflix y Spark (2015):** Netflix migró su pipeline de recomendaciones de Hadoop MapReduce a Spark, reduciendo el tiempo de entrenamiento del modelo de 24 horas a 4 horas. El sistema genera recomendaciones personalizadas para 200M usuarios. Fuente: Netflix Tech Blog, 2015.

2. **Uber y Spark Streaming:** Uber usa Spark Streaming junto con Apache Kafka para calcular el surge pricing (precio dinámico) en tiempo real. Cada 5 minutos, analiza la demanda en 4,000 zonas de Manhattan simultáneamente y ajusta los precios. Escala: 18M viajes/día. Fuente: Uber Engineering Blog.

3. **Alibaba en el 11/11:** En el Singles Day 2020, Alibaba procesó 32 PB de datos de transacciones en 24 horas usando Spark. En el pico: 583,000 pedidos por segundo. Spark manejó la agregación en tiempo real del dashboard ejecutivo. Fuente: Alibaba Cloud, 2020.

4. **BCP y detección de fraude:** El Banco de Crédito del Perú (BCP) implementó un sistema de detección de fraude en tiempo real usando Spark Streaming y modelos de ML. Procesa 5M transacciones diarias y alerta en < 200ms cuando detecta patrones anómalos. Fuente: presentación DataLatam 2022.

5. **LinkedIn y GraphX:** LinkedIn usa GraphX (ahora migrado a GraphFrames) para calcular el "grado de separación" entre profesionales y recomendar conexiones de 2do y 3er grado. La red tiene 900M nodos y billones de aristas. GraphX procesa el grafo completo en horas. Fuente: LinkedIn Engineering Blog.

---

## EVALUACIÓN FORMATIVA

| Momento | Herramienta | Indicador de comprensión |
|---------|-------------|-------------------------|
| Inicio | Preguntas orales sobre S4 | Responde correctamente 2/3 preguntas de revisión |
| Transformación 3.2 | Mini actividad `spark.version` | Celda ejecutada sin error |
| Transformación 3.3 | Pregunta sobre UDF | Menciona pérdida de vectorización |
| Práctica | Ejercicio individual Yango | Query con HAVING y GROUP BY correcto |
| Cierre | 3 preguntas síntesis | Responde diferencia batch vs streaming |

---

## REFERENCIAS APA 7 {#referencias}

Chambers, B., & Zaharia, M. (2018). *Spark: The definitive guide*. O'Reilly Media.

Damji, J., Wenig, B., Das, T., & Lee, D. (2020). *Learning Spark: Lightning-fast data analytics* (2nd ed.). O'Reilly Media.

Karau, H., Konwinski, A., Wendell, P., & Zaharia, M. (2015). *Learning Spark* (1st ed.). O'Reilly Media.

Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

Zaharia, M., Chowdhury, M., Das, T., Dave, A., Ma, J., McCauley, M., Franklin, M. J., Shenker, S., & Stoica, I. (2012). Resilient distributed datasets: A fault-tolerant abstraction for in-memory cluster computing. *Proceedings of the 9th USENIX Symposium on Networked Systems Design and Implementation*, 15–28.

Apache Spark. (2024). *Spark SQL, DataFrames and Datasets Guide*. https://spark.apache.org/docs/latest/sql-programming-guide.html

Apache Spark. (2024). *Structured Streaming Programming Guide*. https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay*
