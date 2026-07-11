# SEMANA 2 — COMPUTACIÓN EN LA NUBE + HADOOP + HDFS + MAPREDUCE + HBASE
## Big Data (DD283) | Universidad Autónoma del Perú

---

# PARTE A — GUÍA DE SESIÓN 

**Duración**: 3 horas  
**Resultado**: El estudiante describe una propuesta de arquitectura de Big Data para la nube y procesa un archivo distribuido usando Hadoop con integridad.

## APERTURA (15 min) — Warm-Up

**Pregunta gancho**:
> "La semana pasada diseñaron una arquitectura. Hoy van a ver cómo funciona por dentro. Si tuvieras que guardar 1 MILLÓN de archivos, ¿los guardarías todos en la misma carpeta? ¿Por qué no?"

**Demostración de velocidad** (ejecutar en vivo):
```bash
# En local: contar palabras en un archivo pequeño vs. distribuido
# Mostrar el tiempo con time command
time cat grande.txt | tr ' ' '\n' | sort | uniq -c | sort -rn | head -10
```
Pregunta: "¿Cómo escala esto si el archivo tiene 1 TB?"

## TEORÍA (45 min)

### Bloque 1: Cloud para Big Data (15 min)

**Los 3 grandes proveedores**:
| | AWS | Azure | GCP |
|--|-----|-------|-----|
| Servicio Big Data | EMR | HDInsight | Dataproc |
| Data Warehouse | Redshift | Synapse | BigQuery |
| Data Lake | S3 | ADLS | Cloud Storage |
| Streaming | Kinesis | Event Hub | Pub/Sub |
| Free tier | 1 año | 200 USD crédito | 300 USD crédito |

**¿Qué es la Computación en la Niebla (Fog Computing)?**
- Edge Computing: procesamiento cerca de la fuente de datos
- Ejemplo: cámara de seguridad con IA local en una tienda → no necesita enviar video completo a la nube
- Reduce latencia y ancho de banda

### Bloque 2: HADOOP — El ecosistema (20 min)

**La historia de Hadoop** (contar como historia):
> "En 2003, Google tenía un problema: tenía más datos de los que nadie había tenido. Publicaron 2 papers: GFS (Google File System) y MapReduce. Doug Cutting y Mike Cafarella los leyeron y crearon Hadoop en su tiempo libre. El nombre viene del elefante de juguete del hijo de Doug."

**Los 4 pilares de Hadoop**:

```
HADOOP ECOSYSTEM
├── HDFS (Hadoop Distributed File System)
│   ├── NameNode: el directorio (sabe dónde están los datos)
│   └── DataNodes: donde viven los datos reales (bloques de 128MB)
│
├── MapReduce (el motor de procesamiento)
│   ├── Map: divide y procesa en paralelo
│   └── Reduce: combina los resultados
│
├── YARN (Yet Another Resource Negotiator)
│   ├── ResourceManager: administra los recursos del cluster
│   └── NodeManager: administra recursos por nodo
│
└── Common (librerías compartidas)
```

**HDFS en detalle — dibujar en pizarrón**:
```
Cliente quiere guardar un archivo de 300MB:
  → HDFS lo divide en bloques de 128MB
  → Bloque 1 (128MB): guardado en Nodo1, Nodo3, Nodo5 (3 réplicas)
  → Bloque 2 (128MB): guardado en Nodo2, Nodo4, Nodo6 (3 réplicas)  
  → Bloque 3 (44MB):  guardado en Nodo1, Nodo4, Nodo2 (3 réplicas)

Si Nodo1 falla → los datos siguen en Nodo3 y Nodo5 → SIN PÉRDIDA DE DATOS
```

**MapReduce — Word Count como ejemplo canónico**:
```
TEXTO: "el cielo es azul el sol es amarillo el cielo brilla"

MAP (divide y cuenta):
  Nodo1: "el"→1, "cielo"→1, "es"→1, "azul"→1
  Nodo2: "el"→1, "sol"→1, "es"→1, "amarillo"→1  
  Nodo3: "el"→1, "cielo"→1, "brilla"→1

SHUFFLE (reagrupa por clave):
  "el" → [1,1,1]
  "cielo" → [1,1]
  "es" → [1,1]

REDUCE (suma):
  "el" → 3
  "cielo" → 2
  "es" → 2
  "azul" → 1, "sol" → 1, "amarillo" → 1, "brilla" → 1
```

### Bloque 3: HBase (10 min)

**HBase = NoSQL columnar sobre HDFS**:
- Inspirado en Bigtable de Google
- Ideal para: datos de series de tiempo, logs, sensor data
- NO es reemplazante de SQL — es complementario

