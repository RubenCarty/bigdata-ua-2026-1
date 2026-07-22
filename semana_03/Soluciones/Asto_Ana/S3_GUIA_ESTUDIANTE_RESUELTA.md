# S3 — GUÍA DE TRABAJO DEL ESTUDIANTE — DESARROLLADA
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Ana Concepción Asto Arotinco |
| **Código** | — |
| **Sección** | — |
| **Fecha** | Junio 2026 |
| **Tiempo estimado** | 90 minutos |
| **Puntaje total** | 100 puntos |

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos)

---

**1.** ¿Cuál fue el problema principal del JobTracker en Hadoop 1.x que motivó la creación de YARN?

**✅ Respuesta: b) El JobTracker mezclaba la gestión de recursos del clúster con la coordinación de jobs, convirtiéndose en cuello de botella y punto único de fallo**

El JobTracker tenía dos responsabilidades incompatibles en un solo proceso: administrar los recursos del clúster (cuánta CPU y RAM tiene cada nodo) y coordinar la ejecución de cada job MapReduce. Esto significaba que si el JobTracker fallaba, todo el clúster quedaba paralizado. Además, como único punto de gestión de recursos, no podía manejar múltiples frameworks (solo MapReduce). YARN separó estas responsabilidades en el ResourceManager (recursos globales) y el ApplicationMaster (coordinación por job), resolviendo ambos problemas.

---

**2.** Apache Hive traduce las consultas HiveQL en ¿qué tipo de trabajos distribuidos?

**✅ Respuesta: c) Jobs MapReduce (o Tez/Spark en versiones modernas) que procesan los archivos de HDFS en paralelo**

Hive es esencialmente un traductor: convierte el SQL del analista en jobs distribuidos que el clúster puede ejecutar. En versiones antiguas siempre generaba MapReduce, lo que implicaba alta latencia (minutos). En versiones modernas usa Tez (DAG optimizado) o Spark como motor de ejecución, reduciendo la latencia significativamente.

---

**3.** ¿Qué diferencia fundamental existe entre Apache Hive y Apache Impala?

**✅ Respuesta: b) Hive compila las consultas en jobs MapReduce (alta latencia); Impala ejecuta SQL directamente en HDFS sin MapReduce (baja latencia, segundos)**

Hive tiene latencia de minutos porque cada consulta genera un job MapReduce con su overhead de inicio, escritura a disco y shuffle. Impala usa un motor MPP (Massively Parallel Processing) que ejecuta las consultas directamente en los DataNodes sin pasar por MapReduce, respondiendo en segundos. La contrapartida es que Impala necesita que los datos quepan en memoria y no toleran tan bien los fallos como Hive.

---

**4.** Apache Ambari fue diseñado principalmente para:

**✅ Respuesta: c) Gestionar, monitorear e instalar componentes del ecosistema Hadoop desde una interfaz web centralizada**

Ambari es la herramienta de administración del ecosistema Hadoop de Hortonworks. Desde una sola interfaz web puedes instalar HDFS, YARN, Hive, HBase y otros componentes, monitorear el estado de cada nodo, configurar parámetros del clúster y recibir alertas cuando algo falla. Simplifica enormemente la gestión de clústeres Hadoop que de otro modo requerirían configuración manual en decenas de servidores.

---

**5.** Sistema de facturación que nunca debe mostrar montos incorrectos. ¿Qué combinación CAP?

**✅ Respuesta: c) CP — Consistencia y Tolerancia a Particiones**

En un sistema de facturación, mostrar un monto incorrecto es catastrófico para el negocio. Se sacrifica la Disponibilidad (A): si hay una partición de red, el sistema prefiere devolver un error ("sistema no disponible") antes de mostrar datos inconsistentes. Un cliente puede tolerar que el sistema esté brevemente no disponible, pero jamás debe recibir un cobro incorrecto. CockroachDB y otros NewSQL usan esta combinación exactamente.

---

**6.** ¿Cuál es la diferencia entre el modelo ACID y el modelo BASE?

**✅ Respuesta: b) ACID garantiza consistencia estricta en transacciones (apropiado para bancos); BASE acepta consistencia eventual a favor de alta disponibilidad (apropiado para redes sociales)**

