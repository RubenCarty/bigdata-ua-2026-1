# S3 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | LINDO BARRIENTOS JHONN VIQUIER |
| **Código** | 2221896680 |
| **Sección** | 06 |
| **Fecha** | 20/06/2026 |
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
**b) El JobTracker mezclaba la gestión de recursos del clúster con la coordinación de jobs, convirtiéndose en cuello de botella y punto único de fallo[x]**    
c) El JobTracker solo podía gestionar un job MapReduce a la vez en todo el clúster  
d) El JobTracker no tenía interfaz gráfica para monitorear el estado de los nodos  

---

**2.** Apache Hive traduce las consultas HiveQL en ¿qué tipo de trabajos distribuidos para ejecutarlas sobre HDFS?

a) Consultas SQL directas que corren en tiempo real sobre los DataNodes  
b) Jobs de Python que se distribuyen entre los DataNodes vía SSH  
**c) Jobs MapReduce (o Tez/Spark en versiones modernas) que procesan los archivos de HDFS en paralelo[x]**    
d) Procedimientos almacenados en Java que se ejecutan en el NameNode  

---

**3.** ¿Qué diferencia fundamental existe entre Apache Hive y Apache Impala en cuanto a su arquitectura de ejecución de consultas?

a) Hive usa SQL estándar e Impala usa un lenguaje de scripting propio llamado Pig Latin  
**b) Hive compila las consultas en jobs MapReduce (alta latencia); Impala ejecuta SQL directamente en HDFS sin MapReduce (baja latencia, segundos)[x]**    
c) Hive solo funciona con datos estructurados, mientras Impala soporta JSON y XML  
d) Hive es de pago (Cloudera) e Impala es la versión gratuita open source  

---

**4.** Apache Ambari fue diseñado principalmente para:

a) Almacenar datos no estructurados de forma distribuida en el ecosistema Hadoop  
b) Ejecutar consultas SQL interactivas sobre archivos en HDFS sin usar MapReduce  
**c) Gestionar, monitorear e instalar componentes del ecosistema Hadoop desde una interfaz web centralizada[x]**    
d) Transferir datos de bases de datos relacionales a HDFS mediante conexiones JDBC  

---

**5.** Según el Teorema CAP (Brewer, 2000), un sistema distribuido NO puede garantizar simultáneamente las tres propiedades. Si una empresa de telecomunicaciones necesita que el sistema de facturación nunca muestre montos incorrectos (aunque el sistema esté temporalmente no disponible), ¿qué combinación CAP debe elegir?

a) AP — Disponibilidad y Tolerancia a Particiones  
b) CA — Consistencia y Disponibilidad  
**c) CP — Consistencia y Tolerancia a Particiones[x]**    
d) CAP — Las tres simultáneamente mediante replicación síncrona  

---

**6.** ¿Cuál es la diferencia entre el modelo ACID y el modelo BASE en bases de datos?

a) ACID usa SQL y BASE usa Python; son lenguajes de consulta distintos  
**b) ACID garantiza consistencia estricta en transacciones (apropiado para bancos); BASE acepta consistencia eventual a favor de alta disponibilidad (apropiado para redes sociales)[x]**    
c) ACID solo funciona en bases de datos locales; BASE solo funciona en bases de datos distribuidas en la nube  
d) ACID es el modelo de NoSQL y BASE es el modelo relacional tradicional  

---

**7.** Una empresa de streaming de música necesita almacenar el perfil de 50 millones de usuarios donde cada usuario puede tener atributos completamente diferentes (algunos tienen listas de reproducción, otros favoritos, otros historial de podcasts, con esquemas variables). ¿Qué tipo de base de datos NoSQL es más adecuada?

a) Key-Value (Redis) — porque permite acceso ultrarápido por clave de usuario  
**b) Document (MongoDB) — porque cada documento puede tener estructura diferente sin esquema fijo[x]**    
c) Column-family (Cassandra) — porque está optimizada para escrituras masivas en tiempo real  
d) Graph (Neo4j) — porque permite modelar las relaciones entre usuarios y canciones  

---