**Cuándo usar HBase vs. MongoDB vs. HDFS**:
| Caso de uso | HBase | MongoDB | HDFS |
|-------------|-------|---------|------|
| Datos de IoT en tiempo real | ✓✓ | ✓ | ✗ |
| Documentos JSON | ✗ | ✓✓ | ✗ |
| Análisis histórico masivo | ✓ | ✗ | ✓✓ |
| Búsqueda full-text | ✗ | ✗ | ✗ (usar Elasticsearch) |

## DEMO EN VIVO (50 min)

### Demo 1: Hadoop con Docker (30 min)

**Prerequisito**: Docker Desktop instalado y corriendo

```bash
# Paso 1: Descargar imagen de Hadoop
docker pull sequenceiq/hadoop-docker:2.7.0

# Paso 2: Iniciar contenedor
docker run -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash

# Dentro del contenedor:
# Paso 3: Ver el sistema de archivos HDFS
hdfs dfs -ls /

# Paso 4: Crear directorio en HDFS
hdfs dfs -mkdir /datos_curso
hdfs dfs -mkdir /datos_curso/entrada

# Paso 5: Crear archivo de texto local
echo "el big data es el futuro el futuro es ahora ahora aprendemos big data" > texto_prueba.txt
cat texto_prueba.txt

# Paso 6: Subir archivo a HDFS
hdfs dfs -put texto_prueba.txt /datos_curso/entrada/

# Paso 7: Verificar que se subió
hdfs dfs -ls /datos_curso/entrada/
hdfs dfs -cat /datos_curso/entrada/texto_prueba.txt

# Paso 8: Ejecutar Word Count (MapReduce incluido en Hadoop)
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar \
  wordcount /datos_curso/entrada/ /datos_curso/salida/

# Paso 9: Ver resultados
hdfs dfs -cat /datos_curso/salida/part-r-00000
```

**Output esperado**:
```
ahora   2
aprendemos  1
big     2
data    2
el      3
es      2
futuro  2
```

### Demo 2: PySpark como alternativa a MapReduce (20 min)
*(Para mostrar que Spark es más fácil)*

```python
# En Google Colab — instalar PySpark
!pip install pyspark -q

from pyspark.sql import SparkSession
from pyspark import SparkContext

# Crear contexto Spark
sc = SparkContext('local', 'WordCount')
spark = SparkSession(sc)

# Crear datos
texto = ["el big data es el futuro el futuro es ahora ahora aprendemos big data"]

# MapReduce en Spark (mucho más simple)
palabras = sc.parallelize(texto) \
    .flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .sortBy(lambda x: -x[1])

print("=== WORD COUNT CON SPARK ===")
for palabra, count in palabras.collect():
    print(f"  {palabra}: {count}")

sc.stop()
```

## TRABAJO COLABORATIVO (30 min)

**Actividad**: "Procesar datos del sector que tu grupo eligió para el proyecto"

Cada grupo debe:
1. Tomar el problema de su proyecto
2. Diseñar el flujo MapReduce que necesitarían: ¿Cuál sería el Map? ¿Cuál sería el Reduce?
3. Implementar un mini Word Count con los datos de su dominio (ej: contar palabras en tweets sobre su empresa)

## CIERRE (20 min)

**Tarea semana 3**:
1. Completar Guía de Trabajo S2 (preguntas teóricas)
2. Completar el Lab S2 (Word Count con Hadoop/PySpark)
3. Instalar MongoDB Compass o crear cuenta en MongoDB Atlas
4. Leer: Capítulo de Hadoop del libro "Big Data con Python" de Rafael Caballero

---

# PARTE B — GUÍA DE TRABAJO ESTUDIANTE S2

**Nombre**: _______________ | **Fecha entrega**: Antes de Semana 3 | **Individual**

## PREGUNTAS TEÓRICAS (10 preguntas)

# GUÍA DE TRABAJO S2 – BIG DATA
**Curso:** DD283 - Big Data  
**Alumno:** Javier Flores Condeña  
**Fecha:** 15/06/2026

---

# P1: HDFS vs. Sistema de Archivos Tradicional
Explica cómo almacena un archivo de 1 GB el sistema de archivos de tu laptop vs. cómo lo almacenaría HDFS. Usa un diagrama o esquema.

Un sistema de archivos tradicional almacena un archivo de 1 GB en un único disco físico. Si el disco falla, existe riesgo de pérdida de datos.

Por otro lado, HDFS divide el archivo en bloques y distribuye copias de cada bloque en distintos nodos del clúster.

