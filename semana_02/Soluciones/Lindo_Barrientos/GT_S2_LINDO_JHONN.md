# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | LINDO BARRIENTOS JHONN VIEQUIER |
| **Código de estudiante** | 2221896680 |
| **Sección** | SECCION 06 |
| **Fecha** | 18/06/2026 |
| **Tiempo estimado** | 1.5 horas |
| **Puntaje total** | 100 puntos |

---

### INSTRUCCIONES

- Lee cada pregunta con atención antes de responder.
- Esta guía evalúa los temas vistos en la sesión de la Semana 2.
- Tiempo recomendado: 90 minutos.
- **No incluyas respuestas en este documento** — responde en papel o en el documento que te indique el docente.
- Las preguntas van de menor a mayor dificultad. Completa en orden.
- Para las preguntas de código, puedes escribir pseudocódigo si no recuerdas la sintaxis exacta.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts cada una)

*Marca con una X la alternativa correcta. Solo una respuesta es válida.*

---

**1.** ¿Cuál es la función principal del NameNode en HDFS?

a) Almacenar los bloques de datos distribuidos en el clúster  
b) Procesar las tareas MapReduce asignadas a cada nodo  
**c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos[x]**  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
**c) 128 MB[x]**  
d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
**b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer[x]**  
c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
**c) YARN[x]**  
d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
**b) HBase — porque permite acceso aleatorio en tiempo real por Row Key[x]**  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
**b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos[x]**  
c) Cloud es gratuito y Fog es de pago  
d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
**d) 12[x]**  

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
**c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)[x]**  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
**c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs[x]**  
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  

---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
**c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3[x]**  
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama **NameNode**, mientras que los nodos que guardan físicamente los bloques de datos se llaman **DataNodes**.

**12.** El modelo de programación **MapReduce** divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares **clave-valor (key-value)**, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada **Hipervisor**.

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado **Row Key**, que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el **borde (edge)** de la red (cerca de los dispositivos), reduciendo la **latencia** de comunicación con el data center central.

---

### B2. Relacionar columnas (10 puntos | 1 pt cada par correcto)

Relaciona cada concepto (columna izquierda) con su descripción correcta (columna derecha). Escribe la letra correspondiente.

| N° | Concepto | | Letra | Descripción |
|----|----------|-|-------|-------------|
| 1 | YARN |E | A | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real |
| 2 | ZooKeeper |C | B | Herramienta para importar/exportar datos entre RDBMS y HDFS |
| 3 | HBase |A | C | Framework de coordinación y sincronización distribuida en el ecosistema Hadoop |
| 4 | Sqoop |B | D | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse) |
| 5 | Hive |D | E | Gestor de recursos del clúster Hadoop que asigna CPU/RAM a los trabajos |
| 6 | Kafka |F | F | Plataforma de streaming de eventos y mensajería distribuida en tiempo real |
| 7 | Spark |G | G | Motor de procesamiento en memoria, sucesor de MapReduce, 100x más rápido |
| 8 | Docker |H | H | Tecnología de contenedores para desplegar clústeres Hadoop aislados |
| 9 | NameNode |I | I | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos |
| 10 | DataNode |J | J | Nodo trabajador de HDFS que almacena físicamente los bloques de datos |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas. Extensión sugerida: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El MINSA desea implementar un sistema para analizar los reportes de emergencias en todos los hospitales de Lima en tiempo real (cada hospital envía datos cada 30 segundos) y también quiere hacer análisis históricos de los últimos 5 años para identificar patrones estacionales de enfermedades.

a) ¿Qué tipo de procesamiento requiere cada necesidad (batch o streaming)?

**Reportes de emergencias cada 30 segundos → procesamiento STREAMING (tiempo real)**

**Análisis histórico de patrones estacionales de 5 años → procesamiento BATCH (por lotes)** 
 
b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?

**Para el streaming: Apache Kafka (ingesta de los eventos que envían los hospitales cada 30s) + Apache Spark Streaming (procesamiento en tiempo real) y un dashboard de monitoreo.**

