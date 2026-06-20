# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código de estudiante** | ______________________________________________ |
| **Sección** | ______________________________________________ |
| **Fecha** | ______________________________________________ |
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
c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
c) 128 MB  
d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer  
c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
c) YARN  
d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
b) HBase — porque permite acceso aleatorio en tiempo real por Row Key  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos  
c) Cloud es gratuito y Fog es de pago  
d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
d) 12  

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs  
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  

---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3  
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama ______________________, mientras que los nodos que guardan físicamente los bloques de datos se llaman ______________________.

**12.** El modelo de programación ______________________ divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares ______________________, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada ______________________.

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado ______________________, que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el ______________________ de la red (cerca de los dispositivos), reduciendo la ______________________ de comunicación con el data center central.

---

### B2. Relacionar columnas (10 puntos | 1 pt cada par correcto)

Relaciona cada concepto (columna izquierda) con su descripción correcta (columna derecha). Escribe la letra correspondiente.

| N° | Concepto | | Letra | Descripción |
|----|----------|-|-------|-------------|
| 1 | YARN | | A | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real |
| 2 | ZooKeeper | | B | Herramienta para importar/exportar datos entre RDBMS y HDFS |
| 3 | HBase | | C | Framework de coordinación y sincronización distribuida en el ecosistema Hadoop |
| 4 | Sqoop | | D | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse) |
| 5 | Hive | | E | Gestor de recursos del clúster Hadoop que asigna CPU/RAM a los trabajos |
| 6 | Kafka | | F | Plataforma de streaming de eventos y mensajería distribuida en tiempo real |
| 7 | Spark | | G | Motor de procesamiento en memoria, sucesor de MapReduce, 100x más rápido |
| 8 | Docker | | H | Tecnología de contenedores para desplegar clústeres Hadoop aislados |
| 9 | NameNode | | I | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos |
| 10 | DataNode | | J | Nodo trabajador de HDFS que almacena físicamente los bloques de datos |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas. Extensión sugerida: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El MINSA desea implementar un sistema para analizar los reportes de emergencias en todos los hospitales de Lima en tiempo real (cada hospital envía datos cada 30 segundos) y también quiere hacer análisis históricos de los últimos 5 años para identificar patrones estacionales de enfermedades.

a) ¿Qué tipo de procesamiento requiere cada necesidad (batch o streaming)?  
b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?  
c) Justifica por qué elegiste esos componentes y no otros.

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Qué problema resuelve la "localidad de datos" en Hadoop?  
b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?  
c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

---

**18. (6 puntos) — Mini caso de análisis:**

*La cadena Tottus Perú genera 2 millones de boletas de venta al día en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, método de pago. Al final del mes, el gerente de analytics quiere saber: ¿qué combinaciones de productos se compran juntas con mayor frecuencia (análisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.  
b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

---

**19. (8 puntos)** Explica por qué el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y cómo lo resolvió Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). ¿Qué implicaciones tiene este problema para el diseño de sistemas críticos de producción?

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

b) Para los datos GPS, ¿usarías HBase o HDFS? ¿Por qué depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

c) ¿Los videos irían a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/día × 30 días = 1.15 PB). (5 puntos)

---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)
- Cómo fluyen los datos desde la transacción hasta la alerta
- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso
- Qué herramienta reemplazaría a MapReduce en este escenario

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
- ¿Es técnicamente posible?
- ¿Cuáles serían los problemas de rendimiento, costo y escalabilidad?
- ¿Cuál sería el riesgo de este diseño en producción?
- ¿Qué evidencia de la sesión de clase apoya tu respuesta?

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
