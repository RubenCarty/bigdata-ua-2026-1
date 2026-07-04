# S3 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Paredes hilario Noe Jesus |
| **Código** | 2221895643 |
| **Sección** | 6-202601 |
| **Fecha** | 27/06/2026 |
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

**1.** ¿Cuál fue el problema principal del JobTracker en Hadoop 1.x que motivó la creación de YARN?

a) El JobTracker no soportaba el lenguaje Python para escribir jobs MapReduce  
X  b) El JobTracker mezclaba la gestión de recursos del clúster con la coordinación de jobs, convirtiéndose en cuello de botella y punto único de fallo  
c) El JobTracker solo podía gestionar un job MapReduce a la vez en todo el clúster  
d) El JobTracker no tenía interfaz gráfica para monitorear el estado de los nodos  

---

**2.** Apache Hive traduce las consultas HiveQL en ¿qué tipo de trabajos distribuidos para ejecutarlas sobre HDFS?

a) Consultas SQL directas que corren en tiempo real sobre los DataNodes  
b) Jobs de Python que se distribuyen entre los DataNodes vía SSH  
X c) Jobs MapReduce (o Tez/Spark en versiones modernas) que procesan los archivos de HDFS en paralelo  
d) Procedimientos almacenados en Java que se ejecutan en el NameNode  

---

**3.** ¿Qué diferencia fundamental existe entre Apache Hive y Apache Impala en cuanto a su arquitectura de ejecución de consultas?

a) Hive usa SQL estándar e Impala usa un lenguaje de scripting propio llamado Pig Latin  
X  b) Hive compila las consultas en jobs MapReduce (alta latencia); Impala ejecuta SQL directamente en HDFS sin MapReduce (baja latencia, segundos)  
c) Hive solo funciona con datos estructurados, mientras Impala soporta JSON y XML  
d) Hive es de pago (Cloudera) e Impala es la versión gratuita open source  

---

**4.** Apache Ambari fue diseñado principalmente para:

a) Almacenar datos no estructurados de forma distribuida en el ecosistema Hadoop  
b) Ejecutar consultas SQL interactivas sobre archivos en HDFS sin usar MapReduce  
X  c) Gestionar, monitorear e instalar componentes del ecosistema Hadoop desde una interfaz web centralizada  
d) Transferir datos de bases de datos relacionales a HDFS mediante conexiones JDBC  

---

**5.** Según el Teorema CAP (Brewer, 2000), un sistema distribuido NO puede garantizar simultáneamente las tres propiedades. Si una empresa de telecomunicaciones necesita que el sistema de facturación nunca muestre montos incorrectos (aunque el sistema esté temporalmente no disponible), ¿qué combinación CAP debe elegir?

a) AP — Disponibilidad y Tolerancia a Particiones  
b) CA — Consistencia y Disponibilidad  
X  c) CP — Consistencia y Tolerancia a Particiones  
d) CAP — Las tres simultáneamente mediante replicación síncrona  

---

**6.** ¿Cuál es la diferencia entre el modelo ACID y el modelo BASE en bases de datos?

a) ACID usa SQL y BASE usa Python; son lenguajes de consulta distintos  
X  b) ACID garantiza consistencia estricta en transacciones (apropiado para bancos); BASE acepta consistencia eventual a favor de alta disponibilidad (apropiado para redes sociales)  
c) ACID solo funciona en bases de datos locales; BASE solo funciona en bases de datos distribuidas en la nube  
d) ACID es el modelo de NoSQL y BASE es el modelo relacional tradicional  

---

**7.** Una empresa de streaming de música necesita almacenar el perfil de 50 millones de usuarios donde cada usuario puede tener atributos completamente diferentes (algunos tienen listas de reproducción, otros favoritos, otros historial de podcasts, con esquemas variables). ¿Qué tipo de base de datos NoSQL es más adecuada?

a) Key-Value (Redis) — porque permite acceso ultrarápido por clave de usuario  
X  b) Document (MongoDB) — porque cada documento puede tener estructura diferente sin esquema fijo  
c) Column-family (Cassandra) — porque está optimizada para escrituras masivas en tiempo real  
d) Graph (Neo4j) — porque permite modelar las relaciones entre usuarios y canciones  

---

**8.** ¿Cuál es la principal ventaja de Apache Cassandra frente a MongoDB para almacenar el historial de llamadas de una operadora con 2,000 millones de registros al año?

a) Cassandra tiene una interfaz SQL más intuitiva que MongoDB para analistas de negocio  
b) Cassandra permite esquemas más flexibles que MongoDB para datos con atributos variables  
X c) Cassandra está optimizada para escrituras masivas y continuas con acceso predecible por partition key + timestamp, sin punto único de fallo  
d) Cassandra soporta transacciones ACID completas, mientras MongoDB solo tiene consistencia eventual  