**Para el histórico: HDFS o un Data Lake en la nube (almacenamiento de los 5 años de datos) + Apache Spark / Hive para las consultas analíticas por lotes.**
  
c) Justifica por qué elegiste esos componentes y no otros.

**Kafka y Spark Streaming son ideales para el flujo continuo porque procesan los eventos a medida que llegan, con baja latencia, permitiendo alertas inmediatas ante un brote. Para el histórico de 5 años no se necesita tiempo real, sino capacidad de procesar grandes volúmenes acumulados; por eso HDFS (almacenamiento distribuido y barato) con Spark/Hive (consultas analíticas masivas) es lo más eficiente y económico. Usar streaming para el histórico sería innecesariamente caro, y usar batch para las emergencias sería demasiado lento para salvar vidas.**

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Qué problema resuelve la "localidad de datos" en Hadoop?

**Resuelve el cuello de botella de la red. En lugar de mover los datos hacia donde está el programa (como en cliente-servidor), Hadoop mueve el código de procesamiento hacia donde ya están los datos (al DataNode que tiene el bloque). Así se evita transferir grandes volúmenes por la red.**
  
b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?

**Mover 1 TB a través de la red para procesarlo en otro servidor tomaría muchísimo tiempo y saturaría el ancho de banda del clúster. Procesando cada bloque en el nodo donde ya reside, el trabajo se hace en paralelo y solo viajan por la red los resultados (pequeños), no los datos crudos (enormes).**
  
c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

**El principio se relaja en la nube, porque al separar almacenamiento (S3) y cómputo (EC2/EMR) los datos sí deben viajar por la red. Sin embargo, los proveedores compensan esto con redes internas de altísima velocidad, capas de caché y formatos columnares optimizados (como Parquet) que minimizan cuántos datos hay que leer. Es un trade-off: se pierde algo de localidad pero se gana flexibilidad y escalado independiente de cómputo y almacenamiento.**

---

**18. (6 puntos) — Mini caso de análisis:**

*La cadena Tottus Perú genera 2 millones de boletas de venta al día en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, método de pago. Al final del mes, el gerente de analytics quiere saber: ¿qué combinaciones de productos se compran juntas con mayor frecuencia (análisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.

**Usaría HDFS. Una base relacional tradicional sufre con 60 millones de filas en consultas analíticas que recorren toda la tabla, y el análisis de canasta es un proceso batch (una vez al mes), no transaccional. HDFS + un motor distribuido (Spark/MapReduce) procesa esos 25 GB en paralelo de forma mucho más eficiente y escalable que un SQL monolítico.**
  
b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

<b>// FASE MAP
map(clave, boleta):
    productos = boleta.lista_de_productos
    // generar todos los pares de productos comprados juntos
    para cada par (A, B) en combinaciones(productos, 2):
        par_ordenado = ordenar(A, B)   // (Leche, Pan) = (Pan, Leche)
        emitir(par_ordenado, 1)

// FASE SHUFFLE AND SORT (automática)
// agrupa todos los "1" de cada par de productos igual

// FASE REDUCE
reduce(par_producto, lista_de_unos):
    total = suma(lista_de_unos)
    emitir(par_producto, total)

// PASO FINAL (ordenar y tomar top 10)
ordenar todos los pares por total descendente
devolver los primeros 10 pares</b>

---

**19. (8 puntos)** Explica por qué el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y cómo lo resolvió Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). 

<b>En Hadoop 1.x existía un único NameNode que guardaba todos los metadatos del sistema de archivos. Si ese NameNode fallaba, todo el clúster quedaba inaccesible: aunque los datos seguían físicamente en los DataNodes, sin el "mapa" de metadatos era imposible saber dónde estaba cada bloque. Ese era el famoso "Single Point of Failure" (punto único de fallo).

