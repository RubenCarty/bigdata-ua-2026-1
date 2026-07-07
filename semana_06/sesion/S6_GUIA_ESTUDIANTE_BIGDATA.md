# S6 — GUÍA DE TRABAJO DEL ESTUDIANTE: Machine Learning en Big Data
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 6: Algoritmos de ML, Pipelines y Ética en Datos Masivos

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha de entrega** | ______________________________________________ |
| **Tiempo estimado** | 1.5 horas |
| **Puntaje total** | 100 puntos |

---

## INSTRUCCIONES DE USO

- Responde con tus propias palabras. Las respuestas copiadas de compañeros anulan el puntaje.
- Tienes 1.5 horas para completar todas las secciones.
- Para la Sección A, marca con una **X** la alternativa correcta.
- Para las secciones C y D, justifica siempre con argumentos técnicos específicos.
- Entrega en PDF en el aula virtual o como PR en el repositorio del curso.

> **Nota:** Esta guía evalúa lo aprendido en la Semana 6. No incluye respuestas — las respuestas están en el documento del docente.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts c/u)

### Preguntas básicas (1-4)

**1.** Un banco quiere predecir si un cliente pagará o no su préstamo el próximo mes. ¿Qué tipo de Machine Learning se debe aplicar?

- a) Aprendizaje por refuerzo, porque el modelo mejora con cada error
- b) Aprendizaje no supervisado, porque los datos del banco son privados
- c) Aprendizaje supervisado de clasificación, porque la variable objetivo es binaria (paga/no paga)
- d) Aprendizaje no supervisado de clustering, porque se agrupan los clientes por perfil

**Respuesta:** [ ]

---

**2.** ¿Qué representa el "entrenamiento" de un modelo de Machine Learning?

- a) El proceso de instalar y configurar las librerías de ML en el servidor
- b) El ajuste automático de los parámetros del modelo usando datos históricos con respuestas conocidas
- c) La validación del modelo con datos nuevos que no se usaron antes
- d) La generación de gráficos y reportes de las predicciones del modelo

**Respuesta:** [ ]

---

**3.** En el pipeline de ML, ¿en qué paso se divide el dataset en "entrenamiento" y "prueba"?

- a) En el primer paso, antes de explorar los datos
- b) En el paso de limpieza y preprocesamiento de datos
- c) Después del preprocesamiento e ingeniería de características, antes de entrenar
- d) Después de entrenar el modelo, para evaluar su rendimiento final

**Respuesta:** [ ]

---

**4.** ¿Cuál de las siguientes es la principal ventaja del árbol de decisión frente a la regresión logística?

- a) Siempre produce mayor accuracy que la regresión logística
- b) Es más rápido de entrenar con datasets de más de 1 millón de filas
- c) Sus reglas de decisión son visualmente interpretables y pueden explicarse a personas sin conocimiento técnico
- d) No requiere preprocesamiento de los datos (no hay que escalar ni codificar variables)

**Respuesta:** [ ]

---

### Preguntas intermedias (5-7)

**5.** Un modelo de detección de tumores cancerígenos tiene 95% de accuracy. Sin embargo, el médico descubre que el modelo predice "benigno" para todos los casos. ¿Qué problema tiene este modelo?

- a) Overfitting: el modelo ha memorizado los datos de entrenamiento
- b) El modelo tiene class imbalance y 95% son tumores benignos; su accuracy alta es engañosa
- c) El modelo necesita más datos de entrenamiento para aprender la diferencia
- d) El modelo tiene underfitting porque no llegó al 100% de accuracy

**Respuesta:** [ ]

---

**6.** Para el modelo de detección de tumores de la pregunta anterior, ¿cuál métrica debe optimizarse prioritariamente?

- a) Accuracy — es la métrica estándar para todos los modelos de clasificación
- b) Precision — porque el costo de una biopsia innecesaria (falso positivo) es alto
- c) Recall — porque perder un tumor cancerígeno real (falso negativo) puede costar la vida del paciente
- d) F1-Score — porque equilibra la Precision y el Recall en partes iguales

**Respuesta:** [ ]

---

**7.** El algoritmo K-Means necesita que el usuario especifique el valor de K antes de ejecutar. ¿Qué técnica se usa para determinar cuál es el mejor valor de K?

