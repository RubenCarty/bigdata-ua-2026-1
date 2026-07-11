# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Alexis Patricio 
**Grupo de proyecto**: Predicción de Fuga de Clientes en Telco GRUPO 2
**Fecha de entrega**: Antes de la sesión de la Semana 2  
**Modalidad**: Individual  
**Puntaje**: 20 puntos (2 puntos por pregunta)

---

> **Instrucciones**: Responde cada pregunta con tus propias palabras. No copies y pegues definiciones de internet — el objetivo es que construyas TU comprensión del tema. Se valorará la conexión con ejemplos reales de tu entorno laboral.

---

## PARTE 1: CONCEPTOS FUNDAMENTALES DE BIG DATA (10 preguntas)

### Pregunta 1
Define Big Data con tus propias palabras. ¿Cuál es la diferencia fundamental entre Big Data y una base de datos tradicional como SQL Server o MySQL que probablemente usas en tu empresa?

_Respuesta_:  
```text
Big Data no es simplemente un gran volumen de información; es todo un ecosistema tecnológico diseñado para capturar, almacenar, procesar y analizar conjuntos de datos tan masivos, rápidos y caóticos que las herramientas informáticas convencionales quedan obsoletas. Es la capacidad de encontrar patrones ocultos donde antes solo había ruido.

La diferencia fundamental radica en la arquitectura y su escalabilidad:
1. Escalabilidad: Las bases de datos tradicionales (SQL Server/MySQL) escalan de forma VERTICAL (necesitas un servidor con más RAM y mejor CPU cuando se llena). Big Data escala de forma HORIZONTAL (añade múltiples computadoras comerciales o "nodos" interconectados en red para repartirse el trabajo).
2. Estructura: Las bases de datos tradicionales te obligan a tener un esquema rígido de filas y columnas. Big Data procesa datos estructurados, semiestructurados (JSON, logs) y no estructurados (videos, audios) sin despeinarse.
```

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida (Ejemplo: Intercorp / Tiendas Mass) |
|---|---------------------------|---------------------------------------|
| **Volumen** | La cantidad masiva e ingente de datos generados que satura el almacenamiento común. | Los millones de transacciones de compra diarias que ocurren en todas las Tiendas Mass a nivel nacional, sumadas a los datos de la tarjeta Oh! |
| **Velocidad** | La rapidez con la que los datos se crean, se transmiten y necesitan ser analizados en tiempo real. | El procesamiento inmediato de cada boleta en caja para actualizar el stock del almacén central antes de que el cliente salga de la tienda. |
| **Variedad** | Los múltiples formatos, tipos y fuentes de procedencia de los datos (tablas, textos, imágenes). | Boletas estructuradas (SQL), videos de cámaras de seguridad para analizar colas, audios de quejas en el call center y comentarios en su página de Facebook. |
| **Veracidad** | La limpieza, calidad y autenticidad del dato; separar la información útil del "ruido" o datos falsos. | Validar que los DNI digitados en caja existan (cruzar con Reniec), descartar registros duplicados por caídas de red y limpiar lecturas erróneas del escáner de barras. |
| **Valor** | La utilidad real del dato para el negocio; transformar la información en dinero, ahorro o decisiones estratégicas. | Identificar qué productos se compran juntos (ej. cerveza y snacks los viernes) para diseñar promociones personalizadas y optimizar la disposición de los estantes. |


### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
* **Razones Técnicas:**
  1. **Cuello de botella por concurrencia extrema (Bloqueo de tablas):** En días de pago (quincenas o fines de mes), millones de peruanos usan Yape y la Banca Móvil en simultáneo. Una base de datos relacional tradicional asegura la consistencia del dato mediante el bloqueo de filas o tablas (propiedades ACID). A esa escala, el bloqueo masivo genera colas de espera en el sistema, lentitud y la clásica caída de las aplicaciones.
  2. **Límite físico de Escalabilidad Vertical:** Oracle tradicional corre sobre un servidor centralizado. Existe un límite físico en el hardware donde ya no se pueden añadir más discos duros, procesadores o memoria RAM a un solo equipo para soportar el crecimiento exponencial del volumen de datos del banco.
  3. **Conflicto Transaccional vs. Analítico (OLTP vs. OLAP):** Si el servidor central intenta procesar de manera simultánea los billones de filas históricas para detectar fraudes, evaluar créditos o buscar patrones de lavado de activos, consumirá todos los recursos de hardware, ralentizando o congelando las operaciones transaccionales (transferencias, pagos) que los usuarios intentan realizar en ese mismo instante.

