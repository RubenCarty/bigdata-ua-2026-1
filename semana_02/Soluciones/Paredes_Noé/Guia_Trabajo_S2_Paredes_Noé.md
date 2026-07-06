<<<<<<< HEAD
# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Noé Jesús paredes Hilario |
| **Código de estudiante** | 2221895643|
| **Sección** | 6 - 202601  |
| **Fecha** | 19/06/2026 |
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
X c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
X c) 128 MB  
d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
X b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer  
c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
X c) YARN  
d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
X b) HBase — porque permite acceso aleatorio en tiempo real por Row Key  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos  
c) Cloud es gratuito y Fog es de pago  
X d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
X d) 12  

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
X c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
X c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs  
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  

---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
X c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3  
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama NameNode, mientras que los nodos que guardan físicamente los bloques de datos se llaman DataNodes.

**12.** El modelo de programación MapReduce divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares clave-valor, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada hipervisor (o Hypervisor / Monitor de Máquina Virtual).

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado Row Key (o Clave de Fila), que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el borde (o edge) de la red (cerca de los dispositivos), reduciendo la latencia de comunicación con el data center central.

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
El reporte de emergencias cada 30 segundos requiere procesamiento en tiempo real (streaming) para actuar de inmediato, mientras que el análisis histórico de los últimos 5 años exige procesamiento por lotes (batch) para manejar grandes volúmenes de datos acumulados.

b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?  

Para la necesidad de streaming se recomienda utilizar Apache Kafka junto con Apache Spark Streaming, mientras que para el análisis batch de datos históricos se debe emplear HDFS (o un Data Lake como AWS S3) combinado con Apache Spark SQL.

c) Justifica por qué elegiste esos componentes y no otros.

Se eligen porque Kafka soporta la ingesta masiva y continua de todos los hospitales con baja latencia, mientras que Spark unifica ambos mundos al procesar el streaming en tiempo real y el análisis batch en memoria RAM, siendo hasta 100 veces más rápido que el antiguo MapReduce.

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Qué problema resuelve la "localidad de datos" en Hadoop? 

La localidad de datos resuelve el cuello de botella de la red al mover el código de procesamiento (que pesa pocos kilobytes) hacia el nodo donde ya están guardados los datos, evitando tener que transferir gigabytes de información a través de los cables del clúster. 
b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?  

Mover un archivo de 1 TB o más por la red saturaría los switches y tardaría minutos u horas en transferirse antes de poder empezar a procesar; al aplicar este principio, el procesamiento inicia de inmediato de forma paralela y local en los discos donde residen los bloques del archivo.

c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

No sigue siendo estrictamente válido porque el almacenamiento y el cómputo se separan físicamente para ahorrar costos; sin embargo, se mitiga el impacto usando redes de altísima velocidad (100 Gbps), almacenamiento en caché local (como Alluxio o NVMe) y técnicas de data-skipping para minimizar la transferencia de datos.

---

**18. (6 puntos) — Mini caso de análisis:**

*La cadena Tottus Perú genera 2 millones de boletas de venta al día en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, método de pago. Al final del mes, el gerente de analytics quiere saber: ¿qué combinaciones de productos se compran juntas con mayor frecuencia (análisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.  

Se recomienda utilizar HDFS (o un Data Lake) porque, aunque 25 GB caben en una base de datos SQL tradicional, las tablas relacionales sufren y se vuelven sumamente lentas al ejecutar consultas analíticas complejas de combinaciones masivas (joins cruzados de 60 millones de filas), mientras que HDFS permite procesar esto de forma distribuida y escalable.

b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

**b) Pseudocódigo de MapReduce:**

<pre style="background-color: #2d3748; color: #fff; padding: 15px; border-radius: 5px; font-family: monospace; font-size: 13px; line-height: 1.5; margin: 10px 0;">
Función MAP(id_boleta, lista_productos):
    Para cada producto_A en lista_productos:
        Para cada producto_B en lista_productos posterior a producto_A:
            Emitir(Clave: "producto_A, producto_B", Valor: 1)