**8.** ¿Cuál es la principal ventaja de Apache Cassandra frente a MongoDB para almacenar el historial de llamadas de una operadora con 2,000 millones de registros al año?

a) Cassandra tiene una interfaz SQL más intuitiva que MongoDB para analistas de negocio  
b) Cassandra permite esquemas más flexibles que MongoDB para datos con atributos variables  
**c) Cassandra está optimizada para escrituras masivas y continuas con acceso predecible por partition key + timestamp, sin punto único de fallo[x]**    
d) Cassandra soporta transacciones ACID completas, mientras MongoDB solo tiene consistencia eventual  

---

**9.** Sqoop es una herramienta del ecosistema Hadoop diseñada para:

a) Monitorear la salud de los DataNodes y alertar cuando alguno falla  
b) Ejecutar consultas SQL interactivas sobre datos almacenados en HDFS  
**c) Transferir datos en batch entre bases de datos relacionales (Oracle, MySQL) y HDFS en ambas direcciones[x]**    
d) Gestionar la seguridad y autenticación de usuarios en el clúster Hadoop  

---

**10.** Una startup peruana lanza una app de redes sociales. Al inicio tienen 10,000 usuarios. Proyectan 5 millones en 12 meses. El perfil de cada usuario incluye fotos, listas de amigos, publicaciones con diferentes formatos (texto, imagen, video, encuesta). ¿Qué argumento técnico justifica usar MongoDB en lugar de PostgreSQL desde el inicio?

a) MongoDB es más rápido en todas las operaciones, incluyendo transacciones financieras, sin importar el volumen  
**b) MongoDB permite escalar horizontalmente con sharding automático y soporta esquemas flexibles que se adaptan a los distintos tipos de contenido sin costosas migraciones de esquema[x]**    
c) PostgreSQL no soporta datos de tipo JSON, por lo que no puede almacenar publicaciones de redes sociales  
d) MongoDB incluye un motor de búsqueda de texto completo que PostgreSQL no tiene en ninguna versión  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts c/u)

**11.** En la arquitectura YARN, el componente **ResourceManager** gestiona los recursos del clúster (CPU, RAM) a nivel global, mientras que el **ApplicationMaster** coordina la ejecución de cada aplicación individual en los nodos del clúster.

**12.** El Teorema CAP establece que un sistema distribuido solo puede garantizar dos de tres propiedades simultáneamente: **Consistencia** (todos los nodos ven los mismos datos), **Disponibilidad** (el sistema siempre responde), y Tolerancia a Particiones (el sistema funciona aunque la red falle).

**13.** En MongoDB, los datos se organizan en **colecciones (collections)** (equivalente a una tabla SQL), que contienen **documentos (documents)** (equivalente a filas) en formato JSON/BSON, donde cada uno puede tener una estructura diferente.

**14.** Apache **Pig** traduce un lenguaje de scripting llamado "Pig Latin" en jobs MapReduce, mientras que Apache **Hive** traduce consultas en un dialecto SQL propio (HiveQL) en jobs MapReduce o Spark.

**15.** La herramienta **Sqoop** (SQL-to-Hadoop) permite importar datos de una base de datos MySQL a HDFS de forma paralela usando múltiples conexiones JDBC simultáneas.

---

### B2. Relacionar columnas (10 puntos | 1 pt c/par correcto)

Relaciona cada tecnología/concepto (columna A) con su descripción correcta (columna B):

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | Redis |D| A | Motor SQL interactivo de Cloudera que ejecuta consultas directamente sobre HDFS sin MapReduce |
| 2 | Apache Cassandra |E| B | Base de datos de grafos optimizada para navegar relaciones complejas en milisegundos |
| 3 | Impala |A| C | Herramienta de gestión de clúster Hadoop con interfaz web (instala, monitorea, configura servicios) |
| 4 | Neo4j |B| D | Base de datos Key-Value en memoria con latencia < 1ms, usada para caché de sesiones |
| 5 | Ambari |C| E | Base de datos columnar distribuida sin maestro (ring), optimizada para escrituras masivas |
| 6 | Dremel |F| F | Tecnología de Google que inspira los formatos de almacenamiento columnar y BigQuery |
| 7 | Apache Drill |G| G | Motor SQL schema-free que consulta HDFS, MongoDB, S3 y otros sin esquema previo |
| 8 | MongoDB |H| H | Base de datos NoSQL documental con esquema flexible (BSON/JSON), más usada mundialmente |
| 9 | Tez |I| I | Framework de procesamiento DAG que reemplaza MapReduce como motor de ejecución de Hive |
| 10 | Flume |J| J | Herramienta de ingesta de logs/eventos en streaming hacia HDFS o Kafka |

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

