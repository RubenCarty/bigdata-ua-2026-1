# S3 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Carbajal Campomanes, Armando Jheferson |
| **Código** | 2231896838|
| **Sección** | ______________________________________________ |
| **Fecha** | 22/06/2026 |
| **Tiempo estimado** | 90 minutos |
| **Puntaje total** | 100 puntos |

---

### INSTRUCCIONES GENERALES

- Lee cada enunciado con atención antes de responder.
- Esta guía evalúa los temas de la Semana 3: YARN, Hive, Impala, Ambari, NoSQL y el Teorema CAP.
- Tiempo recomendado: 90 minutos.
- Las secciones van de menor a mayor dificultad.
- En preguntas abiertas: responde en oraciones completas con argumentos técnicos.
- No hay respuestas en este documento — responde en el espacio indicado o en el documento que indique el docente.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts c/u)

*Marca con X la alternativa correcta. Solo una es válida.*

---

## 1. ¿Cuál fue el problema principal del JobTracker en Hadoop 1.x que motivó la creación de YARN?

a) El JobTracker no soportaba el lenguaje Python para escribir jobs MapReduce  
**b) ✔️ El JobTracker mezclaba la gestión de recursos del clúster con la coordinación de jobs, convirtiéndose en cuello de botella y punto único de fallo**  
c) El JobTracker solo podía gestionar un job MapReduce a la vez en todo el clúster  
d) El JobTracker no tenía interfaz gráfica para monitorear el estado de los nodos  

---

## 2. Apache Hive traduce las consultas HiveQL en ¿qué tipo de trabajos distribuidos para ejecutarlas sobre HDFS?

a) Consultas SQL directas que corren en tiempo real sobre los DataNodes  
b) Jobs de Python que se distribuyen entre los DataNodes vía SSH  
**c) ✔️ Jobs MapReduce (o Tez/Spark en versiones modernas) que procesan los archivos de HDFS en paralelo**  
d) Procedimientos almacenados en Java que se ejecutan en el NameNode  

---

## 3. ¿Qué diferencia fundamental existe entre Apache Hive y Apache Impala en cuanto a su arquitectura de ejecución de consultas?

a) Hive usa SQL estándar e Impala usa Pig Latin  
**b) ✔️ Hive usa MapReduce (alta latencia); Impala ejecuta SQL directamente en memoria/HDFS sin MapReduce (baja latencia)**  
c) Hive solo funciona con datos estructurados  
d) Hive es de pago e Impala es gratuito  

---

## 4. Apache Ambari fue diseñado principalmente para:

a) Almacenar datos no estructurados en Hadoop  
b) Ejecutar SQL en HDFS sin MapReduce  
**c) ✔️ Gestionar, monitorear e instalar componentes del ecosistema Hadoop desde una interfaz web centralizada**  
d) Transferir datos entre RDBMS y HDFS  

---

## 5. Según el Teorema CAP, si una empresa necesita que el sistema nunca muestre datos incorrectos aunque haya caídas, debe elegir:

a) AP — Disponibilidad y Tolerancia a Particiones  
b) CA — Consistencia y Disponibilidad  
**c) ✔️ CP — Consistencia y Tolerancia a Particiones**  
d) CAP — Las tres simultáneamente  

---

## 6. ¿Cuál es la diferencia entre ACID y BASE?

a) ACID usa SQL y BASE usa Python  
**b) ✔️ ACID garantiza consistencia fuerte (bancos), BASE prioriza disponibilidad y consistencia eventual (redes sociales)**  
c) ACID solo funciona en local  
d) ACID es NoSQL y BASE es relacional  

---

## 7. Una empresa necesita almacenar perfiles de usuarios con estructuras variables. ¿Qué NoSQL es más adecuado?

a) Key-Value (Redis)  
**b) ✔️ Document (MongoDB) — permite esquemas flexibles por usuario**  
c) Column-family (Cassandra)  
d) Graph (Neo4j)  

---

## 8. ¿Cuál es la ventaja de Cassandra frente a MongoDB en sistemas con millones de registros?