---

**9.** Sqoop es una herramienta del ecosistema Hadoop diseñada para:

a) Monitorear la salud de los DataNodes y alertar cuando alguno falla  
b) Ejecutar consultas SQL interactivas sobre datos almacenados en HDFS  
X  c) Transferir datos en batch entre bases de datos relacionales (Oracle, MySQL) y HDFS en ambas direcciones  
d) Gestionar la seguridad y autenticación de usuarios en el clúster Hadoop  

---

**10.** Una startup peruana lanza una app de redes sociales. Al inicio tienen 10,000 usuarios. Proyectan 5 millones en 12 meses. El perfil de cada usuario incluye fotos, listas de amigos, publicaciones con diferentes formatos (texto, imagen, video, encuesta). ¿Qué argumento técnico justifica usar MongoDB en lugar de PostgreSQL desde el inicio?

a) MongoDB es más rápido en todas las operaciones, incluyendo transacciones financieras, sin importar el volumen  
X b) MongoDB permite escalar horizontalmente con sharding automático y soporta esquemas flexibles que se adaptan a los distintos tipos de contenido sin costosas migraciones de esquema  
c) PostgreSQL no soporta datos de tipo JSON, por lo que no puede almacenar publicaciones de redes sociales  
d) MongoDB incluye un motor de búsqueda de texto completo que PostgreSQL no tiene en ninguna versión  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts c/u)

**11.** En la arquitectura YARN, el componente ResourceManager gestiona los recursos del clúster (CPU, RAM) a nivel global, mientras que el ApplicationMaster  coordina la ejecución de cada aplicación individual en los nodos del clúster.

**12.** El Teorema CAP establece que un sistema distribuido solo puede garantizar dos de tres propiedades simultáneamente: Consistencia (todos los nodos ven los mismos datos), Disponibilidad (el sistema siempre responde), y Tolerancia a Particiones (el sistema funciona aunque la red falle).

**13.** En MongoDB, los datos se organizan en COLECCIONES (equivalente a una tabla SQL), que contienen DOCUMENTOS (equivalente a filas) en formato JSON/BSON, donde cada uno puede tener una estructura diferente.

**14.** Apache Pig traduce un lenguaje de scripting llamado "Pig Latin" en jobs MapReduce, mientras que Apache Hive traduce consultas en un dialecto SQL propio (HiveQL) en jobs MapReduce o Spark.

**15.** La herramienta Apache Sqoop (SQL-to-Hadoop) permite importar datos de una base de datos MySQL a HDFS de forma paralela usando múltiples conexiones JDBC simultáneas.

---

### B2. Relacionar columnas (10 puntos | 1 pt c/par correcto)

Relaciona cada tecnología/concepto (columna A) con su descripción correcta (columna B):

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | Redis |D | A | Motor SQL interactivo de Cloudera que ejecuta consultas directamente sobre HDFS sin MapReduce |
| 2 | Apache Cassandra |E | B | Base de datos de grafos optimizada para navegar relaciones complejas en milisegundos |
| 3 | Impala |A | C | Herramienta de gestión de clúster Hadoop con interfaz web (instala, monitorea, configura servicios) |
| 4 | Neo4j |B | D | Base de datos Key-Value en memoria con latencia < 1ms, usada para caché de sesiones |
| 5 | Ambari |C | E | Base de datos columnar distribuida sin maestro (ring), optimizada para escrituras masivas |
| 6 | Dremel |F | F | Tecnología de Google que inspira los formatos de almacenamiento columnar y BigQuery |
| 7 | Apache Drill |G | G | Motor SQL schema-free que consulta HDFS, MongoDB, S3 y otros sin esquema previo |
| 8 | MongoDB |H | H | Base de datos NoSQL documental con esquema flexible (BSON/JSON), más usada mundialmente |
| 9 | Tez |I| I | Framework de procesamiento DAG que reemplaza MapReduce como motor de ejecución de Hive |
| 10 | Flume |J | J | Herramienta de ingesta de logs/eventos en streaming hacia HDFS o Kafka |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas y argumentos técnicos. Extensión: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El Ministerio de Salud (MINSA) del Perú quiere modernizar su sistema de información para el programa de Vigilancia Epidemiológica. El sistema debe:
- Almacenar reportes de casos de enfermedades de 8,000 establecimientos de salud a nivel nacional
- Cada reporte tiene campos variables (dengue tiene campos de serotipos; COVID tenía campos de variante; hepatitis tiene campos de cronología de vacunas)
- Permitir consultas como "¿cuántos casos de dengue hubo en Loreto en la semana 23?"
- Responder en menos de 2 segundos para el dashboard del epidemiólogo

a) ¿Qué tipo de base de datos NoSQL recomendarías para almacenar los reportes? Justifica con al menos 2 razones técnicas relacionadas al caso.

