<<<<<<< HEAD
# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Noé Jesús Paredes Hilario  
**Grupo de proyecto**: _______________________________________________  
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
Big Data es el manejo de grandes cantidades de datos que se generan constantemente y que pueden servir para obtener información útil.

La diferencia con bases de datos como SQL Server o MySQL es que estas trabajan mejor con datos organizados y cantidades más manejables, mientras que Big Data está preparado para procesar volúmenes mucho más grandes y variados de información.
```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen |Se refiere a la gran cantidad de datos que se generan y almacenan. Tb, Pb, Zb |Una empresa de ventas registra miles de compras de clientes todos los días. |
| Velocidad |Es la rapidez con la que se generan y procesan los datos.|Los pagos realizados por una aplicación se registran casi al instante. |
| Variedad |Los datos pueden venir en diferentes formatos - SQL·JSON·Video |Una empresa recibe información de formularios, correos y redes sociales. |
| Veracidad |Significa que los datos deben ser confiables y correctos. |La empresa verifica que los datos de sus clientes estén actualizados.|
| Valor |Es el beneficio que se obtiene al analizar los datos.|Analizar las ventas ayuda a tomar mejores decisiones sobre qué productos ofrecer.|

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
Gran cantidad de datos: El banco maneja millones de transacciones todos los días, por lo que una base de datos tradicional podría volverse lenta.
Velocidad de procesamiento: Los clientes esperan que sus operaciones se registren casi en tiempo real, algo que requiere tecnologías más avanzadas.
Diferentes tipos de información: Además de transacciones, el banco maneja datos de aplicaciones móviles, páginas web y otros sistemas que generan información variada.

Razón de negocio: El banco necesita analizar los datos rápidamente para mejorar sus servicios, detectar posibles fraudes y tomar decisiones más rápidas para sus clientes.
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales |Estructurado |Tiene datos organizados en filas y columnas.|
| Un tweet sobre el precio del dólar |No estructurado |Contiene texto libre que puede variar mucho |
| Una foto del ticket de compra en Metro |No estructurado |Es una imagen y los datos no están organizados en tablas.|
| Un archivo JSON de la API de SUNAT |Semi-estructurado |Tiene una estructura definida, pero no es una tabla tradicional. |
| Un audio de una llamada al call center de Claro |No estructurado |Es información en formato de audio. |
| Un archivo CSV de exportaciones del BCRP |Estructurado |Los datos están ordenados en filas y columnas. |
| Un video de seguridad de un supermercado |No estructurado |La información está en formato de video |
| Un log de errores de un servidor web |Semi-estructurado |Sigue un formato definido, pero no siempre está organizado como una base de datos.|

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
```
                    CLÚSTER EN BIG DATA

     Es un grupo de computadoras (nodos) que trabajan juntas
          para almacenar y procesar grandes volúmenes de datos.


1. SISTEMA DE MEMORIA COMPARTIDA

      +--------+    +--------+    +--------+
      | CPU 1  |    | CPU 2  |    | CPU 3  |
      +--------+    +--------+    +--------+
            \           |           /
             \          |          /
              +------------------+
              | MEMORIA ÚNICA    |
              | COMPARTIDA       |
              +------------------+

Características:
✓ Todos los procesadores usan la misma memoria.
✓ El intercambio de datos es rápido.
✗ Tiene límites de crecimiento.
✗ Si la memoria falla, afecta a todo el sistema.


2. SISTEMA DE MEMORIA DISTRIBUIDA (USADO EN BIG DATA)

      +----------------+      +----------------+
      |    NODO 1      |      |    NODO 2      |
      | CPU + MEMORIA  |<---->| CPU + MEMORIA  |
      +----------------+      +----------------+
               ^                      ^
               |                      |
               v                      v
      +----------------+
      |    NODO 3      |
      | CPU + MEMORIA  |
      +----------------+

Características:
✓ Cada nodo tiene su propia memoria.
✓ Los datos se distribuyen entre varios equipos.
✓ Se pueden agregar más nodos fácilmente.
✓ Mayor capacidad para procesar grandes cantidades de datos.
✓ Si un nodo falla, los demás pueden seguir trabajando.