Función REDUCE(par_productos, lista_valores):
    suma_total = 0
    Para cada valor en lista_valores:
        suma_total += valor
    Emitir(Clave: par_productos, Valor: suma_total)

Función LIMITE_TOP10(salida_reduce):
    Ordenar salida_reduce de mayor a menor según el Valor
    Retornar los primeros 10 elementos.
</pre>

---

**19. (8 puntos)** Explica por qué el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y cómo lo resolvió Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). ¿Qué implicaciones tiene este problema para el diseño de sistemas críticos de producción?


a) El problema en Hadoop 1.x: El NameNode centralizaba todos los metadatos del clúster; si este único servidor fallaba por hardware o software, todo el sistema quedaba inoperable de inmediato, bloqueando el acceso a los datos y deteniendo la producción de la empresa durante horas.
b) Solución en Hadoop 2.x (Alta Disponibilidad): Se implementó un esquema Activo-Pasivo mediante dos NameNodes sincronizados en tiempo real a través de un grupo de nodos llamado Journal Nodes; si el principal falla, el de respaldo asume el control de forma automática en milisegundos sin interrumpir el servicio.
c) Implicaciones en producción: Para el diseño de sistemas críticos, este caso demuestra que nunca se debe permitir un único punto de falla, obligando a los arquitectos a estructurar soluciones con redundancia de hardware y mecanismos de failover automático para asegurar una disponibilidad de $24/7$

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

### a) Tabla de Arquitectura Tecnológica

| Requerimiento | Tecnología | Justificación |
| :--- | :--- | :--- |
| **1. Monitorear posición en tiempo real** | Apache Kafka + Redis | Kafka absorbe los eventos GPS cada 15 segundos sin latencia y Redis guarda la última posición para consultas instantáneas de los pasajeros. |
| **2. Detectar conducción peligrosa** | Apache Spark Streaming | Procesa el flujo continuo de datos GPS en ventanas de tiempo para calcular aceleraciones y alertar excesos de velocidad en segundos. |
| **3. Análisis histórico de 2 años** | HDFS + Apache Spark | Permite almacenar miles de millones de registros GPS históricos a bajo costo y ejecutar consultas masivas para optimizar rutas y tiempos. |
| **4. Almacenamiento de videos (30 días)** | AWS S3 o MinIO | Es el único almacenamiento con la escalabilidad y economía necesarias para albergar 1.15 PB de archivos binarios sin saturar los nodos. |

b) Para los datos GPS, ¿usarías HBase o HDFS? ¿Por qué depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

Depende del patrón de acceso: se usa HBase para lecturas y escrituras aleatorias rápidas en tiempo real, mientras que HDFS se usa para análisis masivo secuencial por lotes (batch).

Ejemplo HBase (Tiempo Real): Cuando un pasajero abre la app de Civa para ver dónde está exactamente su bus, la app consulta a HBase usando la clave ID_BUS, trayendo de forma inmediata (milisegundos) la última coordenada registrada.

Ejemplo HDFS (Histórico): Cuando el equipo de analytics quiere saber la velocidad promedio de los buses en la ruta Lima-Piura durante todo el año 2025; se escanea el archivo consolidado en HDFS de forma secuencial para procesar grandes volúmenes en bloque.

c) ¿Los videos irían a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/día × 30 días = 1.15 PB). (5 puntos)

Los videos deben ir obligatoriamente a un almacenamiento de objetos (AWS S3 o MinIO).

Por qué no HDFS/HBase: HDFS sufriría con el NameNode al gestionar millones de bloques de video gigantescos, elevando los costos drásticamente por su factor de réplica por defecto ($3x$), lo que exigiría triplicar el hardware físico a más de 3.4 PB. HBase es para datos estructurados tabulares, no para archivos binarios masivos (blobs).

