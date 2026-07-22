# S3 — LABORATORIO EN CASA: MongoDB Atlas + Python — RESUELTO
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Implementación NoSQL con MongoDB Atlas — Análisis de Empresas SUNAT

---

| Campo | Detalle |
|-------|---------| 
| **Nombre del estudiante** | Ana Concepción Asto Arotinco |
| **Código** | — |
| **Fecha de entrega** | Junio 2026 |
| **Duración estimada** | 2 horas |
| **Modalidad** | Individual |
| **Entrega** | Screenshot del Atlas + Notebook (.ipynb) con resultados |

---

## PARTE 1 — EXPLORACIÓN: Conectar y Explorar MongoDB

### Celda 1 — Instalación y conexión

```python
!pip install pymongo dnspython -q

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
from datetime import datetime
import pprint

# REEMPLAZA CON TU CONNECTION STRING DE ATLAS:
CONNECTION_STRING = "mongodb+srv://administrador:Yape2026%40@cluster0.cqppmkk.mongodb.net/?appName=Cluster0"

client = MongoClient(CONNECTION_STRING)

try:
    client.admin.command('ping')
    print("✅ Conexión exitosa a MongoDB Atlas!")
    print(f"   Databases disponibles: {client.list_database_names()}")
except ConnectionFailure:
    print("❌ No se pudo conectar.")

db = client["bigdata_s3_sunat"]
print(f"\n📁 Base de datos: {db.name}")
```

---

### Celda 2 — Insertar documentos con estructura diferente

```python
empresas = db["empresas"]
empresas.delete_many({})  # Limpiar para re-ejecuciones

# Empresa de tecnología
empresa_tech = {
    "ruc": "20123456789",
    "razon_social": "Tecnología Andina SAC",
    "tipo_empresa": "SOCIEDAD ANONIMA CERRADA",
    "departamento": "Lima",
    "distrito": "Miraflores",
    "sector": "Tecnología",
    "regimen_tributario": "Régimen General",
    "estado": "ACTIVO",
    "fecha_registro_sunat": datetime(2018, 3, 15),
    "num_empleados": 45,
    "facturacion_anual": {
        "2022": 650000,
        "2023": 850000,
        "2024": 1200000
    },
    "productos_servicios": ["Software ERP", "Consultoría TI", "Soporte"],
    "certificaciones": ["ISO 9001", "CMMI Level 3"],
    "contacto": {
        "email": "contacto@tecandina.com",
        "telefono": "01-4567890",
        "web": "www.tecandina.com"
    },
    "exporta": False
}

resultado = empresas.insert_one(empresa_tech)
print(f"✅ Empresa insertada con ID: {resultado.inserted_id}")

# Empresa agroindustrial con ESTRUCTURA DIFERENTE
empresa_agricola = {
    "ruc": "20987654321",
    "razon_social": "Agroindustrias del Sur EIRL",
    "departamento": "Arequipa",
    "sector": "Agroindustria",
    "estado": "ACTIVO",
    "num_empleados": 120,
    "facturacion_anual": {"2023": 2800000, "2024": 3200000},
    "cultivos_principales": ["Páprika", "Cebolla amarilla", "Ajo"],
    "hectareas_certificadas": 450,
    "certificaciones_organicas": ["USDA Organic", "BIO Suisse"],
    "mercados_exportacion": ["Estados Unidos", "Países Bajos", "España"],
    "exporta": True,
    "volumen_exportacion_tn": 1200
}

resultado2 = empresas.insert_one(empresa_agricola)
print(f"✅ Empresa agroindustrial insertada con ID: {resultado2.inserted_id}")

print("\n📄 DOCUMENTOS EN LA COLECCIÓN:")
for emp in empresas.find():
    print(f"\n  RUC: {emp['ruc']} | {emp['razon_social']}")
    print(f"  Campos: {list(emp.keys())}")
    print(f"  Total campos: {len(emp.keys())}")
```

**✅ Respuesta — Pregunta de reflexión 1.1:**

La empresa de tecnología tiene **14 campos** (incluyendo objetos anidados como `facturacion_anual`, `contacto`, y arrays como `productos_servicios`). La empresa agroindustrial tiene **13 campos**, pero completamente distintos — tiene `cultivos_principales`, `hectareas_certificadas`, `mercados_exportacion` que la empresa tech no tiene; y no tiene `contacto`, `productos_servicios`, ni `certificaciones` TI.