## Sistema Tradicional

```text
+------------------+
| Archivo 1 GB     |
+------------------+
         |
         v
+------------------+
| Disco Local      |
+------------------+
```

## HDFS

```text
Archivo 1 GB

├── Bloque 1 (128 MB)
│    ├── Nodo 1
│    ├── Nodo 3
│    └── Nodo 5
│
├── Bloque 2 (128 MB)
│    ├── Nodo 2
│    ├── Nodo 4
│    └── Nodo 6
│
├── Bloque 3 (128 MB)
│    ├── Nodo 1
│    ├── Nodo 2
│    └── Nodo 4
│
└── ...
```

Si un nodo falla, las demás copias permiten mantener la disponibilidad de los datos.

---

# P2: NameNode y DataNodes
¿Qué pasaría si el NameNode de un clúster Hadoop falla? ¿Cómo soluciona Hadoop este problema? (pista: busca "Hadoop HA - High Availability")

El NameNode almacena los metadatos del clúster HDFS y conoce la ubicación de cada bloque.

Si el NameNode falla, el clúster pierde temporalmente la capacidad de localizar los archivos.

## Solución: Hadoop High Availability (HA)

```text
                +----------------+
                | Active NameNode|
                +----------------+
                        |
                        |
                +----------------+
                | Standby NameNode|
                +----------------+
                        |
       -----------------------------------
       |               |                |
+-------------+ +-------------+ +-------------+
| DataNode 1  | | DataNode 2  | | DataNode 3  |
+-------------+ +-------------+ +-------------+
```

Si el NameNode principal falla, el secundario asume automáticamente el control.

---

# P3: El algoritmo MapReduce
Explica con un ejemplo diferente al Word Count (usa algo de tu industria) cómo funcionaría el patrón Map → Shuffle → Reduce.

## Ejemplo: Ventas por categoría en una empresa retail

### Datos de entrada

```text
Venta 1 → Bebidas
Venta 2 → Lácteos
Venta 3 → Bebidas
Venta 4 → Limpieza
Venta 5 → Bebidas
```

### Fase MAP

```text
(Bebidas,1)
(Lácteos,1)
(Bebidas,1)
(Limpieza,1)
(Bebidas,1)
```

### Fase SHUFFLE

```text
Bebidas  → [1,1,1]
Lácteos  → [1]
Limpieza → [1]
```

### Fase REDUCE

```text
Bebidas  → 3
Lácteos  → 1
Limpieza → 1
```

Resultado: cantidad total de ventas por categoría.

---

# P4: YARN — El cerebro del clúster
¿Qué problema resolvió YARN en Hadoop 2.x que no existía en Hadoop 1.x? ¿Por qué fue tan importante este cambio?

En Hadoop 1.x, MapReduce era responsable tanto del procesamiento como de la gestión de recursos.

YARN introdujo una separación entre ambas funciones.

## Arquitectura simplificada

```text
                 +------------------+
                 | Resource Manager |
                 +------------------+
                          |
        -----------------------------------------
        |                  |                    |
+----------------+ +----------------+ +----------------+
| Node Manager 1 | | Node Manager 2 | | Node Manager 3 |
+----------------+ +----------------+ +----------------+
```

Gracias a YARN, aplicaciones como Spark, Hive y Tez pueden compartir el mismo clúster.

---

# P5: Replicación de datos
Si un bloque de HDFS tiene factor de replicación = 3 y el clúster tiene 5 nodos, ¿en cuántos nodos diferentes estará guardado ese bloque? ¿Si fallan 2 nodos simultáneamente, se pierden los datos?

Si el factor de replicación es 3 y existen 5 nodos:

```text
Bloque A

Nodo 1 ✓
Nodo 2 ✓
Nodo 3 ✓
Nodo 4
Nodo 5
```

El bloque estará almacenado en 3 nodos distintos.

Si fallan 2 nodos simultáneamente y queda al menos una réplica disponible, los datos no se pierden.

---

# P6: AWS vs Azure vs GCP para Big Data
Investiga: Si una empresa peruana quisiera migrar su data warehouse a la nube, ¿cuál proveedor recomendarías y por qué? Compara al menos en 3 dimensiones.

Recomendaría **Microsoft Azure** para una empresa peruana que desea migrar su Data Warehouse a la nube.

| Característica | AWS | Azure | GCP |
|---------------|------|--------|-----|
| Big Data | EMR | HDInsight | Dataproc |
| Data Warehouse | Redshift | Synapse | BigQuery |
| Integración Microsoft | Baja | Alta | Media |
| Power BI | Integración externa | Nativa | Integración externa |
| Adopción empresarial | Alta | Muy alta | Media |