Ventaja de Objetos: S3 o MinIO escalan de forma transparente a nivel de Petabytes a una fracción del costo, poseen políticas de ciclo de vida automáticas para borrar los videos a los 30 días exactos y permiten el acceso directo a cada archivo de video mediante una URL única solo cuando ocurre un incidente.

---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)

Para soportar 10,000 transacciones por segundo (tps) con una latencia menor a 2 segundos, se requiere una Arquitectura Kappa o de streaming unificado utilizando los siguientes componentes:

Capa de Ingesta (Mensajería): Apache Kafka. Actúa como el búfer central de alta disponibilidad capaz de recibir las 10,000 tps desde los sistemas bancarios con latencias de milisegundos.

Capa de Procesamiento en Tiempo Real: Apache Spark Streaming (o Apache Flink). Procesa las transacciones en micro-lotes o evento por evento aplicando las reglas de negocio y modelos de Machine Learning.

Capa de Almacenamiento Rápido (Servicio): Apache HBase (o Amazon DynamoDB). Guarda perfiles rápidos de los clientes (últimos saldos, ubicaciones recientes) para enriquecer la transacción sobre la marcha.

Capa de Alertas: Redis + Sistema de Notificaciones push (Websockets/Microservicios). Almacena las alertas temporales y las despacha inmediatamente al sistema de bloqueos del banco.

- Cómo fluyen los datos desde la transacción hasta la alerta

1. Captura: El cliente pasa su tarjeta; el sistema transaccional del banco envía los datos en formato JSON/Avro a un tópico de Kafka (transactions-stream).

2. Enriquecimiento: Spark Streaming consume el evento de Kafka al instante y hace un lookup (búsqueda rápida) en HBase mediante la clave de cliente para obtener su historial reciente (ej. "¿Hizo una compra en otro país hace 10 minutos?").

3. Evaluación: Spark evalúa las reglas anti-fraude o ejecuta un modelo predictivo sobre los datos consolidados.

4. Alerta: Si el patrón es sospechoso, Spark escribe el resultado en Redis y gatilla un evento de alerta hacia el microservicio de seguridad del banco, el cual bloquea la transacción en menos de 2 segundos.

- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso

El procesamiento batch tradicional con MapReduce está diseñado para rendimiento masivo, no para baja latencia.

a.- Uso intensivo de disco: MapReduce escribe obligatoriamente todos los resultados intermedios de los pasos Map y Reduce en los discos duros de HDFS. Este intercambio constante de lectura/escritura (I/O de disco) eleva los tiempos de procesamiento a minutos u horas.

b.- Modelo por lotes: MapReduce necesita acumular un volumen de datos ("el lote") antes de arrancar el trabajo. En un caso de fraude bancario, esperar a juntar las transacciones de los últimos 10 minutos para iniciar el análisis significaría que el dinero ya habría sido robado mucho antes de emitir la alerta.

- Qué herramienta reemplazaría a MapReduce en este escenario

La herramienta ideal para reemplazar a MapReduce en este escenario es Apache Spark (específicamente Spark Streaming) o Apache Flink.

Justificación: Estas herramientas reemplazan el flujo basado en disco de MapReduce por un motor de procesamiento en memoria RAM. Permiten analizar flujos continuos de datos con abstracciones como DataStreams, ejecutando operaciones analíticas complejas directamente sobre la memoria de los nodos del clúster, reduciendo el tiempo de procesamiento de horas a simples fracciones de segundo (milisegundos).

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
- ¿Es técnicamente posible?

Sí, es técnicamente posible. Dado que HBase se ejecuta sobre HDFS como su capa de almacenamiento subyacente, toda la información guardada en HBase se almacena físicamente en el clúster. Sin embargo, que sea posible no significa que sea correcto: HBase está diseñado como una base de datos NoSQL para accesos aleatorios rápidos de lectura/escritura, no como un repositorio de archivos de propósito general para analítica masiva.

- ¿Cuáles serían los problemas de rendimiento, costo y escalabilidad?

