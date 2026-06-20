# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: _Tolentino Vargas Jesus Antonio       
**Grupo de proyecto**: Grupo 2  
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
Para mi, la big data no es solo "muchos datos", sino el ecosistema tecnológico y las estrategias que se necesitan cuando la información desborda por completo las capacidades de las herramientas comunes.```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen |Cantidad masiva |Los miles de millones de clics y transacciones anuales en la app. |
| Velocidad |Rapidez de llegada. |Evaluar alertas de fraude con la tarjeta en milisegundos. |
| Variedad |Diversidad de formatos. |Mezclar tablas de saldos, PDFs de contratos y audios del call center. |
| Veracidad |Limpieza de datos falsos. |Cruzar DNIs con RENIEC para eliminar registros duplicados. |
| Valor |Utilidad para el negocio. |Predecir qué cliente necesita un préstamo justo hoy para cerrar la venta. |

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
Razones Técnicas: 
-Un servidor Oracle centralizado colapsaría en quincena o Cyber Days por exceso de peticiones.
-Las bases tradicionales bloquean las filas al procesar, lo que causaría colas de espera eternas en Yape.
-Oracle no está optimizado para procesar a la vez logs de apps, geolocalización y datos de red.
Razón de Negocio: Si Yape o la banca móvil se caen en hora punta, los clientes migran a la competencia (Plin), generando pérdidas millonarias y daño de reputación.
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales |Estructurado |Formato rígido de filas y columnas |
| Un tweet sobre el precio del dólar |Semi-estructurado |Texto libre, pero con etiquetas fijas (autor, fecha) |
| Una foto del ticket de compra en Metro |No estructurado |Es una imagen binaria (.jpg); requiere un software OCR para leerla |
| Un archivo JSON de la API de SUNAT |Semi-estructurado |Organización por llaves y valores, sin tabla fija |
| Un audio de una llamada al call center de Claro |No estructurado |Onda de sonido libre; no tiene etiquetas nativas |
| Un archivo CSV de exportaciones del BCRP |Estructurado |Datos tabulares separados por comas |
| Un video de seguridad de un supermercado |No estructurado |Archivo binario visual sin esquema de datos |
| Un log de errores de un servidor web |Semi-estructurado |Texto libre pero con un patrón repetitivo e identificable (IP - Hora - Error) |

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
```
Clúster: Grupo de computadoras independientes (nodos) conectadas en red que trabajan juntas como si fueran una sola máquina.
Memoria Compartida: Varios procesadores usan la misma memoria RAM y disco (si se llena, todo muere).

Memoria Distribuida (Big Data): Cada nodo tiene su propio procesador, RAM y disco. Se comunican por red. Si falta potencia, se agregan más nodos.```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro)_: https://www.studocu.com/pe/u/96614669?sid=01781381489&page=1

_Respuesta_:  
```
Alicorp 
Problema: Su fuerza de ventas estimaba los pedidos de las bodegas por intuición, causando quiebres de stock o productos vencidos en tienda.

Solución: Crearon un Data Lake en la nube (AWS) que unifica históricos de ventas, clima y datos de la zona, aplicando Machine Learning para sugerir pedidos automáticos.

Resultados: Incremento en ventas, reducción del 15% en devoluciones de productos y rutas logísticas optimizadas.
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición |Depósito gigante de datos en bruto. |Almacén de datos limpios y estructurados. |
| Tipo de datos |Crudos (Estructurados y No estructurados). |Solo estructurados (tablas procesadas). |
| Cuándo usarlo |Para análisis predictivo e IA a futuro. |Para reportes de negocio y dashboards (BI). |
| Ejemplo de negocio |Guardar audios de quejas y logs de la app. |Reporte financiero de ingresos mensuales. |
| Herramienta típica |Amazon S3 / Hadoop HDFS. |Snowflake / Google BigQuery. |

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
Escalabilidad: Crecer en hardware fácilmente. Si falla: El sistema se congela al aumentar los datos.
Tolerancia a fallos: Seguir operando si se apaga un nodo. Si falla: Pérdida de datos a mitad de un proceso.
Procesamiento Distribuido: Dividir la tarea en muchas máquinas. Si falla: Un reporte tarda días en vez de minutos.
Baja Latencia: Respuestas casi en tiempo real. Si falla: Detectas un fraude cuando el dinero ya fue robado.
Seguridad y Gobernanza: Encriptación y permisos. Si falla: Multas por violar la Ley de Protección de Datos Personales.```

---

### Pregunta 9
La empresa en la que trabajas actualmente, ¿tiene algún problema de datos que podría resolverse con Big Data? Describe:
- El problema o necesidad
- Qué tipo de datos implicaría (V's del Big Data)
- Una propuesta inicial de solución (aunque sea básica)

*(Si no puedes compartir información de tu empresa por confidencialidad, usa una empresa pública del sector)*

_Respuesta_:  
```
Problema: En el centro de control sufrimos de fatiga de alertas. Más del 90% de los eventos recibidos (CCTV, sensores perimetrales, GPS) son falsos positivos provocados por el viento, sombras o conectividad, saturando a los operadores humanos.

