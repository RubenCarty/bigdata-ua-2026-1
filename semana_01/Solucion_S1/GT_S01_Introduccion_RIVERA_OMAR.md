# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Omar Rivera Castillo
**Grupo de proyecto**:semana_01
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
```
[Las bases de datos tradicionales están diseñadas para la estructura y la centralización; Big Data está diseñado para el caos y la distribución.]
```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen | Es la cantidad masiva de datos que se generan a cada segundo.|Millones de transacciones diarias con tarjetas de crédito, retiros en cajeros GlobalNet |
| Velocidad |La rapidez con la que llegan los datos |La detección instantánea de fraudes |
| Variedad |La diversidad de formatos en los que vienen los datos. |El banco recibe transferencias (datos estructurados). |
| Veracidad | El nivel de confianza, calidad y limpieza de los datos.| Asegurar que los perfiles de los clientes no tengan datos duplicados o falsos.|
| Valor |La utilidad real que se le saca a los datos. | Crear campañas de marketing hiperpersonalizadas.|

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
[El BCP sí usa Oracle, pero solo para lo que es excelente: mantener los saldos finales y contables con precisión milimétrica, 1. Cuello de botella, 2.Limitación del Escalado Vertical vs. Horizontal 3.Ineficiencia en el procesamiento analítico simultáneo, el negocio seria : Las licencias de Oracle se cobran por la cantidad de núcleos (cores) del procesador del servidor.]
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales | Estructurado|Los datos están organizados rígidamente en filas y columnas definidas |
| Un tweet sobre el precio del dólar | No estructurado| Es texto libre redactado por un usuario.|
| Una foto del ticket de compra en Metro |No estructurado |Es un archivo de imagen (píxeles). |
| Un archivo JSON de la API de SUNAT |Semi-estructurado |No tiene una estructura de tabla rígida, pero utiliza etiquetas, claves y corchetes. |
| Un audio de una llamada al call center de Claro | No estructurado| Es un archivo multimedia binario.|
| Un archivo CSV de exportaciones del BCRP |Estructurado |los datos están estrictamente separados por comas (u otros delimitadores). |
| Un video de seguridad de un supermercado |No estructurado | Es una secuencia masiva de imágenes y movimiento en formato de video.|
| Un log de errores de un servidor web |Semi-estructurado |Es un archivo de texto plano, pero cada línea sigue un patrón o formato predecible. |

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
```
[ es un grupo de computadoras (llamadas nodos) conectadas en red que trabajan juntas como si fueran una sola máquina gigante

MEMORIA COMPARTIDA (Shared Memory)
+-------------+  +-------------+  +-------------+

| Procesador  |  | Procesador  |  | Procesador  |
|     (CPU)   |  |     (CPU)   |  |     (CPU)   |
+------+------+  +------+------+  +------+------+

       |                |                |
       +----------------+----------------+
                        |
                        v
         [ MEMORIA CENTRAL COMPARTIDA ]]
```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro) [Caso de éxito – Big Data & Analytics: Rimac – Data Lake Perú (Morris & Opazo)](https://blog.morrisopazo.com/casos-de-exito/financial-services/caso-de-exito-big-data-analytics-rimac-data-lake/)

_Respuesta_:  
```
[Caso de Éxito: Rímac Seguros (Perú)El problema que tenían: La compañía manejaba una carga de trabajo sumamente grande y pesada alojada en servidores locales (on-premise).La solución Big Data que implementaron: Rímac migró su arquitectura analítica hacia la nube de Amazon Web Services (AWS)Los resultados que obtuvieron: Lograron eliminar los cuellos de botella informáticos al independizar los procesos analíticos de los sistemas operativos principales. ]
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición | Es un gran repositorio centralizado que almacena datos en su estado bruto.| Es un sistema de almacenamiento optimizado específicamente para analizar datos corporativos que ya han sido limpiados, modelados y estructurados.|
| Tipo de datos |Todo tipo de datos: Estructurados, semi-estructurados y no estructurados (como JSONs, audios, videos, logs y tablas). |Únicamente datos altamente estructurados y limpios que encajan perfectamente en tablas y esquemas relacionales. |
| Cuándo usarlo |Cuando tienes volúmenes masivos de datos crudos cuyo uso final aún no está definido. |Cuando necesitas reportes financieros operativos exactos, dashboards de inteligencia de negocios (BI) y métricas fijas para la toma de decisiones directivas. |
| Ejemplo de negocio | Una empresa de retail (como Falabella) guarda todas las grabaciones de las cámaras de seguridad de sus tiendas y los clics de su web para que sus científicos de datos entrenen un algoritmo que prediga el comportamiento de compra.|La misma empresa utiliza un repositorio limpio para generar el reporte de facturación semanal por sucursal y medir si se llegó a la meta de ventas del mes. |
| Herramienta típica | Amazon S3, Azure Data Lake Storage (ADLS), Apache Hadoop (HDFS).| Snowflake, Google BigQuery, Amazon Redshift, Oracle Exadata.|

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
[. Escalabilidad Horizontal: Añadir más servidores baratos al clúster para repartir el trabajo.
Si NO se cumple: El sistema se congela o colapsa ante picos de tráfico (como un Cyber Wow).
2. Tolerancia a Fallos: Duplicar datos en varias máquinas por si una se quema.
Si NO se cumple: Si un servidor físico falla, se pierden datos críticos y se cae el servicio.
3. Procesamiento Distribuido: Dividir una consulta pesada entre muchas computadoras a la vez.
Si NO se cumple: Un reporte analítico tardaría días o semanas en completarse, volviendo la información obsoleta.
4. Flexibilidad (Esquema libre): Almacenar cualquier formato (JSON, imágenes, videos) sin orden previo.
Si NO se cumple: Solo se podrían guardar tablas tradicionales, perdiendo información valiosa de redes sociales o audios.
5. Seguridad y Gobernanza: Controlar accesos y encriptar la información sensible.
Si NO se cumple: La empresa sufre hackeos, filtraciones y multas severas por la ley de protección de datos (ANPD).]
```

---

### Pregunta 9
La empresa en la que trabajas actualmente, ¿tiene algún problema de datos que podría resolverse con Big Data? Describe:
- El problema o necesidad
- Qué tipo de datos implicaría (V's del Big Data)
- Una propuesta inicial de solución (aunque sea básica)

*(Si no puedes compartir información de tu empresa por confidencialidad, usa una empresa pública del sector)*

_Respuesta_:  
```
[Problema y Datos: Promart no analiza los clics web en tiempo real para dar ofertas antes de que el usuario se vaya (Volumen, Velocidad y Variedad).

Solución: Capturar las interacciones en vivo con Apache Kafka y procesarlas con Apache Spark para lanzar cupones automáticos en la pantalla.]
```

---

### Pregunta 10
**Análisis crítico**: Lee el siguiente caso y responde las preguntas:

> "Una empresa de telecomunicaciones en Perú tiene 8 millones de clientes. Cada cliente genera en promedio 500 registros de datos al día (llamadas, SMS, datos móviles, pagos). La empresa quiere predecir qué clientes cancelarán su contrato en los próximos 30 días para ofrecerles retención proactiva."

**a)** ¿Cuántos registros se generan por día? ¿Por año?  
**b)** ¿Qué tipo de datos están involucrados?  
**c)** ¿Cuáles de las 5 V's son más relevantes en este caso?  
**d)** ¿Qué tecnologías Big Data necesitarían para resolver este problema?  
**e)** ¿Qué impacto ético podría tener esta solución? (pista: privacidad de datos)