En una base de datos SQL, la empresa agroindustrial que no tiene `contacto.web` tendría esa columna en la tabla con valor **NULL**. Con 2 millones de empresas de distintos sectores, la tabla SQL tendría decenas de columnas NULL para la mayoría de registros — ineficiente en almacenamiento y confuso para los analistas. MongoDB simplemente no incluye el campo si no existe.

---

### Celda 3 — Insertar dataset masivo de 100 empresas

```python
import random

empresas.delete_many({"ruc": {"$regex": "^SYNTHETIC"}})

departamentos = ["Lima", "Arequipa", "La Libertad", "Piura", "Cusco",
                 "Junin", "Puno", "Ancash", "Loreto", "Cajamarca", "Moquegua"]
sectores = ["Tecnología", "Comercio", "Manufactura", "Construcción",
            "Agroindustria", "Minería", "Servicios", "Transporte", "Salud", "Educación"]
regimenes = ["Régimen General", "MYPE Tributario", "NRUS", "Régimen Especial"]
estados = ["ACTIVO", "ACTIVO", "ACTIVO", "SUSPENDIDO", "BAJA"]

dataset_empresas = []
for i in range(100):
    dep = random.choice(departamentos)
    sector = random.choice(sectores)
    empleados = random.randint(1, 500)

    empresa = {
        "ruc": f"SYNTHETIC{i:06d}",
        "razon_social": f"Empresa {sector} {dep} {i:03d} SAC",
        "departamento": dep,
        "sector": sector,
        "regimen_tributario": random.choice(regimenes),
        "estado": random.choice(estados),
        "num_empleados": empleados,
        "facturacion_anual": {
            "2022": random.randint(50000, 5000000),
            "2023": random.randint(50000, 5000000),
            "2024": random.randint(50000, 5000000)
        },
        "exporta": random.choice([True, False]),
        "fecha_registro": datetime(random.randint(2000, 2023),
                                   random.randint(1, 12),
                                   random.randint(1, 28))
    }
    dataset_empresas.append(empresa)

resultado = empresas.insert_many(dataset_empresas)
print(f"✅ Insertadas {len(resultado.inserted_ids)} empresas")
print(f"   Total documentos en colección: {empresas.count_documents({})}")
```

**✅ Respuesta — Pregunta de reflexión 1.2:**

`insert_many()` es más eficiente que 100 llamadas a `insert_one()` porque **reduce el overhead de red de 100 round-trips a 1**. Cada llamada a `insert_one()` implica: (1) serializar el documento a BSON, (2) abrir/usar la conexión TCP al servidor en São Paulo, (3) enviar el documento, (4) esperar el acknowledgment, (5) recibir la respuesta. Con latencia de ~180ms entre Lima y São Paulo, 100 `insert_one()` tomarían ~18 segundos solo en overhead de red. `insert_many()` serializa todos los documentos en un único payload, hace un solo viaje de red y recibe un único acknowledgment — el mismo resultado en menos de 1 segundo.

---

## PARTE 2 — CONSULTAS Y AGGREGATION PIPELINE

### Celda 4 — Consultas básicas