Las V's del Big Data implicadas:

Velocidad: Flujo masivo de miles de eventos por segundo que exigen respuesta inmediata.

Volumen: Terabytes de video continuo y logs diarios que saturan el almacenamiento.

Variedad: Formatos diversos (video binario, telemetría GPS y texto plano de radios).

Propuesta de solución: Implementar un pipeline en tiempo real usando Apache Kafka centralizado y un motor de procesamiento en streaming con Machine Learning. El sistema correlacionará variables de forma automática: si una cámara detecta movimiento pero el sensor físico perimetral de esa zona no se activa, la prioridad de la alerta disminuye. De este modo, los operadores solo verán en pantalla amenazas con alta probabilidad de ser reales.```

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
a) Cálculos:Por día: $8,000,000 \times 500 = 4,000,000,000$ (4 mil millones de registros/día).Por año: $4,000,000,000 \times 365 = 1,460,000,000,000$ (1.46 billones de registros/año).
b) Tipo de datos: Estructurados (pagos) y semi-estructurados (logs de navegación).
c) V's más relevantes: Volumen (billones de datos) y Valor (evitar que los clientes se vayan).
d) Tecnologías: Amazon S3 para guardar, Apache Spark para procesar y algoritmos de Machine Learning para predecir la fuga.
e) Impacto ético: Riesgo de invadir la privacidad. Se debe cumplir la Ley N° 29733 en Perú, analizando patrones de comportamiento de forma 100% anónima.```

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
Nombre del proyecto: WinLoyal: Sistema Inteligente de Predicción de Abandono (Churn Risk) en Tiempo Real.

Empresa o sector al que aplica: Sector de Telecomunicaciones — Enfocado en la empresa peruana de internet de fibra óptica Win.

Problema que resuelve: El mercado de internet de hogar en el Perú es altamente competitivo. Win experimenta la pérdida de clientes (churn) debido a insatisfacciones acumuladas por caídas del servicio técnico local, lentitud percibida, ofertas agresivas de competidores o demoras en la atención de reclamos. Retener a un cliente existente es hasta 5 veces más barato que adquirir uno nuevo. Este proyecto busca identificar patrones ocultos de insatisfacción antes de que el cliente llame a solicitar la baja de su servicio, permitiendo al equipo de retención actuar de forma preventiva con promociones o soluciones técnicas prioritarias.

Las 5 V's en nuestro proyecto:

Volumen: Procesamiento de logs diarios de tráfico de routers de miles de usuarios conectados, historial de tickets de soporte y estados de cuenta.

Velocidad: Necesidad de capturar las alertas de interrupción del servicio o reclamos reiterados rápidamente para predecir el riesgo antes del cierre de su ciclo de facturación.

Variedad: Integración de datos estructurados (planes contratados, pagos de recibos), semi-estructurados (logs de estado técnico de las ONT/routers) y no estructurados (comentarios/quejas en redes sociales de Win, transcripciones de chats de soporte).```

---

### Pregunta 12 — Arquitectura inicial
Dibuja (a mano o usando draw.io) una arquitectura inicial **muy básica** de cómo crees que debería funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualización.

```
c:\Users\arian\Downloads\diagrama de prediccion telecomp.png---

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
