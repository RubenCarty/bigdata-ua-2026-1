# S2 — LABORATORIO EN CASA
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Procesamiento Distribuido con PySpark en Databricks

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | LINDO BARRIENTOS JHONN VIEQUIER |
| **Código** | 2221896680 |
| **Fecha de entrega** | 18/06/2026 |
| **Duración estimada** | 2 horas |
| **Modalidad** | Individual (o en pareja con autorización del docente) |
| **Entrega** | Notebook exportado como `.ipynb` + link al notebook en Databricks |

---

## OBJETIVO DEL LABORATORIO

Implementar un pipeline Big Data completo usando PySpark en Databricks Community Edition: desde la carga de datos hasta el análisis distribuido con operaciones equivalentes a MapReduce (groupBy, aggregations) y generación de insights sobre un dataset real peruano.

## COMPETENCIA QUE DESARROLLA

Procesa archivos distribuidos usando el ecosistema Hadoop/Spark con integridad, identificando el rol de cada componente en la arquitectura.

---

## SOFTWARE Y HERRAMIENTAS REQUERIDAS

| Herramienta | Versión | Link | Tipo |
|-------------|---------|------|------|
| **Databricks Community Edition** | Última | community.cloud.databricks.com | Cloud gratuito (PRINCIPAL) |
| **Google Colab** (alternativo) | — | colab.research.google.com | Cloud gratuito (ALTERNATIVO) |
| **Navegador web** | Chrome/Firefox/Edge | — | Requerido |
| **Cuenta Google** | — | gmail.com | Para Colab alternativo |

### Configuración de Databricks Community Edition (10 min)

**Paso 1 — Registrarse:**
```
1. Ir a: community.cloud.databricks.com
2. Clic en "Get Started for Free"
3. Llenar formulario: nombre, email, empresa (poner "Universidad Autónoma del Perú")
4. Verificar email → clic en el link de activación
5. Iniciar sesión en: community.cloud.databricks.com
```

**Paso 2 — Crear clúster:**
```
1. Panel izquierdo → "Compute" (ícono de nube)
2. Clic "Create compute"
3. Nombre del clúster: "BigData-S2-TuApellido"
4. Databricks Runtime: DBR 14.x LTS (incluye Spark 3.5 + Python 3.10)
5. Nodo: Community Optimized (único disponible gratis: ~6 GB RAM, 2 cores)
6. Clic "Create compute"
7. Esperar 3-5 minutos hasta que el estado diga "Running" (punto verde)
```

**Paso 3 — Crear notebook:**
```
1. Panel izquierdo → "Workspace" → tu nombre de usuario
2. Clic "Create" → "Notebook"
3. Nombre: "S2_Lab_TuApellido_BigData"
4. Lenguaje predeterminado: Python
5. Clúster: seleccionar el que creaste en el Paso 2
6. Clic "Create"
```

**Verificación de entorno listo:**
Escribe en la primera celda y ejecuta (Shift+Enter):
```python
print(f"Spark version: {spark.version}")
print(f"Python version: {sc.pythonVer}")
print("Entorno listo!")
```
Si ves "Spark version: 3.x.x" → estás listo.

---

**ALTERNATIVA: Google Colab (si no puedes usar Databricks)**

```python
# Celda 1 en Colab — instalar PySpark
!pip install pyspark==3.5.0 --quiet

# Celda 2 — iniciar sesión Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("BigDataS2Lab") \
    .master("local[2]") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

print(f"Spark version: {spark.version}")
```

> **Nota:** En Colab, Spark corre en modo local (sin clúster real). Los conceptos son los mismos, pero no hay distribución entre nodos. Para el laboratorio es suficiente.

---

## DATOS DEL LABORATORIO

Usaremos un dataset real de accidentes de tránsito en Lima (datos del MTC / INEI), en formato CSV.

**Para cargar los datos en Databricks DBFS (Databricks File System — equivalente a HDFS):**