## Justificación

1. Integración nativa con Active Directory.
2. Integración directa con Power BI.
3. Amplia adopción en empresas peruanas.

---

# P7: Computación en la Niebla (Fog Computing)
Da un ejemplo de un caso de uso real en Perú donde Fog Computing sería mejor solución que Cloud Computing. Justifica técnicamente.

## Caso de uso: Dollar City

Cámaras inteligentes para detección de robos en tiendas.

### Cloud Computing

```text
Cámara
   |
Internet
   |
Nube
   |
Análisis
```

### Fog Computing

```text
Cámara
   |
Servidor Local
   |
Análisis IA
   |
Nube (solo resultados)
```

### Beneficios

- Menor latencia.
- Menor consumo de ancho de banda.
- Respuesta en tiempo real.

---

# P8: HBase vs MySQL
Una empresa de telecomunicaciones necesita almacenar el historial de llamadas de 8 millones de clientes (última semana: 500M registros). ¿HBase o MySQL? ¿Por qué?

## Escenario

- 8 millones de clientes.
- 500 millones de registros semanales.

## Comparación

| Característica | HBase | MySQL |
|---------------|--------|--------|
| Escalabilidad horizontal | Sí | Limitada |
| Grandes volúmenes | Excelente | Regular |
| Escrituras masivas | Excelente | Media |
| Big Data | Sí | No |

Se recomienda **HBase**, ya que está diseñado para manejar grandes volúmenes de datos distribuidos.

---

# P9: El problema de los datos calientes
En un clúster HDFS, los datos más accedidos se convierten en "hot data". ¿Qué solución propone Hadoop para esto? ¿Cómo se llama esta optimización?

Los datos más consultados generan concentración de carga en ciertos nodos.

Hadoop utiliza:

- Replicación de bloques.
- Balanceo de carga.
- Data Locality.

## Data Locality

```text
Datos + Procesamiento

Nodo 1
├── Datos
└── Procesamiento

Nodo 2
├── Datos
└── Procesamiento
```

En lugar de mover los datos hacia el proceso, Hadoop mueve el proceso hacia donde están los datos.

Esto reduce tráfico de red y mejora el rendimiento.

---

# P10: Reflexión crítica
"Hadoop está muriendo. Spark lo reemplazó completamente." ¿Estás de acuerdo o en desacuerdo con esta afirmación? Argumenta con evidencia técnica.

## ¿Hadoop está muriendo?

No estoy de acuerdo con la afirmación de que Spark reemplazó completamente a Hadoop.

Spark es más rápido para procesamiento distribuido y análisis en memoria, pero Hadoop sigue siendo ampliamente utilizado mediante HDFS como plataforma de almacenamiento distribuido.

Actualmente muchas arquitecturas Big Data utilizan ambos componentes:

```text
           +---------+
           |  Spark  |
           +---------+
                |
                v
           +---------+
           |  HDFS   |
           +---------+
```

Por ello, Spark y Hadoop suelen ser tecnologías complementarias más que competidoras.

---

# PARTE C — LABORATORIO ESTUDIANTE S2

## Objetivo: Implementar Word Count con PySpark en Google Colab

### PASO 1: Configurar PySpark en Colab

```python
# Celda 1: Instalar PySpark
!pip install pyspark findspark -q
print("PySpark instalado!")
```

### PASO 2: Word Count básico

```python
# Celda 2: Word Count básico
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("WordCount_TuNombre") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

# TU TEXTO: Usa párrafos sobre la industria de tu proyecto
texto_negocio = """
[AQUI ESCRIBE 5-10 oraciones sobre la industria de tu proyecto de Big Data.
Ejemplo si tu proyecto es retail: 
Las ventas del retail peruano crecieron 15% en 2024. El comercio electrónico 
representa el 20% de las ventas totales. Los supermercados lideran las ventas online. 
La digitalización del retail es una tendencia imparable en Peru y Latinoamerica.]
"""

# Procesar con MapReduce
palabras_rdd = sc.parallelize([texto_negocio]) \
    .flatMap(lambda x: x.split()) \
    .map(lambda w: (w.lower().strip('.,!?'), 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .filter(lambda x: len(x[0]) > 3)  # filtrar palabras muy cortas
    
resultado = sorted(palabras_rdd.collect(), key=lambda x: -x[1])

print("=== TOP 20 PALABRAS MÁS FRECUENTES ===")
print(f"{'Palabra':<20} {'Frecuencia':>10}")
print("-" * 32)
for palabra, freq in resultado[:20]:
    print(f"{palabra:<20} {freq:>10}")
```

