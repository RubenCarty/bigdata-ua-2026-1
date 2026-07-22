# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

| | |
|---|---|
| **Nombre** | Ana Concepción Asto Arotinco |
| **Grupo de proyecto** | Grupo 01 |
| **Fecha de entrega** | Antes de la sesión de la Semana 2 |
| **Modalidad** | Individual |
| **Puntaje** | 20 puntos (2 puntos por pregunta) |
| **Docente** | Mg. Rubén Quispe Llacctarimay |

---

## PARTE 1: CONCEPTOS FUNDAMENTALES DE BIG DATA

---

### Pregunta 1 — Definición de Big Data

Big Data es el conjunto de técnicas y tecnologías que permiten procesar y analizar grandes volúmenes de datos que son imposibles de manejar con herramientas tradicionales.

La diferencia fundamental con bases de datos como SQL Server o MySQL es:

- **SQL Server / MySQL** → manejan datos estructurados en tablas, corren en un solo servidor, tienen límites físicos de almacenamiento y procesamiento.
- **Big Data** → puede manejar cualquier tipo de dato (estructurado, semi-estructurado y no estructurado), distribuye el trabajo en múltiples máquinas (clústeres), escala horizontalmente sin límite fijo.

En otras palabras: SQL Server es como una libreta organizada, Big Data es como una red de miles de libretas que trabajan juntas al mismo tiempo.

---

### Pregunta 2 — Las 5 V's del Big Data (ejemplo: BCP)

| V | Definición con mis palabras | Ejemplo en BCP |
|---|---------------------------|----------------|
| **Volumen** | La cantidad enorme de datos que se generan y almacenan | BCP procesa millones de transacciones diarias de tarjetas, cuentas y préstamos |
| **Velocidad** | La rapidez con que los datos llegan y necesitan procesarse | Las transacciones con tarjeta se procesan en milisegundos para detectar fraude en tiempo real |
| **Variedad** | Los diferentes tipos de datos: estructurados, semi y no estructurados | BCP combina registros de transacciones (estructurado), PDFs de estados de cuenta (semi) y grabaciones del call center (no estructurado) |
| **Veracidad** | La confiabilidad y calidad de los datos | Los datos de clientes pueden tener errores o duplicados; se validan antes de analizarlos |
| **Valor** | El beneficio real que se obtiene de analizar los datos | BCP analiza patrones de comportamiento para ofrecer productos personalizados y reducir cancelaciones |

---

### Pregunta 3 — ¿Por qué BCP no puede usar solo Oracle?

**Razones técnicas:**

1. **Escalabilidad limitada:** Oracle corre en un solo servidor. BCP tiene millones de transacciones diarias y no puede simplemente "comprar un servidor más grande" indefinidamente — llega un límite físico y económico.
2. **Tipos de datos restringidos:** Oracle maneja datos estructurados en tablas, pero BCP también tiene audios de llamadas al call center, imágenes de cheques escaneados y logs de sistemas que no encajan en filas y columnas.
3. **Latencia alta para tiempo real:** Para detectar fraude en milisegundos, Oracle no tiene la velocidad necesaria. Se necesitan tecnologías como Apache Kafka o Spark Streaming que procesan datos en tiempo real.

**Razón de negocio:**

BCP debe operar 24/7 sin interrupciones. Oracle concentrado en un solo servidor es un punto único de falla — si cae, todo el sistema bancario se cae. Big Data distribuye los datos en múltiples nodos tolerantes a fallos, garantizando disponibilidad continua.

---

### Pregunta 4 — Clasificación de tipos de datos

| Dato | Clasificación | Justificación |
|------|--------------|---------------|
| Excel con ventas mensuales | **Estructurado** | Datos organizados en filas y columnas con tipos definidos (número, fecha, texto) |
| Tweet sobre el precio del dólar | **Semi-estructurado** | Texto libre pero con metadatos estructurados en JSON (usuario, fecha, hashtags) |
| Foto del ticket de compra en Metro | **No estructurado** | Imagen binaria sin esquema; requiere OCR o análisis visual para extraer datos |
| Archivo JSON de la API de SUNAT | **Semi-estructurado** | Tiene campos definidos pero la estructura puede variar entre respuestas |
| Audio de llamada al call center de Claro | **No estructurado** | Audio raw; requiere transcripción automática para poder analizarse |
| CSV de exportaciones del BCRP | **Estructurado** | Datos tabulares delimitados por comas con columnas fijas y tipos definidos |
| Video de seguridad de supermercado | **No estructurado** | Video binario por frames; requiere visión computacional para interpretar |
| Log de errores de servidor web | **Semi-estructurado** | Tiene un patrón (timestamp + nivel + mensaje) pero el contenido varía libremente |