```python
# OPCIÓN A — Dataset en línea (copiar y ejecutar directamente)
# Generamos datos sintéticos basados en estadísticas reales del MTC Perú 2023

import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

np.random.seed(42)
n = 50000  # 50,000 registros de accidentes

departamentos = ['Lima', 'Arequipa', 'La Libertad', 'Piura', 'Cusco', 
                 'Junin', 'Puno', 'Ancash', 'Loreto', 'Cajamarca']
tipos = ['Choque', 'Atropello', 'Volcadura', 'Caida_ocupante', 'Incendio', 'Despiste']
causas = ['Exceso_velocidad', 'Impericia', 'Embriaguez', 'Exceso_carga', 
          'Falla_mecanica', 'Mal_estado_via', 'Distraccion', 'No_respeta_señal']
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
         'Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']

# Distribución de probabilidad por departamento (Lima tiene más accidentes)
probs_dep = [0.35, 0.12, 0.10, 0.08, 0.07, 0.07, 0.05, 0.05, 0.06, 0.05]

data = {
    'ID_accidente': range(1, n+1),
    'departamento': np.random.choice(departamentos, n, p=probs_dep),
    'tipo_accidente': np.random.choice(tipos, n, p=[0.45, 0.20, 0.15, 0.10, 0.02, 0.08]),
    'causa_principal': np.random.choice(causas, n),
    'mes': np.random.choice(meses, n),
    'hora': np.random.randint(0, 24, n),
    'fallecidos': np.random.choice([0,1,2,3], n, p=[0.85, 0.10, 0.03, 0.02]),
    'heridos': np.random.randint(0, 8, n),
    'vehiculos_involucrados': np.random.randint(1, 5, n),
    'danio_material_soles': np.random.exponential(5000, n).astype(int)
}

df_pandas = pd.DataFrame(data)

# Guardar como CSV
df_pandas.to_csv('/tmp/accidentes_mtc_peru.csv', index=False)
print(f"Dataset creado: {len(df_pandas):,} registros")
print(df_pandas.head(3))
```

---

## PARTE 1 — EXPLORACIÓN DEL ENTORNO SPARK (30 min)

### Actividad 1.1 — Cargar datos en Spark

```python
# Cargar el CSV en un DataFrame de Spark
# En Databricks, Spark ya está disponible como variable global 'spark'

df = spark.read.csv('/tmp/accidentes_mtc_peru.csv', 
                    header=True,       # Primera fila = nombres de columnas
                    inferSchema=True)  # Detecta automáticamente int, string, etc.

# Ver la estructura del DataFrame (equivale a DESCRIBE TABLE en SQL)
df.printSchema()

# Ver las primeras 5 filas
df.show(5)

# Contar registros (equivale a SELECT COUNT(*) FROM tabla)
print(f"\nTotal de registros: {df.count():,}")
```

**¿Qué debes observar?**
- El schema muestra los tipos de datos detectados automáticamente
- `show()` muestra datos en formato tabla
- `count()` lanza un job distribuido — en Spark UI verás el DAG

---

### Actividad 1.2 — Explorar el SparkUI (el "monitor" del clúster)

```python
# En Databricks: clic en "Spark Jobs" en la barra superior del notebook
# En Colab local: abrir http://localhost:4040 en otro tab

# Ejecuta esta consulta y LUEGO mira el SparkUI:
resultado_prueba = df.groupBy("departamento").count()
resultado_prueba.show()

# En SparkUI verás:
# - Stages: cuántas etapas tuvo el job
# - Tasks: cuántas tareas corrieron en paralelo
# - Shuffle Read/Write: cuántos datos se movieron entre nodos
```

**Pregunta de reflexión 1.1:**
> ¿Cuántas "stages" (etapas) tiene el job de `groupBy`? ¿Puedes identificar cuál es la etapa Map (scan del CSV) y cuál es la etapa Reduce (agrupación)?
>
> Escribe tu respuesta en una celda de texto del notebook (Insert → Text cell o `# Respuesta:` en comentario).

---

### Actividad 1.3 — Operaciones básicas de Spark DataFrame

```python
# Estadísticas descriptivas de todas las columnas numéricas
df.describe().show()

# Filtrar: solo accidentes con fallecidos > 0 (equivale a WHERE en SQL)
accidentes_fatales = df.filter(df.fallecidos > 0)
print(f"Accidentes fatales: {accidentes_fatales.count():,}")
print(f"Porcentaje: {accidentes_fatales.count()/df.count()*100:.1f}%")

# Seleccionar columnas específicas (equivale a SELECT en SQL)
muestra = df.select("departamento", "tipo_accidente", "fallecidos", "danio_material_soles")
muestra.show(10)
```

