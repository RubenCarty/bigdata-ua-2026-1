# GUÍA DE RESPUESTAS PARA EL DOCENTE — SEMANA 1
## CONFIDENCIAL — Solo para uso del docente
### Big Data (DD283) | Universidad Autónoma del Perú

---

> **Nota para el docente**: Este documento contiene las respuestas modelo y los criterios de corrección detallados. Úsalo para revisar trabajos, dar retroalimentación y preparar la clase. NO distribuir a estudiantes.

---

## RESPUESTAS MODELO

### Pregunta 1 — Definición de Big Data vs. BD Tradicional

**Respuesta modelo completa**:

Big Data se refiere a conjuntos de datos tan voluminosos, variados y generados a tal velocidad que las herramientas de bases de datos tradicionales (relacionales como MySQL, SQL Server, Oracle) son incapaces de capturarlos, almacenarlos, procesarlos y analizarlos de manera eficiente.

**Diferencias clave**:

| Aspecto | BD Tradicional | Big Data |
|---------|---------------|----------|
| Escala | GB a pocos TB | TB, PB, ZB |
| Estructura | Solo estructurada | Cualquier tipo |
| Escalabilidad | Vertical (más RAM/CPU) | Horizontal (más servidores) |
| Procesamiento | Transaccional (ACID) | Batch + Streaming |
| Consistencia | Inmediata (ACID) | Eventual (BASE) |
| Costo | Alto por licencias | Bajo (open source + commodity hardware) |
| Ejemplo | Nómina de empleados | Análisis de comportamiento de 10M usuarios |

**Criterio de corrección**:
- Mención de volumen masivo: ✓ (3 pts)
- Diferencia de escalabilidad: ✓ (3 pts)
- Ejemplo concreto: ✓ (2 pts)
- Usa sus propias palabras: ✓ (2 pts)

**Respuestas parcialmente correctas a aceptar**:
- Si el estudiante menciona "los datos no caben en un solo servidor" → aceptar como correcto
- Si menciona "necesitas muchas máquinas trabajando juntas" → concepto correcto

**Respuestas incorrectas a rechazar**:
- "Big Data es una base de datos muy grande" → INCOMPLETO, pedir que desarrolle más
- Copiar la definición de Wikipedia literalmente → pedir reformular

---

### Pregunta 2 — Las 5 V's con ejemplos

**Respuesta modelo** (usando BCP como ejemplo):

| V | Definición | Ejemplo BCP |
|---|-----------|------------|
| **Volumen** | Cantidad de datos: millones/billones de registros | 10+ millones de transacciones diarias |
| **Velocidad** | Rapidez de generación y procesamiento | Transacciones en tiempo real, aprobación en < 2 segundos |
| **Variedad** | Tipos: estructurado, semi, no estructurado | Transacciones (SQL) + llamadas call center (audio) + tweets sobre el banco (texto) |
| **Veracidad** | Calidad y confiabilidad de los datos | ¿Es real esta transacción o es fraude? |
| **Valor** | Utilidad de negocio del análisis | Detectar fraude ahorra $X millones al año |

**Criterio de corrección**:
- 5 V's correctamente definidas: 10 pts (2 pts cada V)
- Ejemplo de empresa real o propia: +bonus feedback positivo
- Si el estudiante agrega una 6ta V (Variabilidad, Visualización): dar crédito extra

---

### Pregunta 3 — Limitaciones de Oracle para BCP

**Respuesta modelo completa**:

**Razones técnicas**:
1. **Escalabilidad vertical tiene límite**: Oracle en un servidor tiene un máximo de RAM y CPU. BCP genera millones de transacciones por día — un servidor Oracle necesitaría hardware exorbitantemente caro para manejar esa carga
2. **No puede manejar datos no estructurados**: Oracle es relacional — no puede almacenar nativamente audio de call centers, fotos de documentos, o análisis de texto de quejas en Twitter
3. **Latencia en análisis masivos**: Hacer un query de "¿cuál fue el patrón de fraude del último año analizando 500M transacciones?" en Oracle tomaría horas/días vs. minutos en Hadoop/Spark
4. **Costo de licencias**: Oracle cobra por número de CPUs. Para un cluster de 100 nodos, el costo sería prohibitivo. Hadoop/Spark es open source

