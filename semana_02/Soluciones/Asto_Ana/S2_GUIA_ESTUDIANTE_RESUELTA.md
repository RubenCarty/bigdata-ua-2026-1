# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE — DESARROLLADA
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Ana Concepción Asto Arotinco |
| **Código de estudiante** | — |
| **Sección** | — |
| **Fecha** | Junio 2026 |
| **Tiempo estimado** | 1.5 horas |
| **Puntaje total** | 100 puntos |

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos)

---

**1.** ¿Cuál es la función principal del NameNode en HDFS?

**✅ Respuesta: c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos**

El NameNode no guarda los datos en sí, solo guarda el "mapa" del sistema de archivos — qué archivos existen, en qué bloques están divididos y en qué DataNodes está cada bloque. Es como el índice de un libro: no tiene el contenido, pero te dice en qué página está cada cosa.

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

**✅ Respuesta: c) 128 MB**

Hadoop 3.x usa bloques de 128 MB por defecto. Este tamaño grande reduce la sobrecarga de metadatos en el NameNode y está diseñado para archivos de varios GB o TB típicos de Big Data, no para archivos pequeños.

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

**✅ Respuesta: b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer**

El Shuffle and Sort es la fase intermedia que ocurre automáticamente entre Map y Reduce. Toma todos los pares (clave, valor) emitidos por los Mappers, los ordena por clave y asegura que todos los valores con la misma clave lleguen al mismo Reducer. Sin esta fase, sería imposible agregar datos distribuidos en distintos nodos.

---

**4.** ¿Qué componente de Hadoop gestiona los recursos del clúster?

**✅ Respuesta: c) YARN**

YARN (Yet Another Resource Negotiator) es el gestor de recursos de Hadoop. Decide cuánta CPU y RAM asigna a cada job que se ejecuta en el clúster, arbitrando entre múltiples trabajos que compiten por los mismos recursos.

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 ms por DNI.

**✅ Respuesta: b) HBase — porque permite acceso aleatorio en tiempo real por Row Key**

HBase está diseñado exactamente para esto: acceso aleatorio a registros individuales en tiempo real usando una clave (Row Key). Si usas el DNI como Row Key, HBase puede devolver el registro en milisegundos. HDFS y MapReduce están diseñados para procesar grandes volúmenes en batch, no para consultas de un solo registro en tiempo real.

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

**✅ Respuesta: b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos**

Cloud = procesamiento centralizado en servidores remotos (AWS, Azure, GCP). Fog = procesamiento en el "borde" de la red, cerca de los dispositivos que generan los datos (sensores IoT, cámaras, GPS). Fog reduce la latencia y el ancho de banda consumido enviando solo los datos relevantes a la nube.

---

**7.** Archivo de 400 MB en HDFS con bloques de 128 MB y factor de replicación 3, ¿cuántos bloques físicos?

**✅ Respuesta: d) 12**

Cálculo:
- 400 MB ÷ 128 MB = 4 bloques (3 de 128 MB + 1 de 16 MB)
- 4 bloques × 3 réplicas = **12 bloques físicos** almacenados en el clúster

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

**✅ Respuesta: c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)**

MapReduce hace I/O a disco en cada fase intermedia (después del Map, después del Shuffle). Spark mantiene los datos en memoria RAM entre operaciones, lo que lo hace hasta 100 veces más rápido para cargas de trabajo iterativas como machine learning o grafos.

---

**9.** ¿Cuál corresponde a "Platform as a Service" (PaaS) en Big Data?

**✅ Respuesta: c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs**

- IaaS → tú gestionas el SO y el software (EC2 con Hadoop manual)
- **PaaS → el proveedor gestiona la plataforma, tú solo ejecutas código (EMR, Dataproc)**
- SaaS → todo gestionado, solo usas la interfaz (Databricks podría ser SaaS)

---

**10.** Un DataNode con factor de replicación 3 falla. ¿Qué pasa?

**✅ Respuesta: c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3**

Esta es exactamente la tolerancia a fallos de HDFS. El NameNode monitorea los heartbeats de los DataNodes. Si un nodo no responde en 10 minutos, lo marca como muerto, redirige las lecturas a las réplicas vivas y ordena a otros DataNodes que creen nuevas copias para volver al factor de replicación configurado.

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama **NameNode**, mientras que los nodos que guardan físicamente los bloques de datos se llaman **DataNodes**.