a.- Rendimiento en consultas masivas (Batch): Para un análisis histórico de 5 años (Petabytes), HBase sufrirá una degradación masiva. Mientras que HDFS lee archivos secuencialmente a gran velocidad en bloque, HBase tiene que buscar a través de sus regiones (RegionServers) y estructuras internas (MemStore, HFiles), sobrecargando la CPU y la memoria RAM para un proceso que solo requería lectura lineal de discos.

b.- Costos elevados de infraestructura: Mantener Petabytes en HBase exige una cantidad enorme de memoria RAM y almacenamiento en discos de alta velocidad (como SSD o NVMe) para que los índices de las tablas sigan siendo rápidos. Guardar datos históricos fríos de 5 años en un entorno tan caro destruye el principio de costo-eficiencia de Big Data.

c.- Escalabilidad: Al acumular Petabytes de datos históricos, la cantidad de regiones en HBase se multiplicará. Esto generará problemas críticos en el NameNode y en el Zookeeper para coordinar el clúster, ralentizando las operaciones de división de regiones (region splits) y compactaciones de datos.

- ¿Cuál sería el riesgo de este diseño en producción?

El mayor riesgo es el impacto directo y destructivo en el negocio en tiempo real. Si el equipo de analítica lanza una consulta pesada para procesar los 5 años de historia, los RegionServers se saturarán al 100% de CPU y memoria RAM. Como consecuencia, las consultas críticas de los clientes en tiempo real (las que necesitan responder en milisegundos) se encolarán o fallarán por timeout, provocando caídas del servicio en producción.

- ¿Qué evidencia de la sesión de clase apoya tu respuesta?

Este análisis se fundamenta en la separación de capas de la Arquitectura Lambda/Kappa y el funcionamiento nativo de los componentes:

a.- HDFS está optimizado para accesos secuenciales (Streaming Read) de archivos gigantescos (bloques de 128 MB por defecto), ideal para escaneos de lotes (MapReduce/Spark).

b.- HBase organiza los datos en tablas de columnas llave-valor orientadas a accesos aleatorios de baja latencia (Random Read/Write), utilizando memoria RAM (MemStore) para asegurar la velocidad en tiempo real.


---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
=======
# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Noé Jesús paredes Hilario |
| **Código de estudiante** | 2221895643|
| **Sección** | 6 - 202601  |
| **Fecha** | 19/06/2026 |
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
X c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
X c) 128 MB  
d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
X b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer  
c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
X c) YARN  
d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
X b) HBase — porque permite acceso aleatorio en tiempo real por Row Key  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos  
c) Cloud es gratuito y Fog es de pago  
X d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
X d) 12  

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
X c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
X c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs  
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  

---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
X c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3  
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama NameNode, mientras que los nodos que guardan físicamente los bloques de datos se llaman DataNodes.

**12.** El modelo de programación MapReduce divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares clave-valor, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada hipervisor (o Hypervisor / Monitor de Máquina Virtual).

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado Row Key (o Clave de Fila), que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el borde (o edge) de la red (cerca de los dispositivos), reduciendo la latencia de comunicación con el data center central.

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
El reporte de emergencias cada 30 segundos requiere procesamiento en tiempo real (streaming) para actuar de inmediato, mientras que el análisis histórico de los últimos 5 años exige procesamiento por lotes (batch) para manejar grandes volúmenes de datos acumulados.

b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?  

Para la necesidad de streaming se recomienda utilizar Apache Kafka junto con Apache Spark Streaming, mientras que para el análisis batch de datos históricos se debe emplear HDFS (o un Data Lake como AWS S3) combinado con Apache Spark SQL.

c) Justifica por qué elegiste esos componentes y no otros.

Se eligen porque Kafka soporta la ingesta masiva y continua de todos los hospitales con baja latencia, mientras que Spark unifica ambos mundos al procesar el streaming en tiempo real y el análisis batch en memoria RAM, siendo hasta 100 veces más rápido que el antiguo MapReduce.

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Qué problema resuelve la "localidad de datos" en Hadoop? 