**Pregunta de reflexión 1.2:**
> Si cambias `df.filter(df.fallecidos > 0)` por `df.filter(df.fallecidos >= 1)`, ¿obtienes el mismo resultado? ¿Por qué? ¿Qué pasa si cambias la condición a `df.fallecidos.isNotNull()`?
>
> Responde probando en el notebook.

---

## PARTE 2 — IMPLEMENTACIÓN DEL PIPELINE MAPREDU CE CON PYSPARK (60 min)

### Actividad 2.1 — Análisis de accidentes por departamento (equivalente a MapReduce)

Implementa el siguiente análisis usando PySpark. Este es el corazón del laboratorio — reproduce el patrón MapReduce (groupBy = fase Reduce, distribución = fase Map automática de Spark).

```python
from pyspark.sql import functions as F

# ============================================================
# ANÁLISIS 1: Total de accidentes y fallecidos por departamento
# Equivalente MapReduce: MAP emite (departamento, {accidentes:1, fallecidos:N})
#                        REDUCE suma por departamento
# ============================================================

analisis_departamento = df.groupBy("departamento") \
    .agg(
        F.count("*").alias("total_accidentes"),           # COUNT(*)
        F.sum("fallecidos").alias("total_fallecidos"),    # SUM(fallecidos)
        F.sum("heridos").alias("total_heridos"),          # SUM(heridos)
        F.avg("danio_material_soles").alias("danio_promedio_soles"),  # AVG(daño)
        F.sum("danio_material_soles").alias("danio_total_soles")      # SUM(daño)
    ) \
    .orderBy("total_accidentes", ascending=False)

print("=== ACCIDENTES POR DEPARTAMENTO ===")
analisis_departamento.show()

# Guardar resultado en DBFS (equivalente a guardar en HDFS)
# En Databricks Community: /FileStore es tu "HDFS"
analisis_departamento.write.mode("overwrite") \
    .csv("/FileStore/resultados/analisis_departamento")

print("Resultado guardado en DBFS: /FileStore/resultados/analisis_departamento")
```

**Punto de verificación 2.1:** ¿Lima aparece primero en la lista? ¿El porcentaje de Lima coincide con la probabilidad con que generamos los datos (35%)? Si tu resultado muestra Lima con ~35% del total de accidentes, tu análisis es correcto.

---

### Actividad 2.2 — Análisis temporal: Horas con más accidentes

```python
# ============================================================
# ANÁLISIS 2: Distribución de accidentes por hora del día
# Objetivo: encontrar las horas más peligrosas en las vías peruanas
# ============================================================

# Clasificar hora en período del día
df_con_periodo = df.withColumn(
    "periodo_dia",
    F.when(F.col("hora").between(6, 11), "Mañana (6-11h)")
     .when(F.col("hora").between(12, 17), "Tarde (12-17h)")
     .when(F.col("hora").between(18, 23), "Noche (18-23h)")
     .otherwise("Madrugada (0-5h)")
)

analisis_temporal = df_con_periodo.groupBy("periodo_dia") \
    .agg(
        F.count("*").alias("total_accidentes"),
        F.sum("fallecidos").alias("fallecidos"),
        F.round(F.avg("danio_material_soles"), 2).alias("daño_promedio")
    ) \
    .orderBy("total_accidentes", ascending=False)

print("=== ACCIDENTES POR PERÍODO DEL DÍA ===")
analisis_temporal.show()

# -----------------------------------
# Tu turno: agrega la columna "tasa_mortalidad"
# = (fallecidos / total_accidentes) * 100
# Tip: usa .withColumn() después del groupBy
# -----------------------------------

# ESCRIBE TU CÓDIGO AQUÍ:
# analisis_temporal_con_tasa = analisis_temporal.withColumn(...)
```

**Pregunta de análisis 2.2:** ¿En qué período del día la tasa de mortalidad (fallecidos/accidentes) es más alta, aunque no sea el período con más accidentes? ¿Por qué crees que sucede esto? Escribe tu hipótesis en el notebook.

---

### Actividad 2.3 — Análisis multi-dimensión: Causa × Tipo de accidente