a) Tiene mejor SQL  
b) Tiene más flexibilidad de esquema  
**c) ✔️ Optimizada para escrituras masivas y escalabilidad sin punto único de fallo**  
d) Soporta ACID completo  

---

## 9. Sqoop es una herramienta que:

a) Monitorea nodos Hadoop  
b) Ejecuta SQL en HDFS  
**c) ✔️ Transfiere datos entre bases relacionales y HDFS en batch**  
d) Gestiona seguridad Hadoop  

---

## 10. ¿Por qué usar MongoDB en una red social en crecimiento?

a) Es más rápido en todo  
**b) ✔️ Permite escalabilidad horizontal y esquemas flexibles sin migraciones complejas**  
c) PostgreSQL no soporta JSON  
d) MongoDB tiene buscador único  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts c/u)

## 11.
En la arquitectura YARN, el componente **ResourceManager** gestiona los recursos del clúster (CPU, RAM) a nivel global, mientras que el **ApplicationMaster** coordina la ejecución de cada aplicación individual en los nodos del clúster.

---

## 12.
El Teorema CAP establece que un sistema distribuido solo puede garantizar dos de tres propiedades simultáneamente: **Consistencia** (todos los nodos ven los mismos datos), **Disponibilidad** (el sistema siempre responde), y Tolerancia a Particiones (el sistema funciona aunque la red falle).

---

## 13.
En MongoDB, los datos se organizan en **colecciones** (equivalente a una tabla SQL), que contienen **documentos** (equivalente a filas) en formato JSON/BSON, donde cada uno puede tener una estructura diferente.

---

## 14.
Apache **Pig** traduce un lenguaje de scripting llamado "Pig Latin" en jobs MapReduce, mientras que Apache **Hive** traduce consultas en un dialecto SQL propio (HiveQL) en jobs MapReduce o Spark.

---

## 15.
La herramienta **Sqoop** (SQL-to-Hadoop) permite importar datos de una base de datos MySQL a HDFS de forma paralela usando múltiples conexiones JDBC simultáneas.

---

### B2. Relacionar columnas (10 puntos | 1 pt c/par correcto)

Relaciona cada tecnología/concepto (columna A) con su descripción correcta (columna B):

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | Redis | **D** | Base de datos Key-Value en memoria con latencia < 1ms, usada para caché de sesiones |
| 2 | Apache Cassandra | **E** | Base de datos columnar distribuida sin maestro (ring), optimizada para escrituras masivas |
| 3 | Impala | **A** | Motor SQL interactivo que ejecuta consultas directamente sobre HDFS sin MapReduce |
| 4 | Neo4j | **B** | Base de datos de grafos optimizada para navegar relaciones complejas |
| 5 | Ambari | **C** | Herramienta de gestión de clúster Hadoop con interfaz web |
| 6 | Dremel | **F** | Tecnología de Google que inspira formatos columnar y BigQuery |
| 7 | Apache Drill | **G** | Motor SQL schema-free que consulta HDFS, MongoDB, S3 sin esquema previo |
| 8 | MongoDB | **H** | Base de datos NoSQL documental con esquema flexible (BSON/JSON) |
| 9 | Tez | **I** | Framework DAG que reemplaza MapReduce como motor de ejecución de Hive |
| 10 | Flume | **J** | Herramienta de ingesta de logs/eventos hacia HDFS o Kafka |
---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas y argumentos técnicos. Extensión: 3-5 líneas por pregunta.*

---

## 16. Sistema de Vigilancia Epidemiológica (MINSA)

### a) Base de datos NoSQL recomendada

La mejor opción es una base de datos **NoSQL tipo documental (MongoDB)**.

**Justificación:**
- Permite **esquemas flexibles**, ideal para enfermedades con campos variables (dengue, COVID, hepatitis).
- Soporta almacenamiento en formato **JSON/BSON**, lo que facilita agregar nuevos atributos sin modificar la estructura de la base de datos.

---

### b) Componente para consultas del dashboard

Se recomienda usar **Impala o Spark SQL**.