Razón 1 — Esquema flexible por enfermedad:

Cada enfermedad tiene campos completamente distintos. Dengue necesita campos de serotipos, COVID necesitaba campos de variante, hepatitis campos de cronología de vacunas. En MongoDB cada reporte se almacena como un documento JSON independiente con su propia estructura, sin necesidad de hacer ALTER TABLE cada vez que surge una nueva enfermedad o campo. Esto es crítico en epidemiología donde los formularios cambian constantemente.
Razón 2 — Escalabilidad para 8,000 establecimientos:

Con 8,000 establecimientos reportando diariamente, el volumen de documentos crece rápidamente. MongoDB soporta sharding horizontal automático, distribuyendo los documentos entre nodos por región geográfica (shard key = región/departamento), lo que permite escalar sin rediseñar la arquitectura.
Razón adicional — Consultas geográficas:

MongoDB tiene soporte nativo para índices geoespaciales, útil para consultas por departamento, provincia o distrito, que son frecuentes en vigilancia epidemiológica

b) ¿Qué componente del ecosistema Hadoop usarías para las consultas analíticas del dashboard? ¿Hive, Impala/Spark SQL, o HBase? Justifica.

Respuesta: Impala / Spark SQL
La justificación central es el requisito de menos de 2 segundos, que es el filtro técnico que descarta a Hive y HBase para este caso.

¿Por qué NO Hive?

Hive traduce las consultas en jobs MapReduce, lo que implica escrituras intermedias en disco entre fases. Una consulta como "casos de dengue en Loreto en la semana 23" tardaría varios minutos, inaceptable para un dashboard en tiempo real.
¿Por qué NO HBase?

HBase está optimizado para acceso por clave primaria (buscar un registro específico en millisegundos), pero la consulta del epidemiólogo es analítica y agregada — requiere escanear múltiples registros, filtrar por región y semana, y contar. HBase no está diseñado para ese patrón de consulta.

¿Por qué SÍ Impala o Spark SQL?
Ejecutan SQL directamente sobre HDFS en memoria, sin pasar por MapReduce 
Responden consultas analíticas agregadas en segundos 
Soportan filtros por múltiples columnas (enfermedad + región + semana epidemiológica) 
Impala es ideal si el clúster es Cloudera; Spark SQL si la infraestructura ya usa Spark 

---


**17. (8 puntos)** Compara el paradigma ACID de las bases de datos relacionales con el paradigma BASE de las bases de datos NoSQL. Luego responde:

a) ¿En qué tipo de aplicaciones es OBLIGATORIO usar ACID y por qué?  

ACID es obligatorio en cualquier sistema donde un error de datos tenga consecuencias legales, financieras o de seguridad irreversibles:
Banca y finanzas: Una transferencia bancaria debe ser atómica — o se debita de una cuenta Y se acredita en otra, o no ocurre ninguna de las dos. Si el sistema falla a mitad de la operación y no hay atomicidad, el dinero desaparece. La consistencia eventual de BASE sería catastrófica aquí.
Sistemas de salud: La prescripción de medicamentos o el historial clínico de un paciente no puede mostrar datos desactualizados. Una dosis incorrecta por inconsistencia temporal puede costar una vida.
Comercio electrónico con inventario: Si dos usuarios compran el último producto simultáneamente, el aislamiento de ACID garantiza que solo uno lo obtenga. Sin aislamiento, ambos recibirían confirmación de compra y el inventario quedaría en negativo.
Razón técnica central: En estos sistemas el costo de un dato incorrecto supera ampliamente el costo de una menor disponibilidad o velocidad.


b) ¿En qué tipo de aplicaciones es ACEPTABLE y BENEFICIOSO usar BASE y por qué?  

BASE es aceptable cuando la disponibilidad y la escala importan más que la precisión absoluta en cada milisegundo:
Redes sociales (contador de likes): Si el contador de likes de una publicación muestra 1,842 en lugar de 1,843 durante unos millisegundos, no hay consecuencia real. La consistencia eventual garantiza que todos los nodos convergerán al valor correcto pronto. Bloquear millones de escrituras simultáneas para mantener ACID sería imposible a esa escala.
Catálogos de e-commerce: Si el precio de un producto tarda 200ms en propagarse a todos los nodos del mundo, es aceptable. Lo que no es aceptable es que el sitio caiga por intentar mantener consistencia estricta entre datacenter de Lima y servidor de São Paulo.
Streaming y recomendaciones: Netflix o Spotify pueden mostrar recomendaciones ligeramente desactualizadas sin impacto en el usuario. La disponibilidad del servicio (que la música suene) es infinitamente más importante que la precisión exacta del algoritmo en ese instante.
Razón técnica central: BASE permite escalar horizontalmente a millones de usuarios porque elimina los bloqueos y la coordinación global que ACID requiere.