- a) Se prueba con K=1 y se aumenta hasta que la accuracy llegue al 100%
- b) El método del codo (elbow method): se busca el K donde la inercia deja de disminuir rápidamente
- c) Se calcula K como la raíz cuadrada del número total de filas del dataset
- d) Se usa un árbol de decisión previo para determinar automáticamente el número óptimo de clusters

**Respuesta:** [ ]

---

### Preguntas avanzadas (8-10)

**8.** Un Data Scientist entrena un modelo de aprobación de crédito con datos de 2015-2020. Al analizar las métricas por grupo, encuentra que el modelo tiene F1-Score de 0.87 para clientes de Lima y 0.51 para clientes de provincias. ¿Cuál es la explicación más probable?

- a) El modelo tiene overfitting porque usó demasiados datos de entrenamiento
- b) Los datos de entrenamiento tenían más clientes de Lima, por lo que el modelo no aprendió bien los patrones de comportamiento de clientes de provincias
- c) La regresión logística es el algoritmo incorrecto para este problema; debería usarse K-Means
- d) El modelo necesita más features (columnas) para mejorar el F1-Score en provincias

**Respuesta:** [ ]

---

**9.** ¿Cuál es la diferencia entre el sesgo de selección y el sesgo de proxy en modelos de ML?

- a) El sesgo de selección ocurre en modelos supervisados; el sesgo de proxy en modelos no supervisados
- b) El sesgo de selección ocurre cuando los datos de entrenamiento no representan a toda la población; el sesgo de proxy cuando una variable aparentemente neutra esconde discriminación indirecta
- c) El sesgo de selección siempre favorece a la clase minoritaria; el sesgo de proxy siempre perjudica a la clase mayoritaria
- d) El sesgo de selección y el sesgo de proxy son el mismo fenómeno con distintos nombres según el país

**Respuesta:** [ ]

---

**10.** ¿En qué situación es preferible usar Spark MLlib en lugar de scikit-learn para entrenar un modelo de ML?

- a) Cuando se requiere mayor accuracy, porque Spark usa más núcleos de procesamiento
- b) Cuando el dataset tiene más de 50 columnas (features), independientemente del número de filas
- c) Cuando los datos no caben en la RAM de una sola máquina y deben procesarse de forma distribuida en un clúster
- d) Cuando se trabaja con algoritmos de deep learning que requieren GPU, ya que scikit-learn no soporta GPU

**Respuesta:** [ ]

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### Parte 1: Completa los espacios en blanco (10 puntos | 2 pts c/u)

**1.** El aprendizaje supervisado requiere un dataset con _______________ conocidas (la variable Y), mientras que el aprendizaje no supervisado busca _______________ en los datos sin que alguien haya etiquetado los ejemplos previamente.

**2.** En el pipeline de ML, la función `train_test_split()` divide los datos en dos conjuntos: los de _______________ (80%) que usa el modelo para aprender, y los de _______________ (20%) que se usan para medir cómo funciona el modelo con datos nuevos nunca vistos.

**3.** Un modelo que obtiene 99% de accuracy en entrenamiento pero solo 58% en prueba sufre de _______________, lo que significa que el modelo _______________ los datos de entrenamiento en lugar de aprender la regla general.

**4.** La métrica _______________ responde a la pregunta "de todos los casos positivos REALES, ¿cuántos detectó el modelo?", mientras que _______________ responde a "de todos los casos que el modelo predijo como positivos, ¿cuántos eran realmente positivos?".

**5.** En Spark MLlib, el componente _______________ convierte múltiples columnas en un único vector numérico requerido por los algoritmos de ML, y el objeto _______________ permite encadenar múltiples transformaciones en una secuencia reproducible.

---

### Parte 2: Relaciona las columnas (10 puntos | 1 pt c/par)

Escribe en la columna derecha el número del concepto de la columna izquierda que corresponde:

| # | CONCEPTO | Letra | DESCRIPCIÓN |
|---|---------|-------|-------------|
| 1 | Sesgo histórico | ___ | A. Agrupa datos sin etiquetas en K grupos minimizando la distancia intra-cluster |
| 2 | Overfitting | ___ | B. El modelo refleja discriminación pasada presente en los datos históricos de entrenamiento |
| 3 | K-Means | ___ | C. Evalúa el modelo en múltiples particiones del dataset para tener una estimación más robusta del error |
| 4 | Random Forest | ___ | D. El modelo memoriza los datos de entrenamiento y falla con datos nuevos |
| 5 | Recall | ___ | E. Combina múltiples árboles de decisión para producir predicciones más robustas y resistentes al overfitting |
| 6 | Cross-validation | ___ | F. Porcentaje de casos positivos reales que el modelo detecta correctamente |
| 7 | VectorAssembler | ___ | G. Componente de Spark MLlib que convierte columnas en un vector de features |
| 8 | Sesgo de proxy | ___ | H. Variable aparentemente neutra que esconde discriminación indirecta hacia un grupo |
| 9 | StandardScaler | ___ | I. Transforma cada columna numérica para que tenga media 0 y desviación estándar 1 |
| 10 | Matriz de confusión | ___ | J. Tabla 2×2 que muestra TP, TN, FP, FN para evaluar un clasificador binario |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

### Pregunta C1 (8 puntos)

Interbank está evaluando implementar un modelo de ML para ofrecer préstamos personales pre-aprobados a través de su app. El equipo de Data Science propone dos modelos:

- **Modelo A (Regresión Logística):** accuracy 78%, F1 0.71, tiempo de entrenamiento: 2 minutos
- **Modelo B (Random Forest 500 árboles):** accuracy 84%, F1 0.79, tiempo de entrenamiento: 45 minutos

a) ¿Cuál modelo recomendarías para este caso? Justifica con al menos 2 argumentos técnicos y 1 argumento de negocio. *(3 puntos)*

b) El equipo de Compliance de Interbank pide que el modelo sea "explicable" — que se pueda justificar a un cliente POR QUÉ su préstamo fue rechazado. ¿Cambia tu recomendación? ¿Por qué? *(3 puntos)*

c) ¿Qué información adicional (que no está en la descripción anterior) necesitarías saber antes de elegir el modelo definitivo? Menciona al menos 2 preguntas críticas. *(2 puntos)*

**Tu respuesta:**

---

### Pregunta C2 (8 puntos)

Una startup de RRHH en Lima desarrolla un modelo de ML que analiza CVs y predice cuáles candidatos son los "mejores" para empresas tecnológicas. El modelo fue entrenado con los CVs de las 500 personas más exitosas (según sus empleadores) en empresas de tecnología en Lima entre 2018-2024.

a) Identifica 3 tipos de sesgo potencial en este modelo con su causa específica. *(4 puntos)*

b) ¿Qué impacto concreto tendría este sesgo para un candidato con las siguientes características: bachiller de una universidad pública de Lima, mujer, 27 años, sin experiencia en empresas "conocidas" pero con 3 proyectos personales en GitHub? *(2 puntos)*

c) Propón 2 acciones técnicas (cambios en el proceso de ML, no en las políticas de la empresa) para reducir el sesgo identificado. *(2 puntos)*

**Tu respuesta:**

---

### Pregunta C3 — Mini caso con análisis (14 puntos)

**Escenario — Alerta temprana de abandono escolar en la UGEL Lima:**

La Unidad de Gestión Educativa Local (UGEL) de Lima quiere implementar un sistema de ML para identificar estudiantes en riesgo de abandonar el colegio antes de que ocurra, con el objetivo de asignar tutorías preventivas.

**Dataset disponible (por estudiante):**
- Asistencia mensual (%)
- Notas promedio por bimestre
- Número de materias desaprobadas
- Cambios de colegio en los últimos 3 años
- Si el estudiante trabaja (sí/no)
- Distancia al colegio en km
- Nivel socioeconómico de la familia (A/B/C/D/E)
- Si tiene acceso a internet en casa
- Si recibe beca o apoyo económico

**Variable objetivo:** `abandono = 1` (abandonó ese año) / `abandono = 0` (continuó)

**Preguntas de análisis:**

**C3a.** ¿Qué tipo de ML es este problema? ¿Cuál sería la distribución esperada de la clase positiva (abandono=1) en Lima? ¿Por qué eso importa para elegir las métricas de evaluación? *(3 puntos)*

**C3b.** Para el sistema de tutorías (presupuesto limitado para 300 estudiantes de riesgo por mes), ¿optimizarías Precision o Recall? Justifica con el costo real de cada tipo de error (Falso Positivo y Falso Negativo en este contexto). *(4 puntos)*