**Justificación:**
- Permiten **consultas SQL interactivas de baja latencia (<2 segundos)**.
- Trabajan directamente sobre datos en HDFS o data lake.
- Son mucho más rápidos que Hive tradicional (MapReduce), lo cual es clave para dashboards epidemiológicos en tiempo real o casi real.

---

## 17. ACID vs BASE

### a) Aplicaciones donde es obligatorio ACID

ACID es obligatorio en sistemas donde la **consistencia es crítica**, como:
- Banca (transferencias de dinero)
- Sistemas de facturación
- Sistemas de reservas

**Razón:** se necesita garantizar que las transacciones sean correctas, sin pérdidas ni duplicaciones.

---

### b) Aplicaciones donde es aceptable BASE

BASE es adecuado en sistemas donde se prioriza:
- Alta disponibilidad
- Escalabilidad masiva
- Consistencia eventual

Ejemplos:
- Redes sociales
- Sistemas de recomendaciones
- Logs y analítica web

---

### c) Sistema que combina ACID y BASE

Sí existe: **NewSQL (ejemplo: Google Spanner, CockroachDB)**.

**Cómo lo logra:**
- Mantiene consistencia fuerte tipo ACID
- Pero escala horizontalmente como NoSQL
- Usa sincronización distribuida y relojes globales para consistencia

---

## 18. Mini caso – CompraYa Perú

### a) Tipo de base de datos por componente

- **Catálogo de productos → MongoDB**
  - Porque los productos tienen atributos variables (esquema flexible).

- **Carrito de compras → Redis**
  - Porque necesita alta velocidad y datos temporales (cache en memoria con expiración).

- **Órdenes de compra → SQL (PostgreSQL/MySQL)**
  - Porque requiere transacciones ACID (cobro exacto una sola vez).

- **Historial de navegación → Cassandra**
  - Porque maneja grandes volúmenes de eventos (50M/día) con escrituras masivas.

---

### b) ¿Una sola base de datos?

No es recomendable usar una sola base de datos.

**Justificación:**
- Cada componente tiene requerimientos diferentes (latencia, consistencia, escalabilidad).
- Una sola BD no optimiza bien todos los casos.
- Se necesita arquitectura **polyglot persistence**.

**Ventaja de polyglot persistence:**
- Cada sistema usa la base de datos óptima para su caso.
- Mejora rendimiento, escalabilidad y eficiencia.

---

## 19. Evolución Pig → Spark

Apache Pig fue importante porque:
- Simplificó el uso de Hadoop con un lenguaje más fácil (Pig Latin).
- Permitió escribir pipelines de datos sin Java MapReduce.

Sin embargo, fue reemplazado por Apache Spark porque:

- Pig dependía de MapReduce, lo que generaba **alta latencia por escritura en disco**.
- Spark introdujo **procesamiento en memoria (in-memory computing)**.
- Spark es mucho más rápido (hasta 100x).

---

### ¿Qué característica de Pig sobrevivió en Spark?

- El concepto de **transformaciones en pipelines de datos** (ETL declarativo).

---

### ¿Qué limitación eliminó Spark?

- Eliminó la dependencia de **MapReduce y disco entre etapas**, reduciendo drásticamente la latencia.

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional real (15 puntos)**

*Eres el Data Architect de Interbank. El banco tiene 3.5 millones de clientes con las siguientes necesidades de datos:*

*Sistema 1 — Core bancario (transacciones):* 5 millones de transacciones diarias (depósitos, retiros, transferencias). Cada transacción debe procesarse exactamente una vez. Si el sistema falla a mitad de una transferencia, el dinero no puede perderse ni duplicarse.

*Sistema 2 — App móvil (perfil del cliente):* Cuando el cliente abre la app, ve su saldo, últimas 5 transacciones y ofertas personalizadas. El tiempo de carga aceptable es 300ms. En días de pago (quincena, fin de mes), hay 800K logins simultáneos.

*Sistema 3 — Motor de recomendaciones:* El banco quiere mostrar "Productos que te pueden interesar" basado en el perfil financiero del cliente. El modelo necesita analizar historial de 5 años de transacciones de 3.5M clientes (75TB de datos) cada semana para re-entrenar el modelo.