c) ¿Existe algún sistema de bases de datos que combine ambos paradigmas? ¿Cuál es su nombre y cómo lo logra?

Sí existen, se denominan bases de datos NewSQL.
Ejemplos principales:

| Sistema | Cómo combina ACID + escala |
|---|---|
| **Google Spanner** | ACID distribuido globalmente usando relojes atómicos (TrueTime) para sincronización |
| **CockroachDB** | Transacciones ACID distribuidas sobre arquitectura NoSQL peer-to-peer |
| **YugabyteDB** | Compatible con PostgreSQL (ACID) pero con sharding automático horizontal |
| **MongoDB 4.0+** | Agregó transacciones ACID multi-documento manteniendo su esquema flexible |


---

**18. (6 puntos) — Mini caso de análisis:**

*La plataforma de e-commerce "CompraYa Perú" tiene estos componentes en su sistema:*
- *Catálogo: 2 millones de productos con atributos variables (electrónicos tienen voltaje, ropa tiene talla, alimentos tienen fecha de vencimiento)*
- *Carrito de compras: almacena el carrito activo de 200K usuarios simultáneos (expira en 2 horas si no compran)*
- *Órdenes de compra: cada orden debe debitarse exactamente una vez de la cuenta del usuario (si el pago falla, no debe cobrarse)*
- *Historial de navegación: registra cada producto visto por cada usuario (50M eventos/día para recomendaciones)*

a) Para cada componente, identifica el tipo de base de datos más adecuado (SQL, MongoDB, Redis, Cassandra) y justifica brevemente cada elección.

1. Catálogo — MongoDB
Los 2 millones de productos tienen atributos completamente distintos por categoría. Un electrónico necesita campos de voltaje y garantía; una prenda necesita talla y color; un alimento necesita fecha de vencimiento. MongoDB permite que cada producto sea un documento JSON con su propia estructura sin forzar un esquema rígido. En PostgreSQL habría que crear tablas separadas por categoría o usar columnas nullable masivas, lo cual es ineficiente y difícil de mantener.
2. Carrito de compras — Redis
El carrito tiene tres características que apuntan directamente a Redis: es temporal (expira en 2 horas), requiere acceso ultrarrápido (el usuario espera respuesta inmediata al agregar productos) y hay 200K usuarios simultáneos. Redis maneja esto con su estructura de datos nativa (Hash por usuario), latencia menor a 1ms y TTL automático que elimina carritos expirados sin intervención manual. Persistirlo en disco sería un desperdicio de recursos para datos que viven 2 horas.

3. Órdenes de compra — PostgreSQL (SQL)
Este es el componente más crítico del sistema. La frase clave es "debe debitarse exactamente una vez — si el pago falla, no debe cobrarse". Eso es una transacción ACID obligatoria. Se necesita atomicidad (o se cobra y se crea la orden, o no ocurre nada), consistencia (el inventario se descuenta correctamente) y durabilidad (la orden no puede perderse). Ninguna base de datos NoSQL ofrece estas garantías de forma nativa y confiable. PostgreSQL es la única opción correcta aquí.

4. Historial de navegación — Cassandra
50 millones de eventos por día es escritura masiva y continua, el escenario perfecto para Cassandra. El patrón de acceso es predecible: se consulta por usuario + rango de fechas (partition key = user_id, clustering key = timestamp), que es exactamente el modelo de datos de Cassandra. Su arquitectura sin maestro garantiza disponibilidad continua incluso si algún nodo falla, y escala linealmente agregando nodos cuando el volumen crezca.

b) ¿Una sola base de datos o Polyglot Persistence?
La arquitectura polyglot persistence es claramente superior aquí.
Usar una sola base de datos para todo el sistema significaría hacer compromisos inaceptables:
Si se elige PostgreSQL para todo, el catálogo con esquemas variables requeriría tablas con cientos de columnas nullable o esquemas EAV (Entity-Attribute-Value) que son lentos y difíciles de mantener. Los 50M eventos diarios de navegación saturarían el almacenamiento relacional. El carrito temporal desperdiciaría espacio en disco para datos que viven 2 horas.
Si se elige MongoDB para todo, las órdenes de compra perderían las garantías ACID que son obligatorias. Un fallo a mitad del proceso de pago podría cobrar al usuario sin crear la orden, o crear la orden sin cobrar.


b) ¿Es correcto usar UNA SOLA base de datos para todo el sistema? Argumenta si la arquitectura polilíngüe (polyglot persistence) es mejor o peor aquí.

Si todo en PostgreSQL:

El catálogo con atributos variables obligaría a crear cientos de columnas nullable o un modelo EAV (Entity-Attribute-Value) extremadamente lento
Los 50M eventos diarios de navegación saturarían el almacenamiento relacional rápidamente
El carrito temporal desperdiciaría espacio en disco para datos que viven solo 2 horas
Escalar horizontalmente es costoso y complejo en SQL

Si todo en MongoDB:

Las órdenes de compra perderían garantías ACID obligatorias
Un fallo a mitad del pago podría cobrar al usuario sin crear la orden, o crear la orden sin cobrar
Inaceptable legalmente y comercialmente

Si todo en Cassandra:

No tiene transacciones ACID para órdenes
No tiene TTL eficiente para carritos temporales
Consultas analíticas complejas son limitadas

Si todo en Redis:

Los datos no persisten de forma confiable a largo plazo
No escala bien para 2 millones de productos o 50M eventos

---

**19. (8 puntos)** Explica por qué Apache Pig (2008) fue un paso importante en la evolución del ecosistema Hadoop, y luego explica por qué la industria lo abandonó en favor de Apache Spark (2014). ¿Qué característica de Pig sobrevivió en Spark? ¿Qué limitación eliminó Spark?

Apache Pig (2008): Un paso importante en la evolución de Hadoop

¿Por qué Pig fue importante en su momento?
Antes de Pig, la única forma de procesar datos en Hadoop era escribir jobs MapReduce en Java, lo que requería decenas o cientos de líneas de código para operaciones simples como filtrar, agrupar o unir datasets. Un analista de datos sin experiencia en Java simplemente no podía trabajar con Hadoop.
Pig resolvió esto con Pig Latin, un lenguaje de scripting de flujo de datos que abstraía completamente MapReduce:
pig-- Esto en Pig Latin reemplazaba cientos de líneas de Java
datos = LOAD 'ventas.csv' USING PigStorage(',');
filtrado = FILTER datos BY region == 'Lima';
agrupado = GROUP filtrado BY producto;
resultado = FOREACH agrupado GENERATE group, COUNT(filtrado);
DUMP resultado;
Pig traducía automáticamente ese script en jobs MapReduce, democratizando el acceso a Hadoop para científicos de datos y analistas sin perfil de ingeniero Java.
Contribuciones clave de Pig:

Paso 1 → RAM → Paso 2 → RAM → Paso 3 → escribe resultado final

Introdujo el concepto de pipeline de transformaciones declarativo sobre datos distribuidos
Permitió operaciones complejas (JOIN, GROUP, FILTER) sin MapReduce manual
Fue adoptado masivamente por Yahoo, Twitter y LinkedIn para ETL a gran escala


¿Por qué la industria abandonó Pig en favor de Spark?
Pig tenía una limitación arquitectónica fundamental que no podía resolver: cada operación del pipeline escribía resultados intermedios en disco (HDFS) antes de pasar a la siguiente.
Paso 1 → escribe en HDFS → Paso 2 → escribe en HDFS → Paso 3
Esto significaba que un pipeline de 10 transformaciones hacía 10 lecturas y 10 escrituras en disco, con latencias de minutos u horas para datasets grandes.
Spark eliminó exactamente esa limitación con su modelo de procesamiento en memoria (RDD/DataFrame):

¿Qué característica de Pig sobrevivió en Spark?
El concepto de pipeline de transformaciones lazy (perezoso) sobrevivió y evolucionó en Spark.
En Pig, se describía el flujo completo de transformaciones y el sistema optimizaba el plan de ejecución antes de correrlo. Spark adoptó exactamente ese modelo con sus transformaciones lazy: cuando escribes filter(), groupBy(), join() en Spark, no se ejecutan inmediatamente — Spark construye un plan de ejecución (DAG) y lo optimiza globalmente antes de procesar un solo dato. Esto se llama Catalyst Optimizer en Spark SQL.

Conclusión
Pig fue el puente necesario entre el MapReduce manual y el procesamiento moderno de datos. Demostró que era posible abstraer la complejidad de Hadoop con un lenguaje de alto nivel, abriendo el ecosistema a perfiles no técnicos. Spark tomó esa idea, eliminó el cuello de botella del disco y añadió procesamiento en memoria, streaming, ML y SQL en una sola plataforma unificada, haciendo a Pig obsoleto. La herencia real de Pig vive en la filosofía de los pipelines declarativos que hoy es el estándar en toda la industria de datos.

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

a) Tabla de tecnologías por sistema