<b>Recomiendo una base documental (MongoDB). Dos razones técnicas relacionadas al caso:

1. Esquema flexible: cada enfermedad tiene campos distintos (dengue → serotipos, COVID → variante, hepatitis → cronología de vacunas). Una base documental permite que cada reporte tenga su propia estructura sin columnas vacías ni migraciones de esquema, algo imposible de manejar limpiamente en SQL.
2. Escalado horizontal: con 8,000 establecimientos reportando a nivel nacional, MongoDB permite sharding para distribuir la carga y crecer agregando nodos.</b>

b) ¿Qué componente del ecosistema Hadoop usarías para las consultas analíticas del dashboard? ¿Hive, Impala/Spark SQL, o HBase? Justifica.

**Para el dashboard que debe responder en menos de 2 segundos, usaría Impala o Spark SQL (no Hive). Hive compila a MapReduce y tiene alta latencia (minutos), inservible para un dashboard interactivo. Impala/Spark SQL ejecutan consultas en segundos. Para la consulta puntual "casos de dengue en Loreto semana 23", también podría apoyarse en los índices de la propia MongoDB. HBase no es ideal aquí porque las consultas son analíticas con filtros múltiples, no solo búsquedas por Row Key.**

---

**17. (8 puntos)** Compara el paradigma ACID de las bases de datos relacionales con el paradigma BASE de las bases de datos NoSQL. Luego responde:

a) ¿En qué tipo de aplicaciones es OBLIGATORIO usar ACID y por qué?

**En aplicaciones donde un dato incorrecto causa daño real e irreversible: sistemas bancarios y financieros, facturación, reservas de vuelos, control de inventario con stock crítico. Una transferencia bancaria debe ser atómica: o se completa entera o no se hace; no puede quedar el dinero descontado de una cuenta sin acreditarse en la otra. ACID garantiza esa integridad.**
  
b) ¿En qué tipo de aplicaciones es ACEPTABLE y BENEFICIOSO usar BASE y por qué?

**En aplicaciones donde la disponibilidad y la escala importan más que la consistencia inmediata: redes sociales, contadores de "me gusta", historial de navegación, catálogos de productos, sistemas de recomendación. Si tu publicación tarda 2 segundos en aparecerle a todos tus contactos (consistencia eventual), no pasa nada grave, y a cambio el sistema nunca se cae aunque tenga millones de usuarios.**
  
c) ¿Existe algún sistema de bases de datos que combine ambos paradigmas? ¿Cuál es su nombre y cómo lo logra?

**Sí, las bases de datos NewSQL, como Google Spanner (y CockroachDB). Logran combinar la consistencia fuerte tipo ACID de las relacionales con el escalado horizontal distribuido típico de NoSQL. Spanner lo consigue usando relojes sincronizados de altísima precisión (TrueTime, con GPS y relojes atómicos) para ordenar las transacciones globalmente y mantener consistencia a escala mundial.**

---

**18. (6 puntos) — Mini caso de análisis:**

*La plataforma de e-commerce "CompraYa Perú" tiene estos componentes en su sistema:*
- *Catálogo: 2 millones de productos con atributos variables (electrónicos tienen voltaje, ropa tiene talla, alimentos tienen fecha de vencimiento)*
- *Carrito de compras: almacena el carrito activo de 200K usuarios simultáneos (expira en 2 horas si no compran)*
- *Órdenes de compra: cada orden debe debitarse exactamente una vez de la cuenta del usuario (si el pago falla, no debe cobrarse)*
- *Historial de navegación: registra cada producto visto por cada usuario (50M eventos/día para recomendaciones)*