*Sistema 4 — Detección de redes de fraude:* Algunos clientes crean redes de cuentas para mover dinero ilícito. El banco necesita detectar cuando una transacción forma parte de un ciclo: A → B → C → A en menos de 5 minutos.

Responde:

a) Para cada sistema (1, 2, 3, 4), ¿qué tecnología de almacenamiento/procesamiento utilizarías? Crea una tabla con: Sistema | Tecnología | Tipo (SQL/NoSQL/qué tipo) | Justificación técnica específica (3 líneas por sistema) (8 puntos)

b) Aplica el Teorema CAP a los Sistemas 1 y 2 específicamente. ¿Cuál combinación CAP debe tener cada uno y por qué? Da un ejemplo de qué pasaría si eligieras la combinación incorrecta. (4 puntos)

c) En el Sistema 3 (recomendaciones), el equipo de ML propone usar un archivo CSV de 75 TB almacenado en el servidor local del equipo para entrenar el modelo semanalmente. ¿Qué argumentas tú como Data Architect en contra de esta propuesta? ¿Qué propones en su lugar? (3 puntos)

## a) Arquitectura por sistema

| Sistema | Tecnología | Tipo | Justificación técnica |
|--------|------------|------|----------------------|
| Sistema 1 – Core bancario (transacciones) | PostgreSQL / Oracle + logs en Kafka | SQL (ACID RDBMS) | Requiere transacciones ACID estrictas para garantizar consistencia financiera. Cada operación debe ejecutarse exactamente una vez (no duplicación ni pérdida). Integración con Kafka para auditoría y trazabilidad en tiempo real. |
| Sistema 2 – App móvil (perfil cliente) | Redis + Cassandra | NoSQL (Key-Value + Column-Family) | Redis permite respuestas <300ms para sesiones activas y datos frecuentes (saldo, últimas transacciones). Cassandra escala horizontalmente para 800K usuarios concurrentes con alta disponibilidad. |
| Sistema 3 – Motor de recomendaciones | HDFS + Spark (MLlib) | Big Data / Data Lake | HDFS almacena los 75TB históricos de forma distribuida. Spark permite entrenamiento de modelos en memoria de forma semanal eficiente sobre grandes volúmenes. |
| Sistema 4 – Detección de fraude (redes) | Neo4j + Kafka + Spark Streaming | NoSQL (Graph + Streaming) | Neo4j permite modelar relaciones A→B→C→A fácilmente. Kafka ingiere transacciones en tiempo real. Spark Streaming detecta patrones en menos de 5 minutos. |

---

## b) Aplicación del Teorema CAP

### Sistema 1 (Core bancario)

Debe ser **CP (Consistencia + Tolerancia a particiones)**.

- Es crítico que el dinero nunca se duplique ni pierda.
- Si hay caída de red, es mejor bloquear temporalmente que permitir inconsistencia.

👉 Ejemplo si eliges AP:
- Se podrían mostrar saldos incorrectos o duplicar transferencias → **grave error financiero**.

---

### Sistema 2 (App móvil)

Debe ser **AP (Disponibilidad + Tolerancia a particiones)**.

- El usuario debe poder ingresar siempre, incluso con datos ligeramente desactualizados.
- Es preferible mostrar datos con pequeña latencia antes que no mostrar nada.

👉 Ejemplo si eliges CP:
- En días de alta carga, el sistema podría bloquear accesos → mala experiencia del cliente.

---

## c) Crítica al uso de CSV local (75 TB)

### Problemas de la propuesta:

- Un solo servidor local no puede manejar 75 TB de forma eficiente.
- No hay escalabilidad horizontal.
- Alto riesgo de pérdida de datos (sin redundancia).
- No permite procesamiento distribuido.
- El tiempo de entrenamiento sería extremadamente lento.

---

### Propuesta del Data Architect:

- Usar **Data Lake en HDFS o S3**
- Procesamiento con **Spark (cluster distribuido)**
- Orquestación con herramientas como **Airflow**
- Posible uso de **Databricks o EMR**

---

### Beneficio:

- Procesamiento distribuido de 75 TB en paralelo
- Escalabilidad horizontal
- Mayor velocidad de entrenamiento
- Alta disponibilidad y tolerancia a fallos