```python
# ============================================================
# ANÁLISIS 3: Cruce de causa principal con tipo de accidente
# Spark SQL - escribe como si fuera SQL tradicional
# ============================================================

# Registrar el DataFrame como tabla temporal (vista SQL)
df.createOrReplaceTempView("accidentes")

# Usar Spark SQL directamente
resultado_sql = spark.sql("""
    SELECT 
        causa_principal,
        tipo_accidente,
        COUNT(*) as total_casos,
        SUM(fallecidos) as total_fallecidos,
        ROUND(SUM(fallecidos) * 100.0 / COUNT(*), 2) as tasa_mortalidad_pct
    FROM accidentes
    WHERE tipo_accidente IN ('Choque', 'Atropello', 'Volcadura')
    GROUP BY causa_principal, tipo_accidente
    HAVING COUNT(*) > 100
    ORDER BY total_fallecidos DESC
    LIMIT 15
""")

print("=== TOP 15: CAUSA × TIPO (solo accidentes frecuentes) ===")
resultado_sql.show(15, truncate=False)
```

**Pregunta de análisis 2.3:** Spark SQL y los DataFrames de PySpark generan el mismo plan de ejecución internamente (Catalyst Optimizer). ¿Cuál prefieres escribir y por qué? Escribe tu respuesta como comentario en el notebook. Luego ejecuta el mismo análisis usando solo operaciones de DataFrame (sin `spark.sql()`).

---

### Actividad 2.4 — Pipeline completo con guardado en formato columnar

```python
# ============================================================
# ANÁLISIS FINAL: Pipeline completo Medallion Architecture
# Bronze (raw) → Silver (limpio) → Gold (analítico)
# ============================================================

# CAPA BRONZE — datos tal como llegan (ya los tenemos en 'df')
print("BRONZE: Datos raw cargados")
print(f"  Registros: {df.count():,} | Columnas: {len(df.columns)}")

# CAPA SILVER — datos limpios y tipados
df_silver = df \
    .filter(df.danio_material_soles > 0) \       # Quitar registros con daño = 0
    .filter(df.hora.between(0, 23)) \             # Horas válidas
    .withColumn("es_fatal", 
                F.when(df.fallecidos > 0, True).otherwise(False)) \
    .withColumn("costo_total",
                F.col("danio_material_soles") + F.col("heridos") * 2000 + 
                F.col("fallecidos") * 50000)  # Costo estimado incluyendo víctimas

print(f"\nSILVER: Datos limpios")
print(f"  Registros: {df_silver.count():,} | Columnas: {len(df_silver.columns)}")

# Guardar Silver como Parquet (formato columnar, 80% más comprimido que CSV)
df_silver.write.mode("overwrite").parquet("/FileStore/silver/accidentes_silver")
print("  Guardado como Parquet en /FileStore/silver/")

# CAPA GOLD — datos agregados para analytics
df_gold = df_silver.groupBy("departamento", "mes") \
    .agg(
        F.count("*").alias("accidentes"),
        F.sum("fallecidos").alias("fallecidos"),
        F.sum("heridos").alias("heridos"),
        F.sum("costo_total").alias("costo_total_estimado"),
        F.sum(F.col("es_fatal").cast("int")).alias("accidentes_fatales")
    ) \
    .withColumn("tasa_fatalidad_pct",
                F.round(F.col("accidentes_fatales") / F.col("accidentes") * 100, 2))

print(f"\nGOLD: Tabla analítica")
df_gold.orderBy("costo_total_estimado", ascending=False).show(10)

# Guardar Gold como Parquet particionado (más eficiente para queries por departamento)
df_gold.write.mode("overwrite") \
    .partitionBy("departamento") \
    .parquet("/FileStore/gold/accidentes_gold")

print("  Guardado particionado por departamento en /FileStore/gold/")
```

**Punto de verificación 2.4:** Verifica que los archivos existen en DBFS:
```python
# Listar archivos en DBFS (equivale a `hdfs dfs -ls /`)
display(dbutils.fs.ls("/FileStore/gold/accidentes_gold"))
# Debes ver una carpeta por cada departamento: departamento=Lima, departamento=Arequipa, etc.
```

---

## PARTE 3 — DESAFÍO (30 min)

### Actividad 3.1 — Análisis no visto en clase: Ventanas Temporales

Investiga el concepto de **Window Functions** en Spark (funciones de ventana) y úsalas para este análisis:

> Calcular, para cada departamento, qué mes tuvo el MAYOR número de accidentes, y compararlo con el promedio de ese departamento.