* **Razón de Negocio:**
  * **Costos de licenciamiento prohibitivos y pérdida de clientes:** El modelo de licenciamiento de las bases de datos tradicionales como Oracle se calcula por la cantidad de núcleos (cores) del procesador del servidor. Escalar esta arquitectura para soportar a más de 12 millones de usuarios en Yape costaría millones de dólares anuales solo en contratos de software. Además, la falta de agilidad y la lentitud del servicio empujarían a los clientes a migrar hacia la competencia (Plin / otros bancos).

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales | **Estructurado** | Tiene filas, columnas y tipos de datos predefinidos (fechas, montos, strings) con un esquema rígido y conocido. |
| Un tweet sobre el precio del dólar | **No estructurado** | Es texto libre redactado por un usuario. No sigue ninguna regla fija de campos y puede incluir jerga, enlaces, hashtags o emojis. |
| Una foto del ticket de compra en Metro | **No estructurado** | Es una imagen binaria (matriz de píxeles). No contiene texto estructurado ejecutable a menos que se le aplique un software de IA (OCR). |
| Un archivo JSON de la API de SUNAT | **Semi-estructurado** | No tiene una estructura rígida de filas y columnas, pero posee etiquetas jerárquicas y marcadores (`"RUC": "2010..."`) que organizan los datos internamente. |
| Un audio de una llamada al call center de Claro | **No estructurado** | Es una onda sonora binaria sin campos definidos. Requiere herramientas de *Speech-to-Text* para transcribir las palabras y analizar su contenido. |
| Un archivo CSV de exportaciones del BCRP | **Estructurado** | Es un archivo de texto plano rígidamente delimitado por comas, donde cada línea representa un registro idéntico con campos y variables fijas. |
| Un video de seguridad de un supermercado | **No estructurado** | Secuencia de imágenes en movimiento a través del tiempo. No contiene datos relacionales nativos estructurados en su almacenamiento básico. |
| Un log de errores de un servidor web | **Semi-estructurado** | Es texto plano libre, pero sigue un patrón estándar y repetitivo (Fecha/Hora - IP - Código HTTP) que facilita su separación (*parseo*) mediante código. |

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
Un **clúster** es un conjunto de múltiples computadoras independientes (llamadas **nodos**) interconectadas entre sí mediante una red de alta velocidad, las cuales trabajan de forma centralizada y coordinada para comportarse como si fueran una sola supercomputadora. Se utiliza en Big Data para dividir tareas masivas de almacenamiento y cómputo que una sola máquina no podría soportar.

#### Esquema de Diferencias de Arquitectura

```text
SISTEMA DE MEMORIA COMPARTIDA (Arquitectura Tradicional Monolítica)
┌─────────────────────────────────────────┐
│     [Procesador 1]   [Procesador 2]     │
│           │                │            │
│           └───► [ BUS DE  ]◄────────────┤
│                 [ MEMORIA ]             │
│                      │                  │
│            ▼         ▼                  │
│       [ MEMORIA RAM CENTRALIZADA ]       │
└─────────────────────────────────────────┘
* Característica: Todos los procesadores acceden a un único espacio de memoria global.
* Desventaja: Sufre cuellos de botella en el Bus de datos al intentar escalar.

SISTEMA DE MEMORIA DISTRIBUIDA (Arquitectura Big Data / Clúster)
┌─────────────────────────┐       ┌─────────────────────────┐
│  NODO 1 (Servidor 1)    │       │  NODO 2 (Servidor 2)    │
│  [Procesador 1]         │       │  [Procesador 2]         │
│        │                │       │        │                │
│  [Memoria RAM Local 1]  │       │  [Memoria RAM Local 2]  │
└───────────┬─────────────┘       └───────────┬─────────────┘
            │                                 │
            └───► [ RED DE ALTA VELOCIDAD ] ◄─┘
                  (Paso de Mensajes / Network)
* Característica: Cada nodo tiene su propio procesador y su propia memoria RAM exclusiva.
* Ventaja: Escalabilidad horizontal prácticamente infinita para Big Data.
```
### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro)_: https://www.alicorp.com.pe / Casos de Éxito Corporativo de Transformación Digital y Advanced Analytics.

