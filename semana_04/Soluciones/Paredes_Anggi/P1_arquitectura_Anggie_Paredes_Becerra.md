# P1 - Arquitectura Big Data para Yape

| Campo | Detalle |
|---|---|
| Estudiante | Anggie Paredes Becerra |
| Codigo | 2221891736 |
| Curso | Big Data |
| Evaluacion | Parcial - Semana 04 |
| Video | https://youtu.be/lZVBpmuDp3g |
| Repositorio | https://github.com/Anggie-28/yape-paredes-anggie.git |

## Uso de IA

Para el desarrollo de esta actividad se utilizo Claude IA  como herramienta de apoyo para ordenar las alternativas de arquitectura, contrastar tecnologias y mejorar la explicacion tecnica. El contenido fue ajustado al contexto de Yape, tomando en cuenta pagos digitales, volumen de transacciones, analitica de datos y deteccion de posibles fraudes.

---

## 1.1 Tabla de arquitectura Big Data de Yape

| Componente del sistema | Tecnologia elegida | Tipo BD/Herramienta | Justificacion para el caso Yape |
|---|---|---|---|
| Core de pagos (3.2M transacciones/dia, no puede perder dinero) | CockroachDB | NewSQL distribuida, ACID | El modulo principal de pagos requiere consistencia fuerte, transacciones ACID y tolerancia a fallos, porque cualquier error en un debito o credito afecta directamente dinero real. CockroachDB permite distribuir la carga y escalar horizontalmente sin renunciar al control transaccional, algo indispensable para operaciones financieras. |
| Sesiones de login activo (15M usuarios, expira en 30 min) | Redis Cluster | Key-value en memoria | Las sesiones de usuarios son informacion temporal que necesita respuestas de muy baja latencia y expiracion automatica. Redis Cluster es adecuado porque trabaja en memoria, soporta TTL y puede manejar una gran cantidad de claves activas sin requerir consultas complejas. |
| Perfil del comerciante (bodega, restaurante, taxi - atributos distintos) | MongoDB Atlas | Base documental NoSQL | Los perfiles de comercios no tienen todos la misma estructura: una bodega puede registrar categorias, un restaurante su carta y un taxi datos del vehiculo. MongoDB Atlas permite manejar estos documentos flexibles sin forzar un esquema rigido ni llenar una tabla relacional con campos vacios. |
| Historial de transacciones para analisis (18 TB/anio) | Delta Lake en Databricks sobre almacenamiento cloud | Data Lakehouse / Spark | El historial transaccional de gran volumen debe orientarse a analitica y procesamiento distribuido, no al uso como base operacional del core. Delta Lake permite trabajar con archivos Parquet, control de versiones, arquitectura Medallion y procesamiento escalable mediante Spark. |
| Red de deteccion de fraude (ciclo A->B->C->A en < 5 min) | Neo4j o TigerGraph | Base de datos de grafos | Los fraudes pueden identificarse mediante relaciones entre usuarios, cuentas, comercios y dispositivos. Una base de grafos facilita encontrar ciclos, caminos sospechosos y patrones de conexion con mayor eficiencia que una solucion basada en multiples joins relacionales. |
| Dashboard ejecutivo (top 10 distritos, actualizacion diaria) | Power BI conectado a Gold tables de Databricks | BI + tablas analiticas | La gerencia necesita informacion resumida y lista para la toma de decisiones, no transacciones crudas. Con tablas Gold en Databricks se pueden preparar indicadores por distrito, tipo de comercio o volumen, reduciendo tiempo de consulta y costo para reportes diarios en Power BI. |

---

## 1.2 Teorema CAP

| Componente | Combinacion CAP | Propiedad sacrificada | Justificacion del sacrificio |
|---|---|---|---|
| Core de pagos (debito/credito de saldos) | CP | Disponibilidad durante particiones de red | En el core de pagos es correcto priorizar consistencia y tolerancia a particiones. Si ocurre un problema de red, es preferible detener o rechazar temporalmente una operacion antes que registrar saldos incorrectos, duplicar dinero o descontar dos veces una misma transaccion. |
| Historial "mis ultimas 50 transacciones" | AP | Consistencia fuerte inmediata | Para el historial visible al usuario se puede aceptar consistencia eventual por un periodo breve. Esta informacion es principalmente de consulta y no modifica el saldo, por lo que resulta mas importante mantener el servicio disponible y rapido aunque una transaccion reciente demore unos segundos en aparecer. |

---

## 1.3 NewSQL

**a) Que limitacion de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?**

CockroachDB ayuda a superar la dificultad de escalar horizontalmente un sistema transaccional tradicional. En una solucion Oracle clasica, crecer en escrituras distribuidas puede depender de infraestructura vertical, configuraciones complejas de replicas o particionamiento dificil de administrar. En cambio, CockroachDB distribuye datos y transacciones entre varios nodos, permitiendo aumentar capacidad agregando servidores sin abandonar SQL ni las propiedades ACID.

**b) Por que MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque tambien escala horizontalmente?**

MongoDB es una buena opcion para informacion flexible, como perfiles, catalogos o documentos con estructuras variables. Sin embargo, el procesamiento central de pagos necesita controles financieros estrictos, consistencia fuerte, aislamiento transaccional, trazabilidad y reglas precisas para debitos y creditos. Aunque MongoDB permite transacciones, su enfoque principal no esta pensado para funcionar como libro mayor financiero central de una plataforma de pagos.

**c) Que mecanismo tecnico usa CockroachDB para mantener ACID en multiples nodos distribuidos?**

CockroachDB mantiene la consistencia entre nodos distribuidos mediante un protocolo de consenso basado en **Raft**.