| Sistema | Tecnología | Tipo | Justificación técnica |
|---|---|---|---|
| **1** Core bancario | PostgreSQL + Oracle RAC | SQL relacional | Las transacciones bancarias exigen ACID obligatorio — atomicidad para que una transferencia no quede a mitad, consistencia para que el saldo nunca sea negativo, durabilidad para que ningún dato se pierda ante fallo. 5M transacciones diarias (~58 TPS) es manejable para SQL optimizado con particionado por fecha. |
| **2** App móvil | Redis + MongoDB | NoSQL Key-Value + Documental | Redis almacena en memoria el saldo y últimas 5 transacciones con latencia <1ms, cumpliendo los 300ms de carga total. MongoDB almacena el perfil completo y ofertas personalizadas con esquema flexible. Para 800K logins simultáneos, Redis escala horizontalmente con Redis Cluster sin degradar performance. |
| **3** Motor de recomendaciones | Apache Spark + HDFS / Delta Lake | Procesamiento distribuido + Data Lake | 75TB de datos históricos requieren procesamiento distribuido en memoria — Spark procesa en paralelo sobre múltiples nodos en minutos lo que un servidor local tardaría días. HDFS o Delta Lake almacenan los 5 años de historial con compresión columnar (Parquet). MLlib de Spark permite re-entrenar el modelo directamente sobre los datos distribuidos. |
| **4** Detección de fraude | Neo4j | NoSQL Grafo | Detectar ciclos A→B→C→A es un problema de traversal de grafos, el caso de uso exacto para el que Neo4j fue diseñado. Una consulta Cypher como `MATCH (a)-[:TRANSFIERE*3]->(a)` detecta ciclos en millisegundos navegando relaciones. En SQL o Cassandra, esa misma consulta requeriría múltiples JOINs recursivos extremadamente lentos para el límite de 5 minutos. |


b) Aplica el Teorema CAP a los Sistemas 1 y 2 específicamente. ¿Cuál combinación CAP debe tener cada uno y por qué? Da un ejemplo de qué pasaría si eligieras la combinación incorrecta. (4 puntos)

b) Teorema CAP aplicado a Sistemas 1 y 2
Sistema 1 — Core bancario: CP (Consistencia + Tolerancia a Particiones)
En una transferencia bancaria, la consistencia es innegociable. Si hay una partición de red entre nodos, el sistema debe preferir negarse a responder antes que procesar una transacción con datos inconsistentes.

¿Qué pasaría si eligiéramos AP (incorrecto)?

Si el Sistema 1 priorizara disponibilidad sobre consistencia, ante una partición de red dos nodos podrían procesar simultáneamente la misma transferencia de S/1,000. El cliente vería el débito dos veces o el dinero desaparecería entre nodos desincronizados. Eso es un fraude sistémico generado por el propio banco, con consecuencias legales y regulatorias gravísimas ante la SBS.

c) En el Sistema 3 (recomendaciones), el equipo de ML propone usar un archivo CSV de 75 TB almacenado en el servidor local del equipo para entrenar el modelo semanalmente. ¿Qué argumentas tú como Data Architect en contra de esta propuesta? ¿Qué propones en su lugar? (3 puntos)

La propuesta del equipo de ML es técnicamente inviable por tres razones:

**Razón 1 — Capacidad física imposible:**
75TB en un servidor local requiere hardware especializado de altísimo costo. Pero más crítico aún, leer 75TB secuencialmente desde un disco para entrenar el modelo tomaría días, no horas. El re-entrenamiento semanal sería imposible de completar dentro de la ventana de tiempo disponible.

**Razón 2 — Sin tolerancia a fallos:**
Un servidor local es un punto único de fallo. Si el disco falla durante el entrenamiento (que dura horas), se pierde todo el progreso y potencialmente los datos. Los 5 años de historial transaccional de 3.5M clientes son irrecuperables si no hay replicación.

**Razón 3 — CSV es el formato menos eficiente posible:**
CSV no tiene compresión, no tiene indexación columnar y no permite lectura paralela eficiente. Leer una columna específica (ej. monto) de un CSV de 75TB requiere leer los 75TB completos. Es el peor formato posible para analítica a esta escala.

**¿Qué propongo en su lugar?**

Arquitectura con HDFS + Apache Spark + formato Parquet:

Transacciones diarias → Pipeline ETL (Spark) → HDFS / Delta Lake
                                                    ↓ (formato Parquet, comprimido)
                                              Spark MLlib
                                                    ↓
                                            Modelo re-entrenado
                                                    ↓
                                              Redis (serving)

**Ventajas concretas:**
- Parquet columnar reduce los 75TB a ~15-20TB con compresión, y permite leer solo las columnas necesarias para el modelo
- Spark distribuido paraleliza el entrenamiento en decenas de nodos, reduciendo el tiempo de horas a minutos
- HDFS replica los datos en 3 nodos automáticamente, eliminando el punto único de fallo
- Delta Lake agrega versionado de datos, permitiendo reproducir entrenamientos anteriores y hacer rollback si un modelo nuevo degrada las recomendaciones
---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías una base de datos NoSQL para el sistema de seguimiento de paquetes de Olva Courier Perú? El sistema debe: (a) registrar cada evento de cada paquete (recepción, en tránsito, en distribución, entregado) en tiempo real; (b) permitir al cliente consultar 'dónde está mi paquete' por número de guía en menos de 100ms; (c) guardar historial de los últimos 2 años (150M paquetes × 8 eventos = 1.2B eventos)."*