**C3c.** Identifica las 3 variables del dataset que generan mayor riesgo de sesgo. Para cada una, explica el tipo de sesgo y su consecuencia en la práctica. *(4 puntos)*

**C3d.** ¿El modelo debería publicarse (hacerse visible a los padres y estudiantes)? ¿Qué riesgo ético específico tiene que los estudiantes sepan que fueron marcados como "alto riesgo de abandono"? *(3 puntos)*

**Tu respuesta:**

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

### Caso profesional: Clasificación de riesgo crediticio en Caja Huancayo

**Caja Huancayo** es una de las microfinancieras más grandes del Perú, con presencia en 12 regiones. Tiene 850,000 clientes activos y procesa 2,800 solicitudes de crédito al mes, principalmente de agricultores, comerciantes de mercado y micro empresarios.

El equipo de analítica de datos implementó en 2024 un modelo de Random Forest para clasificar el riesgo crediticio en tres categorías: BAJO (aprobado automáticamente), MEDIO (revisión humana) y ALTO (rechazado automáticamente).

**Resultados del modelo al cabo de 6 meses:**

| Métricas del Modelo | Valor |
|---------------------|-------|
| Accuracy global | 81% |
| F1-Score clase BAJO | 0.88 |
| F1-Score clase MEDIO | 0.72 |
| F1-Score clase ALTO | 0.53 |
| F1-Score Lima | 0.84 |
| F1-Score Sierra | 0.61 |
| F1-Score Selva | 0.49 |

**Métricas de negocio a los 6 meses:**
- Mora en créditos aprobados automáticamente (BAJO): 3.8%
- Mora en créditos aprobados tras revisión humana (MEDIO): 5.1%
- Reclamos de clientes por rechazo: +180% respecto al sistema anterior

**D1.** Análisis profundo del modelo *(10 puntos)*

a) ¿Por qué el F1-Score de la clase ALTO (0.53) es tan inferior al de la clase BAJO (0.88)? ¿Qué problema de datos subyace? *(3 puntos)*

b) Los datos de métricas de negocio muestran un resultado preocupante: ¿cuál es y qué dice sobre el modelo? *(3 puntos)*

c) La distribución geográfica de las métricas (Lima 0.84, Sierra 0.61, Selva 0.49) es una señal de alarma. ¿Qué tipo de sesgo representa y qué consecuencia concreta tiene para un agricultor de Pucallpa que solicita S/8,000 para su cosecha? *(4 puntos)*

---

**D2.** Diseño de solución: "¿Cómo implementarías un modelo justo?" *(10 puntos)*

El Gerente General de Caja Huancayo pide un plan para mejorar el modelo antes de que la SBS (Superintendencia de Banca y Seguros) realice su auditoría en 3 meses.

Diseña un plan técnico de mejora que incluya:
a) 3 cambios en el proceso de datos (antes de entrenar el modelo) *(3 puntos)*
b) 2 cambios en el proceso de entrenamiento del modelo (algoritmos, parámetros, métricas) *(3 puntos)*
c) 1 mecanismo de auditoría continua para después del despliegue (cómo monitorear que el modelo sigue siendo justo con el tiempo) *(4 puntos)*

---

**D3.** Pensamiento crítico: El dilema de la transparencia *(10 puntos)*

La SBS podría exigir que Caja Huancayo explique a cada cliente rechazado POR QUÉ fue rechazado (GDPR y regulaciones de IA en Europa ya lo requieren, y el regulador peruano va en esa dirección).

a) "¿Qué pasaría si Caja Huancayo implementa un Random Forest de 500 árboles y la SBS exige explicar individualmente cada decisión de rechazo?" Analiza el conflicto técnico entre la performance del modelo y su interpretabilidad. *(4 puntos)*

b) ¿Cuál es el riesgo de explicar incorrectamente la razón de un rechazo a un cliente? Da un ejemplo concreto de cómo una explicación imprecisa podría generar un problema legal para la entidad financiera. *(3 puntos)*

c) ¿Qué técnica de ML o herramienta conoces que permita hacer explicables los modelos de "caja negra"? (Investiga SHAP o LIME si no los conoces — están en la bibliografía del curso). ¿Cómo ayudaría en el caso de Caja Huancayo? *(3 puntos)*

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 6 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay | github.com/RubenCarty/bigdata-ua-2026-1*