ACID (Atomicity, Consistency, Isolation, Durability) garantiza que cada transacción se complete completamente o no se complete para nada, y que todos los nodos vean los mismos datos al mismo tiempo. BASE (Basically Available, Soft state, Eventually consistent) acepta que los datos pueden estar temporalmente inconsistentes entre nodos, pero eventualmente convergerán al mismo estado. Para ver el like de alguien en Instagram con 1 segundo de retraso es aceptable; para transferir dinero bancario, no lo es.

---

**7.** Plataforma de streaming con 50M usuarios de perfiles con atributos variables.

**✅ Respuesta: b) Document (MongoDB) — porque cada documento puede tener estructura diferente sin esquema fijo**

El caso describe explícitamente esquemas variables por usuario (listas de reproducción, favoritos, historial de podcasts). MongoDB es la solución natural porque cada documento puede tener exactamente los campos que ese usuario necesita, sin columnas NULL. Redis (Key-Value) es excelente para caché pero no para almacenar perfiles complejos con estructuras anidadas. Cassandra está optimizada para escrituras masivas con esquema predefinido, no para esquemas variables.

---

**8.** ¿Cuál es la principal ventaja de Cassandra frente a MongoDB para historial de llamadas de 2,000 millones de registros/año?

**✅ Respuesta: c) Cassandra está optimizada para escrituras masivas y continuas con acceso predecible por partition key + timestamp, sin punto único de fallo**

El historial de llamadas es un caso de uso clásico de Cassandra: insertions masivas y continuas (millones de CDRs por día), acceso predecible siempre por número de teléfono + rango de fechas, y necesidad de alta disponibilidad 24/7. Cassandra usa arquitectura de anillo sin maestro (masterless), eliminando el SPOF. MongoDB es excelente para documentos con esquemas variables, pero Cassandra supera en throughput de escrituras continuas con patrón de acceso conocido.

---

**9.** Sqoop es una herramienta diseñada para:

**✅ Respuesta: c) Transferir datos en batch entre bases de datos relacionales (Oracle, MySQL) y HDFS en ambas direcciones**

Sqoop (SQL-to-Hadoop) es el conector entre el mundo relacional y el mundo Big Data. Permite hacer `sqoop import` para traer datos de Oracle/MySQL/PostgreSQL a HDFS, y `sqoop export` para enviar resultados de HDFS de vuelta a una base de datos relacional. Lo hace en paralelo usando múltiples conexiones JDBC simultáneas, lo que hace la transferencia eficiente para grandes volúmenes.

---

**10.** Startup con 10K usuarios, proyección de 5M en 12 meses, perfiles con contenido variable.

**✅ Respuesta: b) MongoDB permite escalar horizontalmente con sharding automático y soporta esquemas flexibles que se adaptan a los distintos tipos de contenido sin costosas migraciones de esquema**

La combinación de dos factores hace MongoDB la elección correcta: (1) el crecimiento explosivo de 10K a 5M usuarios requiere sharding horizontal — agregar más servidores — que MongoDB hace nativamente; y (2) los diferentes tipos de contenido (texto, imagen, video, encuesta) tienen estructuras distintas que en PostgreSQL requerirían costosas migraciones de esquema (ALTER TABLE) con millones de registros. La nota c es incorrecta — PostgreSQL sí soporta JSON nativo desde la versión 9.2.

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco

**11.** En la arquitectura YARN, el componente **ResourceManager** gestiona los recursos del clúster a nivel global, mientras que el **ApplicationMaster** coordina la ejecución de cada aplicación individual en los nodos.

**12.** El Teorema CAP establece que un sistema distribuido solo puede garantizar dos de tres propiedades: **Consistencia** (todos los nodos ven los mismos datos), **Disponibilidad** (el sistema siempre responde), y Tolerancia a Particiones.

**13.** En MongoDB, los datos se organizan en **colecciones** (equivalente a una tabla SQL), que contienen **documentos** (equivalente a filas) en formato JSON/BSON, donde cada uno puede tener una estructura diferente.

**14.** Apache **Pig** traduce un lenguaje de scripting llamado "Pig Latin" en jobs MapReduce, mientras que Apache **Hive** traduce consultas en un dialecto SQL propio (HiveQL) en jobs MapReduce o Spark.