**12.** El modelo de programación **MapReduce** divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares **clave-valor**, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada **Hypervisor** (o Monitor de Máquina Virtual / VMM).

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado **Row Key**, que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el **borde (edge)** de la red (cerca de los dispositivos), reduciendo la **latencia** de comunicación con el data center central.

---

### B2. Relacionar columnas

| N° | Concepto | Letra | Descripción |
|----|----------|-------|-------------|
| 1 | YARN | **E** | Gestor de recursos del clúster Hadoop que asigna CPU/RAM a los trabajos |
| 2 | ZooKeeper | **C** | Framework de coordinación y sincronización distribuida en el ecosistema Hadoop |
| 3 | HBase | **A** | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real |
| 4 | Sqoop | **B** | Herramienta para importar/exportar datos entre RDBMS y HDFS |
| 5 | Hive | **D** | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse) |
| 6 | Kafka | **F** | Plataforma de streaming de eventos y mensajería distribuida en tiempo real |
| 7 | Spark | **G** | Motor de procesamiento en memoria, sucesor de MapReduce, 100x más rápido |
| 8 | Docker | **H** | Tecnología de contenedores para desplegar clústeres Hadoop aislados |
| 9 | NameNode | **I** | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos |
| 10 | DataNode | **J** | Nodo trabajador de HDFS que almacena físicamente los bloques de datos |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

---

**16. (8 puntos) — MINSA: análisis de emergencias**

**a) Tipo de procesamiento para cada necesidad:**

- **Monitoreo en tiempo real** (datos cada 30 segundos) → **Streaming processing**. Los datos llegan continuamente y necesitan procesarse y responderse en segundos, no horas.
- **Análisis histórico de 5 años** para patrones estacionales → **Batch processing**. Se procesan grandes volúmenes de datos acumulados en períodos definidos (diario, semanal), sin necesidad de respuesta inmediata.

**b) Componentes recomendados:**

| Necesidad | Componentes recomendados |
|-----------|------------------------|
| Tiempo real (streaming) | Apache Kafka (ingesta de eventos) + Apache Spark Streaming o Apache Flink (procesamiento) + HBase (almacenamiento de alertas) |
| Análisis histórico (batch) | HDFS (almacenamiento del histórico) + Apache Spark (procesamiento batch) + Hive o Spark SQL (consultas analíticas) + Tableau o Power BI (visualización) |

**c) Justificación:**

Para el streaming elegí Kafka porque está diseñado para recibir millones de eventos por segundo con baja latencia — es exactamente el caso de 50+ hospitales enviando datos cada 30 segundos. Spark Streaming lo complementa procesando esos eventos en micro-batches de segundos. HBase permite guardar las alertas y consultarlas por hospital (Row Key) en tiempo real.

Para el histórico, HDFS es ideal porque puede almacenar petabytes de datos de forma distribuida y tolerante a fallos. Spark sobre HDFS permite hacer análisis complejos de 5 años de datos en minutos gracias al procesamiento en paralelo. No usaría una base de datos relacional porque 5 años de registros de todos los hospitales de Lima superaría fácilmente los límites de SQL Server.

---

**17. (8 puntos) — Localidad de datos en Hadoop**

**a) Problema que resuelve la "localidad de datos":**

En el modelo cliente-servidor tradicional, cuando necesitas procesar datos, los datos viajan de la base de datos al servidor de aplicaciones por la red. Esto crea un cuello de botella enorme: la red es mucho más lenta que el disco local. Hadoop invierte este principio — en lugar de mover los datos al código, **mueve el código a donde están los datos**. Cada DataNode procesa los bloques que ya tiene almacenados localmente, eliminando el tráfico de red para el procesamiento.

**b) ¿Por qué es especialmente importante con archivos de 1 TB o más?**

Transferir 1 TB por una red LAN de 10 Gbps tarda aproximadamente 800 segundos (más de 13 minutos). Si tienes un job MapReduce que necesita leer 100 TB de datos, la diferencia entre leerlos localmente (disco a velocidad de 500 MB/s) versus traerlos por red sería de horas vs días. La localidad de datos convierte un problema de red en un problema de disco local, que es significativamente más rápido y no genera congestión compartida entre todos los nodos.

