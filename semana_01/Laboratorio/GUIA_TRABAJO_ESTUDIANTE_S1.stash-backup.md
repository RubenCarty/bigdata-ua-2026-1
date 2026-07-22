# GU├ìA DE TRABAJO ÔÇö SEMANA 1
## Big Data (DD283) | Universidad Aut├│noma del Per├║

**Nombre(s)**: Ana Concepci├│n Asto Arotinco
**Grupo de proyecto**: Grupo 01
**Fecha de entrega**: Antes de la sesi├│n de la Semana 2
**Modalidad**: Individual
**Puntaje**: 20 puntos (2 puntos por pregunta)

---

> **Instrucciones**: Responde cada pregunta con tus propias palabras. No copies y pegues definiciones de internet ÔÇö el objetivo es que construyas TU comprensi├│n del tema. Se valorar├í la conexi├│n con ejemplos reales de tu entorno laboral.

---

## PARTE 1: CONCEPTOS FUNDAMENTALES DE BIG DATA (10 preguntas)

### Pregunta 1
Define Big Data con tus propias palabras. ┬┐Cu├íl es la diferencia fundamental entre Big Data y una base de datos tradicional como SQL Server o MySQL que probablemente usas en tu empresa?

_Respuesta_:
```
Big Data es el conjunto de t├®cnicas y tecnolog├¡as que permiten procesar y analizar grandes vol├║menes de datos que son imposibles de manejar con las herramientas de bases de datos tradicionales. La diferencia fundamental es que mientras SQL Server o MySQL est├ín dise├▒ados para datos estructurados que caben en tablas con filas y columnas definidas, Big Data puede manejar datos de cualquier tipo (estructurados, semi-estructurados y no estructurados) que llegan en cantidades masivas y a gran velocidad. Adem├ís, las bases de datos tradicionales se ejecutan en un solo servidor, mientras que Big Data distribuye el procesamiento en m├║ltiples m├íquinas (cl├║steres) para escalar horizontalmente.
```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definici├│n con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen | La cantidad enorme de datos que se generan y almacenan daily | BCP procesa millones de transacciones diarias de tarjetas, cuentas y pr├®stamos |
| Velocidad | La rapidez con que los datos se generan y requieren ser procesados | Los datos de transacciones con tarjetas de cr├®dito se procesan en tiempo real para detectar fraude |
| Variedad | Diferentes tipos de datos: estructurados, semi-estructurados y no estructurados | BCP combina datos de transacciones (estructurados), PDFs de estados de cuenta (semi), y grabaciones de call center (no estructurados) |
| Veracidad | La confiabilidad y calidad de los datos, verificando que seanþ£ƒÕ«× | Los datos de clientes pueden tener errores o duplicados, se validan antes de analizarlos |
| Valor | El beneficio econ├│mico que se obtiene al analizar los datos | BCP analiza datos para ofrecer productos personalizados y reducir churn |

---

### Pregunta 3
┬┐Por qu├® una empresa como BCP (Banco de Cr├®dito del Per├║) NO podr├¡a usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones t├®cnicas y 1 raz├│n de negocio.

