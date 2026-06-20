# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: DALIA NANCY LEON AGUILAR  
**Grupo de proyecto**: GRUPO N° 3
**Fecha de entrega**: A13 JUN 2026 
**Modalidad**: Individual  
**Puntaje**: 20 puntos (2 puntos por pregunta)

---

> **Instrucciones**: Responde cada pregunta con tus propias palabras. No copies y pegues definiciones de internet — el objetivo es que construyas TU comprensión del tema. Se valorará la conexión con ejemplos reales de tu entorno laboral.

---

## PARTE 1: CONCEPTOS FUNDAMENTALES DE BIG DATA (10 preguntas)

### Pregunta 1
Define Big Data con tus propias palabras. ¿Cuál es la diferencia fundamental entre Big Data y una base de datos tradicional como SQL Server o MySQL que probablemente usas en tu empresa?

_Respuesta_: Big Data es cuando la cantidad, velocidad o variedad de información es tan grande que una computadora normal o una base de datos tradicional ya no pueden procesarla en un tiempo razonable. Es como intentar llenar una piscina con un vaso pequeño: aunque puedas hacerlo, sería demasiado lento e ineficiente. 
```

```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen |La cantidad masiva de datos generados, que puede ser de terabytes o petabytes | Plaza Vea genera millones de transacciones por día en todas sus tiendas a nivel nacional|
| Velocidad |La rapidez con la que se generan y necesitan procesar los datos |BCP procesa en tiempo real las compras con tarjeta para detectar fraudes al instante|
| Variedad | Los diferentes formatos de datos: textos, números, imágenes, videos, audios| En un supermercado, tienes: códigos de barra (estructurado), fotos de promociones, audios de reclamos, videos de cámaras de seguridad|
| Veracidad | La confiabilidad y calidad de los datos (datos sucios, incompletos o inconsistentes)| Si los sensores de una tienda reportan mal los inventarios, todo el análisis de reposición será erróneo|
| Valor | El beneficio o conocimiento útil que se obtiene del análisis, que debe justificar la inversión| Usar los datos para saber qué productos ofrecer a cada cliente y aumentar las ventas en 20%|

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
Razones técnicas:

Escalabilidad limitada: Una base Oracle tradicional corre en un servidor (o pocos servidores). Si crece el número de transacciones, llega un punto donde no se puede agregar más potencia. Big Data permite agregar servidores baratos (escalado horizontal).

Cuello de botella en escritura/lectura: Oracle maneja bien miles de transacciones, pero BCP tiene millones por segundo (especialmente en Yape o pagos con POS). Una sola base se saturaría.

Procesamiento en lote vs. real: Oracle está diseñado para procesar consultas una por una. Big Data puede distribuir el procesamiento en cientos de máquinas a la vez (como Spark o Hadoop).

Razón de negocio:
El costo operativo y la oportunidad perdida. Si Oracle no puede procesar en tiempo real, BCP no podría detectar fraudes al instante, lo que generaría pérdidas millonarias y mala experiencia al cliente (por ejemplo, que rechace una compra legítima o que apruebe una fraudulenta).