```python
print("=" * 60)
print("CONSULTAS MONGODB — con equivalente SQL comentado")
print("=" * 60)

# CONSULTA 1: Empresas activas de Lima
# SQL: SELECT * FROM empresas WHERE estado='ACTIVO' AND departamento='Lima'
query1 = empresas.find({"estado": "ACTIVO", "departamento": "Lima"})
lista1 = list(query1)
print(f"\n1. Empresas activas en Lima: {len(lista1)}")

# CONSULTA 2: Top 5 empresas por empleados (>50)
# SQL: SELECT razon_social, num_empleados FROM empresas WHERE num_empleados > 50
#      ORDER BY num_empleados DESC LIMIT 5
query2 = empresas.find(
    {"num_empleados": {"$gt": 50}},
    {"razon_social": 1, "num_empleados": 1, "_id": 0}
).sort("num_empleados", -1).limit(5)

print(f"\n2. Top 5 empresas por empleados (>50):")
for e in query2:
    print(f"   {e['razon_social']}: {e['num_empleados']} empleados")

# CONSULTA 3: Exportadoras en sectores productivos
# SQL: SELECT * FROM empresas WHERE exporta=TRUE AND sector IN ('Agroindustria','Manufactura','Minería')
count3 = empresas.count_documents({
    "exporta": True,
    "sector": {"$in": ["Agroindustria", "Manufactura", "Minería"]}
})
print(f"\n3. Empresas exportadoras en sectores productivos: {count3}")

# CONSULTA 4: Facturación 2024 > 1M (campo anidado con notación punto)
# SQL: SELECT e.razon_social, f.monto FROM empresas e
#      JOIN facturacion f ON e.id=f.empresa_id WHERE f.año=2024 AND f.monto > 1000000
# ← MongoDB lo hace SIN JOIN con notación punto:
query4 = empresas.find(
    {"facturacion_anual.2024": {"$gt": 1000000}},
    {"razon_social": 1, "facturacion_anual.2024": 1, "_id": 0}
)
print(f"\n4. Empresas con facturación 2024 > S/1M:")
for e in list(query4)[:5]:
    print(f"   {e['razon_social']}: S/{e['facturacion_anual']['2024']:,}")
```

---

### Celda 5 — Aggregation Pipeline por sector

```python
print("\n" + "=" * 60)
print("AGGREGATION PIPELINE — Análisis de empresas por sector")
print("=" * 60)

pipeline_sector = [
    {"$match": {"estado": "ACTIVO"}},
    {"$group": {
        "_id": "$sector",
        "total_empresas": {"$sum": 1},
        "empleados_promedio": {"$avg": "$num_empleados"},
        "facturacion_total_2024": {"$sum": "$facturacion_anual.2024"},
        "empresas_exportadoras": {"$sum": {"$cond": ["$exporta", 1, 0]}}
    }},
    {"$addFields": {
        "pct_exportadoras": {
            "$round": [
                {"$multiply": [
                    {"$divide": ["$empresas_exportadoras", "$total_empresas"]},
                    100
                ]}, 1
            ]
        }
    }},
    {"$sort": {"total_empresas": -1}},
    {"$limit": 8},
    {"$project": {
        "sector": "$_id",
        "total_empresas": 1,
        "empleados_promedio": {"$round": ["$empleados_promedio", 0]},
        "facturacion_total_2024": 1,
        "pct_exportadoras": 1,
        "_id": 0
    }}
]

resultados = list(empresas.aggregate(pipeline_sector))

print(f"\n{'SECTOR':<20} {'TOTAL':>8} {'EMP.PROM':>10} {'FACTURAC.2024':>15} {'%EXPORT':>8}")
print("-" * 70)
for r in resultados:
    print(f"{r['sector']:<20} {r['total_empresas']:>8} {int(r['empleados_promedio']):>10} "
          f"S/{r['facturacion_total_2024']:>13,.0f} {r['pct_exportadoras']:>7.1f}%")
```

---

### Celda 6 — ✅ IMPLEMENTACIÓN PROPIA: Análisis por departamento

```python
# ============================================================
# CELDA 6 COMPLETADA: Análisis por departamento
# ============================================================

pipeline_departamento = [
    # Filtro: solo empresas activas
    {"$match": {"estado": "ACTIVO"}},

    # Agrupar por departamento
    {"$group": {
        "_id": "$departamento",
        "total_empresas": {"$sum": 1},              # ✅ completado: 1 para contar
        "total_empleados": {"$sum": "$num_empleados"},
        "facturacion_promedio_2024": {"$avg": "$facturacion_anual.2024"},  # ✅ completado
        "regimenes": {"$push": "$regimen_tributario"}
    }},

    # Ordenar por total de empleados descendente
    {"$sort": {"total_empleados": -1}},             # ✅ completado: -1 descendente

    # Top 5
    {"$limit": 5},

    # Formatear salida
    {"$project": {
        "departamento": "$_id",
        "total_empresas": 1,
        "total_empleados": 1,
        "facturacion_promedio_2024": {"$round": ["$facturacion_promedio_2024", 0]},
        "_id": 0
    }}
]

resultados_dep = list(empresas.aggregate(pipeline_departamento))

print("TOP 5 DEPARTAMENTOS POR TOTAL DE EMPLEADOS (empresas activas):")
print(f"\n{'DEPARTAMENTO':<20} {'EMPRESAS':>10} {'EMPLEADOS':>12} {'FACT.PROM 2024':>18}")
print("-" * 65)
for r in resultados_dep:
    print(f"{r['departamento']:<20} {r['total_empresas']:>10} "
          f"{r['total_empleados']:>12} "
          f"S/{r['facturacion_promedio_2024']:>15,.0f}")

print("\n✅ Si Lima aparece primero → código correcto (Lima tiene ~35% de empresas del Perú)")
```

