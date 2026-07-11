---
**UNIVERSIDAD AUTÓNOMA DEL PERÚ**
**FACULTAD DE INGENIERÍA Y ARQUITECTURA**
**ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS COMPUTACIONALES**

---

# EVALUACIÓN PARCIAL — BIG DATA
## Código: DD283 | Ciclo VIII | Semestre 2026-1

| Campo | Detalle |
|-------|---------|
| **Apellidos y Nombres** | Lindo Barrientos, Jhonn Viequier |
| **Docente** | Mg. Rubén Quispe Llacctarimay |
| **Modalidad** | Implementación + Video |

---

## ENLACES DE ENTREGA

| Recurso | Enlace |
|---------|--------|
| **Repositorio personal (implementación completa)** | `https://github.com/jlindo-cloud/yape-lindo-jhonn.git` |
| **Video de sustentación (5-8 min)** | `https://drive.google.com/file/d/13eRXoVqyRF0ZNR-XWrbAEL1Yq2Mgvgro/view?usp=sharing` |

> El repositorio personal contiene toda la implementación: Parte B (Databricks), Parte C (MongoDB Atlas) y Parte D (Docker), junto con los screenshots de evidencia.

---

# PARTE A — DISEÑO Y ARQUITECTURA (4 puntos)

**Herramienta de IA usada:** Claude (Anthropic) como asistente para explorar opciones de arquitectura. Las justificaciones y adaptaciones al caso Yape son propias.

---

## PREGUNTA 1 — Arquitectura Big Data de Yape

### 1.1 — Tabla de arquitectura

| Componente del sistema | Tecnología elegida | Tipo BD/Herramienta | Por qué esta tecnología para Yape |
|------------------------|-------------------|--------------------|--------------------------------------------|
| Core de pagos (3.2M transacciones/día, no puede perder dinero) | PostgreSQL / Oracle / CockroachDB | SQL relacional (ACID) | Las transferencias exigen atomicidad: cada pago se procesa exactamente una vez o se revierte completo. ACID garantiza que el dinero nunca se pierda ni duplique |
| Sesiones de login activo (15M usuarios, expira en 30 min) | Redis | NoSQL Key-Value (en memoria) | Acceso por clave en menos de 1ms para validar sesión en cada request, y expiración automática (TTL) que borra la sesión a los 30 min sin proceso adicional |
| Perfil del comerciante (bodega, restaurante, taxi — atributos distintos) | MongoDB | NoSQL Documental | Cada tipo de comercio tiene campos propios (la cevichería tiene carta, el taxi tiene placa); el esquema flexible evita las columnas NULL masivas de SQL |
| Historial de transacciones para análisis (18 TB/año) | Data Lake (S3/HDFS) + Spark | Big Data / procesamiento distribuido | 18 TB/año superan cualquier BD transaccional; un Data Lake con Parquet + Spark procesa ese volumen en paralelo y a bajo costo de almacenamiento |
| Red de detección de fraude (ciclo A→B→C→A en < 5 min) | Neo4j | NoSQL de Grafos | Detectar ciclos de transacciones es un problema de relaciones; las bases de grafos recorren conexiones en milisegundos, algo que en SQL requeriría JOINs recursivos costosísimos |
| Dashboard ejecutivo (top 10 distritos, actualización diaria) | Power BI / Tableau sobre capa Gold (Spark SQL) | Visualización + BD analítica | El dashboard consume datos ya agregados (capa Gold de la arquitectura medallion); la actualización diaria es batch, no requiere tiempo real |

---

### 1.2 — Teorema CAP

| Componente | Combinación CAP | Propiedad sacrificada | ¿Por qué ese sacrificio es correcto o incorrecto? |
|------------|----------------|----------------------|----------------------------------------------------------------|
| Core de pagos (débito/crédito de saldos) | **CP** (Consistencia + Tolerancia a Particiones) | Disponibilidad | **CORRECTO.** En un pago, mostrar o mover un saldo incorrecto es inaceptable. Si hay un problema de red, es preferible rechazar temporalmente la operación (perder disponibilidad un instante) antes que permitir un doble gasto. La consistencia del dinero es lo primero |
| Historial "mis últimas 50 transacciones" | **AP** (Disponibilidad + Tolerancia a Particiones) | Consistencia (fuerte) | **CORRECTO.** Si el historial muestra las transacciones con 2-3 segundos de retraso (consistencia eventual), no pasa nada grave. Lo crítico es que la pantalla **siempre cargue rápido** aunque una transacción recién hecha tarde un momento en aparecer. La disponibilidad prima en la experiencia de consulta |