---

### Pregunta 5 — Clúster, Memoria Compartida vs Memoria Distribuida

Un **clúster** en Big Data es un grupo de computadoras (llamadas nodos) que trabajan juntas como si fueran una sola máquina para procesar grandes cantidades de datos. Cada nodo hace una parte del trabajo y luego se combinan los resultados.

**Diferencia entre los dos sistemas:**

**Sistema de Memoria Compartida:**
```
  [CPU 1] [CPU 2] [CPU 3]
      \       |       /
       [ MEMORIA COMÚN ]
```
Todos los procesadores acceden al mismo banco de memoria. Es más rápido porque no hay que comunicarse por red, pero tiene un límite físico claro y es muy costoso escalar. Ejemplo: servidores Oracle Exadata.

**Sistema de Memoria Distribuida:**
```
  [Nodo 1]   [Nodo 2]   [Nodo 3]
  [Mem A ]   [Mem B ]   [Mem C ]
      \           |         /
        [ Red de comunicación ]
           [ Nodo Master ]
```
Cada nodo tiene su propia memoria local. Se comunican por red para coordinar el trabajo. Es más económico, escala fácilmente agregando más nodos y es tolerante a fallos. Ejemplo: Hadoop HDFS, Spark.

**Conclusión:** Big Data usa memoria distribuida porque permite escalar horizontalmente (agregar más máquinas) en lugar de depender de una sola máquina muy cara.

---

### Pregunta 6 — Empresa latinoamericana con Big Data exitoso: BBVA Perú

> *Fuente: https://www.bbva.com/es/pe/bbva-peru-utiliza-big-data-para-mejorar-experiencia-cliente/*

**El problema que tenían:**
BBVA Perú acumulaba millones de datos de clientes dispersos en sistemas distintos — transacciones, comportamiento en la web, llamadas al call center — pero no podían cruzar esa información para entender al cliente de forma completa. Los análisis tardaban días y las campañas de marketing eran genéricas.

**La solución Big Data que implementaron:**
Implementaron una plataforma Big Data basada en Hadoop que integra todos los datos de clientes en un Data Lake unificado. Aplicaron técnicas de machine learning para analizar patrones de comportamiento y predecir qué clientes podrían abandonar el banco.

**Los resultados que obtuvieron:**
- 15% de reducción en la tasa de cancelación de clientes
- 20% de incremento en ventas cruzadas de productos financieros
- 40% de reducción en tiempo de análisis para campañas de marketing
- Personalización real de ofertas según el perfil de cada cliente

---

### Pregunta 7 — Data Lake vs Data Warehouse

| | Data Lake | Data Warehouse |
|--|-----------|----------------|
| **Definición** | Almacén de datos crudos tal como llegan, sin transformar ni estructurar | Almacén de datos ya estructurados, limpios y optimizados para consultas |
| **Tipo de datos** | Cualquier tipo: estructurados, semi-estructurados, no estructurados (fotos, videos, logs) | Solo datos estructurados, previamente procesados y depurados |
| **Cuándo usarlo** | Cuando necesitas guardar muchos datos de distintas fuentes para analizarlos después | Cuando necesitas reportes y dashboards rápidos con datos confiables |
| **Ejemplo de negocio** | Guardar todos los logs de cajeros automáticos de BCP para analizarlos en el futuro | Reporte mensual de ventas por tienda y por región para la gerencia |
| **Herramienta típica** | AWS S3, Hadoop HDFS, Azure Data Lake Storage | Snowflake, Google BigQuery, Amazon Redshift |

---

### Pregunta 8 — Requisitos de un sistema Big Data robusto