a) Para cada componente, identifica el tipo de base de datos más adecuado (SQL, MongoDB, Redis, Cassandra) y justifica brevemente cada elección.

| Componente | Base de datos | Justificación |
| :--- | :--- | :--- |
| Catálogo (2M productos, atributos variables) | <b>MongoDB (documental)</b> | Cada categoría tiene atributos distintos (voltaje, talla, vencimiento); el esquema flexible evita columnas NULL |
| Carrito (200K usuarios, expira en 2h) | <b>Redis (key-value en memoria)</b> | Acceso ultrarrápido por clave de usuario y soporte nativo de expiración (TTL) para vaciar el carrito tras 2 horas |
| Órdenes de compra (débito exacto una vez) | <b>SQL relacional (ACID)</b> | El pago exige atomicidad y consistencia estricta: cobrar exactamente una vez, sin duplicar ni perder dinero |
| Historial de navegación (50M eventos/día) | Cassandra (columnar) |Escritura masiva continua, sin punto único de fallo, optimizada para grandes volúmenes de eventos|

b) ¿Es correcto usar UNA SOLA base de datos para todo el sistema? Argumenta si la arquitectura polilíngüe (polyglot persistence) es mejor o peor aquí.

**No es correcto usar una sola base de datos. Aquí la persistencia políglota (polyglot persistence) es claramente mejor, porque cada componente tiene necesidades opuestas: las órdenes exigen ACID, el carrito exige velocidad y expiración, el catálogo exige flexibilidad de esquema, y el historial exige escritura masiva. Ninguna base de datos es óptima para los cuatro casos. Usar la herramienta adecuada para cada necesidad da mejor rendimiento, escala y confiabilidad que forzar una sola tecnología para todo.**

---

**19. (8 puntos)** Explica por qué Apache Pig (2008) fue un paso importante en la evolución del ecosistema Hadoop, y luego explica por qué la industria lo abandonó en favor de Apache Spark (2014). ¿Qué característica de Pig sobrevivió en Spark? ¿Qué limitación eliminó Spark?

<b>Antes de Pig, escribir un job MapReduce exigía mucho código Java de bajo nivel, incluso para tareas simples. Pig introdujo Pig Latin, un lenguaje de scripting de alto nivel que permitía expresar transformaciones de datos (filtrar, agrupar, unir) en pocas líneas, que luego se traducían automáticamente a MapReduce. Democratizó el procesamiento de datos al hacerlo accesible sin programar MapReduce manualmente.

La gran limitación de Pig era que, por debajo, seguía generando jobs MapReduce que escribían los resultados intermedios en disco entre cada paso, lo que lo hacía lento. Spark (2014) procesa en memoria (RAM), siendo hasta 100x más rápido, y ofrece una API más rica (SQL, streaming, machine learning, grafos) en un solo motor.

La idea de abstraer el procesamiento en transformaciones de alto nivel encadenables (un flujo de operaciones sobre los datos), que en Spark se materializa en las transformaciones de RDD/DataFrame.</b>

Eliminó la escritura constante de resultados intermedios a disco entre fases, gracias al procesamiento en memoria y la evaluación perezosa (lazy evaluation) con su DAG de ejecución optimizado.

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


| Sistema | Tecnología | Tipo | Justificación técnica |
| :--- | :--- | :--- | :--- |
| 1. Core bancario (transacciones) | PostgreSQL / Oracle (relacional ACID) | SQL | Las transacciones exigen atomicidad y consistencia estricta: cada transferencia se procesa exactamente una vez; si falla a mitad, se hace rollback completo. ACID es obligatorio para no perder ni duplicar dinero |
| 2. App móvil (perfil, saldo, ofertas) | Redis (caché) + base de lectura | NoSQL key-value | El requisito es 300ms con 800K logins simultáneos. Redis cachea en memoria el saldo y últimas transacciones para respuesta inmediata, absorbiendo los picos de quincena sin golpear el core bancario |
| 3. Motor de recomendaciones (75TB, 5 años) | Data Lake (HDFS/S3) + Spark | Big Data batch | El re-entrenamiento semanal sobre 75TB exige procesamiento distribuido en paralelo. Spark sobre un Data Lake escala a ese volumen; ninguna BD transaccional lo soporta |
| 4. Detección de redes de fraude (ciclos A&rarr;B&rarr;C&rarr;A) | Neo4j (base de grafos) | NoSQL grafo | Detectar ciclos de transacciones es un problema de relaciones entre nodos. Las bases de grafos navegan estas conexiones en milisegundos, algo que en SQL requeriría JOINs recursivos costosísimos |