**Razón de negocio**:
- Oracle no tiene las capacidades de Machine Learning integradas que necesita BCP para hacer credit scoring sobre millones de clientes ni detección de fraude en tiempo real

**Criterio de corrección**:
- Mínimo 3 razones técnicas válidas: 12 pts
- Razón de negocio: 4 pts
- Ejemplos cuantitativos (aunque aproximados): 4 pts adicionales

---

### Pregunta 4 — Clasificación de tipos de datos

**Respuestas correctas**:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Excel con ventas mensuales | **Estructurado** | Filas y columnas con tipos de dato fijos (fecha, número, texto) |
| Tweet sobre precio del dólar | **Semi-estructurado** | Tiene campos definidos (usuario, fecha, texto) pero el contenido del texto es libre |
| Foto del ticket de compra | **No estructurado** | Imagen binaria, sin esquema predefinido — necesita OCR para extraer datos |
| JSON de API SUNAT | **Semi-estructurado** | Tiene jerarquía y claves definidas pero sin esquema rígido tipo SQL |
| Audio de llamada call center | **No estructurado** | Señal de audio, necesita speech-to-text para procesarse |
| CSV de exportaciones BCRP | **Estructurado** | Columnas fijas, tipos de dato definidos, sin ambigüedad |
| Video de seguridad | **No estructurado** | Secuencia de imágenes, necesita visión computacional |
| Log de errores servidor web | **Semi-estructurado** | Tiene patrón (timestamp, nivel, mensaje) pero contenido libre |

**Errores comunes de estudiantes**:
- Clasificar JSON como "estructurado" → corregir: JSON es semi-estructurado porque no tiene esquema fijo tipo SQL, puede tener campos opcionales y anidados
- Clasificar CSV como "semi-estructurado" → depende: si tiene esquema fijo, es estructurado
- No saber clasificar los logs → orientar hacia semi-estructurado (tienen patrón reconocible)

---

### Pregunta 5 — Clusters y tipos de memoria

**Respuesta modelo**:

Un **clúster** es un conjunto de computadoras (nodos) interconectadas que trabajan juntas como si fueran una sola máquina más potente para procesar grandes volúmenes de datos.

**Memoria Compartida**:
```
[CPU 1] ─┐
[CPU 2] ─┤─→ [MEMORIA RAM COMPARTIDA] ─→ [DISCO]
[CPU 3] ─┘
```
- Todas las CPUs acceden a la misma RAM
- Comunicación rápida (bus de memoria)
- Límite físico: no puedes agregar RAM indefinidamente
- Ejemplo: Un servidor con 32 cores y 512GB RAM
- Paradigma: "scale-up" (hacer la máquina más grande)

**Memoria Distribuida**:
```
[NODO 1: CPU + RAM propia + Disco]
         ↕ Red de comunicación (Ethernet/InfiniBand)
[NODO 2: CPU + RAM propia + Disco]
         ↕
[NODO 3: CPU + RAM propia + Disco]
```
- Cada nodo tiene su propia RAM independiente
- Se comunican por red (más lento que bus de memoria)
- Sin límite teórico: puedes agregar nodos indefinidamente
- Ejemplo: Clúster Hadoop de 100 nodos con 64GB RAM cada uno = 6.4TB RAM total
- Paradigma: "scale-out" (agregar más máquinas)

**Por qué Hadoop usa memoria distribuida**: Porque es más barato comprar 100 máquinas normales que 1 supercomputadora con 6.4TB de RAM.

---

### Pregunta 6 — Caso de empresa latinoamericana

**Respuesta modelo** (el docente acepta cualquier caso real verificable):