**1. ESCALABILIDAD**
Capacidad de aumentar recursos (más datos, más usuarios) sin rediseñar la arquitectura — solo agregando más nodos.
*Si no se cumple:* El sistema se vuelve lento o colapsa cuando crece el volumen de datos.

**2. TOLERANCIA A FALLOS**
Capacidad de seguir funcionando aunque uno o varios nodos fallen, replicando los datos en múltiples máquinas.
*Si no se cumple:* Si un servidor se cae, se pierden datos y el servicio se interrumpe completamente.

**3. CONFIABILIDAD (VERACIDAD)**
Garantizar que los datos se procesen correctamente sin pérdida ni corrupción, manteniendo consistencia.
*Si no se cumple:* Datos incorrectos o duplicados llevan a decisiones de negocio equivocadas.

**4. BAJA LATENCIA**
Capacidad de procesar y responder en tiempo real o casi tiempo real según el caso de uso.
*Si no se cumple:* Retrasos en el procesamiento hacen inútiles casos como detección de fraude o alertas de stock.

**5. FLEXIBILIDAD**
Capacidad de adaptarse a nuevos tipos de datos, nuevas fuentes y nuevas tecnologías sin reconstruir todo.
*Si no se cumple:* Quedas atrapado con las tecnologías iniciales y no puedes incorporar nuevas fuentes de datos.

---

### Pregunta 9 — Caso: Supermercados Peruanos

**El problema:**
La cadena de supermercados tiene tiendas a nivel nacional pero no tiene visibilidad en tiempo real de ventas ni de inventario. Los reportes se generan con 2 días de retraso, lo que genera dos problemas: exceso de inventario en productos que no se venden (generando merma y vencimiento) y quiebres de stock en productos de alta demanda (perdiendo ventas).

**V's del Big Data involucradas:**
- **Volumen:** Millones de transacciones diarias en puntos de venta de todas las tiendas
- **Velocidad:** Necesidad de datos en tiempo real para reaccionar ante picos de demanda
- **Variedad:** Datos de ventas (estructurado), cámaras de seguridad (video no estructurado), comentarios en redes sociales (texto no estructurado)
- **Veracidad:** Inconsistencias entre el sistema POS, el sistema de inventario y el ERP
- **Valor:** Optimizar pedidos, reducir merma y mejorar disponibilidad de productos

**Propuesta de solución:**
Implementar Apache Kafka para capturar datos en tiempo real desde las cajas registradoras, almacenar en un Data Lake con Hadoop HDFS (arquitectura Medallion: Bronze → Silver → Gold), procesar con Apache Spark, y visualizar en Power BI con dashboards por tienda y por producto.

---

### Pregunta 10 — Análisis crítico: Empresa de telecomunicaciones

**a) Cálculo de registros:**
- Por día: 8,000,000 clientes × 500 registros = **4,000,000,000 registros/día (4 mil millones)**
- Por año: 4,000,000,000 × 365 = **1.46 billones de registros/año**

**b) Tipos de datos involucrados:**
- **Estructurados:** CDR (Call Detail Records), registros de pagos, consumo de datos móviles
- **Semi-estructurados:** Logs de red en formato JSON, eventos del sistema
- **No estructurados:** Grabaciones de llamadas al call center, datos de geolocalización en tiempo real

**c) V's más relevantes:**
- **Volumen:** Extremadamente alto (billones de registros anuales)
- **Velocidad:** Crítico — necesita análisis en tiempo real para actuar antes de que el cliente cancele
- **Variedad:** Múltiples fuentes de datos con formatos distintos
- **Veracidad:** Los modelos de ML requieren datos limpios y confiables para ser precisos
- **Valor:** Alto impacto directo en reducción de churn y retención de clientes

**d) Tecnologías Big Data necesarias:**
- **Ingesta:** Apache Kafka (captura de eventos en tiempo real)
- **Almacenamiento:** Hadoop HDFS o Apache Iceberg (Data Lake)
- **Procesamiento:** Apache Spark (batch y streaming)
- **Machine Learning:** Spark MLlib o Databricks (modelo de predicción de churn)
- **Visualización:** Databricks Notebooks o Power BI (dashboard de riesgo de cancelación)