_Respuesta_:  
* **El problema:** Alicorp (Perú) sufría constantes desabastecimientos de productos clave en algunas zonas o acumulación de inventario sin vender en otras, debido a que su fuerza de ventas tomaba pedidos basándose solo en la intuición o en históricos de compra muy básicos de las bodegas.
* **La solución:** Implementaron una plataforma analítica de Big Data en la nube que unificó múltiples fuentes de datos masivos: historial transaccional, geolocalización de los comercios, niveles socioeconómicos por manzanas y factores climáticos locales, procesando todo con modelos de aprendizaje automático (*Machine Learning*).
* **Los resultados:** Lograron generar sugerencias automatizadas de "venta inteligente" para cada bodega en tiempo real. Esto optimizó las rutas de distribución, redujo las pérdidas por sobre-inventario y aumentó la eficiencia en las ventas del canal tradicional.

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| Característica | Data Lake | Data Warehouse |
|---|---|---|
| **Definición** | Repositorio centralizado que almacena datos masivos en su estado nativo o en bruto, sin procesar y sin un esquema fijo predefinido (*Schema-on-read*). | Base de datos corporativa altamente optimizada y estructurada, diseñada para el análisis y consolidación de datos previamente limpios (*Schema-on-write*). |
| **Tipo de datos** | Datos estructurados, semi-estructurados (JSON, XML, logs) y no estructurados (imágenes, audios, videos). | Estrictamente datos estructurados organizados en tablas relacionales (filas y columnas). |
| **Cuándo usarlo** | Cuando necesitas guardar flujos masivos de información heterogénea a muy bajo costo para futuros análisis avanzados, Ciencia de Datos o Inteligencia Artificial. | Cuando los analistas y directivos necesitan realizar consultas rápidas, generar reportes de negocio estables y visualizar tableros de control (KPIs) de forma exacta. |
| **Ejemplo de negocio** | Almacenar las grabaciones de audio completas de los últimos 5 años de llamadas a un call center para entrenar un modelo de IA que detecte el estado de ánimo de los usuarios. | Consultar el volumen exacto de ventas del mes de mayo de 2026 clasificado por tienda y por categoría de producto para calcular las comisiones del equipo comercial. |
| **Herramienta típica** | Apache Hadoop HDFS, Amazon S3, Azure Data Lake Storage (ADLS). | Snowflake, Google BigQuery, AWS Redshift, Oracle Exadata. |

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
Los **requisitos de un sistema Big Data** son las capacidades técnicas, operativas y de diseño que garantizan que una infraestructura tecnológica sea capaz de capturar, almacenar y procesar flujos masivos de información de forma eficiente, segura y sin interrupciones para el negocio.

Los 5 requisitos principales son:

1. **Escalabilidad (Scalability):** Capacidad del sistema para crecer de forma modular agregando servidores estándar y económicos (escalabilidad horizontal) a medida que aumenta el volumen de información.
   * *Si NO se cumple:* La infraestructura colapsará, se congelará o se volverá extremadamente lenta cuando la base de datos de clientes crezca, deteniendo la operación de la empresa.

2. **Tolerancia a fallos (Fault Tolerance):** Capacidad de la arquitectura para seguir funcionando correctamente y sin perder información si una o varias computadoras (nodos) del clúster fallan o se queman físicamente.
   * *Si NO se cumple:* Cualquier falla de hardware detendrá por completo los procesos analíticos, corromperá los archivos de la empresa y causará costosos tiempos de inactividad.

3. **Procesamiento distribuido (Distributed/Parallel Cómputo):** Habilidad de dividir una tarea gigantesca en múltiples sub-tareas más pequeñas para ejecutarlas simultáneamente en diferentes nodos del clúster.
   * *Si NO se cumple:* El procesamiento de los datos masivos tardaría semanas o meses en finalizar, haciendo que la información llegue completamente tarde para la toma de decisiones del negocio.

4. **Seguridad y Privacidad de los Datos:** Implementación de protocolos estrictos de cifrado de información (en tránsito y en reposo), control de accesos basados en roles y auditorías automatizadas de usuarios.
   * *Si NO se cumple:* La empresa quedará expuesta a hackeos, filtración de datos confidenciales y severas sanciones legales bajo la Ley de Protección de Datos Personales en el Perú.

5. **Extensibilidad / Flexibilidad:** Capacidad de la arquitectura para integrar nuevas herramientas tecnológicas y nuevos formatos de datos sin necesidad de rediseñar o reconstruir todo el sistema desde cero.
   * *Si NO se cumple:* El sistema se volverá obsoleto rápidamente y adaptarlo a nuevos canales digitales (como conectar el flujo de datos de una nueva red social o app móvil) resultará sumamente complejo y costoso.