b) Aplica el Teorema CAP a los Sistemas 1 y 2 específicamente. ¿Cuál combinación CAP debe tener cada uno y por qué? Da un ejemplo de qué pasaría si eligieras la combinación incorrecta. (4 puntos)


**1. Sistema 1 (Core bancario) → CP (Consistencia + Tolerancia a Particiones). El saldo debe ser siempre correcto; si hay un problema de red, es preferible rechazar la operación antes que mostrar o mover un monto incorrecto. Si eligieras AP por error: dos cajeros podrían leer el mismo saldo simultáneamente y permitir dos retiros del mismo dinero, generando sobregiros y pérdida para el banco.**

**2. Sistema 2 (App móvil) → AP (Disponibilidad + Tolerancia a Particiones). Cuando el cliente abre la app para ver su saldo y ofertas, lo crítico es que la app siempre responda rápido (300ms), aunque el saldo mostrado tenga unos segundos de retraso (consistencia eventual). Si eligieras CP por error: en días de pago con 800K logins, la app se volvería lenta o no cargaría mientras espera la consistencia perfecta, arruinando la experiencia justo en el pico de uso.**

c) En el Sistema 3 (recomendaciones), el equipo de ML propone usar un archivo CSV de 75 TB almacenado en el servidor local del equipo para entrenar el modelo semanalmente. ¿Qué argumentas tú como Data Architect en contra de esta propuesta? ¿Qué propones en su lugar? (3 puntos)

**Como Data Architect argumentaría en contra por tres motivos: (1) No escala — un solo servidor no tiene capacidad ni memoria para procesar 75TB; el entrenamiento tardaría días o fallaría. (2) Punto único de fallo — si ese servidor se daña, se pierden los datos y se detiene todo el sistema de recomendaciones. (3) Sin procesamiento paralelo — un archivo plano local no aprovecha la computación distribuida.**

**En su lugar propongo: almacenar los datos en un Data Lake distribuido (HDFS o Amazon S3) en formato columnar Parquet (mucho más comprimido y eficiente que CSV), y procesarlos con Apache Spark en un clúster. Así el entrenamiento se paraleliza entre nodos, escala con el crecimiento del banco y mantiene tolerancia a fallos con replicación.**

---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías una base de datos NoSQL para el sistema de seguimiento de paquetes de Olva Courier Perú? El sistema debe: (a) registrar cada evento de cada paquete (recepción, en tránsito, en distribución, entregado) en tiempo real; (b) permitir al cliente consultar 'dónde está mi paquete' por número de guía en menos de 100ms; (c) guardar historial de los últimos 2 años (150M paquetes × 8 eventos = 1.2B eventos)."*

Diseña:
- El tipo de NoSQL elegido y justificación
- El modelo de datos (cómo organizarías los documentos/columnas/claves)
- La consulta que usarías para responder "¿dónde está el paquete #PE123456?"
- Por qué esta solución es mejor que usar una tabla SQL con índices

**Tipo de NoSQL elegido y justificación:
Elegiría una base de datos columnar tipo Cassandra, porque el caso combina (a) escritura masiva y continua de eventos en tiempo real (cada paquete genera múltiples eventos), (b) lectura ultrarrápida por número de guía (partition key), y (c) un volumen enorme de 1,200 millones de eventos en 2 años, donde Cassandra brilla por su escalado horizontal sin punto único de fallo. (Una base documental como MongoDB también sería válida si se prioriza flexibilidad sobre volumen de escritura.)**