Diseña:
- El tipo de NoSQL elegido y justificación
- El modelo de datos (cómo organizarías los documentos/columnas/claves)
- La consulta que usarías para responder "¿dónde está el paquete #PE123456?"
- Por qué esta solución es mejor que usar una tabla SQL con índices


Respuesta: 

## Solución NoSQL para Olva Courier Perú

---

### 1. Tipo de NoSQL elegido: Apache Cassandra (Column-family)

**Justificación:**
- 1.2B eventos es escritura masiva y continua → Cassandra es la BD más optimizada para esto
- La consulta "dónde está mi paquete" es por número de guía → acceso predecible por partition key
- Sin punto único de fallo → si un nodo cae, el sistema sigue registrando eventos en tiempo real
- TTL nativo → los eventos de más de 2 años se eliminan automáticamente sin jobs de limpieza

---

### 2. Modelo de datos

```cql
CREATE TABLE seguimiento_paquetes (
    numero_guia    TEXT,
    fecha_hora     TIMESTAMP,
    estado         TEXT,
    ubicacion      TEXT,
    ciudad         TEXT,
    responsable    TEXT,
    observacion    TEXT,
    PRIMARY KEY (numero_guia, fecha_hora)
) WITH CLUSTERING ORDER BY (fecha_hora DESC)
  AND default_time_to_live = 63072000;  -- 2 años en segundos
```

**¿Por qué este diseño?**

| Elemento | Decisión | Razón |
|---|---|---|
| `numero_guia` como partition key | Todos los eventos del mismo paquete van al mismo nodo | Consulta en <100ms sin escanear otros nodos |
| `fecha_hora` como clustering key | Los eventos se ordenan cronológicamente dentro de la partición | El evento más reciente aparece primero (ORDER BY DESC) |
| TTL = 2 años | Cassandra elimina automáticamente eventos viejos | Sin jobs de limpieza manual sobre 1.2B registros |

---

### 3. Consulta "¿dónde está el paquete #PE123456?"

```cql
-- Último evento (ubicación actual)
SELECT estado, ubicacion, ciudad, fecha_hora
FROM seguimiento_paquetes
WHERE numero_guia = 'PE123456'
LIMIT 1;

-- Historial completo del paquete
SELECT estado, ubicacion, ciudad, fecha_hora, responsable
FROM seguimiento_paquetes
WHERE numero_guia = 'PE123456';
```

**Resultado esperado:**
---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si MongoDB Atlas (la plataforma cloud de MongoDB) tiene una caída de servicio de 2 horas durante el horario pico de tu aplicación? ¿Qué riesgos concretos implica depender de una sola base de datos NoSQL en la nube para una aplicación crítica como la app de Claro Perú?"*

Analiza:
- ¿Qué componentes de la app dejarían de funcionar?
- ¿Qué estrategias de resiliencia implementarías para mitigar el riesgo?
- ¿Es mejor tener múltiples proveedores de NoSQL o un solo proveedor con alta disponibilidad configurada?
- ¿Qué nivel de SLA (Service Level Agreement) deberías negociar con MongoDB Atlas?

## Análisis de riesgo: Caída de MongoDB Atlas 2 horas en Claro Perú

---

### 1. Componentes que dejarían de funcionar

Asumiendo que Claro Perú usa MongoDB Atlas como base de datos central de su app:

| Componente | Impacto | Severidad |
|---|---|---|
| Consulta de saldo y consumo | Sin acceso al perfil del cliente → pantalla en blanco | 🔴 Crítico |
| Recarga de saldo | No se puede escribir la transacción → recargas fallidas | 🔴 Crítico |
| Historial de llamadas/datos | No disponible → cliente no puede ver su consumo | 🟠 Alto |
| Cambio de plan | No se puede actualizar el documento del cliente | 🟠 Alto |
| Ofertas personalizadas | No se pueden leer las ofertas del perfil | 🟡 Medio |
| Login / autenticación | Si el perfil vive en MongoDB, el login falla completamente | 🔴 Crítico |

**Impacto cuantificable:**
Claro Perú tiene ~8M clientes móviles. En horario pico (7-9pm) aproximadamente
20-30% usa la app simultáneamente → 1.6M a 2.4M usuarios afectados durante 2 horas.
A esto se suman llamadas masivas al call center, daño reputacional y posibles
multas regulatorias de OSIPTEL por indisponibilidad de servicio.

---

### 2. Estrategias de resiliencia

