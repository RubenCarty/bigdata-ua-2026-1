## PARTE A — DISEÑO Y ARQUITECTURA (4 puntos)
### *Puedes usar IA generativa en esta sección — cita qué herramienta usaste*

---

### PREGUNTA 1 — Arquitectura Big Data de Yape (4 puntos)

**1.1 (2 pts) — Tabla de arquitectura:**

Diseña la arquitectura completa de datos para Yape. Para cada componente del sistema, elige la tecnología adecuada y justifica. Puedes usar IA para explorar opciones, pero la justificación debe ser tuya.

| Componente del sistema | Tecnología elegida | Tipo BD/Herramienta | Por qué esta tecnología para Yape (2 líneas) |
|------------------------|-------------------|--------------------|--------------------------------------------|
| Core de pagos (3.2M transacciones/día, no puede perder dinero) | CockroachDB | NewSQL | Garantiza transacciones ACID estrictas para no perder dinero y escala de forma horizontal automáticamente. |
| Sesiones de login activo (15M usuarios, expira en 30 min) | Redis | NoSQL (Clave-Valor) | Guarda los datos en memoria RAM ofreciendo respuestas en milisegundos para soportar millones de accesos. |
| Perfil del comerciante (bodega, restaurante, taxi — atributos distintos) | MongoDB | NoSQL (Documental) | Permite un esquema flexible en formato JSON; ideal porque una bodega y un taxi tienen datos totalmente diferentes. |
| Historial de transacciones para análisis (18 TB/año) | Databricks / Spark | Lakehouse / Big Data | Procesa terabytes de datos de forma distribuida para analítica avanzada usando almacenamiento masivo y económico. |
| Red de detección de fraude (ciclo A→B→C→A en < 5 min) | Neo4j | NoSQL (Grafos) | Diseñada para recorrer relaciones complejas y detectar patrones circulares de lavado de dinero en tiempo real. |
| Dashboard ejecutivo (top 10 distritos, actualización diaria) | Power BI / Matplotlib | BI / Visualización | Permite conectar los datos limpios de la capa Gold y transformarlos en gráficos interactivos para los directivos. |

---

**1.2 (1 pt) — Teorema CAP:**

Para los siguientes 2 componentes de Yape, indica la combinación CAP correcta (CP, AP o CA) y explica qué propiedad sacrifica y por qué ese sacrificio es aceptable o inaceptable:

| *Componente* | *Combinación CAP* | *Propiedad sacrificada* | *¿Por qué ese sacrificio es correcto o incorrecto para este caso?* |
| ----- | ----- | ----- | ----- |
| Core de pagos (débito/crédito de saldos) | CP | Disponibilidad | Es correcto. En transacciones de dinero, la Consistencia es prioritaria. Si hay una falla de red, es preferible bloquear temporalmente el sistema antes que permitir saldos erróneos o duplicados. |
| Historial "mis últimas 50 transacciones" | AP | Consistencia estricta | Es correcto. Para el usuario es más importante que la app responda rápido y muestre datos (Disponibilidad). Una consistencia eventual es aceptable aquí; no importa si el historial tarda unos minutos en actualizarse. |

---

**1.3 (1 pt) — NewSQL:**

El equipo de Yape evalúa migrar el core de pagos a **CockroachDB** (NewSQL). Responde:

* **a) ¿Qué limitación de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?:** Oracle escala principalmente de forma *vertical* (requiere un servidor más grande, costoso y genera un punto único de falla). CockroachDB resuelve esto escalando de forma *horizontal* (permite añadir nodos de servidores estándar en la nube de manera ilimitada para soportar el crecimiento masivo de usuarios sin detener el sistema).

* **b) ¿Por qué MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque también escala horizontalmente?:** Porque el procesamiento de pagos requiere transacciones financieras con consistencia estricta en múltiples tablas o nodos distribuidos. Aunque MongoDB maneja transacciones, no fue diseñado nativamente desde su arquitectura para garantizar el cumplimiento estricta de las propiedades ACID a escala global distribuida con el nivel de seguridad financiera que ofrece un motor NewSQL.

* **c) ¿Qué mecanismo técnico usa CockroachDB para mantener ACID en múltiples nodos distribuidos?:** Usa el protocolo de consenso **Raft** (para la replicación de datos y consistencia entre los nodos).