**Caso: Mercado Libre — Sistema de Detección de Fraude**
- **Problema**: 100+ millones de transacciones mensuales en Latinoamérica, imposible revisar manualmente
- **Solución Big Data**: Implementaron Apache Spark + Machine Learning para analizar patrones de comportamiento en tiempo real. Cada transacción se evalúa en < 300ms contra modelos entrenados con billones de transacciones históricas
- **Resultados**: 60% de reducción en fraudes, ahorro de millones de dólares anuales

**Otros casos aceptables**:
- Falabella → análisis de comportamiento de compra
- Bancolombia → credit scoring alternativo para no-bancarizados
- SUNAT Perú → cruce de información para detección de evasión fiscal
- EsSalud → predicción de demanda de camas UCI (COVID-19)

**Criterio**: El caso debe incluir problema + solución + resultado. Penalizar si solo copia información sin mostrar comprensión.

---

### Pregunta 7 — Data Lake vs Data Warehouse

**Respuesta modelo**:

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| **Definición** | Repositorio de datos en su formato original (crudo), sin procesar | Repositorio de datos ya procesados, limpiados y estructurados para análisis |
| **Tipo de datos** | Cualquier tipo: raw, JSON, CSV, imágenes, audio | Solo datos estructurados y limpios |
| **Esquema** | Schema-on-read (el esquema se define al leer) | Schema-on-write (el esquema se define al escribir) |
| **Usuarios** | Data scientists, ingenieros de datos | Analistas de negocio, gerentes |
| **Cuándo usarlo** | Cuando no sabes aún cómo vas a usar los datos | Cuando ya sabes exactamente qué preguntas de negocio responder |
| **Ejemplo** | SUNAT guarda todos los archivos XML de declaraciones de impuestos sin procesar | BI de SUNAT con reportes de recaudación por sector, región, período |
| **Herramienta típica** | AWS S3, Azure Data Lake, GCP Cloud Storage | Amazon Redshift, Azure Synapse, Google BigQuery |
| **Costo** | Bajo (almacenamiento barato) | Alto (procesamiento optimizado = más caro) |

---

### Pregunta 8 — Requisitos de un sistema Big Data

**Respuesta modelo** (5 requisitos principales):

1. **Alta disponibilidad (HA)**: El sistema debe funcionar 24/7 sin interrupciones. Sin esto: si falla un nodo, el sistema completo deja de funcionar (catastrófico para e-commerce)

2. **Tolerancia a fallos (Fault Tolerance)**: Cuando un servidor falla, el sistema continúa funcionando con los demás nodos y los datos no se pierden. Sin esto: pérdida de datos y downtime

3. **Escalabilidad horizontal**: Capacidad de agregar más nodos al clúster sin cambiar la arquitectura. Sin esto: cuando el volumen crece, debes rediseñar todo el sistema desde cero

4. **Procesamiento paralelo**: Los datos se dividen y procesan simultáneamente en múltiples nodos. Sin esto: el procesamiento sería secuencial y tomaría días en vez de minutos

5. **Consistencia de datos**: Los datos deben ser correctos y coherentes aunque estén distribuidos en muchos nodos. Sin esto: decisiones de negocio basadas en datos incorrectos (fraude no detectado, stock mal calculado)

---

### Pregunta 9 — Problema en su empresa

**Criterio de evaluación** (no hay respuesta "incorrecta" aquí):
- El estudiante identifica un problema real relacionado con datos: ✓
- Conecta con las 5 V's: ✓
- La propuesta de solución es coherente con los conceptos aprendidos: ✓

**Respuesta típica esperada** (trabajador en retail, por ejemplo):
> "En mi empresa (tienda retail) generamos 50,000 tickets de venta diarios en Lima. El problema es que cuando gerencia quiere saber cuál producto se vendió más por zona geográfica, el análisis tarda 3 días porque hay que exportar datos de 5 sistemas diferentes a Excel. Con Big Data podríamos centralizar todos los datos en un Data Lake, procesarlos con Spark y tener un dashboard en tiempo real. Esto mejoraría las decisiones de reposición de stock y reduciría mermas."