**15.** La herramienta **Sqoop** permite importar datos de una base de datos MySQL a HDFS de forma paralela usando múltiples conexiones JDBC simultáneas.

---

### B2. Relacionar columnas

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | Redis | **D** | Base de datos Key-Value en memoria con latencia < 1ms, usada para caché de sesiones |
| 2 | Apache Cassandra | **E** | Base de datos columnar distribuida sin maestro (ring), optimizada para escrituras masivas |
| 3 | Impala | **A** | Motor SQL interactivo de Cloudera que ejecuta consultas directamente sobre HDFS sin MapReduce |
| 4 | Neo4j | **B** | Base de datos de grafos optimizada para navegar relaciones complejas en milisegundos |
| 5 | Ambari | **C** | Herramienta de gestión de clúster Hadoop con interfaz web (instala, monitorea, configura servicios) |
| 6 | Dremel | **F** | Tecnología de Google que inspira los formatos de almacenamiento columnar y BigQuery |
| 7 | Apache Drill | **G** | Motor SQL schema-free que consulta HDFS, MongoDB, S3 y otros sin esquema previo |
| 8 | MongoDB | **H** | Base de datos NoSQL documental con esquema flexible (BSON/JSON), más usada mundialmente |
| 9 | Tez | **I** | Framework de procesamiento DAG que reemplaza MapReduce como motor de ejecución de Hive |
| 10 | Flume | **J** | Herramienta de ingesta de logs/eventos en streaming hacia HDFS o Kafka |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

---

**16. (8 puntos) — MINSA: Vigilancia Epidemiológica**

**a) Tipo de base de datos NoSQL recomendado:**

Recomendaría **MongoDB (base de datos documental)** por dos razones técnicas directamente relacionadas al caso:

**Razón 1 — Esquema flexible por enfermedad:** Cada enfermedad tiene campos completamente distintos (dengue necesita serotipos y semana epidemiológica; COVID necesitaba variante y número de dosis; hepatitis necesita cronología de vacunas). En MongoDB cada reporte es un documento que tiene exactamente los campos que esa enfermedad requiere, sin columnas NULL masivas. En SQL, cada vez que aparece una nueva enfermedad con nuevos campos habría que hacer un ALTER TABLE, que con 8,000 establecimientos generando datos sería una operación costosísima.

**Razón 2 — Escalabilidad geográfica:** Los 8,000 establecimientos distribuidos a nivel nacional generan un volumen creciente de reportes. MongoDB escala horizontalmente con sharding, distribuyendo los datos por departamento o semana epidemiológica. Un servidor SQL centralizado sería un cuello de botella para miles de establecimientos escribiendo simultáneamente.

**b) Componente para consultas del dashboard (< 2 segundos):**

Usaría **Impala o Spark SQL**, no Hive ni HBase.

- **Hive: NO** — genera jobs MapReduce con latencia de minutos. Inaceptable para un epidemiólogo que necesita respuesta en 2 segundos.
- **HBase: NO** — HBase es para acceso a registros individuales por Row Key, no para consultas analíticas tipo "¿cuántos casos de dengue hubo en Loreto en la semana 23?" que requieren GROUP BY sobre miles de documentos.
- **Impala / Spark SQL: SÍ** — ejecutan SQL directamente sobre HDFS/Delta Lake sin MapReduce, respondiendo en 1-3 segundos. La consulta `SELECT COUNT(*) FROM reportes WHERE enfermedad='dengue' AND departamento='Loreto' AND semana=23` tarda segundos en Spark SQL con datos particionados por semana.

---

**17. (8 puntos) — ACID vs BASE**

**a) Aplicaciones donde ACID es OBLIGATORIO:**

ACID es obligatorio en cualquier operación donde la inconsistencia cause daño real irreversible:

- **Sistemas bancarios:** Un débito de S/1,000 de la cuenta A debe ser atómico con el crédito en la cuenta B. Si el sistema falla a mitad, el dinero no puede "desaparecer" ni duplicarse.
- **Sistemas de salud:** La prescripción de medicamentos debe ser consistente — si un médico prescribe y el sistema falla, no puede haber dos prescripciones o ninguna en el expediente.
- **E-commerce en el momento del pago:** El débito de la tarjeta y la confirmación del pedido deben ocurrir juntos o ninguno.

