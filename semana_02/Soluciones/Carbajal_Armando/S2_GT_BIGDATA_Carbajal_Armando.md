# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Carbajal Campomanes, Armando Jheferson |
| **Código de estudiante** | 2231896838 |
| **Sección** | ______________________________________________ |
| **Fecha** | 17/06/2026 |
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
**c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos**  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
**c) 128 MB**

d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
**b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer**

c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
**c) YARN** 

d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
**b) HBase — porque permite acceso aleatorio en tiempo real por Row Key**  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  

---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
**b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos**  
c) Cloud es gratuito y Fog es de pago  
d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
**d) 12**  

---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
**c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)**  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
**c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs**  
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  

---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
**c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3**  
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)



## 11.

En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama **NameNode**, mientras que los nodos que guardan físicamente los bloques de datos se llaman **DataNodes**.

---

## 12.

El modelo de programación **MapReduce** divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares **clave-valor (Key-Value)**, y una fase de agregación (REDUCE) que consolida los resultados por clave.

---

## 13.

La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada **Hipervisor (Hypervisor)**.

---

## 14.

HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado **Row Key**, que es el único índice nativo disponible para búsquedas rápidas.

---

## 15.

En Fog Computing, el procesamiento ocurre en el **borde (Edge)** de la red (cerca de los dispositivos), reduciendo la **latencia** de comunicación con el data center central.

---

### B2. Relacionar columnas (10 puntos | 1 pt cada par correcto)

Relaciona cada concepto (columna izquierda) con su descripción correcta (columna derecha). Escribe la letra correspondiente.

## Respuestas

| N.° | Concepto | Letra | Descripción |
|:---:|----------|:-----:|-------------|
| 1 | YARN | **E** | Gestor de recursos del clúster Hadoop que asigna CPU/RAM a los trabajos. |
| 2 | ZooKeeper | **C** | Framework de coordinación y sincronización distribuida en el ecosistema Hadoop. |
| 3 | HBase | **A** | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real. |
| 4 | Sqoop | **B** | Herramienta para importar/exportar datos entre RDBMS y HDFS. |
| 5 | Hive | **D** | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse). |
| 6 | Kafka | **F** | Plataforma de streaming de eventos y mensajería distribuida en tiempo real. |
| 7 | Spark | **G** | Motor de procesamiento en memoria, sucesor de MapReduce y mucho más rápido. |
| 8 | Docker | **H** | Tecnología de contenedores para desplegar clústeres Hadoop aislados. |
| 9 | NameNode | **I** | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos. |
| 10 | DataNode | **J** | Nodo trabajador de HDFS que almacena físicamente los bloques de datos. |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas. Extensión sugerida: 3-5 líneas por pregunta.*

---

## 16. Sistema de análisis de emergencias del MINSA

### a) ¿Qué tipo de procesamiento requiere cada necesidad (batch o streaming)?

Los reportes de emergencias que llegan cada 30 segundos requieren **procesamiento en streaming**, ya que la información debe analizarse casi en tiempo real para tomar decisiones rápidas. En cambio, el análisis de los datos históricos de los últimos 5 años requiere **procesamiento batch**, porque se trabaja con grandes volúmenes de información almacenada.

### b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?

Para el procesamiento en tiempo real usaría **Kafka** para recibir los datos y **Spark Streaming** para analizarlos de forma continua. Para el análisis histórico utilizaría **HDFS** para almacenar los datos y **Spark** o **Hive** para procesarlos y realizar consultas.

### c) Justifica por qué elegiste esos componentes y no otros.

Elegí Kafka y Spark Streaming porque permiten procesar datos conforme llegan, con baja latencia. Para el análisis histórico, HDFS es ideal porque almacena grandes cantidades de datos de forma distribuida, mientras que Spark y Hive permiten analizarlos de manera eficiente. No elegiría MapReduce para tiempo real porque su procesamiento es por lotes y resulta más lento.

---

## 17. Localidad de datos en Hadoop

### a) ¿Qué problema resuelve la "localidad de datos" en Hadoop?

La localidad de datos evita mover grandes cantidades de información por la red. En lugar de enviar los datos al programa, Hadoop envía el procesamiento al nodo donde ya se encuentran almacenados los datos, reduciendo el tráfico y mejorando el rendimiento.

### b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?

Cuando los archivos son muy grandes, transferirlos por la red puede tomar mucho tiempo y consumir mucho ancho de banda. Al procesar los datos directamente en el nodo donde están almacenados, se disminuye el tiempo de ejecución y se aprovechan mejor los recursos del clúster.