```python
# Pista: investiga spark.sql.window.Window en PySpark
from pyspark.sql.window import Window
from pyspark.sql import functions as F

# Tu código aquí:
# 1. Primero agrupa por departamento + mes
# 2. Luego usa Window para calcular el máximo por departamento
# 3. Finalmente filtra los registros donde total == maximo

# Pista de código:
windowDep = Window.partitionBy("departamento")

df_mensual = df.groupBy("departamento", "mes") \
    .agg(F.count("*").alias("accidentes_mes"))

# COMPLETA: agrega la columna max_mes con el máximo de accidentes del departamento
# COMPLETA: agrega la columna promedio_mensual con el promedio del departamento
# COMPLETA: filtra solo las filas donde accidentes_mes == max_mes

# ¿Resultado esperado? Cada departamento aparece UNA vez con su peor mes
```

---

### Actividad 3.2 — Visualización con Matplotlib

```python
import matplotlib.pyplot as plt

# Convertir resultado de Spark a Pandas para graficar
df_viz = analisis_departamento.toPandas()

# Gráfico de barras horizontales
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df_viz['departamento'], df_viz['total_accidentes'], color='steelblue')
ax.set_xlabel('Total de Accidentes')
ax.set_title('Accidentes de Tránsito por Departamento\nPerú 2023 (Simulado con datos MTC)')
ax.invert_yaxis()  # Mayor en la parte superior

# En Databricks: la gráfica se muestra automáticamente
# En Colab: plt.show()
plt.tight_layout()
plt.savefig('/tmp/accidentes_por_departamento.png', dpi=150)
display(fig)  # En Databricks
```

**Pregunta de reflexión final 3.1:**
> ¿Qué insight más importante encontraste en los datos que no esperabas? ¿Cómo cambiaría tu análisis si los datos fueran de un año real de 2 millones de accidentes en lugar de 50,000 sintéticos? ¿El código PySpark necesitaría cambios?

**Pregunta de conexión 3.2:**
> Si trabajaras en la empresa Pacífico Seguros y tuvieras acceso a estos datos reales del MTC, ¿qué tres KPIs calcularías con este pipeline para ajustar las tarifas del SOAT por departamento? ¿Qué datos adicionales necesitarías que no están en este dataset?

---

## ENTREGABLES

1. **Notebook exportado:** Exportar el notebook de Databricks como `.ipynb`:
   - File → Export → IPython Notebook (.ipynb)
   - Nombre del archivo: `S2_Lab_TuApellido_TuCodigo.ipynb`

2. **Link del notebook en Databricks:**
   - En Databricks: clic en el ícono de compartir (arriba a la derecha del notebook)
   - Copiar el link y pegarlo en tu tarea

3. **Screenshot de DBFS:**
   - Screenshot de los archivos Parquet en `/FileStore/gold/` (desde Databricks → Data → DBFS)

4. **Respuestas a las preguntas de reflexión:** incluidas en celdas de texto dentro del notebook.

---

## RÚBRICA DE EVALUACIÓN

| Criterio | Excelente (100%) | Suficiente (70%) | Mínimo (40%) |
|----------|------------------|------------------|--------------|
| **Entorno configurado** (10%) | Databricks funcionando con clúster activo | Colab alternativo funcionando | Algún error pero muestra intento |
| **Parte 1: Exploración** (20%) | Todas las actividades completadas + respuestas a reflexiones | 2 de 3 actividades + 1 reflexión | Solo carga de datos básica |
| **Parte 2: Pipeline** (40%) | Pipeline completo Bronze→Silver→Gold, código limpio, análisis multi-dimensión | Actividades 2.1 y 2.2 completas | Solo actividad 2.1 |
| **Parte 3: Desafío** (20%) | Window functions implementadas + visualización + reflexiones completas | Solo visualización o solo window functions | Algún intento de la parte 3 |
| **Calidad del código** (10%) | Código comentado, variables descriptivas, uso correcto de PySpark | Código funcional sin comentarios | Código con errores menores |

---

## RECURSOS DE APOYO

- Documentación oficial PySpark: https://spark.apache.org/docs/latest/api/python/
- Databricks Community tutoriales: https://docs.databricks.com/getting-started/
- Video: "Apache Spark Tutorial for Beginners" (FreeCodeCamp, YouTube, 1.5 hrs)
- Libro gratuito: "Learning Spark 2nd Edition" en databricks.com/resources

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