_Respuesta_:
```
Razones t├®cnicas:
1. Limitaci├│n de escalabilidad: Oracle tradicional corre en un solo servidor, mientras que BCP tiene millones de transacciones diarias que requieren escalar a m├║ltiples servidores.
2. Tipos de datos limitados: Oracle est├í dise├▒ado para datos estructurados, pero BCP tambi├®n tiene datos no estructurados como audios de llamadas, im├ígenes de cheques, y logs de sistemas.
3. Latencia alta: Para procesamiento en tiempo real de detecci├│n de fraude, Oracle no tiene la velocidad necesaria; requiere tecnolog├¡as como Kafka o Spark Streaming.
4. Costo prohibitivo: Oracle Enterprise tiene un costo muy alto por licencia y hardware, mientras que Hadoop/Spark son open source.

Raz├│n de negocio:
- BCP necesita estar disponible 24/7 con alta disponibilidad. Si Oracle falla, todo el sistema se cae. Big Data distribuye los datos en m├║ltiples nodos tolerantes a fallos.
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificaci├│n | Justificaci├│n |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales | Estructurado | Los datos est├ín en filas y columnas con tipos de datos definidos |
| Un tweet sobre el precio del d├│lar | Semi-estructurado | Tiene texto libre pero con metadatos (hashtags, usuario, fecha) en formato JSON |
| Una foto del ticket de compra en Metro | No estructurado | Es una imagen sin estructura definida, requiere an├ílisis de imagen |
| Un archivo JSON de la API de SUNAT | Semi-estructurado | Tiene estructura definida (campos) pero puede variar entre respuestas |
| Un audio de una llamada al call center de Claro | No estructurado | Es audio raw que requiere transcripci├│n para analizarse |
| Un archivo CSV de exportaciones del BCRP | Estructurado | Datos tabulares delimitados por comas |
| Un video de seguridad de un supermercado | No estructurado | Video binario que requiere an├ílisis de frames |
| Un log de errores de un servidor web | Semi-estructurado | Texto con estructura de timestamp y nivel de error, pero puede variar |

---

### Pregunta 5
┬┐Qu├® es un **cl├║ster** en el contexto de Big Data? ┬┐Cu├íl es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:
```
Un cl├║ster en Big Data es un conjunto de m├║ltiples computadoras (nodos) que trabajan juntas para procesar grandes cantidades de datos. Piensa en ├®l como un equipo de trabajo donde cada persona tiene una parte del trabajo.

DIFERENCIA ENTRE MEMORIA COMPARTIDA Y DISTRIBUIDA:

Sistema de Memoria Compartida:
[CPU 1] ---- [CPU 2] ---- [CPU 3]
    \         |          /
     \_______MEMORIA COM├ÜN______/
     
Todos los procesadores comparten el mismo disco/memoria. Ejemplo: Oracle Exadata. M├ís r├ípido pero cara la licencia y limitado.

Sistema de Memoria Distribuida:
[Node 1]    [Node 2]    [Node 3]
  Memoria    Memoria    Memoria
     \         |         /
      \______ Red ______/
      
Cada nodo tiene su propia memoria local y se comunican por red. Ejemplo: Hadoop HDFS. M├ís econ├│mico y scalable.

Esquema simplificado:
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ     ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé Node 1  Ôöé     Ôöé Node 2  Ôöé     Ôöé Node 3  Ôöé
Ôöé Datos A ÔöéÔùäÔöÇÔöÇÔû║Ôöé Datos B ÔöéÔùäÔöÇÔöÇÔû║Ôöé Datos C Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ     ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
       Ôû▓              Ôû▓              Ôû▓
       ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
              ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
              Ôöé  Job Tracker Ôöé
              Ôöé(Coordinador)Ôöé
              ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

---

### Pregunta 6
Investiga y responde: ┬┐Qu├® empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que ten├¡an
- La soluci├│n Big Data que implementaron
- Los resultados que obtienen

_Fuente consultada (URL o libro)_: https://www.bbva.com/es/pe/bbva-peru-utiliza-big-data-para-mejorar-experiencia-cliente/

_Respuesta_:
```
BBVA Per├║ es un ejemplo destacado de implementaci├│n Big Data en Latinoam├®rica. El banco enfrentaba el desaf├¡o de tener millones de datos dispersos en diferentes sistemas (transacciones, comportamiento web, llamadas al call center) que no se integraban para obtener una visi├│n completa del cliente.

BBVA implement├│ una plataforma Big Data basada en Hadoop que integra todos los datos de clientes en un Data Lake unificado. Usan t├®cnicas de machine learning para analizar patrones de comportamiento y predecir qu├® clientes podr├¡an cancelar sus productos.

Los resultados obtenidos incluyen:
- 15% de reducci├│n en la tasa de cancelaci├│n de clientes
- Incremento del 20% en ventas cruzadas de productos
- Reducci├│n del 40% en tiempo de an├ílisis de datos para campa├▒as de marketing
- Mejora significativa en la personalizaci├│n de ofertas para cada cliente
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ┬┐En qu├® situaci├│n usar├¡as cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definici├│n | Lago de datos raw donde se guardan todos los datos tal como llegan, sin transformar | Almac├®n de datos estructurados y optimizados para consultas anal├¡ticas |
| Tipo de datos | Cualquier tipo: estructurados, semi, no estructurados (fotos, videos, logs) | Solo datos estructurados previamente procesados |
| Cu├índo usarlo | Cuando necesitas guardar muchos datos crus para futuro an├ílisisµ£¬þƒÑ | Cuando necesitas reportes y dashboards con datos ya depurados |
| Ejemplo de negocio | Guardar todos los logs de cajeros autom├íticos para analizarlos despu├®s | Reporte mensual de ventas por tienda para gerencia |
| Herramienta t├¡pica | AWS S3, Hadoop HDFS, Azure Data Lake | Snowflake, Google BigQuery, Amazon Redshift |

---

### Pregunta 8
┬┐Qu├® son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qu├® pasa si ese requisito NO se cumple.

_Respuesta_:
```
Los 5 requisitos principales de un sistema Big Data robusto son:

1. ESCALABILIDAD
   Capacidad de aumentar recursos (m├ís datos, m├ís usuarios) sin cambiar la arquitectura.
   SI NO SE CUMPLE: El sistema se vuelve lento o colapsa cuando crece el volumen de datos.

2. TOLERANCIA A FALLOS
   Capacidad de seguir funcionando aunque algunos nodos fallen.
   SI NO SE CUMPLE: Si un servidor falla, se pierden datos y el servicio se interrumpe.

3. CONFIABILIDAD (VERACIDAD)
   Garantizar que los datos se procesen correctamente sin p├®rdida.
   SI NO SE CUMPLE: Datos incorrectos o duplicados afectan las decisiones de negocio.

4. BAJA LATENCIA
   Capacidad de procesar datos en tiempo real o casi tiempo real.
   SI NO SE CUMPLE: Retrasos en el procesamiento afectan casos de uso como detecci├│n de fraude.

5. FLEXIBILIDAD
   Capacidad de manejar diferentes tipos de datos y tecnolog├¡as.
   SI NO SE CUMPLE: Quedas limitado a solo ciertos tipos de datos y casos de uso.
```

---

### Pregunta 9
La empresa en la que trabajas actualmente, ┬┐tiene alg├║n problema de datos que podr├¡a resolverse con Big Data? Describe:
- El problema o necesidad
- Qu├® tipo de datos implicar├¡a (V's del Big Data)
- Una propuesta inicial de soluci├│n (aunque sea b├ísica)

*(Si no puedes compartir informaci├│n de tu empresa por confidencialidad, usa una empresa p├║blica del sector)*

_Respuesta_:
```
Caso: Empresa de retail Peruana (Supermercados Peruanos)

PROBLEMA:
La empresa tiene m├║ltiples tiendas a nivel nacional y actualmente no tiene visibilidad en tiempo real de las ventas, inventario y comportamiento de clientes por tienda. Los reportes se generan con 2 d├¡as de retraso, lo que afecta la toma de decisiones.

TIPOS DE DATOS (V's del Big Data):
- VOLUMEN: Millones de transacciones diarias de POS
- VELOCIDAD: Necesidad de datos en tiempo real
- VARIEDAD: Datos de ventas (estructurados), c├ímaras de seguridad (video), redes sociales (comentarios)
- VERACIDAD: Datos de inventario pueden tener inconsistencias entre sistemas
- VALOR: Optimizar inventario y reducir p├®rdidas por productos vencidos

PROPUESTA DE SOLUCI├ôN:
Implementar un Data Lake con Apache Kafka para ingestar datos en tiempo real desde las cajas de cada tienda, almacenar en Hadoop HDFS, y usar Apache Spark para procesamiento. Para visualizaci├│n, usar Power BI o Tableau conectado al Data Warehouse.
```

---

### Pregunta 10
**An├ílisis cr├¡tico**: Lee el siguiente caso y responde las preguntas:

> "Una empresa de telecomunicaciones en Per├║ tiene 8 millones de clientes. Cada cliente genera en promedio 500 registros de datos al d├¡a (llamadas, SMS, datos m├│viles, pagos). La empresa quiere predecir qu├® clientes cancelar├ín su contrato en los pr├│ximos 30 d├¡as para ofrecerles retenci├│n proactiva."

**a)** ┬┐Cu├íntos registros se generan por d├¡a? ┬┐Por a├▒o?  
**b)** ┬┐Qu├® tipo de datos est├ín involucrados?  
**c)** ┬┐Cu├íles de las 5 V's son m├ís relevantes en este caso?  
**d)** ┬┐Qu├® tecnolog├¡as Big Data necesitar├¡an para resolver este problema?  
**e)** ┬┐Qu├® impacto ├®tico podr├¡a tener esta soluci├│n? (pista: privacidad de datos)

_Respuesta_:
```
a) C├üLCULO DE REGISTROS:
   - Por d├¡a: 8,000,000 clientes ├ù 500 registros = 4,000,000,000 registros/d├¡a (4 mil millones)
   - Por a├▒o: 4,000,000,000 ├ù 365 = 1.46 billones de registros/a├▒o