### c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

Sí, el principio sigue siendo importante, aunque en la nube el almacenamiento y el cómputo suelen estar separados. En estos casos se busca que los recursos estén en la misma región o zona de disponibilidad para reducir la latencia y el costo de transferencia de datos entre los servicios.

---

**18. (6 puntos) — Mini caso de análisis:**

### a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.

Para este caso utilizaría **HDFS**, porque el objetivo principal es realizar análisis masivos sobre millones de registros y encontrar patrones de compra. Aunque 25 GB todavía podrían almacenarse en una base de datos relacional, HDFS ofrece una mejor opción si se espera que el volumen siga creciendo y se van a ejecutar procesos distribuidos con Hadoop o Spark.

### b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

```text
MAP:
Para cada boleta:
    Obtener la lista de productos.
    Generar todas las combinaciones posibles de dos productos.
    Emitir (combinación, 1).

SHUFFLE:
Agrupar todas las combinaciones iguales.

REDUCE:
Para cada combinación:
    Sumar todos los valores recibidos.
    Emitir (combinación, total).

RESULTADO FINAL:
Ordenar las combinaciones por el total de ocurrencias.
Mostrar las 10 combinaciones con mayor frecuencia.
```

---

## 19. Single Point of Failure del NameNode

En Hadoop 1.x el **NameNode** era un único nodo encargado de almacenar todos los metadatos del sistema de archivos. Si este servidor fallaba, el clúster completo dejaba de funcionar, aunque los datos siguieran almacenados en los DataNodes. Esto convertía al NameNode en un **Single Point of Failure (SPOF)**.

Hadoop 2.x solucionó este problema mediante la arquitectura de **Alta Disponibilidad (High Availability - HA)**. Se incorporaron dos NameNodes: uno **Activo** y otro **Standby**. Si el NameNode activo falla, el secundario toma el control automáticamente, evitando la interrupción del servicio y mejorando la disponibilidad del clúster.

En sistemas críticos de producción este cambio es muy importante, ya que garantiza la continuidad del servicio, reduce el riesgo de caídas y permite que las aplicaciones sigan funcionando incluso cuando ocurre una falla en el nodo principal. Además, mejora la confiabilidad y facilita el mantenimiento sin afectar a los usuarios.

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

## a) Componentes del ecosistema Hadoop/Cloud

| Requerimiento | Tecnología | Justificación |
|---------------|------------|---------------|
| Monitoreo en tiempo real de ubicación de buses | Kafka + Spark Streaming + dashboard (Grafana/Power BI) | Kafka ingiere los datos de GPS en tiempo real y Spark Streaming los procesa para actualizar la ubicación casi en vivo. |
| Detección de conducción peligrosa | Spark Streaming (o Flink) | Permite analizar eventos en tiempo real como exceso de velocidad o frenadas bruscas con baja latencia. |
| Análisis histórico de rutas (2 años) | HDFS + Spark + Hive | HDFS almacena grandes volúmenes de datos históricos y Spark/Hive permiten análisis batch eficientes. |
| Almacenamiento de videos (30 días) | S3 / MinIO (Object Storage) | Maneja grandes volúmenes de datos no estructurados (38 TB/día) con alta escalabilidad y bajo costo. |

---

## b) GPS: ¿HBase o HDFS?

La elección depende del caso de uso:

- **HBase** se usa cuando se necesita acceso rápido y aleatorio en tiempo real.  
  Ejemplo: consultar la ubicación actual de un bus específico (bus_id + timestamp reciente) para mostrarlo en un mapa en vivo.

- **HDFS** se usa cuando se requiere análisis masivo histórico.  
  Ejemplo: analizar las rutas de todos los buses durante los últimos 2 años para optimizar trayectos.

👉 Conclusión:  
- HBase = consultas en tiempo real (baja latencia)  
- HDFS = análisis batch a gran escala

---

## c) Almacenamiento de videos

Los videos deben ir a un sistema de **almacenamiento de objetos como S3 o MinIO**.

Esto se debe a que el volumen es extremadamente alto (38 TB por día, aproximadamente 1.15 PB en 30 días), lo que hace inviable usar HDFS o HBase como almacenamiento principal.

El object storage está diseñado para:
- Escalabilidad masiva (petabytes)
- Bajo costo por almacenamiento
- Alta durabilidad
- Manejo eficiente de archivos grandes como video

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)
- Cómo fluyen los datos desde la transacción hasta la alerta
- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso
- Qué herramienta reemplazaría a MapReduce en este escenario