La localidad de datos resuelve el cuello de botella de la red al mover el código de procesamiento (que pesa pocos kilobytes) hacia el nodo donde ya están guardados los datos, evitando tener que transferir gigabytes de información a través de los cables del clúster. 
b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?  

Mover un archivo de 1 TB o más por la red saturaría los switches y tardaría minutos u horas en transferirse antes de poder empezar a procesar; al aplicar este principio, el procesamiento inicia de inmediato de forma paralela y local en los discos donde residen los bloques del archivo.

c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

No sigue siendo estrictamente válido porque el almacenamiento y el cómputo se separan físicamente para ahorrar costos; sin embargo, se mitiga el impacto usando redes de altísima velocidad (100 Gbps), almacenamiento en caché local (como Alluxio o NVMe) y técnicas de data-skipping para minimizar la transferencia de datos.

---

**18. (6 puntos) — Mini caso de análisis:**

*La cadena Tottus Perú genera 2 millones de boletas de venta al día en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, método de pago. Al final del mes, el gerente de analytics quiere saber: ¿qué combinaciones de productos se compran juntas con mayor frecuencia (análisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.  

Se recomienda utilizar HDFS (o un Data Lake) porque, aunque 25 GB caben en una base de datos SQL tradicional, las tablas relacionales sufren y se vuelven sumamente lentas al ejecutar consultas analíticas complejas de combinaciones masivas (joins cruzados de 60 millones de filas), mientras que HDFS permite procesar esto de forma distribuida y escalable.

b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

**b) Pseudocódigo de MapReduce:**

<pre style="background-color: #2d3748; color: #fff; padding: 15px; border-radius: 5px; font-family: monospace; font-size: 13px; line-height: 1.5; margin: 10px 0;">
Función MAP(id_boleta, lista_productos):
    Para cada producto_A en lista_productos:
        Para cada producto_B en lista_productos posterior a producto_A:
            Emitir(Clave: "producto_A, producto_B", Valor: 1)

Función REDUCE(par_productos, lista_valores):
    suma_total = 0
    Para cada valor en lista_valores:
        suma_total += valor
    Emitir(Clave: par_productos, Valor: suma_total)

Función LIMITE_TOP10(salida_reduce):
    Ordenar salida_reduce de mayor a menor según el Valor
    Retornar los primeros 10 elementos.
</pre>

---

**19. (8 puntos)** Explica por qué el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y cómo lo resolvió Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). ¿Qué implicaciones tiene este problema para el diseño de sistemas críticos de producción?


a) El problema en Hadoop 1.x: El NameNode centralizaba todos los metadatos del clúster; si este único servidor fallaba por hardware o software, todo el sistema quedaba inoperable de inmediato, bloqueando el acceso a los datos y deteniendo la producción de la empresa durante horas.
b) Solución en Hadoop 2.x (Alta Disponibilidad): Se implementó un esquema Activo-Pasivo mediante dos NameNodes sincronizados en tiempo real a través de un grupo de nodos llamado Journal Nodes; si el principal falla, el de respaldo asume el control de forma automática en milisegundos sin interrumpir el servicio.
c) Implicaciones en producción: Para el diseño de sistemas críticos, este caso demuestra que nunca se debe permitir un único punto de falla, obligando a los arquitectos a estructurar soluciones con redundancia de hardware y mecanismos de failover automático para asegurar una disponibilidad de $24/7$

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

### a) Tabla de Arquitectura Tecnológica

| Requerimiento | Tecnología | Justificación |
| :--- | :--- | :--- |
| **1. Monitorear posición en tiempo real** | Apache Kafka + Redis | Kafka absorbe los eventos GPS cada 15 segundos sin latencia y Redis guarda la última posición para consultas instantáneas de los pasajeros. |
| **2. Detectar conducción peligrosa** | Apache Spark Streaming | Procesa el flujo continuo de datos GPS en ventanas de tiempo para calcular aceleraciones y alertar excesos de velocidad en segundos. |
| **3. Análisis histórico de 2 años** | HDFS + Apache Spark | Permite almacenar miles de millones de registros GPS históricos a bajo costo y ejecutar consultas masivas para optimizar rutas y tiempos. |
| **4. Almacenamiento de videos (30 días)** | AWS S3 o MinIO | Es el único almacenamiento con la escalabilidad y economía necesarias para albergar 1.15 PB de archivos binarios sin saturar los nodos. |