La razón técnica es que estas operaciones involucran transferencias de valor donde la inconsistencia tiene consecuencias financieras, legales o de salud.

**b) Aplicaciones donde BASE es ACEPTABLE y BENEFICIOSO:**

- **Redes sociales (likes, comentarios):** Si el contador de likes de una publicación muestra 1,245 en un nodo y 1,246 en otro durante medio segundo, nadie sufre daño. La consistencia eventual es perfectamente aceptable.
- **Catálogos de e-commerce:** Si el precio de un producto tarda 2 segundos en actualizarse en todos los servidores, el impacto es mínimo comparado con el beneficio de tener el catálogo siempre disponible para millones de usuarios simultáneos.
- **Historial de actividad/logs:** Los logs de navegación para recomendaciones no necesitan consistencia inmediata — que lleguen eventualmente es suficiente.

BASE es beneficioso aquí porque permite alta disponibilidad (el sistema nunca dice "no disponible") y escalabilidad horizontal sin los costos de coordinación del protocolo ACID distribuido.

**c) Sistema que combina ambos paradigmas:**

**Google Spanner** (y su equivalente open source **CockroachDB**) son sistemas NewSQL que combinan ACID con escalabilidad horizontal. Lo logran usando el protocolo **Paxos/Raft** para consenso distribuido: antes de confirmar una escritura, la mayoría de los nodos deben aceptarla. Esto garantiza consistencia ACID (ningún nodo confirma algo que los demás no aceptaron) manteniendo la distribución horizontal. Google Spanner además usa relojes atómicos sincronizados (TrueTime) para ordenar transacciones globalmente sin un servidor central de tiempo.

---

**18. (6 puntos) — Mini caso CompraYa Perú**

**a) Base de datos adecuada para cada componente:**

| Componente | BD Recomendada | Justificación |
|-----------|---------------|---------------|
| **Catálogo de 2M productos** | **MongoDB** | Cada categoría de producto tiene atributos distintos (electrónicos: voltaje; ropa: talla; alimentos: vencimiento). MongoDB permite documentos con esquemas variables sin columnas NULL. Las 2M de consultas de búsqueda se benefician de índices de texto de MongoDB. |
| **Carrito de compras (200K usuarios simultáneos, expira 2h)** | **Redis** | El carrito es temporal (TTL de 2 horas), necesita acceso ultrarrápido (< 1ms para no afectar UX), y es un caso de uso Key-Value clásico: clave = user_id, valor = lista de productos. Redis con `SETEX` maneja la expiración automáticamente. |
| **Órdenes de compra (débito exactamente una vez)** | **PostgreSQL (SQL)** | Las órdenes de compra involucran transacciones financieras que requieren ACID estricto. Si el pago falla, no debe cobrarse; si el pago tiene éxito, la orden debe crearse exactamente una vez. Ninguna base de datos NoSQL garantiza esto tan robustamente como PostgreSQL con transacciones ACID y constraints de unicidad. |
| **Historial de navegación (50M eventos/día)** | **Cassandra** | 50M eventos/día es escritura masiva y continua — el caso de uso perfecto de Cassandra. El patrón de acceso es predecible: siempre por user_id + rango de fechas para recomendaciones. Cassandra con partition key = user_id y clustering key = timestamp resuelve esto perfectamente con alta disponibilidad. |

**b) ¿Una sola BD para todo o arquitectura polilíngüe?**

La **arquitectura polilíngüe (polyglot persistence) es claramente mejor** para este caso. Usar una sola base de datos para todo implicaría compromisos inaceptables: si usas PostgreSQL para todo, el catálogo con 2M productos de esquema variable requeriría decenas de columnas NULL y migraciones costosas; el carrito temporal no tendría TTL automático; el historial de 50M eventos/día sobrecargaría el servidor SQL hasta el colapso. Si usas MongoDB para todo, las órdenes de compra perderían las garantías ACID necesarias para transacciones financieras.

Cada base de datos hace UNA cosa excepcionalmente bien. La arquitectura polilíngüe permite que cada componente use la herramienta óptima para su caso de uso. El costo es mayor complejidad operacional (4 bases de datos que mantener), pero los beneficios de rendimiento, escalabilidad y correctitud superan ampliamente ese costo para una plataforma de e-commerce seria.

---