## 1. Arquitectura de componentes por capas

| Capa | Tecnología | Función |
|------|------------|--------|
| Ingesta de datos | Kafka | Recibe 10,000 transacciones por segundo en tiempo real y las distribuye como eventos. |
| Procesamiento en streaming | Spark Streaming (o Apache Flink) | Analiza las transacciones en tiempo real y detecta patrones sospechosos en menos de 2 segundos. |
| Motor de reglas / ML | Spark MLlib o modelo externo (API) | Evalúa patrones de fraude como compras inusuales o múltiples transacciones rápidas. |
| Almacenamiento histórico | HDFS / Data Lake (S3) | Guarda transacciones para auditoría y entrenamiento de modelos. |
| Alertas | Microservicio + API + sistema de notificación | Envía alertas a bancos, apps móviles o sistemas internos. |

---

## 2. Flujo de datos

1. El usuario realiza una transacción bancaria.  
2. La transacción se envía inmediatamente a **Kafka** como evento.  
3. **Spark Streaming** consume los eventos en tiempo real.  
4. Se aplican reglas o modelos de machine learning para detectar fraude.  
5. Si se detecta un patrón sospechoso, se genera una alerta en menos de 2 segundos.  
6. La transacción y el resultado se almacenan en **HDFS o S3** para análisis posterior.

---

## 3. Por qué MapReduce NO es suficiente

El modelo tradicional de **MapReduce** no sirve porque:
- Es un procesamiento **batch**, no en tiempo real.
- Escribe resultados intermedios en disco, lo que aumenta la latencia.
- No puede cumplir el requisito de **menos de 2 segundos de respuesta**.
- Está diseñado para grandes lotes de datos, no para flujo continuo de eventos.

---

## 4. Tecnología que reemplaza MapReduce

Se reemplaza por **Spark Streaming o Apache Flink**.

- Permiten procesamiento en memoria (in-memory).
- Soportan flujos continuos de datos (streaming).
- Tienen baja latencia, ideal para detección de fraude en tiempo real.
- Escalan horizontalmente para manejar miles de eventos por segundo.

---

## Conclusión

La arquitectura basada en **Kafka + Spark Streaming + ML + alertas en tiempo real** permite detectar fraude en segundos, algo imposible con MapReduce debido a su naturaleza batch.

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
## ¿Es técnicamente posible?

Sí, es técnicamente posible usar **HBase** para almacenar grandes volúmenes de datos históricos y también datos en tiempo real, ya que HBase está construido sobre HDFS y puede escalar horizontalmente. Sin embargo, no es una buena práctica arquitectónica usarlo como única solución para todo el almacenamiento Big Data.

---

## Problemas de rendimiento, costo y escalabilidad

- **Rendimiento:** HBase está optimizado para acceso aleatorio (lecturas/escrituras por clave), no para análisis masivo tipo batch. Consultas analíticas sobre petabytes serían muy lentas.
- **Costo:** Mantener índices y estructuras de HBase para datos históricos masivos incrementa el uso de memoria y almacenamiento, haciendo el sistema más costoso que usar HDFS directamente.
- **Escalabilidad:** Aunque HBase escala, el rendimiento se degrada en cargas analíticas grandes porque no está diseñado para scans completos de grandes datasets como lo hace HDFS + Spark.

---

## Riesgo en producción

El principal riesgo es la **degradación severa del sistema** cuando se mezclan dos tipos de cargas:

- Consultas en tiempo real pueden volverse lentas por competencia con procesos de lectura masiva.
- Posibles cuellos de botella en RegionServers.
- Mayor complejidad operativa y riesgo de fallos por sobrecarga.
- Dificultad para optimizar simultáneamente workloads transaccionales y analíticos.

---

## Evidencia de la arquitectura vista en clase

En la arquitectura Hadoop se separan claramente los roles:

- **HBase → OLTP / acceso en tiempo real (baja latencia)**
- **HDFS → almacenamiento distribuido para datos históricos (batch processing)**
- **Spark/MapReduce → procesamiento analítico sobre grandes volúmenes**

Esto demuestra el principio de **separación de cargas de trabajo (storage vs processing)**, que es clave en sistemas Big Data.

---

## Conclusión

Usar solo HBase para todo el sistema Big Data no es una buena práctica. Aunque es posible, genera problemas de rendimiento, costo y escalabilidad. La arquitectura correcta separa:
- HBase para tiempo real
- HDFS para histórico
- Spark para análisis

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