**c) ¿Sigue siendo válido en cloud con S3 separado de EC2?**

Parcialmente. En cloud, S3 (almacenamiento) y EC2 (cómputo) están físicamente separados, por lo que la localidad de datos clásica no aplica directamente. Sin embargo, AWS optimiza esto de dos formas: primero, la red interna de AWS entre S3 y EC2 en la misma región es extremadamente rápida (25+ Gbps). Segundo, servicios como Amazon EMR o Spark con S3A connector usan técnicas de prefetch y caché para compensar. El principio sigue siendo válido en espíritu — por eso en cloud se prefiere usar la misma región para almacenamiento y cómputo, y tecnologías como Delta Lake que colean datos frecuentemente accedidos.

---

**18. (6 puntos) — Mini caso Tottus: análisis de canasta**

**a) ¿HDFS o base de datos relacional (SQL) para 25 GB?**

Usaría **HDFS** (o un Data Lake sobre S3). Aunque 25 GB técnicamente cabrían en una base de datos relacional, el análisis de canasta requiere hacer un JOIN o producto cartesiano de todos los productos comprados juntos, lo que genera una explosión combinatoria. Para 60 millones de filas, una base de datos SQL generaría timeouts o usaría índices ineficientes. HDFS + Spark pueden distribuir este procesamiento en múltiples nodos en paralelo, completando el análisis en minutos. Además, el mes siguiente serán otros 60 millones de filas — con HDFS simplemente se agregan sin límite.

**b) Pseudocódigo MapReduce para las 10 combinaciones más frecuentes:**

```
FASE MAP:
  Para cada boleta (una fila del CSV):
    Obtener lista_productos = [prod_A, prod_B, prod_C, ...]
    Para cada par de productos (prod_i, prod_j) donde i < j:
      Emitir clave: (prod_i, prod_j) → valor: 1

FASE SHUFFLE & SORT:
  Agrupar todos los pares iguales:
  (prod_A, prod_B) → [1, 1, 1, 1, ...]
  (prod_A, prod_C) → [1, 1, ...]

FASE REDUCE:
  Para cada par (prod_i, prod_j):
    total = SUM(lista de 1s)
    Emitir: (prod_i, prod_j) → total

POST-PROCESAMIENTO:
  Ordenar todos los pares por total DESC
  Tomar los primeros 10
  
RESULTADO:
  Top 10 pares de productos más comprados juntos
  Ejemplo: (Coca-Cola 1.5L, papas Lay's) → 145,230 boletas
```

---

**19. (8 puntos) — Single Point of Failure del NameNode**

**El problema en Hadoop 1.x:**

En Hadoop 1.x existía un único NameNode. Si ese servidor fallaba (reinicio, corte de luz, fallo de disco), **todo el clúster quedaba completamente inutilizable** aunque los DataNodes con los datos siguieran funcionando perfectamente. Nadie podía leer ni escribir porque no había "mapa" que dijera dónde estaban los bloques. Esto es el Single Point of Failure (SPOF): un único punto cuyo fallo paraliza todo el sistema.

Para empresas como el BCP o Telefónica que necesitan disponibilidad 24/7, esto era inaceptable. Un fallo del NameNode podía significar horas de inactividad total mientras se restauraba desde el último checkpoint — con pérdida de todos los cambios desde ese punto.

**La solución en Hadoop 2.x — Alta Disponibilidad (HA):**

Hadoop 2.x introdujo la arquitectura de HA con dos NameNodes:
- **NameNode Activo:** maneja todas las operaciones normalmente
- **NameNode Standby:** réplica en sincronía continua que puede tomar el control en segundos

La sincronización se hace a través de un conjunto de **JournalNodes** (al menos 3) que registran cada cambio del sistema de archivos. Si el NameNode Activo falla, **ZooKeeper** detecta el fallo automáticamente y promueve al Standby como nuevo Activo en segundos, sin intervención humana (failover automático).

**Implicaciones para sistemas críticos de producción:**