```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales |Estructurado |Tiene filas y columnas fijas, cada celda tiene un tipo de dato definido (número, fecha, texto) |
| Un tweet sobre el precio del dólar | Semi-estructurado| Tiene texto libre (no estructurado) pero incluye metadatos como fecha, usuario, hashtags (estructurados en JSON)|
| Una foto del ticket de compra en Metro |No estructurado |Es una imagen, no tiene un formato de filas y columnas. Para extraer los datos habría que usar OCR |
| Un archivo JSON de la API de SUNAT |Semi-estructurado |Tiene una estructura de clave-valor, pero no es una tabla fija (puede tener campos anidados y variables) |
| Un audio de una llamada al call center de Claro |No estructurado | Es una señal de audio. Para analizarlo hay que transcribirlo a texto (estructurarlo)|
| Un archivo CSV de exportaciones del BCRP | Estructurado| Es un archivo de texto con separadores (comas) que representa una tabla perfectamente definida|
| Un video de seguridad de un supermercado |No estructurado | Es un flujo de frames (imágenes) y audio. No tiene una estructura de tabla|
| Un log de errores de un servidor web | Semi-estructurado|Tiene formato de línea de texto con patrones (fecha, nivel, mensaje), pero el mensaje puede ser libre |

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  Un clúster es un grupo de computadoras normales (llamadas nodos) que se conectan por red y trabajan juntas como si fueran una sola máquina muy poderosa.

Diferencia fundamental:

Memoria compartida: Varios procesadores usan la misma memoria RAM central. Ejemplo: una laptop con 2 núcleos y 8GB RAM. No escala más allá de unas decenas de procesadores.

Memoria distribuida: Cada computadora del clúster tiene su propia RAM y disco. Para procesar, se dividen los datos entre todas. Ejemplo: 100 computadoras, cada una con 16GB RAM, total 1.6TB RAM distribuida.
```
[MEMORIA COMPARTIDA]
     CPU1  CPU2  CPU3
       \    |    /
      ┌─────────┐
      │ RAM     │
      │ central │
      └─────────┘
(Límite: 1 servidor)

[MEMORIA DISTRIBUIDA - CLÚSTER]
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ Nodo 1  │  │ Nodo 2  │  │ Nodo N  │
   │ CPU+RAM │  │ CPU+RAM │  │ CPU+RAM │
   │ Disco   │  │ Disco   │  │ Disco   │
   └────┬────┘  └────┬────┘  └────┬────┘
        └────────────┼────────────┘
                 Red
(Puedo agregar miles de nodos)
```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron
Empresa latinoamericana que ha implementado Big Data exitosamente

Fuente consultada: Caso público de Mercado Libre (2022-2023) y artículos de iProfesional

Caso: Mercado Libre (Argentina, opera en Perú también)

Problema que tenían:
Con más de 140 millones de usuarios activos y 1,000 millones de búsquedas por día, no podían recomendar productos en tiempo real con sus bases de datos tradicionales. Las consultas tardaban segundos (mucho para estándares web) y no podían procesar datos no estructurados como imágenes de productos, reseñas de texto, y clics de navegación simultáneamente.

Solución Big Data:
Implementaron una arquitectura con:

Apache Spark para procesamiento distribuido en tiempo real

Delta Lake como capa de almacenamiento

Kafka para ingesta de eventos (búsquedas, clics, compras)

MongoDB para datos semi-estructurados

Esto les permitió unir datos estructurados (precios, stock) con no estructurados (comentarios, historial de navegación) en menos de 500 milisegundos.

_Respuesta_:  
```
Aumentaron las conversiones (ventas por recomendación) en un 25%

Redujeron los tiempos de búsqueda de 2 segundos a 300 ms

Pueden procesar 10 millones de eventos por segundo en horas pico (Cyber Monday)
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición | Depósito masivo de datos en su formato original (crudos), sin procesar|Almacén de datos ya procesados, limpiados y transformados para análisis |
| Tipo de datos |Todos: estructurados, semi-estructurados, no estructurados | Principalmente estructurados y agregados|
| Cuándo usarlo | Cuando aún no sabes qué preguntas harás; para exploración, machine learning, datos sin esquema fijo|Cuando ya sabes qué reportes y KPI necesitas; para BI tradicional y dashboards |
| Ejemplo de negocio | Una aerolínea guarda todos los sensores de aviones (millones por segundo) para después buscar patrones de fallas| El área comercial quiere el reporte de ventas por región y mes, siempre con el mismo formato|
| Herramienta típica |AWS S3, Azure Data Lake, Hadoop HDFS |Snowflake, Redshift, BigQuery, SQL Server |

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
1. Escalabilidad - Debe poder crecer agregando más servidores (escalado horizontal) sin rediseñar el sistema.

Si no se cumple: El sistema se satura y colapsa cuando crecen los datos.

2. Tolerancia a fallos - Si un servidor se cae, el sistema sigue funcionando sin perder datos.