Hadoop 2.x lo resolvió con la arquitectura de Alta Disponibilidad (HA): introduce dos NameNodes, uno Activo y uno en Espera (Standby). Ambos se mantienen sincronizados mediante JournalNodes (que registran cada cambio) y ZooKeeper (que detecta la caída del activo y promueve automáticamente al standby). Si el NameNode activo cae, el standby toma el control en segundos sin interrumpir el servicio.</b>

¿Qué implicaciones tiene este problema para el diseño de sistemas críticos de producción?

**Ningún sistema de misión crítica (un banco, un hospital, una telco) puede depender de un único componente cuya caída detenga todo. El diseño debe eliminar los puntos únicos de fallo mediante redundancia y failover automático. La lección es que la tolerancia a fallos no es opcional en producción: debe diseñarse desde el inicio, no agregarse después.**

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional real (15 puntos)**

*Eres el arquitecto de datos de la empresa Civa (empresa de transporte interprovincial en Perú). Civa opera 1,200 buses en 300 rutas. Cada bus tiene un dispositivo GPS que envía posición, velocidad y estado del motor cada 15 segundos. Adicionalmente, cada bus tiene cámaras de seguridad que graban continuamente (video comprimido: 2 GB/hora). La empresa quiere:*

*1. Monitorear en tiempo real la posición de todos los buses para informar a los pasajeros*  
*2. Detectar conducción peligrosa (frenadas bruscas, exceso de velocidad) automáticamente*  
*3. Analizar históricamente los datos de los últimos 2 años para optimizar rutas*  
*4. Almacenar los videos para revisión en caso de incidentes (se conservan 30 días)*

*Volumen de datos estimado: 1,200 buses × 4 datos GPS/min × 1,440 min/día = 6.9 millones de registros GPS/día. Videos: 1,200 buses × 2 GB/hora × 16 horas/día = 38,400 GB (38.4 TB) de video al día.*

Responde:

a) ¿Qué componentes del ecosistema Hadoop/Cloud usarías para cada uno de los 4 requerimientos? Crea una tabla con: Requerimiento | Tecnología | Justificación (5 puntos)


| Requerimiento | Tecnología | Justificación |
| :--- | :--- | :--- |
| **1.** Monitoreo en tiempo real de posición de buses | Apache Kafka + Spark Streaming | Los GPS envían datos cada 15s; se necesita procesarlos al instante para mostrar posición en vivo a los pasajeros |
| **2.** Detectar conducción peligrosa | Spark Streaming + reglas/ML en tiempo real | Frenadas bruscas o exceso de velocidad deben detectarse en segundos para alertar; requiere análisis del flujo en vivo |
| **3.** Análisis histórico de 2 años para optimizar rutas | HDFS / Data Lake + Spark (batch) + Hive | Es procesamiento masivo por lotes sobre datos acumulados; no requiere tiempo real |
| **4.** Almacenar videos 30 días para incidentes | Almacenamiento de objetos (Amazon S3 / MinIO) | E1.15 PB de video se guardan más barato y escalable en object storage que en HDFS o HBase |

b) Para los datos GPS, ¿usarías HBase o HDFS? ¿Por qué depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

Depende del caso de uso:


**HBase si la necesidad es consultar la última posición de UN bus específico en tiempo real. Ejemplo: "¿dónde está ahora mismo el bus que cubre la ruta Lima-Arequipa placa X?" → búsqueda puntual por Row Key (placa+timestamp), respuesta en milisegundos.**

**HDFS si la necesidad es el análisis histórico masivo. Ejemplo: "analizar los 6.9 millones de registros GPS diarios de los últimos 2 años para encontrar las rutas con más demoras" → barrido completo de datos en batch con Spark.**

En la práctica se usan ambos: HBase para el acceso en vivo y HDFS para el histórico.

c) ¿Los videos irían a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/día × 30 días = 1.15 PB). (5 puntos)

**Los videos irían a un almacenamiento de objetos (S3 / MinIO), no a HDFS ni HBase. Razones considerando el volumen (38 TB/día × 30 días = 1.15 PB):**