**19. (8 puntos) — Apache Pig → Apache Spark: evolución**

**¿Por qué Pig fue importante?**

Apache Pig (2008) fue revolucionario porque resolvió el problema de productividad de MapReduce. Escribir un job MapReduce en Java para contar palabras requería 60-80 líneas de código con tres clases (Mapper, Reducer, Driver) y tiempo de compilación. Pig Latin permitía hacer lo mismo en 3 líneas de scripting de alto nivel: `datos = LOAD 'archivo'; palabras = FOREACH datos GENERATE ...; resultado = GROUP BY ...`. Pig introdujo el concepto de transformaciones en pipeline (DAG) que se optimizaban y compilaban automáticamente en MapReduce — fue el primer lenguaje de Big Data "amigable" que no requería saber Java.

**¿Por qué la industria lo abandonó en favor de Spark?**

Apache Spark (2014) eliminó la limitación fundamental de Pig: la dependencia de MapReduce. Pig seguía generando jobs MapReduce con toda su lentitud inherente (escritura a disco entre fases). Spark procesa en memoria RAM y puede ser 100x más rápido. Además, Spark unificó en un solo framework lo que antes requería múltiples herramientas: batch (como Pig), streaming (como Storm), ML (como Mahout) y SQL (como Hive) — todo con la misma API en Python, Scala o Java. Para 2016, Pig había perdido relevancia prácticamente total en la industria porque Spark hacía todo lo que Pig hacía, mucho más rápido y con más funcionalidades.

**¿Qué característica de Pig sobrevivió en Spark?**

El paradigma de **pipeline de transformaciones en DAG (Directed Acyclic Graph)**. En Pig escribías: `A = LOAD; B = FILTER A; C = GROUP B; STORE C`. En Spark escribes: `df.filter(...).groupBy(...).agg(...)`. Es exactamente la misma filosofía: una cadena de transformaciones que se compilan en un plan de ejecución optimizado. Spark's Catalyst Optimizer es la evolución directa del optimizador de Pig.

**¿Qué limitación eliminó Spark?**

Spark eliminó la **latencia de disco entre fases**. Pig/MapReduce escribía los resultados intermedios a disco después de cada fase (Map → disco → Reduce → disco). Spark mantiene los datos en memoria entre transformaciones, reduciendo la latencia de minutos a segundos para la misma tarea.

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional: Interbank (15 puntos)**

**a) Tecnología para cada sistema:**

| Sistema | Tecnología | Tipo | Justificación técnica |
|---------|-----------|------|----------------------|
| **Sistema 1 — Core bancario (5M transacciones/día, exactamente una vez)** | **CockroachDB o PostgreSQL con replicación** | NewSQL / SQL relacional | Las transferencias bancarias son la definición de ACID: si falla a mitad, el dinero no puede perderse ni duplicarse. CockroachDB añade escalabilidad horizontal sin sacrificar ACID usando Raft Consensus. PostgreSQL con streaming replication garantiza durabilidad. MongoDB o Cassandra están explícitamente excluidos porque no garantizan la atomicidad cross-document necesaria para débito+crédito simultáneo. |
| **Sistema 2 — App móvil (300ms, 800K logins simultáneos)** | **Redis (caché) + HBase (datos)** | Key-Value + Column-family NoSQL | Redis almacena en RAM el saldo y las últimas 5 transacciones del cliente (TTL de sesión), respondiendo en < 5ms. HBase almacena el perfil completo con Row Key = client_id para acceso aleatorio en tiempo real. La combinación Redis (hot cache) + HBase (warm store) permite manejar 800K logins simultáneos sin que cada login haga una query al core bancario. |
| **Sistema 3 — Recomendaciones (75TB, 3.5M clientes, re-entrenamiento semanal)** | **Delta Lake (HDFS/S3) + Apache Spark + MLlib** | Data Lake + Motor de procesamiento | 75TB de historial de 5 años no puede vivir en memoria ni en una BD relacional. Delta Lake sobre S3 almacena el historial con arquitectura Medallion. Spark procesa los 75TB en paralelo en el clúster semanal (job batch). Spark MLlib entrena el modelo de recomendación directamente sobre los datos distribuidos sin moverlos. |
| **Sistema 4 — Detección de redes de fraude (ciclos A→B→C→A en < 5 min)** | **Neo4j** | Graph database | Detectar ciclos A→B→C→A es un problema de traversal de grafos. En SQL, encontrar ciclos en una red de cuentas requiere JOINs recursivos extremadamente costosos que toman minutos con millones de cuentas. Neo4j representa cada cuenta como nodo y cada transferencia como arista, y puede encontrar ciclos de cualquier longitud en milisegundos con algoritmos de grafos nativos (Cypher: `MATCH path=(a)-[:TRANSFIERE*3]->(a) RETURN path`). |