Si no se cumple: Una falla eléctrica en un nodo detiene todo el procesamiento.

3. Procesamiento distribuido - Dividir los datos y el cómputo entre muchos nodos que trabajan en paralelo.

Si no se cumple: Todo el trabajo lo hace una sola máquina, creando cuello de botella.

4. Disponibilidad (alta) - Los datos deben estar accesibles 24/7 incluso con fallos.

Si no se cumple: Reportes de ventas no disponibles en hora punta, pérdida de ventas.

5. Consistencia eventual o flexible - Acepta que los datos no estén 100% actualizados en todos los nodos al mismo tiempo, pero al final lo estarán.

Si no se cumple: Para lograr consistencia perfecta, el sistema sería muy lento para escribir.


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
(Usaré caso público de una cadena de farmacias peruana como Inkafarma)

Problema: Inkafarma tiene pérdida de clientes frecuente ("churn") porque no pueden anticipar cuándo un cliente dejará de comprar. Actualmente solo ven históricos de compras en SQL Server y no integran otros datos como llamadas al call center, opiniones en redes sociales, o patrones de horario de compra.

Tipo de datos (V's):

Volumen: 5 millones de clientes activos, cada uno con 50 compras promedio al año

Velocidad: Se generan transacciones por minuto (necesario detección temprana)

Variedad: Datos de compras (estructurados), fotos de recetas (no estructurado), chats de WhatsApp (texto), datos de ubicación

Veracidad: Muchos datos mal ingresados (direcciones incompletas, productos mal codificados)

Propuesta inicial de solución:

Usar Apache Kafka para capturar transacciones en tiempo real desde los POS

Almacenar todo crudo en un Data Lake (ej. AWS S3) por 6 meses

Procesar con Spark diariamente para calcular probabilidad de abandono basado en: días sin compra, reclamos recientes, búsqueda de productos en la app

Visualizar en Power BI o Tableau un tablero de "riesgo de fuga" por distrito

Así podrían llamar proactivamente a clientes en riesgo con ofertas personalizadas.


```

---

### Pregunta 10
**Análisis crítico**: Lee el siguiente caso y responde las preguntas:

> "Una empresa de telecomunicaciones en Perú tiene 8 millones de clientes. Cada cliente genera en promedio 500 registros de datos al día (llamadas, SMS, datos móviles, pagos). La empresa quiere predecir qué clientes cancelarán su contrato en los próximos 30 días para ofrecerles retención proactiva."

**a)** ¿Cuántos registros se generan por día? ¿Por año?  
Por día: 8 millones clientes × 500 registros = 4,000 millones de registros/día (4 mil millones)

Por año: 4,000 millones × 365 = 1.46 billones de registros/año (1.46 × 10¹²)
**b)** ¿Qué tipo de datos están involucrados? Estructurados: montos de pago, duración de llamadas, MB consumidos

Semi-estructurados: logs de navegación web, registros de ubicación torre celular

No estructurados: grabaciones de llamadas al soporte, capturas de pantalla de la app 
**c)** ¿Cuáles de las 5 V's son más relevantes en este caso?  
Volumen: 4 mil millones por día es masivo

Velocidad: Necesitan predicción a 30 días, pero idealmente detectar señales de fuga en días o semanas

Valor: Cada cliente retenido vale cientos de soles, el ROI justifica el proyecto
**d)** ¿Qué tecnologías Big Data necesitarían para resolver este problema?  
Ingesta: Apache Kafka o Amazon Kinesis (para 4B eventos/día)

Almacenamiento: Data Lake (HDFS o S3) + Data Warehouse para datos agregados

Procesamiento: Apache Spark para ML distribuido (modelos de clasificación como Random Forest o XGBoost)

Orquestación: Apache Airflow para programar el entrenamiento semanal

Base operacional: Cassandra o HBase para consultar rápidamente el puntaje de riesgo por cliente

**e)** ¿Qué impacto ético podría tener esta solución? (pista: privacidad de datos)

_Respuesta_:  
```
Privacidad: Analizar ubicación en tiempo real, contenido de navegación y patrones de llamadas es invasivo. La empresa debe informar y pedir consentimiento.

Discriminación algorítmica: El modelo podría penalizar barrios pobres si los datos históricos están sesgados. Ej: ofrecer mejores retenciones a clientes de Miraflores que a los de San Juan de Lurigancho.

Manipulación: Ofrecer "retenciones proactivas" justo cuando el cliente quiere irse podría verse como acoso comercial.
```

---

## PARTE 2: REFLEXIÓN Y CONEXIÓN CON TU PROYECTO (2 preguntas adicionales)

### Pregunta 11 — Tu Proyecto
Describe brevemente el proyecto Big Data que tu grupo ha elegido:
- Nombre del proyecto
  
  Sistema de Predicción de Rotación de Personal (Attrition Risk) para una empresa de retail peruana
- Empresa o sector al que aplica
  
  Sector: Retail / Supermercados (ej. Plaza Vea, Tottus)


- Problema que resuelve
  
  La empresa tiene alta rotación de personal en tiendas (hasta 40% anual), especialmente en puestos de cajeros y reponedores. Actualmente usan Excel para ver quién renunció, pero no pueden anticipar quién está a punto de renunciar. Esto les cuesta en reclutamiento, entrenamiento (S/1,500 por nuevo empleado), y pérdida de productividad.

- ¿Cuáles de las 5 V's están presentes en los datos del proyecto?
  Volumen: 15,000 empleados, 50 variables por empleado × 12 meses → 9 millones de registros históricos

Velocidad: Datos generados diariamente (marcajes de asistencia, ventas por turno, quejas internas)

Variedad: Datos de RRHH (estructurados), emails internos (texto), grabaciones de capacitación (video no usado inicialmente), logs del sistema de planillas

Veracidad: Faltan datos de satisfacción, muchos registros inconsistentes (motivos de renuncia mal codificados)

Valor: Si reducimos la rotación en 10%, ahorramos S/2.25 millones al año (15,000 empleados × 40% rotación × 10% reducción × S/1,500 costo)

  
```

```

---

### Pregunta 12 — Arquitectura inicial
Dibuja (a mano o usando draw.io) una arquitectura inicial **muy básica** de cómo crees que debería funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualización.

*(Adjunta la imagen o el link de draw.io)*

[FUENTES DE DATOS]
    │
    ├──→ Base RRHH (SQL Server) ─→ [Kafka Connect] ─→┐
    ├──→ Logs de asistencia (CSV) ─→ [Kafka] ────────→┤
    ├──→ Sistema de ventas (API) ─→ [Kafka REST] ───→┤
    └──→ Encuestas internas (JSON) ─→ [Kafka] ───────→┘
                                                        │
                                                        ▼
                                            [Apache Kafka - Topic "empleados"]
                                                        │
                                                        ▼
                                            [Spark Streaming - Limpieza]
                                                        │
                                                        ├──→ [Data Lake (HDFS)] → Almacenamiento crudo
                                                        │
                                                        ▼
                                            [Feature Engineering - Spark]
                                                        │
                                                        ▼
                                            [Modelo ML - Random Forest]
                                                        │
                                                        ▼
                                            [Base de resultados - PostgreSQL]
                                                        │
                                                        ▼
                                            [Power BI Dashboard]
                                              │
                                              └──→ Alertas a RRHH (correo)
_Link o descripción de tu diagrama_:  
```
Los datos de diferentes fuentes se ingieren en tiempo real con Kafka

Spark Streaming limpia datos nulos y estandariza formatos

Los datos crudos se guardan en HDFS (Data Lake) por si necesitamos reprocesar

Spark Batch (cada noche) calcula características como "días desde última falta", "promedio de horas extra"

El modelo ML predice probabilidad de renuncia en los próximos 60 días

Los resultados se guardan en PostgreSQL para consultas rápidas

RRHH ve un dashboard en Power BI con empleados en riesgo y recibe alertas automáticas
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