---

### Celda 7 — Índices y rendimiento

```python
import time

# SIN ÍNDICE
start = time.time()
for _ in range(100):
    list(empresas.find({"sector": "Tecnología"}))
tiempo_sin_indice = (time.time() - start) / 100 * 1000
print(f"Sin índice (100 consultas): {tiempo_sin_indice:.2f} ms promedio")

# CREAR ÍNDICE
empresas.create_index("sector")
print("\nÍndice creado en campo 'sector'")

# CON ÍNDICE
start = time.time()
for _ in range(100):
    list(empresas.find({"sector": "Tecnología"}))
tiempo_con_indice = (time.time() - start) / 100 * 1000
print(f"Con índice (100 consultas): {tiempo_con_indice:.2f} ms promedio")
print(f"Mejora: {tiempo_sin_indice/tiempo_con_indice:.1f}x más rápido")

print(f"\nÍndices en la colección 'empresas':")
for idx in empresas.list_indexes():
    print(f"  - {idx['name']}: {idx['key']}")
```

**✅ Respuesta — Pregunta de análisis 2.4:**

Con 100 documentos la diferencia es pequeña porque MongoDB hace un **Collection Scan** rápido — leer 100 documentos en memoria es casi instantáneo. Con 1 millón de documentos, sin índice MongoDB tendría que leer y evaluar **1,000,000 documentos** para encontrar los 100 de sector="Tecnología" — `O(n)`. Con el índice B-tree sobre `sector`, MongoDB va directamente a la hoja del árbol correspondiente a "Tecnología" y obtiene los punteros a esos documentos — `O(log n)`. La diferencia entre recorrer 1M documentos vs. hacer 20 comparaciones en un árbol B (log₂ 1,000,000 ≈ 20) es de segundos vs. microsegundos.

MongoDB internamente usa **índices B-tree** (igual que PostgreSQL), donde cada hoja del árbol apunta a la ubicación física del documento en disco. Es análogo al Row Key de HBase en el sentido de que ambos proveen acceso `O(1)` o `O(log n)` al registro buscado.

---

## PARTE 3 — DESAFÍO

### Celda 8 — Comparación SQL vs MongoDB

```python
import sqlite3
import pandas as pd

# ---- PARTE A: SQL con SQLite ----
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript("""
    CREATE TABLE empresas_sql (
        id INTEGER PRIMARY KEY,
        ruc TEXT,
        razon_social TEXT,
        departamento TEXT,
        sector TEXT,
        num_empleados INTEGER,
        exporta INTEGER
    );

    CREATE TABLE facturacion_sql (
        id INTEGER PRIMARY KEY,
        empresa_id INTEGER,
        anio INTEGER,
        monto REAL,
        FOREIGN KEY (empresa_id) REFERENCES empresas_sql(id)
    );
""")

for i, emp in enumerate(dataset_empresas[:10]):
    cursor.execute("INSERT INTO empresas_sql VALUES (?,?,?,?,?,?,?)",
                   (i, emp['ruc'], emp['razon_social'], emp['departamento'],
                    emp['sector'], emp['num_empleados'], int(emp['exporta'])))
    for anio, monto in emp['facturacion_anual'].items():
        cursor.execute("INSERT INTO facturacion_sql VALUES (?,?,?,?)",
                       (None, i, int(anio), monto))
conn.commit()

query_sql = """
    SELECT e.sector,
           COUNT(e.id) as total_empresas,
           SUM(f.monto) as facturacion_total
    FROM empresas_sql e
    JOIN facturacion_sql f ON e.id = f.empresa_id
    WHERE f.anio = 2024
    GROUP BY e.sector
    ORDER BY facturacion_total DESC
"""
df_sql = pd.read_sql_query(query_sql, conn)
print("RESULTADO SQL (con JOIN entre 2 tablas):")
print(df_sql.to_string())

# ---- PARTE B: MongoDB (sin JOIN) ----
pipeline_nosql = [
    {"$group": {
        "_id": "$sector",
        "total_empresas": {"$sum": 1},
        "facturacion_total": {"$sum": "$facturacion_anual.2024"}
    }},
    {"$sort": {"facturacion_total": -1}}
]
resultados_nosql = list(empresas.aggregate(pipeline_nosql))
print("\nRESULTADO MongoDB (sin JOIN, acceso directo a campo anidado):")
for r in resultados_nosql[:5]:
    print(f"  {r['_id']}: {r['total_empresas']} empresas, S/{r['facturacion_total']:,.0f}")

print("\n✅ Conclusión: MongoDB fue más simple para datos anidados (no requirió JOIN ni 2 tablas)")
```