**-El object storage está diseñado para archivos grandes e inmutables (como videos) a un costo por TB mucho menor.  
-HDFS sufriría con tantos archivos grandes porque sobrecargaría la memoria del NameNode con metadatos, y mantener réplicas de 1.15 PB sería carísimo.  
-HBase está pensado para registros pequeños con acceso aleatorio, no para blobs de video de 2 GB/hora.  
-S3/MinIO permite políticas de retención automática (borrar a los 30 días) y escala virtualmente sin límite.**


---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)
- Cómo fluyen los datos desde la transacción hasta la alerta
- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso
- Qué herramienta reemplazaría a MapReduce en este escenario

<b>**Arquitectura por capas:**

* **Capa de ingesta:** Apache Kafka, recibiendo las 10,000 transacciones por segundo como flujo de eventos.
* **Capa de procesamiento en tiempo real:** Apache Spark Streaming (o Apache Flink), que consume el flujo de Kafka y evalúa cada transacción.
* **Capa de consulta rápida:** HBase, para verificar en milisegundos el historial/perfil del cliente (lookup por Row Key) y enriquecer la decisión.
* **Capa de modelo:** un modelo de Machine Learning entrenado (ej. con MLlib) que asigna un score de riesgo a cada transacción.
* **Capa de alerta/salida:** si el score supera el umbral, se emite una alerta (a otro topic de Kafka, a un dashboard o al sistema antifraude).

Flujo de datos:
Transacción → Kafka (ingesta) → Spark Streaming (procesa el evento) → consulta a HBase del perfil del cliente → el modelo ML calcula el score de riesgo → si es sospechoso, se dispara la alerta en menos de 2 segundos.

Por qué MapReduce NO sería suficiente:
MapReduce es un motor batch: agrupa los datos y los procesa en lotes, escribiendo resultados intermedios en disco entre fases. Eso introduce minutos (u horas) de latencia. Para el fraude, una alerta que llega 10 minutos después es inútil porque la transacción fraudulenta ya se aprobó. MapReduce no fue diseñado para procesar eventos individuales en milisegundos.

Qué reemplaza a MapReduce:
Apache Spark Streaming o Apache Flink, que procesan los datos en memoria y en streaming (evento por evento o en micro-lotes), logrando la baja latencia que exige el caso.</b>

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
- ¿Es técnicamente posible?

**Sí, técnicamente se puede almacenar todo en HBase, pero es una mala decisión de diseño.**

- ¿Cuáles serían los problemas de rendimiento, costo y escalabilidad?

Problemas de rendimiento, costo y escalabilidad:


**Rendimiento:** HBase está optimizado para acceso aleatorio puntual (por Row Key), no para escaneos analíticos masivos. Analizar 5 años de datos (petabytes) requeriría full table scans que en HBase son lentos e ineficientes comparados con Spark/Hive sobre HDFS o formatos columnares como Parquet.   
**Costo:** HBase consume mucha más RAM y recursos por la sobrecarga de mantener regiones, memstores y compactaciones. Guardar petabytes históricos en HBase es mucho más caro que en HDFS o en almacenamiento de objetos.  
**Escalabilidad:** Las compactaciones y el balanceo de regiones se vuelven un cuello de botella operativo a escala de petabytes para datos que en realidad solo se consultan ocasionalmente.

- ¿Cuál sería el riesgo de este diseño en producción?

**El clúster se vuelve costoso, difícil de mantener y con rendimiento degradado tanto para el tiempo real como para el análisis. Se pierde la ventaja de HBase (velocidad en acceso aleatorio) al saturarlo con datos históricos que no necesitan ese patrón de acceso.**

- ¿Qué evidencia de la sesión de clase apoya tu respuesta?

**Cada herramienta del ecosistema Hadoop tiene un propósito específico: HDFS para almacenamiento histórico masivo y barato, HBase para acceso aleatorio en tiempo real. La arquitectura correcta los combina (HDFS para el histórico, HBase para el tiempo real) en lugar de forzar una sola herramienta para todo. Usar la herramienta equivocada para un caso de uso es un antipatrón de diseño en Big Data.**

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