### Pregunta 9
La empresa en la que trabajas actualmente, ¿tiene algún problema de datos que podría resolverse con Big Data? Describe:
- El problema o necesidad
- Qué tipo de datos implicaría (V's del Big Data)
- Una propuesta inicial de solución (aunque sea básica)

_Respuesta_:  
* **El problema:** En una empresa del sector retail peruano (como Supermercados Peruanos o Falabella), los datos de atención en tiendas, apps móviles, WhatsApp y redes sociales están fragmentados en bases de datos independientes. Esto impide ver el historial completo del cliente, provocando una mala atención y pérdida de usuarios.
* **Las V's implicadas:** **Variedad** (boletas estructuradas, logs de la app semi-estructurados y chats no estructurados), **Velocidad** (interacciones masivas y simultáneas por minuto) y **Volumen** (gigabytes de datos diarios acumulados).
* **Propuesta de solución:** Ingestar todas las fuentes en bruto en un Data Lake en la nube (como Amazon S3). Luego, procesar la información en paralelo con Apache Spark usando el DNI como clave única para unificar los canales, aplicar análisis de texto a los chats y alimentar un tablero en tiempo real para que los agentes de soporte conozcan el historial del cliente de inmediato.

---

### Pregunta 10
**Análisis crítico**: Lee el siguiente caso y responde las preguntas:

> "Una empresa de telecomunicaciones en Perú tiene 8 millones de clientes. Cada cliente genera en promedio 500 registros de datos al día (llamadas, SMS, datos móviles, pagos). La empresa quiere predecir qué clientes cancelarán su contrato en los próximos 30 días para ofrecerles retención proactiva."

**a) ¿Cuántos registros se generan por día? ¿Por año?**
* **Por día:** $8,000,000 \times 500 = 4,000,000,000$ (4 mil millones de registros diarios).
* **Por año:** $4,000,000,000 \times 365 = 1,460,000,000,000$ (1.46 billones de registros anuales).

**b) ¿Qué tipo de datos están involucrados?**
* **Estructurados:** Montos y fechas de pagos de recibos.
* **Semi-estructurados:** Logs de navegación de internet y marcas de tiempo de llamadas/SMS.
* **No estructurados:** Transcripciones de audio o chats de quejas en el call center.

**c) ¿Cuáles de las 5 V's son más relevantes en este caso?**
* **Volumen:** Por la escala de billones de registros anuales a almacenar.
* **Velocidad:** El comportamiento de uso de red cambia segundo a segundo; se requiere detectar fallas rápido para ganarle a la cancelación.
* **Valor:** El beneficio económico directo de evitar la fuga de clientes (*churn*).

**d) ¿Qué tecnologías Big Data necesitarían para resolver este problema?**
* **Ingesta:** Apache Kafka (captura de flujos de red en tiempo real).
* **Almacenamiento:** Amazon S3 o Hadoop HDFS (almacenamiento masivo de bajo costo).
* **Procesamiento:** Apache Spark (procesamiento distribuido y modelos predictivos de Machine Learning).

**e) ¿Qué impacto ético podría tener esta solución? (pista: privacidad de datos)**
Vulnera potencialmente la **Ley N° 29733 (Ley de Protección de Datos Personales en Perú)**. Usar el rastreo minucioso de llamadas, geolocalización o navegación web para armar perfiles comerciales sin el consentimiento explícito del cliente cruza la línea hacia la invasión de la privacidad. Además, un algoritmo mal calibrado podría generar sesgos automáticos y discriminar injustamente a ciertos sectores de usuarios.

### Pregunta 11 — Tu Proyecto

**Describe brevemente el proyecto Big Data que tu grupo ha elegido:**

* **Nombre del proyecto:** Predicción de Fuga de Clientes en Telco 
* **Empresa o sector al que aplica:** Sector de Telecomunicaciones (Empresas proveedoras de servicios de internet, telefonía móvil y televisión por cable).
* **Problema que resuelve:** La alta tasa de abandono de clientes (*Churn*), la cual genera pérdidas financieras masivas y eleva los costos operativos (es 5 veces más caro adquirir un cliente nuevo que retener a uno actual). El proyecto resuelve la falta de precisión del equipo de Marketing para identificar proactivamente qué clientes específicos planean cancelar su servicio, permitiendo pasar de estrategias masivas costosas a campañas de retención ultra-dirigidas basadas en Inteligencia Artificial.

**¿Cuáles de las 5 V's están presentes en los datos del proyecto?**
En nuestro set de datos de Telco, identificamos la presencia crítica de las siguientes **3 V's del Big Data**:

1.  **Volumen:** Manejamos un dataset masivo con miles de registros históricos de clientes que consolidan múltiples servicios simultáneos (internet de fibra óptica, telefonía, streaming), lo que requiere motores de procesamiento distribuido como Spark para no saturar la memoria tradicional de la máquina local.
2.  **Variedad:** Los datos vienen en formatos mixtos y heterogéneos. Contamos con variables categóricas de texto (tipo de contrato, método de pago, servicios contratados, género) combinadas con variables numéricas continuas (cargos mensuales, cargos totales acumulados, antigüedad o *tenure*), exigiendo una fase compleja de ingeniería de características utilizando *pipelines* y *StringIndexers*.
3.  **Valor:** Es la V más importante del proyecto. Convertimos datos operativos crudos en decisiones financieras estratégicas. Al predecir con un **83.94% de precisión (ROC AUC)** qué clientes se van a ir, la empresa puede salvar el ingreso recurrente mensual (MRR) antes de que el usuario firme con la competencia.

---

### Pregunta 12 — Arquitectura inicial

**Dibuja (a mano o usando draw.io) una arquitectura inicial muy básica de cómo crees que debería funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualización.**

**Link o descripción de tu diagrama:**

Nuestra arquitectura inicial sigue un flujo lineal de datos de 4 capas optimizado para analítica predictiva local y escalable a la nube:
#### 📐 Diagrama de la Arquitectura Inicial
| 📑 FUENTES DE DATOS | 📦 ALMACENAMIENTO | ⚙️ PROCESAMIENTO (ML) | 📊 VISUALIZACIÓN |
| :---: | :---: | :---: | :---: |
| CRM / Facturas de Clientes | Capa Raw / Directorio Local | Motor PySpark ML (Regresión Logística) | Dashboard Ejecutivo (Métricas de Negocio) |
| *Formato estructurado (.csv)* | *Simulación de Capa Bronze* | *Modelado Binario Local* | *Análisis de Impacto Financiero* |

⏬
**Flujo del Dato:** Ingesta ➡️ Almacenamiento Seguro ➡️ Entrenamiento de IA ➡️ Reporte de Resultados



### 🛠️ Descripción Técnica de la Arquitectura

1. **Fuentes de Datos (Ingesta):**
   * **Componente:** CRM y Sistemas de Facturación de Telco.
   * **Detalle:** Extracción de datos históricos crudos consolidados en un formato estructurado `.csv`. Contiene información demográfica, servicios contratados (internet, telefonía) y cargos financieros de los usuarios.

2. **Almacenamiento (Data Lakehouse Local):**
   * **Componente:** Capa *Raw* / Directorio de Datos (`/data/sample/`).
   * **Detalle:** Zona de aterrizaje local dentro del repositorio que simula la arquitectura de un Data Lakehouse empresarial (Capa *Bronze*). Su propósito es resguardar la integridad del dataset original para auditorías, sin aplicar transformaciones destructivas.

3. **Procesamiento (Núcleo Analítico):**
   * **Componente:** Motor de **PySpark (Spark SQL y PySpark ML)**.
   * **Detalle:** Es el cerebro del proyecto, configurado para aprovechar el procesamiento multihilo de la máquina local. Ejecuta de forma secuencial un Pipeline que incluye: la limpieza e imputación de nulos por mediana, la codificación de variables categóricas (*StringIndexer* y *OneHotEncoder*), la vectorización de características (*VectorAssembler*) y el entrenamiento del algoritmo predictivo de **Regresión Logística**.

4. **Visualización (Capa de Negocio):**
   * **Componente:** Dashboard Ejecutivo en Notebook Local (`04_dashboard.ipynb`).
   * **Detalle:** Capa de salida estratégica donde las predicciones probabilísticas generadas por la Inteligencia Artificial se traducen en valor comercial. Se enfoca en cuantificar el impacto financiero del abandono (pérdidas mitigables) y clasificar a los clientes en segmentos operativos de riesgo alto, medio y bajo.
```

---

## CRITERIOS DE EVALUACIÓN

| Criterio | Puntos |
|---------|--------|
| Responde todas las preguntas (no deja en blanco) | 4 |
| Usa sus propias palabras, no copia de internet | 4 |
| Da ejemplos reales de su entorno laboral | 4 |
| Las definiciones son técnicamente correctas | 4 |
| Respuestas de reflexión (P9, P11, P12) muestran pensamiento propio | 4 |
| **TOTAL** | **20** |

---

> **Recuerda**: La nota EC (10% del total) se basa en tu dominio conceptual. Esta guía de trabajo es el mejor preparativo. Si puedes responder estas 12 preguntas con seguridad, el examen EC no debería sorprenderte.

---

*Entrega: Subir al repositorio de GitHub Classroom o al foro de la plataforma virtual antes de la Semana 2*
