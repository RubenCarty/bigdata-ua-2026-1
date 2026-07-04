# Arquitectura Big Data Yape

## 1.1 Arquitectura

| Componente              | Tecnología             | Tipo             | Justificación                                                    |
| ----------------------- | ---------------------- | ---------------- | ---------------------------------------------------------------- |
| Core de pagos           | CockroachDB            | NewSQL           | Garantiza ACID y escala horizontalmente sin perder transacciones |
| Login activo            | Redis                  | Key-Value        | Maneja sesiones temporales rápidas con expiración automática     |
| Perfil comerciantes     | MongoDB                | NoSQL Documental | Cada comercio tiene atributos distintos y esquema flexible       |
| Historial transacciones | Databricks + Data Lake | Big Data         | Procesa grandes volúmenes de datos (18TB/año)                    |
| Detección fraude        | Neo4j                  | Graph Database   | Detecta relaciones sospechosas entre usuarios rápidamente        |
| Dashboard ejecutivo     | Spark + Power BI       | Analytics        | Permite análisis y visualización diaria                          |

## 1.2 CAP Theorem

* Core pagos → CP → sacrifica disponibilidad → prioriza consistencia financiera
* Últimas 50 transacciones → AP → sacrifica consistencia → acepta pequeños retrasos

## 1.3 NewSQL

a) Oracle escala verticalmente, CockroachDB escala horizontalmente en múltiples nodos.

b) MongoDB no es ideal para pagos porque no garantiza consistencia ACID fuerte como un sistema financiero requiere.

c) CockroachDB usa el algoritmo **Raft Consensus**.