**Estrategia 1 — Multi-region replication (activo-activo):**
Configurar MongoDB Atlas con réplicas en al menos 2 regiones AWS:
- Región primaria: São Paulo (más cercana a Perú)
- Región secundaria: us-east-1 (failover automático)

Si São Paulo cae, Atlas promueve automáticamente el nodo secundario
en menos de 30 segundos sin intervención manual.

Cliente → App → Redis (caché) → MongoDB Atlas

↓

Si Atlas cae, Redis sirve datos en modo lectura

con los últimos datos cacheados (TTL: 5 minutos)

**Estrategia 2 — Capa de caché con Redis:**
El 80% de consultas son lectura (saldo, historial) → Redis las
resuelve aunque Atlas esté caído, manteniendo la app parcialmente funcional.

**Estrategia 3 — Circuit Breaker pattern:**
Implementar un circuit breaker (Resilience4j o Hystrix) que:
- Detecta fallos consecutivos a MongoDB en <5 segundos
- Abre el circuito y redirige a caché o datos degradados
- Muestra al usuario "Datos actualizados hace 3 minutos" en lugar de error

**Estrategia 4 — Cola de escrituras con Kafka:**
Las escrituras críticas (recargas, cambios de plan) no van directo a MongoDB:

Kafka garantiza que ninguna recarga se pierda aunque MongoDB esté caído.
Cuando Atlas vuelve, los eventos pendientes se procesan en orden.

**Estrategia 5 — Modo degradado por funcionalidad:**
Definir qué funciona y qué no cuando Atlas cae:

| Funcionalidad | Modo degradado |
|---|---|
| Ver saldo | Sirve último saldo cacheado en Redis |
| Recargar | Encola en Kafka, confirma al usuario |
| Ver historial | Muestra "Temporalmente no disponible" |
| Login | Autentica con JWT válido sin consultar BD |

---

### 3. ¿Múltiples proveedores o un solo proveedor con alta disponibilidad?

**Recomendación: Un solo proveedor (MongoDB Atlas) con alta disponibilidad
configurada correctamente, NO múltiples proveedores NoSQL.**

**¿Por qué NO múltiples proveedores?**
- Mantener MongoDB Atlas + DynamoDB + Cosmos DB simultáneamente triplica
  la complejidad operacional y el costo
- Los equipos deben dominar múltiples APIs, SDKs y modelos de consistencia distintos
- La sincronización de datos entre proveedores genera inconsistencias y latencia adicional
- El costo de ingeniería para mantener dos sistemas en sync supera el beneficio

**¿Por qué SÍ un solo proveedor bien configurado?**
MongoDB Atlas ya ofrece nativamente:
- Réplicas multi-región activo-activo
- Failover automático en <30 segundos
- 99.995% uptime SLA (menos de 26 minutos de caída al año)
- Backups continuos con point-in-time recovery

La combinación Atlas multi-región + Redis + Kafka resuelve el problema
de resiliencia sin la complejidad de múltiples proveedores.

---

### 4. SLA que deberías negociar con MongoDB Atlas

| Métrica | Mínimo aceptable | Ideal para Claro |
|---|---|---|
| **Uptime mensual** | 99.99% (52 min/año caída) | 99.995% (26 min/año) |
| **RTO** (Recovery Time Objective) | < 5 minutos | < 30 segundos con failover automático |
| **RPO** (Recovery Point Objective) | < 1 minuto de datos perdidos | 0 con replicación síncrona |
| **Failover automático** | Obligatorio | Multi-región activo-activo |
| **Soporte** | 24/7 con respuesta < 1 hora | Respuesta < 15 min para P1 |
| **Penalidad por incumplimiento** | Créditos del 10% por hora caída | Créditos del 25% + SLA escalonado |

**Cálculo del impacto del SLA:**
- 99.99% uptime = 52.6 minutos de caída permitida al año
- 99.999% uptime = 5.26 minutos de caída permitida al año
- Para Claro con 8M clientes, cada minuto de caída en horario pico
  representa ~13,000 usuarios afectados → el SLA debe ser 99.995% mínimo

**Cláusulas adicionales obligatorias en el contrato:**
- Notificación proactiva en menos de 5 minutos ante cualquier incidente
- Runbook de escalamiento definido con nombres y teléfonos
- Post-mortem obligatorio con causa raíz en menos de 48 horas
- Pruebas de failover programadas trimestralmente verificadas por Claro

### Conclusión

Una caída de 2 horas en MongoDB Atlas sin estrategias de resiliencia
es un desastre operacional para Claro Perú. La solución no es cambiar
de proveedor sino construir resiliencia en capas:
Redis para lecturas, Kafka para escrituras, Circuit Breaker para
degradación elegante, y Atlas multi-región para failover automático.
Con esta arquitectura, una caída de Atlas se convierte en un evento
transparente para el 80% de usuarios en lugar de una crisis total.


---



*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
