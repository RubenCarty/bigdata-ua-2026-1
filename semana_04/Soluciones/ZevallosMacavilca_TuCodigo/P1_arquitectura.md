Parte A — Diseño y Arquitectura
Estudiante: Ian Jesus Zevallos Macavilca  
Curso: Big Data DD283 | Ciclo VIII | Semestre 2026-1  
Docente: Mg. Rubén Quispe Llacctarimay  
IA utilizada: Claude (Anthropic)
---
P1.1 — Tabla de arquitectura Big Data de Yape (2 pts)
Componente del sistema	Tecnología elegida	Tipo BD/Herramienta	Por qué esta tecnología para Yape
Core de pagos (3.2M transacciones/día, no puede perder dinero)	CockroachDB	NewSQL / Relacional distribuida	Garantiza ACID completo en múltiples nodos, asegurando que ningún débito o crédito se pierda. Escala horizontalmente sin sacrificar consistencia, crítico cuando hay dinero en juego.
Sesiones de login activo (15M usuarios, expira en 30 min)	Redis	Base de datos en memoria (Key-Value)	Lecturas y escrituras en microsegundos gracias al almacenamiento en RAM. El TTL (time-to-live) nativo de Redis elimina sesiones expiradas automáticamente, ideal para los 30 min de Yape.
Perfil del comerciante (bodega, restaurante, taxi — atributos distintos)	MongoDB	NoSQL — Documental	Esquema flexible permite que cada tipo de comercio tenga campos distintos sin columnas NULL. Una bodega tiene "categorías" y un taxi tiene "placa", sin desperdiciar estructura.
Historial de transacciones para análisis (18 TB/año)	Apache Parquet + Databricks	Data Lakehouse / Almacén columnar	Parquet comprime y organiza datos por columna, reduciendo I/O en consultas analíticas sobre 18 TB. Databricks permite queries distribuidos en Spark sin mover los datos a otro sistema.
Red de detección de fraude (ciclo A→B→C→A en < 5 min)	Neo4j	NoSQL — Grafos	Detectar ciclos en redes de pagos es un problema de grafo. Neo4j recorre relaciones en tiempo real con Cypher, algo que SQL tardaría múltiples JOINs recursivos en resolver.
Dashboard ejecutivo (top 10 distritos, actualización diaria)	Apache Hive / BigQuery	Data Warehouse columnar	Consolida métricas pre-agregadas diariamente para consultas rápidas del dashboard. No necesita tiempo real, por lo que un batch diario en DWH es más económico y eficiente que una BD OLTP.
---
P1.2 — Teorema CAP (1 pt)
Componente	Combinación CAP	Propiedad sacrificada	¿Por qué ese sacrificio es correcto o incorrecto para este caso?
Core de pagos (débito/crédito de saldos)	CP	Disponibilidad (A)	Si hay una partición de red, el sistema prefiere no responder antes que dar una respuesta incorrecta. Para pagos esto es correcto: es mejor que Yape muestre "servicio no disponible" a que un usuario cobre dos veces o pierda dinero por inconsistencia. El sacrificio de disponibilidad es aceptable porque la integridad financiera no es negociable.
Historial "mis últimas 50 transacciones"	AP	Consistencia (C)	El usuario puede ver un historial que tarda segundos en actualizarse (consistencia eventual). Este sacrificio es aceptable: si la última transacción no aparece por 2-3 segundos, no hay daño económico. La disponibilidad importa más para que millones de usuarios consulten su historial sin interrupciones.
---
P1.3 — NewSQL: CockroachDB (1 pt)
a) ¿Qué limitación de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?
Oracle escala principalmente de forma vertical (más CPU/RAM en un solo servidor), lo que tiene un límite físico y un costo exponencial. CockroachDB escala horizontalmente: se agregan más nodos al clúster sin downtime ni reescritura de la aplicación. Al pasar de 15M a 50M usuarios, Yape simplemente incorpora nuevos nodos, distribuyendo la carga de manera automática.
---
b) ¿Por qué MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque también escala horizontalmente?
MongoDB es una base de datos documental que no garantiza ACID completo en transacciones distribuidas multi-documento de la misma forma que una BD relacional. Para pagos, si la red falla a mitad de un débito, MongoDB podría dejar el saldo en estado inconsistente. CockroachDB, en cambio, garantiza ACID en múltiples nodos: o la transacción completa ocurre, o no ocurre. MongoDB es ideal para datos flexibles (como perfiles de comerciantes), pero no para operaciones financieras donde la atomicidad es crítica.
---
c) ¿Qué mecanismo técnico usa CockroachDB para mantener ACID en múltiples nodos distribuidos?
Consensus de Raft — un protocolo de consenso distribuido donde la mayoría de los nodos deben acordar una escritura antes de confirmarla. Esto garantiza que aunque un nodo falle, la transacción se confirma solo si la mayoría la aceptó, manteniendo consistencia sin un único punto de falla.