**b) Teorema CAP para Sistemas 1 y 2:**

**Sistema 1 (Core bancario) → CP (Consistencia + Tolerancia a Particiones):**

Se sacrifica la Disponibilidad. Si hay una partición de red y los nodos no pueden sincronizarse, el sistema devuelve un error en lugar de procesar la transacción con datos potencialmente desactualizados.

*¿Qué pasaría si eligieras AP en lugar de CP?* Si el sistema prioriza disponibilidad sobre consistencia durante una partición de red, podría aprobar dos transferencias simultáneas que juntas superen el saldo del cliente (double spending). El cliente con S/100 podría hacer dos transferencias simultáneas de S/80 cada una desde nodos distintos, resultando en saldo negativo de -S/60. Esto es un fraude sistémico causado por el diseño incorrecto.

**Sistema 2 (App móvil) → AP (Disponibilidad + Tolerancia a Particiones):**

Se sacrifica la Consistencia estricta. El saldo mostrado puede tener algunos segundos de retraso respecto al último movimiento (consistencia eventual).

*¿Qué pasaría si eligieras CP en lugar de AP?* Con 800K logins simultáneos en días de pago, si el sistema prioriza consistencia, necesita coordinación entre todos los nodos antes de responder. Esto generaría cuellos de botella masivos y tiempos de respuesta de segundos o timeout para la mayoría de usuarios. Una app bancaria que tarda 10 segundos en cargar el saldo generaría pánico y llamadas al call center durante las quincenas.

**c) Argumento contra el CSV de 75TB en servidor local:**

Como Data Architect argumentaría contra la propuesta del equipo de ML por estas razones:

Primero, **un servidor local con 75TB de datos es un SPOF (Single Point of Failure)** — si ese servidor falla o el disco se corrompe, se pierden 5 años de historial irrecuperable. Los datos de 3.5M clientes son el activo más valioso del banco.

Segundo, **la transferencia semanal es ineficiente y costosa**: mover 75TB desde los sistemas del banco al servidor del equipo de ML tarda horas, consume ancho de banda de la red interna y requiere coordinación manual cada semana.

Tercero, **el modelo resultante tiene problemas de gobierno de datos**: el CSV en el servidor del equipo de ML está fuera del control de seguridad del banco — no hay auditoría, no hay control de acceso, ni cifrado verificable.

**Propuesta alternativa**: Los 75TB deben vivir en un Delta Lake centralizado (S3/HDFS) con control de acceso, cifrado y auditoría. El equipo de ML ejecuta Spark MLlib directamente sobre el Delta Lake sin mover los datos — el código va a los datos, no al revés (principio de localidad de datos de Hadoop). El clúster Spark del banco reemplaza al servidor local, con más capacidad de cómputo y sin dependencia de una sola máquina.

---

**21. Diseño: Sistema de seguimiento de paquetes Olva Courier (8 puntos)**

**Tipo de NoSQL elegido: Apache Cassandra**

Cassandra es la elección óptima por tres razones: (1) los eventos de paquetes son escrituras masivas y continuas (1.2B eventos/año), el punto fuerte de Cassandra; (2) el patrón de consulta es 100% predecible — siempre por número de guía; (3) los 2 años de historial (1.2B eventos) requieren distribución sin maestro para alta disponibilidad 24/7.

**Modelo de datos:**

```
TABLA: eventos_paquete

Partition Key: numero_guia        ← "¿Dónde está el paquete #PE123456?"
Clustering Key: timestamp DESC    ← Orden cronológico, más reciente primero

Columnas:
  numero_guia     TEXT
  timestamp       TIMESTAMP
  estado          TEXT        (RECIBIDO, EN_TRANSITO, EN_DISTRIBUCION, ENTREGADO)
  ubicacion       TEXT        (nombre de la agencia o zona)
  operador_id     TEXT        (empleado que registró el evento)
  latitud         DOUBLE      (coordenada GPS del evento)
  longitud        DOUBLE
  observaciones   TEXT        (campo libre opcional)
```