_Respuesta_:  
```
[a) ¿Cuántos registros se generan por día? ¿Por año?Por día: $8,000,000 \text{ clientes} \times 500 \text{ registros} =$ 4,000 millones de registros al día.Por año: $4,000,000,000 \times 365 \text{ días} =$ 1.46 billones de registros al año ($1.46 \times 10^{12}$).
b) ¿Qué tipo de datos están involucrados?Están involucrados datos mixtos:Estructurados: Registros de pagos, fechas de vencimiento y duración de llamadas (tablas tradicionales).Semi-estructurados y No estructurados: Logs de navegación web (formatos JSON/XML), registros de conexión a antenas (celdas de red) e incluso texto libre en reclamos de SMS o chats de atención.
c) ¿Cuáles de las 5 V's son más relevantes en este caso?Volumen: Por la escala masiva de procesar billones de registros acumulados para entrenar los modelos.Velocidad: Vital para procesar el comportamiento actual y predecir el abandono dentro de la ventana crítica de 30 días.Valor: Es el núcleo del negocio; identificar a tiempo a estos clientes evita la pérdida de ingresos por fuga (churn).
d) ¿Qué tecnologías Big Data necesitarían para resolver este problema?Almacenamiento: Un Data Lake en la nube (como Amazon S3 o Google Cloud Storage) para guardar los históricos de navegación y consumo de forma económica.Procesamiento y Analítica: Apache Spark (o Databricks) para limpiar y procesar los billones de registros en paralelo, utilizando su librería SparkML para ejecutar los algoritmos predictivos de Machine Learning.
e) ¿Qué impacto ético podría tener esta solución?El principal riesgo es la invasión a la privacidad de datos. Analizar a detalle las antenas a las que se conecta un usuario, las páginas que visita con sus datos móviles o sus hábitos diarios para "adivinar" su comportamiento puede rozar el espionaje corporativo]
```

---

## PARTE 2: REFLEXIÓN Y CONEXIÓN CON TU PROYECTO (2 preguntas adicionales)

### Pregunta 11 — Tu Proyecto
Describe brevemente el proyecto Big Data que tu grupo ha elegido:
- Nombre del proyecto
- Empresa o sector al que aplica
- Problema que resuelve
- ¿Cuáles de las 5 V's están presentes en los datos del proyecto?

_Respuesta_:  
```
[Escribe tu respuesta aquí]
```

---

### Pregunta 12 — Arquitectura inicial
Dibuja (a mano o usando draw.io) una arquitectura inicial **muy básica** de cómo crees que debería funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualización.

*(Adjunta la imagen o el link de draw.io)*

_Link o descripción de tu diagrama_:  
```
[Escribe aquí o adjunta imagen]
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