---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías una base de datos NoSQL para el sistema de seguimiento de paquetes de Olva Courier Perú? El sistema debe: (a) registrar cada evento de cada paquete (recepción, en tránsito, en distribución, entregado) en tiempo real; (b) permitir al cliente consultar 'dónde está mi paquete' por número de guía en menos de 100ms; (c) guardar historial de los últimos 2 años (150M paquetes × 8 eventos = 1.2B eventos)."*

Diseña:
- El tipo de NoSQL elegido y justificación
- El modelo de datos (cómo organizarías los documentos/columnas/claves)
- La consulta que usarías para responder "¿dónde está el paquete #PE123456?"
- Por qué esta solución es mejor que usar una tabla SQL con índices


## 1. Tipo de NoSQL elegido

Se utilizaría una base de datos **NoSQL tipo Column-Family (Apache Cassandra)**.

### Justificación:
- Permite **altísima velocidad de escritura** (eventos en tiempo real).
- Escala horizontalmente para manejar **miles de millones de registros** (1.2B eventos).
- No tiene punto único de fallo.
- Optimizada para consultas por clave (tracking por número de guía).
- Baja latencia (<100ms) en lecturas por partition key.

---

## 2. Modelo de datos

### Tabla: `tracking_paquetes`

| Partition Key | Clustering Key | Columnas |
|----------------|----------------|----------|
| guia_id | timestamp_evento | estado, ubicación, centro_logístico, detalle |

### Ejemplo:

- `guia_id = PE123456`
- eventos ordenados por `timestamp_evento`

## 3. Consulta para "¿dónde está mi paquete?"

```sql
SELECT estado, ubicación
FROM tracking_paquetes
WHERE guia_id = 'PE123456'
ORDER BY timestamp_evento DESC
LIMIT 1;
---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si MongoDB Atlas (la plataforma cloud de MongoDB) tiene una caída de servicio de 2 horas durante el horario pico de tu aplicación? ¿Qué riesgos concretos implica depender de una sola base de datos NoSQL en la nube para una aplicación crítica como la app de Claro Perú?"*

Analiza:
##  ¿Qué componentes dejarían de funcionar?

Si MongoDB Atlas cae durante 2 horas en hora pico, dejarían de funcionar todos los componentes que dependan directamente de la base de datos:

- Login y autenticación de usuarios (si el perfil está en MongoDB)
- Consulta de datos del cliente (saldo, historial, líneas, planes)
- APIs de la aplicación móvil que dependan de lectura/escritura
- Gestión de sesiones si no hay cache alternativa
- Procesos de compra/activación de servicios en tiempo real

En general, la app podría quedar parcialmente o totalmente inoperativa.

---

## Estrategias de resiliencia

Para mitigar el riesgo se pueden implementar varias estrategias:

- **Multi-region replication** dentro de MongoDB Atlas para alta disponibilidad
- **Failover automático** entre regiones
- Uso de **Redis como caché** para lecturas críticas (datos recientes del usuario)
- Implementar **circuit breaker pattern** en la API para evitar colapso del sistema
- Uso de **colas (Kafka o RabbitMQ)** para desacoplar procesos y no perder eventos
- Backups automáticos y recuperación rápida (disaster recovery plan)

---

##  ¿Múltiples proveedores o uno solo con HA?

Lo ideal depende del nivel de criticidad:

- Un solo proveedor con **alta disponibilidad bien configurada** es más simple y común.
- Sin embargo, para sistemas críticos (telecomunicaciones o banca), es mejor un enfoque **multi-cloud o multi-proveedor** como respaldo.

 Conclusión:
- Operación principal: un proveedor fuerte (MongoDB Atlas)
- Respaldo: estrategia híbrida o multi-cloud para reducir vendor lock-in

---

##  SLA recomendado

Para una aplicación crítica como Claro Perú:

- Mínimo aceptable: **99.99% (four nines)**
- Ideal: **99.999% (five nines)**

Esto significa:
- 99.99% ≈ 52 minutos de caída al año
- 99.999% ≈ 5 minutos de caída al año
---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