Todo sistema crítico en producción debe diseñarse eliminando los SPOF. En Big Data esto significa: NameNode en HA, múltiples JournalNodes, ZooKeeper con quórum impar (3 o 5 nodos), factor de replicación mínimo de 3, y DataNodes distribuidos en distintos racks físicos para que un corte de energía en un rack no elimine todas las réplicas de un bloque. Este principio se extiende a toda la arquitectura: bases de datos en cluster, balanceadores de carga redundantes, y múltiples zonas de disponibilidad en cloud.

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional: Civa — empresa de transporte (15 puntos)**

**a) Tabla de componentes por requerimiento:**

| Requerimiento | Tecnología | Justificación |
|--------------|-----------|---------------|
| Monitoreo en tiempo real de posición de buses | Apache Kafka + Apache Spark Streaming + HBase | Kafka ingesta los 6.9M registros GPS/día en tiempo real. Spark Streaming los procesa en micro-batches de segundos. HBase almacena la posición actual de cada bus (Row Key = ID_bus) para consultas instantáneas desde la app de pasajeros |
| Detección de conducción peligrosa automáticamente | Apache Kafka + Spark Streaming + MLlib (modelo de ML) | El mismo stream de Kafka alimenta un modelo de ML en Spark que analiza aceleraciones, velocidades y frenadas en ventanas de tiempo de 10 segundos para emitir alertas en tiempo real |
| Análisis histórico de 2 años para optimizar rutas | HDFS + Apache Spark (batch) + Hive / Spark SQL | Los datos GPS se almacenan en HDFS en formato Parquet particionado por fecha y ruta. Spark batch procesa los 2 años de datos para encontrar patrones de tráfico, demanda por ruta y horarios óptimos |
| Almacenamiento de videos 30 días | Amazon S3 / MinIO (Object Storage) | 38.4 TB/día × 30 días = 1.15 PB de video. Ni HDFS ni HBase son adecuados para esto. S3 o MinIO están diseñados para almacenar objetos binarios grandes (blobs) con bajo costo, alta durabilidad y recuperación eficiente por ID de video |

**b) ¿HBase o HDFS para datos GPS? Depende del caso de uso:**

**Usar HBase cuando:**
El caso de uso requiere consultas en tiempo real por bus individual. Ejemplo concreto: la app del pasajero pregunta "¿dónde está el bus Lima-Arequipa con ID 0342 ahora mismo?" HBase con Row Key = `bus_id + timestamp` devuelve esa posición en milisegundos. También para la pantalla del operador que necesita ver la posición de todos los buses en un mapa actualizado cada 5 segundos.

**Usar HDFS cuando:**
El caso de uso es análisis histórico masivo. Ejemplo concreto: el analista quiere saber cuáles rutas tienen más retrasos en las mañanas del mes de enero en los últimos 2 años, procesando todos los registros GPS de todos los buses. Este job en Spark sobre HDFS puede procesar 2 años de datos en minutos haciendo Spark SQL sobre archivos Parquet. Hacer esta query sobre HBase sería extremadamente ineficiente porque HBase no está optimizado para full table scans analíticos.

**c) ¿Dónde van los videos: HDFS, HBase o Object Storage?**

Los videos van en **Amazon S3 / MinIO (almacenamiento de objetos)**. Las razones son claras:

1. **Volumen inmanejable para HDFS:** 38.4 TB/día × 30 días = **1.15 PB** de video. HDFS puede manejar este volumen técnicamente, pero está optimizado para archivos de texto y datos estructurados, no para archivos binarios de video de 2 GB.

2. **HBase es completamente inadecuado:** HBase está diseñado para millones de registros pequeños con acceso aleatorio. Guardar archivos de video de 2 GB en celdas de HBase destruiría el rendimiento del sistema completo.

3. **S3/MinIO es la opción correcta porque:**
   - Diseñado específicamente para objetos binarios grandes (videos, imágenes, backups)
   - Costo por GB significativamente menor que HDFS
   - Recuperación eficiente por ID de video (bus_id + fecha + hora)
   - Lifecycle policies automáticas: elimina automáticamente los videos después de 30 días sin código adicional
   - Alta durabilidad (11 nueves de durabilidad en S3)

---

**21. Diseño: Sistema de detección de fraude bancario en tiempo real (8 puntos)**

**Arquitectura de componentes:**