b) Para los datos GPS, ¿usarías HBase o HDFS? ¿Por qué depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

Depende del patrón de acceso: se usa HBase para lecturas y escrituras aleatorias rápidas en tiempo real, mientras que HDFS se usa para análisis masivo secuencial por lotes (batch).

Ejemplo HBase (Tiempo Real): Cuando un pasajero abre la app de Civa para ver dónde está exactamente su bus, la app consulta a HBase usando la clave ID_BUS, trayendo de forma inmediata (milisegundos) la última coordenada registrada.

Ejemplo HDFS (Histórico): Cuando el equipo de analytics quiere saber la velocidad promedio de los buses en la ruta Lima-Piura durante todo el año 2025; se escanea el archivo consolidado en HDFS de forma secuencial para procesar grandes volúmenes en bloque.

c) ¿Los videos irían a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/día × 30 días = 1.15 PB). (5 puntos)

Los videos deben ir obligatoriamente a un almacenamiento de objetos (AWS S3 o MinIO).

Por qué no HDFS/HBase: HDFS sufriría con el NameNode al gestionar millones de bloques de video gigantescos, elevando los costos drásticamente por su factor de réplica por defecto ($3x$), lo que exigiría triplicar el hardware físico a más de 3.4 PB. HBase es para datos estructurados tabulares, no para archivos binarios masivos (blobs).

Ventaja de Objetos: S3 o MinIO escalan de forma transparente a nivel de Petabytes a una fracción del costo, poseen políticas de ciclo de vida automáticas para borrar los videos a los 30 días exactos y permiten el acceso directo a cada archivo de video mediante una URL única solo cuando ocurre un incidente.

---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)

Para soportar 10,000 transacciones por segundo (tps) con una latencia menor a 2 segundos, se requiere una Arquitectura Kappa o de streaming unificado utilizando los siguientes componentes:

Capa de Ingesta (Mensajería): Apache Kafka. Actúa como el búfer central de alta disponibilidad capaz de recibir las 10,000 tps desde los sistemas bancarios con latencias de milisegundos.

Capa de Procesamiento en Tiempo Real: Apache Spark Streaming (o Apache Flink). Procesa las transacciones en micro-lotes o evento por evento aplicando las reglas de negocio y modelos de Machine Learning.

Capa de Almacenamiento Rápido (Servicio): Apache HBase (o Amazon DynamoDB). Guarda perfiles rápidos de los clientes (últimos saldos, ubicaciones recientes) para enriquecer la transacción sobre la marcha.

Capa de Alertas: Redis + Sistema de Notificaciones push (Websockets/Microservicios). Almacena las alertas temporales y las despacha inmediatamente al sistema de bloqueos del banco.

- Cómo fluyen los datos desde la transacción hasta la alerta

1. Captura: El cliente pasa su tarjeta; el sistema transaccional del banco envía los datos en formato JSON/Avro a un tópico de Kafka (transactions-stream).

2. Enriquecimiento: Spark Streaming consume el evento de Kafka al instante y hace un lookup (búsqueda rápida) en HBase mediante la clave de cliente para obtener su historial reciente (ej. "¿Hizo una compra en otro país hace 10 minutos?").

3. Evaluación: Spark evalúa las reglas anti-fraude o ejecuta un modelo predictivo sobre los datos consolidados.

4. Alerta: Si el patrón es sospechoso, Spark escribe el resultado en Redis y gatilla un evento de alerta hacia el microservicio de seguridad del banco, el cual bloquea la transacción en menos de 2 segundos.

- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso

El procesamiento batch tradicional con MapReduce está diseñado para rendimiento masivo, no para baja latencia.