**Modelo de datos:
Organizaría la tabla con el número de guía como partition key y el timestamp del evento como clustering key, de modo que todos los eventos de un mismo paquete queden físicamente juntos y ordenados por fecha:**

Tabla: seguimiento_paquetes
  PARTITION KEY: numero_guia      (ej. "PE123456")
  CLUSTERING KEY: timestamp_evento (ordena los eventos del paquete)
  Columnas: estado, ubicacion, sede, descripcion

Ejemplo de un paquete:
  PE123456 | 2026-06-18 08:00 | RECEPCION    | Lima Centro
  PE123456 | 2026-06-18 14:30 | EN_TRANSITO  | Arequipa
  PE123456 | 2026-06-19 09:15 | EN_DISTRIBUCION | Arequipa Cerro Colorado
  PE123456 | 2026-06-19 11:40 | ENTREGADO    | Cliente final

**Consulta para "¿dónde está el paquete #PE123456?":**

SELECT estado, ubicacion, timestamp_evento
FROM seguimiento_paquetes
WHERE numero_guia = 'PE123456'
ORDER BY timestamp_evento DESC
LIMIT 1;

**Esto devuelve el último evento del paquete en menos de 100ms, porque la búsqueda va directo a la partición de esa guía.**

**Por qué es mejor que una tabla SQL con índices:
Con 1,200 millones de filas, una tabla SQL con índices se vuelve lenta: el índice crece tanto que las búsquedas y, sobre todo, las escrituras continuas (actualizar el índice en cada evento) se degradan. Cassandra distribuye los datos por partition key entre muchos nodos, así que tanto la escritura masiva como la lectura por guía se mantienen rápidas sin importar el volumen total, y sin punto único de fallo.**

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si MongoDB Atlas (la plataforma cloud de MongoDB) tiene una caída de servicio de 2 horas durante el horario pico de tu aplicación? ¿Qué riesgos concretos implica depender de una sola base de datos NoSQL en la nube para una aplicación crítica como la app de Claro Perú?"*

Analiza:
- ¿Qué componentes de la app dejarían de funcionar?

**Si toda la app depende de una sola instancia de MongoDB Atlas, una caída de 2 horas en horario pico tumbaría las funciones que leen/escriben en esa base: consulta de saldo y plan, historial de consumo, recarga de datos, registro de tickets de soporte y perfil del cliente. La app quedaría prácticamente inutilizable para millones de usuarios**

- ¿Qué estrategias de resiliencia implementarías para mitigar el riesgo?
<b>
- Réplicas multi-región: desplegar el cluster con réplicas en varias zonas/regiones, de modo que si una cae, otra toma el relevo (failover automático).
- Caché intermedia (Redis): servir datos de lectura frecuentes (saldo, plan) desde una caché, para que la app siga mostrando información aunque la base principal esté caída.
- Degradación elegante: diseñar la app para que, ante la caída, muestre datos cacheados y deshabilite solo las funciones críticas en vez de fallar por completo.
Backups y plan de recuperación (DR) probados periódicamente.
</b>
- ¿Es mejor tener múltiples proveedores de NoSQL o un solo proveedor con alta disponibilidad configurada?

**Para la mayoría de los casos, un solo proveedor con alta disponibilidad bien configurada (réplicas multi-región, failover automático) es más práctico y mantenible que la complejidad de orquestar múltiples proveedores NoSQL distintos (que multiplica costos, complejidad de sincronización y errores). La estrategia multi-proveedor solo se justifica para sistemas de criticidad extrema. Lo esencial es no depender de un único nodo o región.**

- ¿Qué nivel de SLA (Service Level Agreement) deberías negociar con MongoDB Atlas?

**Para una app crítica como la de Claro, negociaría un SLA de al menos 99.95% de disponibilidad (los clusters dedicados de Atlas suelen ofrecer este nivel), idealmente apuntando a 99.99% ("cuatro nueves", ~52 minutos de inactividad al año). El SLA debe incluir además compensaciones (créditos) por incumplimiento y tiempos de respuesta de soporte garantizados.**

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