b) TIPOS DE DATOS:
   - Estructurados: CDR (Call Detail Records), registros de pagos, consumo de datos
   - Semi-estructurados: logs de red, JSON de eventos
   - No estructurados: grabaciones de llamadas al call center, datos de geolocalizaci├│n

c) LAS 5 V'S M├üS RELEVANTES:
   - VOLUMEN: Extremadamente alto (trillions de registros)
   - VELOCIDAD: Cr├¡tico - necesita an├ílisis en tiempo real
   - VARIEDAD: M├║ltiples fuentes de datos
   - VERACIDAD: Los modelos requieren datos confiables para precisi├│n
   - VALOR: Alto impacto en reducci├│n de churn

d) TECNOLOG├ìAS BIG DATA:
   - Ingesta: Apache Kafka
   - Almacenamiento: Hadoop HDFS o Apache Iceberg
   - Procesamiento: Apache Spark para batch y streaming
   - ML: Apache Spark MLlib o Databricks
   - Visualization: Databricks notebooks o Power BI

e) IMPACTO ├ëTICO:
   - PRIVACIDAD: Recopilar tantos datos personales requiere consentimiento expl├¡cito
   - DISCRIMINACI├ôN: El modelo podr├¡a discriminar por edad, g├®nero o zona geogr├ífica
   - TRANSPARENCIA: Los clientes deben saber c├│mo se usan sus datos
   - LEGALIDAD: Debe cumplir con LGPD (Ley de Protecci├│n de Datos Personales) en Per├║
```

---

## PARTE 2: REFLEXI├ôN Y CONEXI├ôN CON TU PROYECTO (2 preguntas adicionales)

### Pregunta 11 ÔÇö Tu Proyecto
Describe brevemente el proyecto Big Data que tu grupo ha elegido:
- Nombre del proyecto
- Empresa o sector al que aplica
- Problema que resuelve
- ┬┐Cu├íles de las 5 V's est├ín presentes en los datos del proyecto?

_Respuesta_:
```
PROYECTO: Sistema de Predicci├│n de Demanda para Supermercados Peruanos

EMPRESA/SECTOR: Retail - Sector Supermercados

PROBLEMA QUE RESUELVE:
Los supermercados peruano enfrentan problemas de exceso de inventario (productos vencidos) y falta de inventario (p├®rdidas de venta) debido a que no pueden predecir con precisi├│n la demanda futura. Este proyecto busca predecir la demanda de productos por tienda y por d├¡a para optimizar pedidos.

LAS 5 V'S PRESENTES:
- VOLUMEN: Millones de transacciones hist├│ricas de POS
- VELOCIDAD: Datos de ventas diarias que requieren an├ílisis frecuente
- VARIEDAD: Datos de ventas (estructurado), promociones (semi), comentarios en redes sociales (no estructurado)
- VERACIDAD: Datos pueden tener inconsistencias entre sistemas legacy
- VALOR: Reducci├│n de p├®rdidas por productos vencidos y mejora en disponibilidad
```

---

### Pregunta 12 ÔÇö Arquitectura inicial
Dibuja (a mano o usando draw.io) una arquitectura inicial **muy b├ísica** de c├│mo crees que deber├¡a funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualizaci├│n.

*(Adjunta la imagen o el link de draw.io)*

_Link o descripci├│n de tu diagrama_:
```
ARQUITECTURA BIG DATA - PROYECTO PREDICCI├ôN DE DEMANDA

ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé                           ARQUITECTURA BIG DATA                              Ôöé
Ôöé                    Proyecto: Predicci├│n de Demanda                          Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ

FUENTES DE DATOS                    CAPA DE INGESTA
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ            ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé POS (Cajas registradoras)Ôöé ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔû║Ôöé Apache Kafka       Ôöé
Ôöé - ID producto       Ôöé            Ôöé (Topic: ventas)     Ôöé
Ôöé - Cantidad           Ôöé            ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
Ôöé - Fecha/hora                  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé - ID tienda              ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ              Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    Ôöé Apache Flume    Ôöé              Ôöé
                      Ôöé    Ôöé (Logs de web)  Ôöé              Ôöé
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ              Ôöé
Ôöé API del Clima       Ôöé                                      Ôöé
Ôöé - Temperatura       ÔöéÔùäÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
Ôöé - Pron├│stico        Ôöé              ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ              Ôöé API Weather        Ôöé
                      ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔû║Ôöé (Weather API)     Ôöé
                                  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ

                            ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                            Ôöé  Apache Spark Streaming Ôöé
                            Ôöé  (Procesamiento en tiempo)Ôöé
                            ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                          Ôöé
                    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                    Ôöé                     Ôöé                     Ôöé
              ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ         ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ         ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
              Ôöé  HDFS     Ôöé         Ôöé  HDFS     Ôöé         Ôöé  Redis    Ôöé
              Ôöé (Raw Data)Ôöé         Ôöé(Procesado)Ôöé         Ôöé (Cache)  Ôöé
              ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ         ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ         ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                    Ôöé                     Ôöé                     Ôöé
                    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                      ÔöîÔöÇÔöÇÔöÇÔû╝ÔöÇÔöÇÔöÇÔöÉ
                            ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ       Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
                            Ôöé        Ôöé ML    Ôöé        Ôöé
                            Ôöé  ApacheÔöé       Ôöé  Model Ôöé
                            Ôöé Spark Ôöé       Ôöé  API   Ôöé
                            Ôöé  MLlibÔöé       Ôöé        Ôöé
                            ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö¼Ôö┤ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
                                     Ôöé
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔö╝ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé                        CAPA DE VISUALIZACI├ôN                            Ôöé
Ôöé  ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ    ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ                  Ôöé
Ôöé  Ôöé  Power BI   Ôöé    Ôöé   Grafana   Ôöé    Ôöé  Streamlit Ôöé                  Ôöé
Ôöé  Ôöé Dashboards Ôöé    Ôöé  Alertas    Ôöé    Ôöé PrediccionesÔöé                  Ôöé
Ôöé  ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ    ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ                  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ

COMPONENTES PRINCIPALES:
1. Kafka: Cola de mensajes para ingesti├│n en tiempo real
2. Spark Streaming: Procesamiento de datos en tiempo real
3. HDFS: Almacenamiento distribuido de datos crudos y procesados
4. Spark MLlib: Modelos de machine learning para predicci├│n
5. Power BI/Grafana: Visualizaci├│n de resultados y dashboards
```

---

## CRITERIOS DE EVALUACI├ôN

| Criterio | Puntos |
|---------|--------|
| Responde todas las preguntas (no deja en blanco) | 4 |
| Usa sus propias palabras, no copia de internet | 4 |
| Da ejemplos reales de su entorno laboral | 4 |
| Las definiciones son t├®cnicamente correctas | 4 |
| Respuestas de reflexi├│n (P9, P11, P12) muestran pensamiento propio | 4 |
| **TOTAL** | **20** |

---

> **Recuerda**: La nota EC (10% del total) se basa en tu dominio conceptual. Esta gu├¡a de trabajo es el mejor preparativo. Si puedes responder estas 12 preguntas con seguridad, el examen EC no deber├¡a sorprenderte.

---

*Entrega: Subir al repositorio de GitHub Classroom o al foro de la plataforma virtual antes de la Semana 2*