**Consulta para "¿dónde está el paquete #PE123456?":**

```sql
-- CQL (Cassandra Query Language)
SELECT estado, ubicacion, timestamp, latitud, longitud
FROM eventos_paquete
WHERE numero_guia = 'PE123456'
ORDER BY timestamp DESC
LIMIT 1;
```

Esta consulta responde en < 10ms porque la Partition Key dirige la consulta al nodo exacto que tiene esos datos, sin full table scan.

**¿Por qué es mejor que SQL con índices?**

Con 1.2B eventos en SQL, incluso con índice en `numero_guia`, la consulta compite con millones de escrituras simultáneas (todos los paquetes actualizándose en tiempo real) y el índice B-tree se fragmenta y degrada con escrituras masivas. En Cassandra, las escrituras son siempre `O(1)` — se añaden al final del log de eventos sin actualizar índices. La Partition Key garantiza que todos los eventos de un paquete estén en el mismo nodo, haciendo la lectura igualmente `O(1)`. A 1.2B registros, la ventaja es dramática.

---

**22. Pensamiento crítico: Caída de MongoDB Atlas 2 horas (7 puntos)**

**¿Qué componentes de la app de Claro Perú dejarían de funcionar?**

Todo lo que dependa de MongoDB dejaría de funcionar completamente: perfiles de usuario (no se puede ver el saldo ni el plan contratado), historial de consumo (datos de GB usados, llamadas del mes), configuraciones personalizadas (activación/desactivación de servicios), módulo de atención al cliente (historial de tickets). Si Claro usa MongoDB para todo, el 100% de la app quedaría inoperativa durante 2 horas en horario pico — probablemente afectando a millones de usuarios en simultáneo.

**Estrategias de resiliencia:**

1. **Multi-región en Atlas:** Configurar réplicas en al menos dos regiones geográficas (AWS São Paulo + AWS Virginia). Si una región cae, Atlas hace failover automático en segundos a la réplica secundaria.

2. **Caché con Redis:** Los datos más consultados (saldo, plan activo) se cachean en Redis con TTL de 5 minutos. Durante una caída de MongoDB, Redis sirve los datos cacheados — los usuarios ven datos con hasta 5 minutos de antigüedad pero la app sigue funcionando.

3. **Circuit Breaker pattern:** Si las consultas a MongoDB fallan consistentemente (3 intentos en 500ms), el sistema activa el "modo degradado" — muestra datos cacheados y deshabilita las funciones que requieren datos en tiempo real, en lugar de mostrar pantallas de error en blanco.

4. **Multi-cloud NoSQL:** Para datos críticos, replicar a DynamoDB (AWS) como respaldo. Si Atlas cae completamente, el tráfico se redirige automáticamente a DynamoDB.

**¿Múltiples proveedores o un proveedor con alta disponibilidad?**

Para una app de Claro con millones de usuarios, la respuesta es **un proveedor con alta disponibilidad configurada correctamente**, no múltiples proveedores. Operar dos sistemas de bases de datos diferentes (Atlas + DynamoDB por ejemplo) duplica la complejidad operacional, los costos y el riesgo de inconsistencias entre sistemas. MongoDB Atlas con configuración multi-región y réplicas activas puede garantizar 99.995% de disponibilidad — menos de 26 minutos de downtime al año. Eso es más que suficiente para la mayoría de casos.

**¿Qué SLA negociar con MongoDB Atlas?**

Para una app crítica como Claro Perú se debe negociar un **SLA de 99.99% de disponibilidad mensual** (< 4.4 minutos de downtime/mes), con: compensación económica automática si el SLA se incumple (créditos en factura), soporte 24/7 con tiempo de respuesta < 15 minutos para incidentes críticos, y garantía de RTO (Recovery Time Objective) de < 60 segundos en caso de failover. El SLA estándar de Atlas M0 gratuito no incluye ninguna garantía — se necesita al mínimo un plan M10 dedicado con SLA contractual.

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Estudiante: Ana Concepción Asto Arotinco*