---

### Pregunta 10 — Caso de telecomunicaciones

**a) Cálculo de registros**:
- Por día: 8,000,000 clientes × 500 registros = **4,000,000,000 (4 billones) registros/día**
- Por año: 4,000,000,000 × 365 = **1.46 trillones de registros/año**
- Tamaño aproximado: si cada registro pesa 1KB → **4 PB/año**
- **Esto es definitivamente Big Data** — ninguna BD relacional tradicional maneja esto

**b) Tipos de datos involucrados**:
- Estructurado: registros de llamadas (CDR), pagos, contratos
- Semi-estructurado: logs de red, datos de apps móviles (JSON)
- No estructurado: audios de llamadas al servicio al cliente, emails de quejas

**c) V's más relevantes**:
- **Volumen**: 4 billones de registros/día → claramente el más crítico
- **Velocidad**: Las llamadas se deben registrar en tiempo real
- **Variedad**: CDRs + audios + datos de red = formatos muy diferentes
- **Veracidad**: Los datos de red tienen errores técnicos, duplicados
- **Valor**: Predecir churn evita perder $X por cliente × miles de clientes = millones de dólares

**d) Tecnologías necesarias**:
- Ingesta en tiempo real: Apache Kafka
- Almacenamiento: HDFS (datos históricos) + Cassandra (acceso rápido por cliente)
- Procesamiento batch: Apache Hive para análisis histórico
- Procesamiento streaming: Apache Spark Streaming para alertas en tiempo real
- Machine Learning: PySpark MLlib para modelo de predicción de churn
- Visualización: Power BI para el dashboard de retención

**e) Impacto ético**:
- **Privacidad**: ¿Tienen derecho de analizar las llamadas de los clientes? → Ley 29733 de Protección de Datos Personales en Perú requiere consentimiento explícito
- **Sesgo algorítmico**: El modelo podría discriminar clientes por zona geográfica o nivel socioeconómico
- **Transparencia**: ¿Los clientes saben que están siendo perfilados?
- **Seguridad**: Los datos de comunicaciones son especialmente sensibles → riesgo de hackeo o filtración

---

## RÚBRICA DE CORRECCIÓN RÁPIDA

| Pregunta | Puntos | Criterio clave |
|---------|--------|---------------|
| P1 | 10 | Diferencia técnica clara, no solo "mucho datos" |
| P2 | 10 | 5 V's con ejemplos propios (no del libro) |
| P3 | 10 | Mínimo 3 razones técnicas específicas |
| P4 | 16 | 2 puntos por fila (clasificación + justificación) |
| P5 | 10 | Diagrama o esquema, diferencia clara entre ambos |
| P6 | 10 | Caso real, problema + solución + resultado |
| P7 | 10 | Tabla completa, diferencias correctas |
| P8 | 10 | 5 requisitos con consecuencias de no cumplirlos |
| P9 | 10 | Reflexión genuina sobre su empresa |
| P10 | 14 | 5 sub-preguntas: a(2) b(2) c(3) d(4) e(3) |
| **Total** | **110** | Normalizar a 20 puntos |

---

## RETROALIMENTACIÓN FRECUENTE

**Si el estudiante copia de internet**: Pedir que reescriba en sus propias palabras y entregue nuevamente (sin penalización primera vez, penalización del 50% segunda vez)

**Si el estudiante no conecta con ejemplos reales**: Dar feedback individual: "Tu respuesta es correcta académicamente, pero para el examen final necesitas aplicar esto a un caso real. Te invito a reflexionar cómo aplica en tu empresa."

**Si el estudiante no entiende la diferencia Data Lake / Data Warehouse**: Usar esta analogía: "El Data Lake es como tu escritorio donde guardas TODO sin ordenar. El Data Warehouse es como un archivador bien organizado con carpetas etiquetadas."

---

*Este documento es confidencial. No distribuir a los estudiantes.*