Conclusión:
Big Data utiliza principalmente MEMORIA DISTRIBUIDA porque permite
trabajar con enormes volúmenes de datos de manera escalable y eficiente.
```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro)_: _______________

_Respuesta_:  
```
Una empresa peruana que ha implementado Big Data con éxito es Interbank. El problema que tenía era la necesidad de analizar grandes volúmenes de datos para gestionar mejor sus agencias, cajeros y otros canales de atención. Como solución, implementó una plataforma de Big Data y Data Science con modelos analíticos avanzados. Gracias a ello, pudo identificar zonas con mayor potencial de negocio, optimizar sus canales de atención y mejorar la toma de decisiones basadas en datos.

Fuente : https://www.analytics.pe/caso-de-exito-interbank/
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición |Almacena grandes cantidades de datos en su formato original. |Almacena datos organizados y preparados para análisis y reportes. |
| Tipo de datos |Estructurados, semi-estructurados y no estructurados. |Principalmente datos estructurados.|
| Cuándo usarlo |Cuando la empresa necesita guardar todo tipo de información para futuros análisis, incluso si aún no sabe cómo la utilizará. |Cuando la empresa necesita generar reportes, indicadores y análisis para apoyar la toma de decisiones. |
| Ejemplo de negocio |Una empresa de telecomunicaciones almacena llamadas, mensajes, audios y datos de navegación de sus clientes para analizar comportamientos y mejorar sus servicios. |Un banco almacena las transacciones de sus clientes para generar reportes financieros, analizar ventas y evaluar riesgos. |
| Herramienta típica |adoop, Amazon S3, Azure Data Lake. |SQL Server, Oracle, Amazon Redshift |

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
| Requisito               | Explicación                         | ¿Qué pasa si no se cumple?|

| Escalabilidad           | Permite que el sistema crezca.      | El sistema se vuelve lento.                 |
| Disponibilidad          | Los datos están siempre accesibles. | No se puede acceder a la información.       |
| Tolerancia a fallos     | Sigue funcionando ante errores.     | Se interrumpen los procesos.                |
| Rendimiento             | Procesa datos rápidamente.          | Las consultas tardan mucho.                 |
| Seguridad               | Protege la información.             | Los datos pueden ser robados o modificados. |

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
| Aspecto                                         | Respuesta                                                                                                                                                                                                                                |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problema o necesidad**                        | En el Ejército del Perú se maneja información de personal, inventarios, equipos, proyectos de investigación y documentos administrativos que se encuentran en diferentes sistemas, lo que dificulta el análisis y la toma de decisiones. |
| **Tipo de datos implicaría (V's del Big Data)** | **Volumen:** gran cantidad de registros. **Variedad:** documentos, bases de datos, imágenes y reportes. **Velocidad:** actualización constante de la información.                                                                        |
| **Propuesta inicial de solución**               | Implementar una plataforma Big Data que centralice la información de las diferentes áreas para facilitar consultas, generar reportes automáticos y apoyar la toma de decisiones de manera más rápida y eficiente.                        |

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
a) ¿Cuántos registros se generan por día? ¿Por año?**

* Por día: 8,000,000 × 500 = **4,000,000,000 registros**
* Por año: 4,000,000,000 × 365 = **1,460,000,000,000 registros**

b) ¿Qué tipo de datos están involucrados?**

Datos estructurados y semi-estructurados, como llamadas, SMS, consumo de datos móviles, pagos y registros de clientes.

c) ¿Cuáles de las 5 V's son más relevantes en este caso?**

Volumen:por la enorme cantidad de registros.
Velocidad:los datos se generan continuamente.
Valor:porque ayudan a predecir qué clientes podrían cancelar el servicio.

d) ¿Qué tecnologías Big Data necesitarían para resolver este problema?**

Herramientas como **Hadoop**, **Spark**, bases de datos distribuidas y algoritmos de **Machine Learning** para analizar los datos y predecir cancelaciones.

e) ¿Qué impacto ético podría tener esta solución?**

Puede afectar la **privacidad de los clientes** si sus datos personales son utilizados sin la debida protección o consentimiento. Por ello, la empresa debe garantizar la seguridad y confidencialidad de la información.

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
=======
# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Noé Jesús Paredes Hilario  
**Grupo de proyecto**: _______________________________________________  
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
Big Data es el manejo de grandes cantidades de datos que se generan constantemente y que pueden servir para obtener información útil.