```
TRANSACCIÓN BANCARIA
        │
        ▼
[Apache Kafka]  ← ingesta de 10,000 tx/segundo
Topic: "transacciones"
        │
        ▼
[Apache Spark Streaming]  ← ventanas de 2 segundos
  ├── Reglas de negocio (monto > umbral, país inusual)
  ├── Modelo ML de detección de anomalías (Spark MLlib)
  └── Comparación con historial reciente (Redis cache)
        │
        ├── Si NO sospechosa → [HBase] (registro normal)
        └── Si sospechosa →
                │
                ▼
            [Sistema de alertas]
            ├── Bloqueo automático de la tarjeta (API bancaria)
            ├── Notificación push al cliente
            └── Dashboard de fraude en tiempo real (Grafana)
```

**Flujo de datos:**

1. El cliente hace una transacción → el sistema bancario publica el evento en Kafka
2. Spark Streaming consume el evento en menos de 100ms
3. Spark consulta Redis (caché en memoria) para obtener el historial reciente del cliente en milisegundos
4. El modelo ML evalúa la transacción contra el perfil del cliente
5. Si el score de fraude supera el umbral → alerta en menos de 2 segundos total

**¿Por qué MapReduce NO sirve aquí?**

MapReduce está diseñado para procesamiento batch: toma un conjunto de datos, los procesa todos, y devuelve un resultado. La latencia mínima de un job MapReduce es de varios minutos (tiempo de inicio del job + lectura de disco + shuffle + escritura). Para detectar fraude, cuando MapReduce termina de "analizar" la transacción, el dinero ya salió de la cuenta hace 10 minutos.

**¿Qué reemplaza a MapReduce?**

Apache Spark Streaming (o Apache Flink para mayor precisión). Procesan datos en micro-batches de milisegundos manteniendo el estado en memoria RAM, sin escribir a disco entre operaciones. Esto permite evaluar 10,000 transacciones/segundo con latencia menor a 2 segundos.

---

**22. Pensamiento crítico: ¿HBase para TODO? (7 puntos)**

**¿Es técnicamente posible?**

Técnicamente sí, se puede almacenar todo en HBase. HBase puede guardar petabytes de datos. Pero "posible" no significa "correcto" — sería como usar un Ferrari para transportar cemento: funciona, pero es la herramienta equivocada.

**Problemas de rendimiento:**

HBase está optimizado para acceso aleatorio por Row Key a registros individuales. Cuando intentas hacer un análisis histórico de 5 años sobre petabytes en HBase, necesitas hacer un **full table scan** — leer toda la tabla fila por fila. Esto es extremadamente lento porque HBase no tiene índices secundarios nativos ni optimizaciones para queries analíticos. El mismo análisis sobre HDFS en formato Parquet con Spark tomaría minutos; sobre HBase podría tomar horas o días.

**Problemas de costo:**

HBase requiere un clúster activo y en memoria 24/7 (ZooKeeper, HMaster, RegionServers). HDFS para datos históricos fríos puede usar discos baratos en "cold storage". Almacenar 5 años de datos en HBase costaría significativamente más que en HDFS o S3, sin ningún beneficio para el caso de uso analítico.

**Problemas de escalabilidad:**

HBase escala bien para escrituras y lecturas aleatorias, pero las queries analíticas (GROUP BY, JOIN, agregaciones) son lentas porque no tiene un optimizador de consultas equivalente al Catalyst de Spark. A medida que los datos crecen a petabytes, los full scans analíticos se vuelven inmanejables.

**Riesgo en producción:**

El mayor riesgo es que un full scan analítico sobre HBase puede consumir todos los recursos del clúster (CPU, I/O de red, memoria de los RegionServers), afectando las consultas en tiempo real que son el caso de uso principal de HBase. En producción, esto podría significar que las consultas de saldo de clientes se vuelven lentas o fallan porque un analista lanzó una query histórica masiva al mismo tiempo.

**Evidencia de la sesión de clase:**

La sesión definió que HBase es para "acceso aleatorio en tiempo real" y HDFS para "almacenamiento distribuido de grandes volúmenes para procesamiento batch". La arquitectura Lambda y la arquitectura Medallion (Bronze/Silver/Gold) que vimos en clase separan explícitamente el almacenamiento histórico (cold) del operacional (hot) precisamente por estas razones de rendimiento y costo.

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Estudiante: Ana Concepción Asto Arotinco*