---

## RESPUESTAS A PREGUNTAS DE REFLEXIÓN FINALES

**✅ Pregunta 3.1 — Equivalencia con MapReduce:**

En el Aggregation Pipeline de MongoDB puedo ver claramente la analogía con MapReduce:

- **Etapa `$match`** → equivale a la **fase de filtrado previo al Map**: selecciona qué documentos entrarán al procesamiento, como un mapper que decide qué registros emitir.

- **Etapa `$group`** → es la **fase REDUCE**: recibe todos los documentos agrupados por `_id` (el sector o departamento) y aplica funciones de agregación (`$sum`, `$avg`). Es exactamente lo que hace el Reducer: por cada clave, consolida todos los valores en un resultado.

- **Etapa `$sort`** → equivale al **Shuffle and Sort de MapReduce**: ordena los resultados después de la agregación.

En mi análisis de empresas por sector: el `$match: {estado:"ACTIVO"}` filtraría los documentos (MAP selecciona), el `$group by sector` los agrupa y suma (REDUCE consolida), y el `$sort` ordena el resultado final (equivalente al sort posterior al reduce). La diferencia es que MongoDB ejecuta esto en un solo proceso optimizado en el servidor, mientras MapReduce distribuye Map y Reduce en nodos separados para datasets de TB/PB.

---

**✅ Pregunta 3.2 — Conexión con el proyecto grupal:**

En el proyecto grupal de **Predicción de Demanda para Supermercados Peruanos**, almacenaría en MongoDB el **catálogo de productos**, porque cada producto tiene atributos completamente distintos según su categoría: los perecederos tienen fecha de vencimiento y temperatura de almacenamiento; los electrónicos tienen voltaje y garantía; la ropa tiene talla y composición de materiales. En SQL esto requeriría decenas de columnas NULL.

El campo equivalente al `_id` o clave de acceso principal sería el **código de producto interno (SKU)**, que identifica unívocamente cada ítem en el catálogo y es el campo de búsqueda más frecuente ("¿qué información tiene el producto X?").

Sí tendría sentido usar el Aggregation Pipeline de MongoDB para un análisis específico: calcular las **ventas totales por categoría y por tienda en el mes actual** usando datos del catálogo cruzados con transacciones recientes. Si los datos del mes actual están en MongoDB, el pipeline puede hacer esto directamente sin mover datos a Spark. Sin embargo, para el análisis histórico de años anteriores (el que usa el modelo de predicción) seguiría siendo más eficiente PySpark sobre Delta Lake, porque procesa TB de datos distribuidos que no caben en la memoria de un servidor MongoDB.

---

## ENTREGABLES

```
S3_Lab_AstoAna/
├── S3_Lab_AstoAna.ipynb          ← Notebook exportado desde Colab
├── S3_LAB_CASA_RESUELTO.md       ← Este archivo con código y respuestas
└── screenshots/
    ├── atlas_coleccion_empresas.png    ← Colección con total de documentos
    ├── atlas_documento_expandido.png   ← Documento con facturacion_anual expandido
    └── atlas_indices.png               ← Índices creados en la colección
```

**Link del notebook:** `https://______________________________`

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Estudiante: Ana Concepción Asto Arotinco*