La diferencia con bases de datos como SQL Server o MySQL es que estas trabajan mejor con datos organizados y cantidades más manejables, mientras que Big Data está preparado para procesar volúmenes mucho más grandes y variados de información.
```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen |Se refiere a la gran cantidad de datos que se generan y almacenan. Tb, Pb, Zb |Una empresa de ventas registra miles de compras de clientes todos los días. |
| Velocidad |Es la rapidez con la que se generan y procesan los datos.|Los pagos realizados por una aplicación se registran casi al instante. |
| Variedad |Los datos pueden venir en diferentes formatos - SQL·JSON·Video |Una empresa recibe información de formularios, correos y redes sociales. |
| Veracidad |Significa que los datos deben ser confiables y correctos. |La empresa verifica que los datos de sus clientes estén actualizados.|
| Valor |Es el beneficio que se obtiene al analizar los datos.|Analizar las ventas ayuda a tomar mejores decisiones sobre qué productos ofrecer.|

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
Gran cantidad de datos: El banco maneja millones de transacciones todos los días, por lo que una base de datos tradicional podría volverse lenta.
Velocidad de procesamiento: Los clientes esperan que sus operaciones se registren casi en tiempo real, algo que requiere tecnologías más avanzadas.
Diferentes tipos de información: Además de transacciones, el banco maneja datos de aplicaciones móviles, páginas web y otros sistemas que generan información variada.

Razón de negocio: El banco necesita analizar los datos rápidamente para mejorar sus servicios, detectar posibles fraudes y tomar decisiones más rápidas para sus clientes.
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales |Estructurado |Tiene datos organizados en filas y columnas.|
| Un tweet sobre el precio del dólar |No estructurado |Contiene texto libre que puede variar mucho |
| Una foto del ticket de compra en Metro |No estructurado |Es una imagen y los datos no están organizados en tablas.|
| Un archivo JSON de la API de SUNAT |Semi-estructurado |Tiene una estructura definida, pero no es una tabla tradicional. |
| Un audio de una llamada al call center de Claro |No estructurado |Es información en formato de audio. |
| Un archivo CSV de exportaciones del BCRP |Estructurado |Los datos están ordenados en filas y columnas. |
| Un video de seguridad de un supermercado |No estructurado |La información está en formato de video |
| Un log de errores de un servidor web |Semi-estructurado |Sigue un formato definido, pero no siempre está organizado como una base de datos.|

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
```
                    CLÚSTER EN BIG DATA

     Es un grupo de computadoras (nodos) que trabajan juntas
          para almacenar y procesar grandes volúmenes de datos.


1. SISTEMA DE MEMORIA COMPARTIDA

      +--------+    +--------+    +--------+
      | CPU 1  |    | CPU 2  |    | CPU 3  |
      +--------+    +--------+    +--------+
            \           |           /
             \          |          /
              +------------------+
              | MEMORIA ÚNICA    |
              | COMPARTIDA       |
              +------------------+

Características:
✓ Todos los procesadores usan la misma memoria.
✓ El intercambio de datos es rápido.
✗ Tiene límites de crecimiento.
✗ Si la memoria falla, afecta a todo el sistema.


2. SISTEMA DE MEMORIA DISTRIBUIDA (USADO EN BIG DATA)

      +----------------+      +----------------+
      |    NODO 1      |      |    NODO 2      |
      | CPU + MEMORIA  |<---->| CPU + MEMORIA  |
      +----------------+      +----------------+
               ^                      ^
               |                      |
               v                      v
      +----------------+
      |    NODO 3      |
      | CPU + MEMORIA  |
      +----------------+

Características:
✓ Cada nodo tiene su propia memoria.
✓ Los datos se distribuyen entre varios equipos.
✓ Se pueden agregar más nodos fácilmente.
✓ Mayor capacidad para procesar grandes cantidades de datos.
✓ Si un nodo falla, los demás pueden seguir trabajando.