a.- Uso intensivo de disco: MapReduce escribe obligatoriamente todos los resultados intermedios de los pasos Map y Reduce en los discos duros de HDFS. Este intercambio constante de lectura/escritura (I/O de disco) eleva los tiempos de procesamiento a minutos u horas.

b.- Modelo por lotes: MapReduce necesita acumular un volumen de datos ("el lote") antes de arrancar el trabajo. En un caso de fraude bancario, esperar a juntar las transacciones de los últimos 10 minutos para iniciar el análisis significaría que el dinero ya habría sido robado mucho antes de emitir la alerta.

- Qué herramienta reemplazaría a MapReduce en este escenario

La herramienta ideal para reemplazar a MapReduce en este escenario es Apache Spark (específicamente Spark Streaming) o Apache Flink.

Justificación: Estas herramientas reemplazan el flujo basado en disco de MapReduce por un motor de procesamiento en memoria RAM. Permiten analizar flujos continuos de datos con abstracciones como DataStreams, ejecutando operaciones analíticas complejas directamente sobre la memoria de los nodos del clúster, reduciendo el tiempo de procesamiento de horas a simples fracciones de segundo (milisegundos).

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
- ¿Es técnicamente posible?

Sí, es técnicamente posible. Dado que HBase se ejecuta sobre HDFS como su capa de almacenamiento subyacente, toda la información guardada en HBase se almacena físicamente en el clúster. Sin embargo, que sea posible no significa que sea correcto: HBase está diseñado como una base de datos NoSQL para accesos aleatorios rápidos de lectura/escritura, no como un repositorio de archivos de propósito general para analítica masiva.

- ¿Cuáles serían los problemas de rendimiento, costo y escalabilidad?

a.- Rendimiento en consultas masivas (Batch): Para un análisis histórico de 5 años (Petabytes), HBase sufrirá una degradación masiva. Mientras que HDFS lee archivos secuencialmente a gran velocidad en bloque, HBase tiene que buscar a través de sus regiones (RegionServers) y estructuras internas (MemStore, HFiles), sobrecargando la CPU y la memoria RAM para un proceso que solo requería lectura lineal de discos.

b.- Costos elevados de infraestructura: Mantener Petabytes en HBase exige una cantidad enorme de memoria RAM y almacenamiento en discos de alta velocidad (como SSD o NVMe) para que los índices de las tablas sigan siendo rápidos. Guardar datos históricos fríos de 5 años en un entorno tan caro destruye el principio de costo-eficiencia de Big Data.

c.- Escalabilidad: Al acumular Petabytes de datos históricos, la cantidad de regiones en HBase se multiplicará. Esto generará problemas críticos en el NameNode y en el Zookeeper para coordinar el clúster, ralentizando las operaciones de división de regiones (region splits) y compactaciones de datos.

- ¿Cuál sería el riesgo de este diseño en producción?

El mayor riesgo es el impacto directo y destructivo en el negocio en tiempo real. Si el equipo de analítica lanza una consulta pesada para procesar los 5 años de historia, los RegionServers se saturarán al 100% de CPU y memoria RAM. Como consecuencia, las consultas críticas de los clientes en tiempo real (las que necesitan responder en milisegundos) se encolarán o fallarán por timeout, provocando caídas del servicio en producción.

- ¿Qué evidencia de la sesión de clase apoya tu respuesta?

Este análisis se fundamenta en la separación de capas de la Arquitectura Lambda/Kappa y el funcionamiento nativo de los componentes:

a.- HDFS está optimizado para accesos secuenciales (Streaming Read) de archivos gigantescos (bloques de 128 MB por defecto), ideal para escaneos de lotes (MapReduce/Spark).

b.- HBase organiza los datos en tablas de columnas llave-valor orientadas a accesos aleatorios de baja latencia (Random Read/Write), utilizando memoria RAM (MemStore) para asegurar la velocidad en tiempo real.


---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
>>>>>>> c01f654f9a11075fb9f5ec7728accf12406f02b5