### PASO 3: Análisis de un dataset real con Spark SQL

```python
# Celda 3: Análisis con Spark SQL
import pandas as pd
import numpy as np

# Crear dataset de ventas (simula datos de tu empresa)
np.random.seed(42)
n = 100000  # 100K registros — ya es interesante para Spark

datos = {
    'fecha': pd.date_range('2024-01-01', periods=n, freq='min').astype(str),
    'producto': np.random.choice(['ProductoA', 'ProductoB', 'ProductoC', 'ProductoD'], n),
    'region': np.random.choice(['Lima', 'Arequipa', 'Trujillo', 'Cusco'], n, p=[0.5, 0.2, 0.2, 0.1]),
    'cantidad': np.random.randint(1, 50, n),
    'precio': np.random.uniform(10, 500, n).round(2),
    'canal': np.random.choice(['Online', 'Tienda', 'App_Movil'], n, p=[0.4, 0.4, 0.2])
}

pdf = pd.DataFrame(datos)
pdf['monto'] = pdf['cantidad'] * pdf['precio']

# Convertir a Spark DataFrame
df_spark = spark.createDataFrame(pdf)
df_spark.createOrReplaceTempView("ventas")

print(f"Dataset: {df_spark.count():,} registros cargados en Spark")
print(f"Schema:")
df_spark.printSchema()
```

```python
# Celda 4: Queries con Spark SQL
print("=== ANÁLISIS 1: Ventas totales por región ===")
spark.sql("""
    SELECT region, 
           COUNT(*) as num_transacciones,
           SUM(monto) as monto_total,
           AVG(monto) as ticket_promedio
    FROM ventas
    GROUP BY region
    ORDER BY monto_total DESC
""").show()

print("=== ANÁLISIS 2: Top 3 productos por canal ===")
spark.sql("""
    SELECT canal, producto, SUM(monto) as ventas
    FROM ventas
    GROUP BY canal, producto
    ORDER BY canal, ventas DESC
""").show(12)

print("=== ANÁLISIS 3: Ventas por hora del día ===")
spark.sql("""
    SELECT HOUR(CAST(fecha AS TIMESTAMP)) as hora,
           COUNT(*) as transacciones
    FROM ventas
    GROUP BY hora
    ORDER BY hora
""").show()
```

### PASO 4: Comparar velocidad Pandas vs. Spark

```python
# Celda 5: Benchmark — esto muestra el VALOR de Spark
import time

# Con Pandas
start = time.time()
resultado_pandas = pdf.groupby('region')['monto'].sum().sort_values(ascending=False)
tiempo_pandas = time.time() - start
print(f"Pandas: {tiempo_pandas*1000:.2f} ms")

# Con Spark
start = time.time()
resultado_spark = df_spark.groupBy('region').sum('monto').orderBy('sum(monto)', ascending=False)
resultado_spark.collect()  # forzar ejecución
tiempo_spark = time.time() - start
print(f"Spark: {tiempo_spark*1000:.2f} ms")

print(f"\nNota: Con 100K registros Pandas puede ser más rápido.")
print(f"Con 100M registros Spark sería 10-100x más rápido porque distribuye el trabajo.")
print(f"Esta es la clave de Big Data: escala a donde Pandas no puede llegar.")
```

### ENTREGABLES LAB S2:
- [ ] `lab_s2_wordcount_pyspark.ipynb` — Notebook completo ejecutado
- [ ] Análisis: ¿Qué palabras más frecuentes aparecieron en tu texto de negocio?

La palabra mas frecuente es "Ventas"

- [ ] Reflexión: ¿En qué momento Spark supera a Pandas? (escribe en una celda Markdown)

Con 100K registros Pandas puede ser más rápido.
Con 100M registros Spark sería 10-100x más rápido porque distribuye el trabajo.
Esta es la clave de Big Data: escala a donde Pandas no puede llegar.

---



## Error más común en el Lab S2:
**Error**: `java.lang.OutOfMemoryError: Java heap space`  
**Causa**: Colab tiene memoria limitada  
**Solución**: Reducir n a 10000 en vez de 100000, o reiniciar el kernel de Colab

## Criterio de evaluación Lab S2:
| Criterio | Puntos |
|---------|--------|
| Word Count ejecutado con texto propio del proyecto | 4 |
| Spark SQL queries ejecutadas correctamente | 7 |
| Benchmark Pandas vs. Spark con reflexión | 4 |
| Reflexión en Markdown sobre cuándo usar Spark | 5 |
| **TOTAL** | **20** |