Conclusión:
Big Data utiliza principalmente MEMORIA DISTRIBUIDA porque permite
trabajar con enormes volúmenes de datos de manera escalable y eficiente.
```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro)_: _______________

_Respuesta_:  
```
Una empresa peruana que ha implementado Big Data con éxito es Interbank. El problema que tenía era la necesidad de analizar grandes volúmenes de datos para gestionar mejor sus agencias, cajeros y otros canales de atención. Como solución, implementó una plataforma de Big Data y Data Science con modelos analíticos avanzados. Gracias a ello, pudo identificar zonas con mayor potencial de negocio, optimizar sus canales de atención y mejorar la toma de decisiones basadas en datos.

Fuente : https://www.analytics.pe/caso-de-exito-interbank/
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición |Almacena grandes cantidades de datos en su formato original. |Almacena datos organizados y preparados para análisis y reportes. |
| Tipo de datos |Estructurados, semi-estructurados y no estructurados. |Principalmente datos estructurados.|
| Cuándo usarlo |Cuando la empresa necesita guardar todo tipo de información para futuros análisis, incluso si aún no sabe cómo la utilizará. |Cuando la empresa necesita generar reportes, indicadores y análisis para apoyar la toma de decisiones. |
| Ejemplo de negocio |Una empresa de telecomunicaciones almacena llamadas, mensajes, audios y datos de navegación de sus clientes para analizar comportamientos y mejorar sus servicios. |Un banco almacena las transacciones de sus clientes para generar reportes financieros, analizar ventas y evaluar riesgos. |
| Herramienta típica |adoop, Amazon S3, Azure Data Lake. |SQL Server, Oracle, Amazon Redshift |

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
| Requisito               | Explicación                         | ¿Qué pasa si no se cumple?|

| Escalabilidad           | Permite que el sistema crezca.      | El sistema se vuelve lento.                 |
| Disponibilidad          | Los datos están siempre accesibles. | No se puede acceder a la información.       |
| Tolerancia a fallos     | Sigue funcionando ante errores.     | Se interrumpen los procesos.                |
| Rendimiento             | Procesa datos rápidamente.          | Las consultas tardan mucho.                 |
| Seguridad               | Protege la información.             | Los datos pueden ser robados o modificados. |

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
| Aspecto                                         | Respuesta                                                                                                                                                                                                                                |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problema o necesidad**                        | En el Ejército del Perú se maneja información de personal, inventarios, equipos, proyectos de investigación y documentos administrativos que se encuentran en diferentes sistemas, lo que dificulta el análisis y la toma de decisiones. |
| **Tipo de datos implicaría (V's del Big Data)** | **Volumen:** gran cantidad de registros. **Variedad:** documentos, bases de datos, imágenes y reportes. **Velocidad:** actualización constante de la información.                                                                        |
| **Propuesta inicial de solución**               | Implementar una plataforma Big Data que centralice la información de las diferentes áreas para facilitar consultas, generar reportes automáticos y apoyar la toma de decisiones de manera más rápida y eficiente.                        |

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
a) ¿Cuántos registros se generan por día? ¿Por año?**

* Por día: 8,000,000 × 500 = **4,000,000,000 registros**
* Por año: 4,000,000,000 × 365 = **1,460,000,000,000 registros**

b) ¿Qué tipo de datos están involucrados?**

Datos estructurados y semi-estructurados, como llamadas, SMS, consumo de datos móviles, pagos y registros de clientes.

c) ¿Cuáles de las 5 V's son más relevantes en este caso?**

Volumen:por la enorme cantidad de registros.
Velocidad:los datos se generan continuamente.
Valor:porque ayudan a predecir qué clientes podrían cancelar el servicio.

d) ¿Qué tecnologías Big Data necesitarían para resolver este problema?**

Herramientas como **Hadoop**, **Spark**, bases de datos distribuidas y algoritmos de **Machine Learning** para analizar los datos y predecir cancelaciones.

e) ¿Qué impacto ético podría tener esta solución?**

Puede afectar la **privacidad de los clientes** si sus datos personales son utilizados sin la debida protección o consentimiento. Por ello, la empresa debe garantizar la seguridad y confidencialidad de la información.

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
>>>>>>> c01f654f9a11075fb9f5ec7728accf12406f02b5