**e) Impacto ético:**
- **Privacidad:** Recopilar llamadas, ubicación y comportamiento requiere consentimiento explícito del usuario
- **Discriminación:** El modelo podría discriminar a clientes por zona geográfica, edad o nivel socioeconómico
- **Transparencia:** Los clientes tienen derecho a saber qué datos se usan y con qué propósito
- **Legalidad:** Debe cumplir con la **Ley N° 29733 — Ley de Protección de Datos Personales** del Perú

---

## PARTE 2: REFLEXIÓN Y CONEXIÓN CON EL PROYECTO

---

### Pregunta 11 — Proyecto Big Data del Grupo

**Nombre del proyecto:** Sistema de Predicción de Demanda para Supermercados Peruanos

**Empresa / Sector:** Retail — Sector Supermercados (caso basado en Supermercados Peruanos S.A.)

**Problema que resuelve:**
Los supermercados peruanos pierden dinero por dos razones: exceso de inventario que genera productos vencidos y merma, y quiebres de stock que generan pérdidas de venta y clientes insatisfechos. El proyecto busca predecir la demanda de productos por tienda y por día para optimizar los pedidos automáticamente.

**V's presentes en el proyecto:**

| V | Cómo aplica al proyecto |
|---|------------------------|
| Volumen | Millones de transacciones históricas de POS de todas las tiendas |
| Velocidad | Datos de ventas que se actualizan cada hora para ajustar predicciones |
| Variedad | Ventas (estructurado) + promociones (semi) + comentarios en redes sociales (no estructurado) |
| Veracidad | Inconsistencias entre el sistema POS y el sistema de inventario legacy |
| Valor | Reducción directa de merma y mejora en disponibilidad de productos |

---

### Pregunta 12 — Arquitectura inicial del proyecto

```
┌─────────────────────────────────────────────────────────────┐
│              ARQUITECTURA BIG DATA                          │
│         Predicción de Demanda — Supermercados               │
└─────────────────────────────────────────────────────────────┘

FUENTES DE DATOS
├── POS / Cajas registradoras (ventas en tiempo real)
├── Sistema de inventario (stock actual por tienda)
├── API del clima (temperatura y pronóstico)
└── Redes sociales (tendencias y comentarios)
         │
         ▼
CAPA DE INGESTA
└── Apache Kafka (Topic: ventas, Topic: inventario)
         │
         ▼
CAPA DE ALMACENAMIENTO (Data Lake — Arquitectura Medallion)
├── Bronze → Datos crudos tal como llegan
├── Silver → Datos limpios y enriquecidos
└── Gold   → Métricas de negocio y predicciones
         │
         ▼
CAPA DE PROCESAMIENTO
├── Apache Spark Streaming (tiempo real)
└── Spark MLlib (modelo de predicción de demanda)
         │
         ▼
CAPA DE VISUALIZACIÓN
├── Power BI (Dashboard ejecutivo por tienda)
├── Grafana (Alertas de quiebre de stock)
└── API REST (Integración con sistema de pedidos)
```

**Descripción de componentes:**
1. **Kafka** — captura los datos de ventas en tiempo real desde cada caja registradora
2. **Spark Streaming** — procesa el flujo de datos para actualizar predicciones cada hora
3. **HDFS / Delta Lake** — almacena toda la historia de ventas con arquitectura Medallion
4. **Spark MLlib** — entrena el modelo de predicción de demanda con datos históricos
5. **Power BI** — muestra al gerente de tienda qué productos pedir y cuántos

---

## CRITERIOS DE EVALUACIÓN

| Criterio | Puntos |
|---------|--------|
| Responde todas las preguntas (no deja en blanco) | 4 |
| Usa sus propias palabras, no copia de internet | 4 |
| Da ejemplos reales de su entorno | 4 |
| Las definiciones son técnicamente correctas | 4 |
| Respuestas de reflexión (P9, P11, P12) muestran pensamiento propio | 4 |
| **TOTAL** | **20** |

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 1 | 2026-1*
*Mg. Rubén Quispe Llacctarimay | Estudiante: Ana Concepción Asto Arotinco*