---

### 1.3 — NewSQL (CockroachDB)

**a) ¿Qué limitación de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?**

Oracle escala principalmente de forma **vertical** (agregando más CPU/RAM a un solo servidor), lo que tiene un techo físico y un costo de licencias enorme. Al pasar de 15M a 50M usuarios, ese servidor único se convierte en cuello de botella y punto único de fallo. CockroachDB resuelve esto con **escalado horizontal**: se agregan nodos al clúster y la base distribuye automáticamente los datos y la carga entre ellos, manteniendo las garantías ACID. Así Yape crece agregando servidores commodity en lugar de comprar un mainframe cada vez más caro.

**b) ¿Por qué MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque también escala horizontalmente?**

Porque MongoDB se diseñó bajo el paradigma **BASE (consistencia eventual)**, no ACID estricto a nivel multi-documento de forma nativa y eficiente. En un pago, se necesita una transacción **atómica** que debite de una cuenta y acredite en otra de forma todo-o-nada y consistente al instante. Aunque MongoDB añadió transacciones multi-documento, no es su fortaleza ni su diseño base, y la consistencia eventual abre la puerta a estados intermedios inaceptables en dinero (como un débito que se ve antes que el crédito correspondiente). Para pagos se necesita consistencia fuerte garantizada.

**c) ¿Qué mecanismo técnico usa CockroachDB para mantener ACID en múltiples nodos distribuidos?**

El algoritmo de consenso **Raft** (protocolo de consenso distribuido). CockroachDB replica cada rango de datos en varios nodos y usa Raft para que todos acuerden el orden de las operaciones antes de confirmarlas, manteniendo consistencia ACID a pesar de estar distribuido. *(Paxos es el otro algoritmo de consenso de la misma familia.)*

---

# PARTE D — DOCKER DESKTOP: Análisis (3 puntos)

> El código de implementación (Paso 1 y 2) y los screenshots del contenedor en estado *Running* están en el repositorio personal (`P4_docker.py` y carpeta `screenshots/`).

## PASO 3 — Diferencia entre Docker y Atlas (P4.3)

**a) ¿Cuándo usarías MongoDB en Docker en lugar de Atlas para el equipo de Yape?**

Usaría MongoDB en Docker para el **entorno local de desarrollo y pruebas**: cada desarrollador del equipo levanta una base idéntica en segundos en su propia máquina, sin tocar datos reales ni consumir el cluster de la nube. Es ideal para probar cambios, correr tests automatizados y trabajar sin conexión a internet, manteniendo aislado el entorno de pruebas del de producción.

**b) ¿Qué ventaja tiene Atlas M0 sobre el contenedor Docker para el contexto universitario?**

Atlas M0 está **siempre disponible en la nube sin consumir recursos de mi laptop**, y permite **compartir el acceso** (por ejemplo, mostrar los datos al docente mediante la interfaz web de Atlas Browse Collections). El contenedor Docker solo vive en mi máquina y se apaga cuando la cierro, mientras que Atlas persiste y es accesible desde cualquier lugar, lo cual facilita la entrega y la sustentación en video.

**c) ¿Qué sucede con los datos del contenedor si ejecutas `docker stop` y luego `docker rm`? ¿Y con Atlas?**

Con `docker stop yape-mongo-local` el contenedor se **detiene pero los datos se conservan** dentro de él. Sin embargo, al ejecutar `docker rm yape-mongo-local` se **elimina el contenedor y se pierden todos los datos** que tenía dentro (porque no se configuró un volumen persistente externo). En cambio, los datos de **Atlas permanecen intactos** en la nube sin importar lo que pase con mi máquina local, porque están almacenados de forma persistente y replicada en los servidores de MongoDB. Esta es la diferencia clave entre un contenedor efímero y una base gestionada en la nube.

---

## NOTA SOBRE USO DE IA

Usé Claude (Anthropic) como asistente para explorar opciones de arquitectura y para depurar el código de las celdas de Spark y el aggregation pipeline de MongoDB. Las justificaciones técnicas vinculadas al caso Yape, el completado de los espacios según las pistas, la ejecución real en las tres herramientas y la verificación de los outputs son trabajo propio.

---

*Big Data DD283 | Universidad Autónoma del Perú | Evaluación Parcial | Semana 4 | 2026-1*
*Lindo Barrientos, Jhonn Viequier*