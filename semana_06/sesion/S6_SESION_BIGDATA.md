# S6 — SESIÓN DE CLASE COMPLETA: Machine Learning en Big Data
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 6: ML en Big Data — Algoritmos, Pipelines, Ética y Sesgo

---

| Campo | Detalle |
|-------|---------|
| **Curso** | Big Data DD283 |
| **Semana** | 6 de 8 |
| **Tema** | Machine Learning en Big Data |
| **Logro** | El estudiante identifica patrones en datos masivos con integridad, aplicando algoritmos de ML y analizando el sesgo ético en los modelos |
| **Duración** | 3 horas (180 min + 20 min receso) |
| **Herramientas** | Google Colab (principal) · Databricks MLlib (escala) |
| **Valor** | Integridad al evitar prejuicios en los modelos de aprendizaje |

---

## TABLA DE CONTENIDOS

1. [Cronograma](#cronograma)
2. [INICIO — Rompe-hielo y diagnóstico](#inicio)
3. [UTILIDAD — ML mueve la economía digital](#utilidad)
4. [TRANSFORMACIÓN — De datos a decisiones inteligentes](#transformacion)
5. [PRÁCTICA — Caso MiBanco Perú](#practica)
6. [CIERRE](#cierre)
7. [Guion verbal](#guion)
8. [Casos reales](#casos)
9. [Referencias APA 7](#referencias)

---

## CRONOGRAMA {#cronograma}

| Bloque | Actividad | Duración | Responsable |
|--------|-----------|----------|-------------|
| **INICIO** | Rompe-hielo + Logro + Revisión S5 + Diagnóstico | 20 min | Docente |
| **UTILIDAD** | ML en el mundo profesional real | 10 min | Docente |
| **TRANSFORMACIÓN 1** | Tipos de ML + Pipeline completo | 25 min | Docente + Grupo |
| **TRANSFORMACIÓN 2** | Algoritmos clave: regresión, árboles, clustering | 25 min | Docente + Grupo |
| **TRANSFORMACIÓN 3** | Evaluación de modelos + métricas | 20 min | Docente + Grupo |
| ☕ **RECESO** | | 20 min | — |
| **TRANSFORMACIÓN 4** | Sesgo, ética y fairness en ML | 20 min | Docente + Grupo |
| **TRANSFORMACIÓN 5** | Spark MLlib vs scikit-learn a escala | 10 min | Docente |
| **PRÁCTICA GRUPAL** | Caso MiBanco Perú — diseño de modelo crediticio | 25 min | Grupos |
| **EJERCICIO INDIVIDUAL** | Identificar sesgo en un modelo dado | 15 min | Individual |
| **CIERRE** | Síntesis + Metacognición + Tarea | 10 min | Docente |
| **TOTAL** | | **200 min** | |

---

## 1. INICIO (20 min) {#inicio}

### a) ROMPE-HIELO: "¿La máquina tiene razón?" (5 min)

**Instrucción verbal exacta:**

> *"Quiero que imaginen esta situación real. En 2018, Amazon implementó un sistema de IA para filtrar CVs de candidatos a empleos de ingeniería. El sistema revisaba 100 CVs y elegía los 10 mejores. Después de 1 año, el equipo descubrió que el sistema rechazaba sistemáticamente a las mujeres — incluso cuando sus CVs eran objetivamente mejores que los de hombres seleccionados."*
>
> *"Pregunta rápida en grupos de 3 personas: ¿Cómo creen que ocurrió ese error? ¿Fue un bug de programación? ¿Fue culpa del programador que escribió el código? ¿O hay algo más profundo?"*
>
> *(Escuchar 4-5 respuestas — 2 min)*
>
> *"La respuesta correcta: el modelo aprendió de 10 años de CVs históricos de Amazon, donde el 90% de los ingenieros contratados habían sido hombres. El modelo aprendió que 'hombre = mejor ingeniero' porque eso decían los datos históricos. La máquina no fue malintencionada — simplemente reprodujo el sesgo humano que había en los datos. Hoy vamos a aprender a construir modelos que eviten exactamente esto."*

---

### b) LOGRO DE APRENDIZAJE (3 min)

**Guion verbal textual:**

> *"Al terminar esta sesión van a poder hacer cuatro cosas concretas:"*
>
> *"Uno: explicar la diferencia entre aprendizaje supervisado y no supervisado con un ejemplo real de una empresa peruana."*
>
> *"Dos: construir un pipeline de ML completo en Google Colab — desde los datos crudos hasta la predicción — usando scikit-learn."*
>
> *"Tres: calcular las métricas de evaluación de un modelo (accuracy, precision, recall, F1) e interpretar cuál importa más según el problema de negocio."*
>
> *"Cuatro: identificar al menos 2 tipos de sesgo en un modelo de ML dado y proponer cómo mitigarlos — este último punto es el más importante del día porque es lo que diferencia a un Data Scientist ético de uno que solo corre modelos."*

---

### c) REVISIÓN SESIÓN ANTERIOR (7 min)

**Pregunta 1:** *"La semana pasada vieron Spark. ¿Cuál es la diferencia entre una Transformación y una Acción en Spark? Den un ejemplo de cada una."*

> **Respuesta esperada:** Transformación: operación lazy que define el plan pero no ejecuta (ej: `filter()`, `groupBy()`, `withColumn()`). Acción: dispara la ejecución del DAG completo y devuelve un resultado (ej: `collect()`, `count()`, `show()`, `write()`). El punto clave: las transformaciones son diferidas para que el Catalyst Optimizer pueda crear el plan más eficiente antes de ejecutar.
>
> **Si responde mal:** *"¿Qué pasa cuando escribes `df.filter(col > 100)` — Spark lee los datos inmediatamente? No. ¿Cuándo los lee? Cuando le dices `show()` o `collect()`. ¿Por qué espera? Para optimizar el plan completo antes de ejecutar."*

**Pregunta 2:** *"¿Qué es Structured Streaming y para qué caso de Yape lo usarían?"*

> **Respuesta esperada:** Structured Streaming procesa datos continuos como si fueran una tabla que crece infinitamente, en micro-batches de segundos. Para Yape: detección de fraude en tiempo real — si una tarjeta realiza más de 5 transacciones en 2 minutos en distintas ubicaciones, Streaming detecta el patrón con ventanas deslizantes y alerta antes de que el pago se confirme.

**Pregunta 3:** *"¿Para qué sirve `cache()` en Spark y cuándo es más útil?"*

> **Respuesta esperada:** `cache()` guarda el DataFrame en RAM de los Executors. Es más útil cuando el mismo DataFrame se usa múltiples veces en el código — sin cache, Spark recalcula toda la cadena de transformaciones desde el principio cada vez. El caso más crítico: algoritmos de ML iterativos (regresión logística, k-means) que leen los datos 50-100 veces durante el entrenamiento → con `cache()` leen de RAM en lugar de HDFS → 100x más rápido.

---

### d) DIAGNÓSTICO INICIAL (5 min)

**Pregunta 1:** *"¿Alguien sabe qué significa 'entrenar un modelo de Machine Learning'? Descríbanlo sin usar la palabra modelo."*

> **Respuesta esperada:** Es el proceso de ajustar los parámetros de un algoritmo matemático para que, dado un conjunto de ejemplos de entrada (X) con sus respuestas conocidas (Y), el algoritmo aprenda la relación entre X e Y. El objetivo: que cuando le des una nueva X sin Y conocida, el algoritmo pueda predecir Y correctamente. Es como estudiar 1,000 preguntas de examen con sus respuestas para poder responder correctamente una pregunta nueva.

**Pregunta 2:** *"¿Cuál es la diferencia entre clasificación y regresión?"*

> **Respuesta esperada:** Clasificación: predice una categoría (¿este correo es spam o no? ¿Este tumor es maligno o benigno? ¿Este cliente va a fugarse o no?). Regresión: predice un número continuo (¿cuánto costará este departamento? ¿Cuántas unidades se venderán mañana?). La diferencia fundamental: la variable que se predice (Y) es discreta en clasificación y continua en regresión.

**Pregunta 3:** *"¿Han escuchado de scikit-learn o pandas? ¿Para qué los usarían?"*

> **Respuesta esperada (nivel entrada):** scikit-learn es la librería más usada de Python para Machine Learning — tiene implementaciones listas para usar de decenas de algoritmos (regresión logística, árboles de decisión, k-means, SVM, etc.). pandas es para manipular y limpiar datos tabulares (similar a Excel pero con programación). En ML: pandas prepara los datos, scikit-learn entrena los modelos.

---

## 2. UTILIDAD (10 min) {#utilidad}

### Por qué ML en Big Data define el futuro del trabajo en datos

**Impacto real en números:**

| Empresa | Aplicación ML | Impacto cuantificado |
|---------|---------------|---------------------|
| Netflix | Recomendaciones personalizadas | $1 billion/año evitado en churn (usuarios que no se van gracias a buenas recomendaciones) |
| Spotify | Discover Weekly | 40M usuarios usan la playlist — 100% generada por ML |
| BCP Perú | Scoring crediticio automático | Aprobación de crédito en 3 segundos (antes: 5 días) |
| MINSA | Predicción de brotes de dengue | Anticipación de 3 semanas en zonas de alto riesgo |
| Uber | Precio dinámico (surge pricing) | ML recalcula el precio 15 veces por minuto por zona |
| Amazon | Detección de fraude | 2.3 millones de fraudes detectados/día automáticamente |

**El problema concreto que resuelve:**

Sin ML, un banco como MiBanco tiene que revisar manualmente 500 solicitudes de crédito por día. Con ML: el modelo evalúa los 500 en 3 segundos, aprueba el 70% automáticamente y envía solo el 30% dudoso a revisión humana. El analista de crédito que antes evaluaba 20 solicitudes/día ahora supervisa 500.

**Pregunta retadora:**

*"Si un modelo de ML predice que el 90% de los clientes de Claro pagará su factura a tiempo y el 10% no, ¿con qué accuracy empieza aunque no haya aprendido nada — simplemente prediciendo 'paga' para todos?"*

> **Respuesta esperada (tensión cognitiva):** 90% de accuracy. Si el 90% de los clientes sí paga, un modelo que siempre predice "paga" tendrá 90% de accuracy sin haber aprendido nada útil. Esto se llama el problema de "class imbalance" o desbalance de clases. Por eso accuracy no es la métrica adecuada cuando las clases están desbalanceadas — necesitamos Precision, Recall y F1 para detectar correctamente el 10% que NO paga, que es exactamente el grupo de interés.

---

## 3. TRANSFORMACIÓN (70 min) {#transformacion}

### SUBTEMA 3.1 — Tipos de Machine Learning (15 min)

**Explicación conceptual:**

```
TAXONOMÍA DE MACHINE LEARNING
═══════════════════════════════════════════════════════════

MACHINE LEARNING
├── SUPERVISADO (tiene etiquetas Y conocidas)
│   ├── Clasificación → Y es categórica
│   │   Ejemplos: spam/no-spam, fraude/no-fraude,
│   │             churn/no-churn, diagnóstico médico
│   └── Regresión → Y es numérica continua
│       Ejemplos: precio de casa, temperatura mañana,
│                 ventas del mes, edad del paciente
│
├── NO SUPERVISADO (sin etiquetas — busca estructura)
│   ├── Clustering → agrupar datos similares
│   │   Ejemplos: segmentación de clientes,
│   │             detección de anomalías
│   └── Reducción de dimensionalidad (PCA, t-SNE)
│
└── REFUERZO (aprende por prueba y error con recompensas)
    Ejemplos: AlphaGo, carros autónomos,
              trading algorítmico
```

**Ejemplo real — BCP y segmentación de clientes:**

BCP usa K-Means (no supervisado) para segmentar sus 8 millones de clientes en grupos con comportamiento financiero similar. El banco no sabe cuántos grupos hay ni cómo se llaman — el algoritmo los descubre. Resultado: 6 segmentos naturales (ej: "Jóvenes digitales", "Ahorradores conservadores", "Empresarios activos"). BCP adapta las ofertas de productos para cada segmento → 3x más conversión que ofertas genéricas.

**Pregunta al grupo 1:**

*"Una empresa de telecomunicaciones quiere predecir qué clientes van a cancelar su servicio el próximo mes. ¿Qué tipo de ML usaría? ¿Cuál sería la variable Y (lo que se predice)?"*

> **Respuesta esperada:** Aprendizaje supervisado → Clasificación. La variable Y sería binaria: `churn = 1` (cliente se va) o `churn = 0` (cliente se queda). Las variables X (características) podrían ser: meses como cliente, número de quejas en los últimos 3 meses, GB de datos consumidos, plan contratado, último pago puntual o no, etc. El modelo aprende qué combinación de X predice Y=1 (cancelación) usando clientes históricos cuyo comportamiento ya conocemos.
>
> **Si dice "no supervisado":** *"¿Tienes los datos históricos de clientes que sí cancelaron en el pasado? Sí. ¿Eso significa que tienes etiquetas? Sí. Si tienes datos con etiquetas, ¿cuál tipo de ML aplica?"*

---

### SUBTEMA 3.2 — Pipeline de ML completo (10 min)

**El pipeline es el proceso completo desde datos crudos hasta predicciones en producción:**

```
PIPELINE DE MACHINE LEARNING
═══════════════════════════════════════════════════════

[1] DATOS CRUDOS          →  CSV, base de datos, API
         ↓
[2] EXPLORACIÓN (EDA)     →  histogramas, correlaciones,
    Exploratory Data          distribuciones, outliers
    Analysis
         ↓
[3] PREPROCESAMIENTO      →  manejo de nulos,
                              encoding de categorías,
                              normalización/escalado
         ↓
[4] INGENIERÍA DE         →  crear columnas nuevas útiles
    CARACTERÍSTICAS           (edad = año_actual - año_nac,
    (Feature Engineering)     ratio_deuda = deuda/ingreso)
         ↓
[5] SEPARAR DATOS         →  80% entrenamiento
    Train / Test Split        20% prueba (nunca vistos)
         ↓
[6] ENTRENAMIENTO         →  model.fit(X_train, y_train)
         ↓
[7] EVALUACIÓN            →  model.predict(X_test)
                              comparar con y_test real
         ↓
[8] DESPLIEGUE            →  API REST, batch prediction,
    (Deployment)              integración a sistema
```

**Código en Google Colab — Pipeline completo mínimo:**

```python
# ============================================================
# DEMO: Pipeline ML completo en Google Colab
# Caso: predecir si un cliente de Claro cancelará su servicio
# ============================================================

# PASO 0: Instalar (en Colab ya están instaladas)
# !pip install scikit-learn pandas matplotlib seaborn -q

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
N = 1000

# PASO 1: Generar datos sintéticos de clientes Claro Perú
df = pd.DataFrame({
    "meses_cliente":    np.random.randint(1, 72, N),
    "quejas_3meses":    np.random.poisson(0.8, N),
    "gb_consumidos":    np.round(np.random.exponential(20, N), 1),
    "plan_precio":      np.random.choice([29, 39, 59, 79, 99], N),
    "pagos_tardios":    np.random.randint(0, 6, N),
    "num_productos":    np.random.randint(1, 5, N),
})

# Variable objetivo: churn (1 = se va, 0 = se queda)
# Los que más se van: más quejas, más pagos tardíos, menos tiempo como cliente
prob_churn = (
    0.05 +
    df["quejas_3meses"] * 0.15 +
    df["pagos_tardios"] * 0.08 -
    df["meses_cliente"] * 0.003 -
    df["num_productos"] * 0.04
).clip(0, 0.95)
df["churn"] = (np.random.random(N) < prob_churn).astype(int)

print(f"Dataset: {len(df)} clientes")
print(f"Churn rate: {df['churn'].mean():.1%}")
print(df.head())
```

```python
# ============================================================
# PASO 2: PREPROCESAMIENTO
# ============================================================

# Separar características (X) de la variable objetivo (y)
X = df.drop("churn", axis=1)    # Todas las columnas excepto churn
y = df["churn"]                  # Solo la columna churn

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
    # stratify=y: mantiene la misma proporción de churn en ambas partes
)
print(f"Entrenamiento: {len(X_train)} | Prueba: {len(X_test)}")

# Normalizar: escalar todas las columnas al mismo rango
# IMPORTANTE: el scaler se ajusta SOLO con los datos de entrenamiento
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit + transform
X_test_scaled  = scaler.transform(X_test)         # solo transform (sin fit)

# Por qué no hacer fit en test también: sería "espiar" los datos de prueba
```

```python
# ============================================================
# PASO 3: ENTRENAR Y EVALUAR
# ============================================================

# Regresión Logística (modelo de clasificación, no de regresión)
modelo = LogisticRegression(random_state=42)
modelo.fit(X_train_scaled, y_train)              # ENTRENAR

# Predecir sobre datos de prueba (nunca vistos)
y_pred = modelo.predict(X_test_scaled)

# Reporte completo de métricas
print("=== REPORTE DE EVALUACIÓN ===")
print(classification_report(y_test, y_pred, target_names=["Se queda", "Se va"]))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Pred: Queda", "Pred: Churn"],
            yticklabels=["Real: Queda", "Real: Churn"])
plt.title("Matriz de Confusión — Modelo Churn Claro Perú")
plt.tight_layout()
plt.show()
```

**Pregunta al grupo 2:**

*"El modelo de churn predice 85% de accuracy. ¿Eso es suficiente para el equipo de retención de Claro que quiere llamar a los clientes que van a irse?"*

> **Respuesta esperada:** No necesariamente. Si solo el 10% de clientes hace churn, un modelo que predice "se queda" para todos tiene 90% de accuracy sin haber aprendido nada útil. Para el caso de retención: lo más importante es el **Recall del churn (clase 1)** — cuántos de los clientes que SÍ se van detectamos correctamente. Si el Recall es bajo (ej: 30%), Claro está llamando a los que no iban a irse y dejando escapar al 70% que sí iba a cancelar. La accuracy alta puede ser engañosa con datos desbalanceados.

---

### SUBTEMA 3.3 — Algoritmos clave con ejemplos (25 min)

**Algoritmo 1: Regresión Logística**

A pesar del nombre "regresión", es un algoritmo de **clasificación**. Calcula la probabilidad de pertenencia a cada clase usando una función sigmoide.

```
REGRESIÓN LOGÍSTICA: cómo funciona
═══════════════════════════════════════

Entrada:  X = [quejas=3, meses=8, pagos_tardios=2, ...]
             ↓
         z = w₁*quejas + w₂*meses + w₃*pagos + b
         (combinación lineal ponderada de features)
             ↓
         P(churn) = 1 / (1 + e^(-z))    ← función sigmoide
         (convierte z en probabilidad 0-1)
             ↓
Salida:   si P > 0.5 → churn=1 (se va)
          si P ≤ 0.5 → churn=0 (se queda)

Ventajas:  ✓ Rápido, interpretable, funciona en Big Data
Límites:   ✗ Solo fronteras lineales (no captura relaciones complejas)
```

**Algoritmo 2: Árbol de Decisión y Random Forest**

```python
# ============================================================
# ÁRBOL DE DECISIÓN: interpretable y visual
# ============================================================
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier

# Árbol de decisión simple (profundidad 3 para visualizar)
arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X_train, y_train)

# Ver las reglas que aprendió el árbol
print("=== REGLAS DEL ÁRBOL DE DECISIÓN ===")
print(export_text(arbol, feature_names=list(X.columns)))

# Random Forest: muchos árboles → más robusto
forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)

# Importancia de cada característica
importancias = pd.Series(
    forest.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\n=== IMPORTANCIA DE CARACTERÍSTICAS (Random Forest) ===")
print(importancias)
importancias.plot(kind="barh", color="steelblue")
plt.title("¿Qué variable predice más el churn?")
plt.xlabel("Importancia relativa")
plt.tight_layout()
plt.show()
```

**Pregunta al grupo 3:**

*"El árbol de decisión muestra que 'quejas_3meses > 2' es la primera pregunta del árbol. ¿Eso significa que las quejas son LA razón por la que los clientes se van? ¿Pueden afirmar eso con certeza?"*

> **Respuesta esperada:** No se puede afirmar causalidad, solo correlación. El árbol detecta que los clientes con más de 2 quejas en 3 meses tienen mayor probabilidad de churn — pero la relación puede ser: (a) las quejas causan el churn directamente, (b) ambas son consecuencia de una tercera variable (mala cobertura en la zona del cliente), (c) los clientes ya habían decidido irse y llamaban para quejarse antes de cancelar. Para establecer causalidad necesitaríamos un experimento controlado (A/B test). ML detecta patrones, no causas.
>
> **Si dice "sí, las quejas causan el churn":** *"¿Cómo podrían verificar si es causalidad o solo correlación? ¿Qué experimento diseñarían?"*

**Algoritmo 3: K-Means Clustering (no supervisado)**

```python
# ============================================================
# K-MEANS: segmentación de clientes sin etiquetas
# ============================================================
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Solo usar 2 variables para visualizar el resultado
X_cluster = df[["meses_cliente", "gb_consumidos"]].copy()
scaler_km = StandardScaler()
X_scaled_km = scaler_km.fit_transform(X_cluster)

# Determinar el número óptimo de clusters (método del codo)
inercias = []
for k in range(1, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled_km)
    inercias.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 9), inercias, 'bo-')
plt.xlabel('Número de clusters (K)')
plt.ylabel('Inercia (suma de distancias cuadradas)')
plt.title('Método del Codo — ¿Cuántos segmentos de clientes?')
plt.xticks(range(1, 9))
plt.grid(True, alpha=0.3)
plt.show()
# El "codo" (punto donde la inercia deja de bajar rápido) indica el K óptimo
```

**Pregunta al grupo 4:**

*"Si aplicamos K-Means con K=4 a los clientes de Claro, obtenemos 4 grupos. ¿Cómo sabemos qué significa cada grupo? ¿El algoritmo los etiqueta automáticamente?"*

> **Respuesta esperada:** K-Means solo asigna números (grupo 0, 1, 2, 3) — no tiene semántica propia. El Data Scientist debe analizar las características de cada grupo para interpretar su significado. Por ejemplo: si el Grupo 2 tiene alta antigüedad (30+ meses) y alto consumo de datos, se puede etiquetar "Clientes leales heavy users". Este paso de interpretación requiere conocimiento del negocio, no solo matemáticas. Eso diferencia al Data Scientist del analista: el analista ejecuta el algoritmo, el Data Scientist interpreta y comunica el resultado al equipo de marketing.

---

### SUBTEMA 3.4 — Evaluación de modelos: métricas que importan (20 min)

**La matriz de confusión — la base de todas las métricas:**

```
MATRIZ DE CONFUSIÓN (clasificación binaria)
════════════════════════════════════════════════

                  PREDICCIÓN
                ┌──────────┬──────────┐
                │  Pred: 0 │  Pred: 1 │
REAL  ┌─────────┼──────────┼──────────┤
      │ Real: 0 │    TN    │    FP    │
      │(no churn│  (True   │  (False  │
      │   real) │ Negative)│Positive) │
      ├─────────┼──────────┼──────────┤
      │ Real: 1 │    FN    │    TP    │
      │ (churn  │  (False  │  (True   │
      │   real) │Negative) │Positive) │
      └─────────┴──────────┴──────────┘

TN: predijo "no churn" y tenía razón  ← correcto
FP: predijo "churn" pero no era churn ← Error tipo I (falsa alarma)
FN: predijo "no churn" pero sí era    ← Error tipo II (más grave para retención)
TP: predijo "churn" y tenía razón     ← correcto
```

**Las 4 métricas principales:**

| Métrica | Fórmula | Cuándo importa más | Ejemplo Claro |
|---------|---------|-------------------|---------------|
| **Accuracy** | (TP+TN)/(total) | Clases balanceadas | No útil con 90/10 churn |
| **Precision** | TP/(TP+FP) | Cuando el costo de la falsa alarma es alto | Si llamar a un cliente que no iba a irse es muy costoso |
| **Recall** | TP/(TP+FN) | Cuando perder un caso real es grave | Churn: mejor llamar de más que no llamar al que se va |
| **F1-Score** | 2×(P×R)/(P+R) | Balance entre Precision y Recall | Default cuando no hay preferencia clara |

```python
# ============================================================
# COMPARACIÓN: cuándo importa Precision vs Recall
# ============================================================
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def evaluar_modelo(nombre, y_real, y_pred):
    print(f"\n=== {nombre} ===")
    print(f"Accuracy:  {accuracy_score(y_real, y_pred):.3f}")
    print(f"Precision: {precision_score(y_real, y_pred, zero_division=0):.3f}")
    print(f"Recall:    {recall_score(y_real, y_pred, zero_division=0):.3f}")
    print(f"F1-Score:  {f1_score(y_real, y_pred, zero_division=0):.3f}")

# Modelo 1: conservador — predice churn solo cuando muy seguro
# Alta precision, bajo recall (deja escapar a muchos churners)
y_pred_conservador = (modelo.predict_proba(X_test_scaled)[:, 1] > 0.7).astype(int)

# Modelo 2: agresivo — predice churn ante la menor duda
# Bajo precision (muchas falsas alarmas), alto recall
y_pred_agresivo = (modelo.predict_proba(X_test_scaled)[:, 1] > 0.3).astype(int)

evaluar_modelo("Modelo conservador (umbral 0.7)", y_test, y_pred_conservador)
evaluar_modelo("Modelo agresivo (umbral 0.3)", y_test, y_pred_agresivo)

# Pregunta para el grupo: ¿Cuál usar para el equipo de retención de Claro?
```

**Pregunta al grupo 5:**

*"El equipo de marketing de Claro puede llamar a máximo 500 clientes por semana. Hay 10,000 clientes en la base. ¿Qué métrica del modelo optimizarían: Precision o Recall? ¿Por qué?"*

> **Respuesta esperada:** Precision. Si el equipo puede llamar solo a 500 de 10,000, necesita que esos 500 sean los que MÁS probablemente van a irse. Cada llamada innecesaria a alguien que no iba a irse desperdicia el presupuesto limitado. Alta Precision = de los 500 que llamamos, la mayoría SÍ iba a irse. Contraejemplo: si el presupuesto fuera ilimitado y el costo de perder un cliente fuera enorme (ej: cliente VIP de $50K/año), entonces Recall (no dejar escapar a ninguno) sería más importante. La métrica relevante depende del contexto del negocio, no de la matemática.

---

## RECESO (20 min) ☕

---

### SUBTEMA 3.5 — Sesgo y ética en Machine Learning (20 min)

**Este es el tema más importante del día — y el que más se ignora en la industria.**

**Los 5 tipos de sesgo más comunes:**

| Tipo de sesgo | Descripción | Ejemplo real |
|---------------|-------------|-------------|
| **Sesgo histórico** | Los datos de entrenamiento reflejan discriminación pasada | Amazon CV: datos históricos con 90% hombres |
| **Sesgo de selección** | Los datos de entrenamiento no son representativos | Sistema de crédito entrenado solo con clientes urbanos, aplicado en zonas rurales |
| **Sesgo de confirmación** | El modelo refuerza decisiones previas del humano | Predicción de reincidencia criminal: COMPAS (EE.UU.) |
| **Sesgo de proxy** | Variables "neutras" esconden discriminación | Código postal predice raza en EE.UU. → denegar crédito por zona = discriminación racial indirecta |
| **Sesgo de medición** | La variable Y fue medida de forma sesgada | "Buen médico" medido por horas trabajadas → sesga contra médicos con familia |

**Caso real: COMPAS y el sistema de justicia criminal en EE.UU.:**

COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) era un modelo de ML usado por jueces estadounidenses para predecir la probabilidad de reincidencia de criminales y decidir la sentencia. En 2016, ProPublica analizó el modelo y descubrió:

- La tasa de falsos positivos (predijo reincidencia pero no reincidió) para personas negras: **44.9%**
- La tasa de falsos positivos para personas blancas: **23.5%**
- El modelo era 2 veces más propenso a calificar erróneamente a personas negras como de alto riesgo

El modelo no usaba la raza como variable directa — pero usaba código postal, historial familiar de arrestos, nivel educativo, que en EE.UU. tienen alta correlación con la raza por décadas de discriminación sistemática. Las variables de "proxy" transmitieron el sesgo histórico.

**Código — medir fairness básico:**

```python
# ============================================================
# DETECCIÓN DE SESGO: ¿el modelo discrimina por región?
# ============================================================

# Agregar variable de región al dataset (simulando sesgo geográfico)
df["region"] = np.random.choice(
    ["Lima Metropolitana", "Provincias"],
    N,
    p=[0.6, 0.4]
)

# El modelo fue entrenado principalmente con datos de Lima
# ¿Funciona igual para clientes de provincias?

# Separar las predicciones por grupo
mask_lima = df.loc[X_test.index, "region"] == "Lima Metropolitana"
mask_prov = df.loc[X_test.index, "region"] == "Provincias"

f1_lima = f1_score(y_test[mask_lima], y_pred[mask_lima], zero_division=0)
f1_prov = f1_score(y_test[mask_prov], y_pred[mask_prov], zero_division=0)

print("=== ANÁLISIS DE EQUIDAD (FAIRNESS) ===")
print(f"F1-Score Lima Metropolitana: {f1_lima:.3f}")
print(f"F1-Score Provincias:         {f1_prov:.3f}")
diferencia = abs(f1_lima - f1_prov)
print(f"Diferencia: {diferencia:.3f}")
if diferencia > 0.10:
    print("⚠️  ALERTA: El modelo puede estar discriminando por región")
    print("   El modelo funciona significativamente mejor para un grupo")
else:
    print("✅ El modelo funciona de forma similar para ambos grupos")
```

**Pregunta al grupo 6:**

*"MiBanco quiere usar un modelo de ML para aprobar o rechazar préstamos a MYPES (micro y pequeñas empresas). El modelo fue entrenado con datos históricos de 2010-2020. ¿Cuáles son los 3 mayores riesgos de sesgo en ese modelo?"*

> **Respuesta esperada:**
> 1. **Sesgo histórico:** De 2010-2020, los prestamistas históricamente aprobaron más préstamos a empresas de Lima y lideradas por hombres. El modelo aprenderá que "Lima + hombre = buen deudor" aunque no sea verdad para el futuro.
> 2. **Sesgo de selección:** El modelo solo entrenó con empresas que SÍ solicitaron un préstamo y fueron evaluadas (sesgo de supervivencia). Las empresas que nunca solicitaron porque sabían que serían rechazadas no están en los datos — el modelo no aprende de los casos que no vio.
> 3. **Sesgo de proxy:** Variables como formalidad tributaria (inscrito en SUNAT, tiene RUC), cuenta bancaria formal, acceso a internet para el trámite — todas correlacionan con zona urbana/rural y nivel socioeconómico, actuando como proxies de exclusión financiera histórica.

---

### SUBTEMA 3.6 — Spark MLlib: ML a escala (10 min)

**Cuándo scikit-learn no alcanza:**

| Criterio | scikit-learn | Spark MLlib |
|----------|-------------|-------------|
| **Tamaño máximo de datos** | ~10 GB (RAM de 1 máquina) | Petabytes (distribuido) |
| **Velocidad en 1 GB** | Rápido (segundos) | Más lento (overhead de distribución) |
| **Velocidad en 1 TB** | No funciona (no cabe en RAM) | Minutos |
| **Algoritmos disponibles** | 200+ | ~50 (principales) |
| **Facilidad de uso** | Alta (Python nativo) | Media (requiere SparkSession) |
| **Integración Big Data** | Baja (pandas limitado) | Alta (nativo en el ecosistema Spark) |

**Código MLlib en Databricks:**

```python
# ============================================================
# SPARK MLLIB: el mismo pipeline pero a escala
# (ejecutar en Databricks, no en Colab)
# ============================================================
from pyspark.ml.feature import VectorAssembler, StandardScaler as SparkScaler
from pyspark.ml.classification import LogisticRegression as SparkLR
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import Pipeline

# Preparar features para Spark (requiere Vector)
assembler = VectorAssembler(
    inputCols=["meses_cliente", "quejas_3meses",
               "gb_consumidos", "plan_precio",
               "pagos_tardios", "num_productos"],
    outputCol="features_raw"
)
scaler_spark = SparkScaler(inputCol="features_raw", outputCol="features")
lr_spark     = SparkLR(featuresCol="features", labelCol="churn", maxIter=20)

# Pipeline: todo en cadena
pipeline_ml = Pipeline(stages=[assembler, scaler_spark, lr_spark])

# Entrenar (aquí los datos pueden ser 1 TB distribuido en HDFS)
modelo_spark = pipeline_ml.fit(df_spark_train)

# Evaluar
predicciones = modelo_spark.transform(df_spark_test)
evaluador = BinaryClassificationEvaluator(labelCol="churn", metricName="areaUnderROC")
auc = evaluador.evaluate(predicciones)
print(f"AUC-ROC: {auc:.3f}")
```

**Pregunta al grupo 7:**

*"¿Cuándo usarían Spark MLlib en lugar de scikit-learn para el modelo de churn de Claro Perú?"*

> **Respuesta esperada:** Cuando los datos de clientes no caben en la RAM de 1 máquina. Claro Perú tiene ~20 millones de clientes. Si cada registro tiene 50 columnas × 4 bytes = 200 bytes → 20M × 200 bytes = 4 GB solo de datos crudos. Con preprocesamiento e historial de 2 años → fácilmente 50-100 GB. Claro necesita un servidor con 128+ GB de RAM para scikit-learn, lo cual es muy caro. Con Spark MLlib en 10 nodos de 16 GB c/u = 160 GB de RAM distribuida → resuelve el problema con hardware commodity. Además, el re-entrenamiento mensual del modelo puede correr como job de Spark sin interrumpir los sistemas de producción.

---

### SUBTEMA 3.7 — Overfitting y Underfitting (5 min)

```
BIAS-VARIANCE TRADEOFF: el equilibrio del modelo perfecto
════════════════════════════════════════════════════════

UNDERFITTING (High Bias):        OVERFITTING (High Variance):
Modelo demasiado simple          Modelo demasiado complejo
Aprende poco de los datos        Memoriza los datos de entrenamiento

Accuracy train: 60%              Accuracy train: 99%
Accuracy test:  58%              Accuracy test:  62%
                                 (no generaliza a datos nuevos)

SOLUCIÓN:                        SOLUCIÓN:
- Modelo más complejo            - Más datos de entrenamiento
- Más características            - Regularización (L1/L2)
- Menos regularización           - Reducir complejidad
                                 - Cross-validation
```

**Pregunta al grupo 8:**

*"Un árbol de decisión con profundidad ilimitada alcanza 100% de accuracy en entrenamiento. ¿Eso es bueno? ¿Qué pasaría cuando se use con clientes nuevos?"*

> **Respuesta esperada:** No es bueno — es el síntoma clásico de overfitting. Un árbol sin límite de profundidad puede crear una regla diferente para CADA cliente del conjunto de entrenamiento (memoriza en lugar de aprender). Con accuracy 100% en train y luego 55% en test, el modelo es inútil en producción. La solución: `max_depth=5`, `min_samples_leaf=20` — forzar al árbol a generalizar en lugar de memorizar. Otro indicador de overfitting: cuando el accuracy en test sube al añadir más datos de entrenamiento (modelo no estaba generalizando).

---

## 4. PRÁCTICA (40 min) {#practica}

### a) CASO PRÁCTICO GRUPAL: Diseñar el modelo de crédito de MiBanco (25 min)

**Escenario:**

MiBanco Perú (banco líder en microfinanzas) recibe 3,000 solicitudes de crédito por día de pequeños emprendedores. Actualmente, el 70% se evalúa manualmente (3-5 días de espera) y el 30% se rechaza automáticamente por incumplir criterios mínimos. El Gerente de Riesgos quiere un modelo de ML que:
1. Apruebe automáticamente el 60% de las solicitudes más seguras
2. Envíe solo el 40% más dudoso a revisión humana
3. Mantenga la tasa de mora (impago) por debajo del 5%

**Variables disponibles:**

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `meses_historial_credito` | Numérica | Tiempo en el sistema financiero |
| `num_creditos_anteriores` | Numérica | Préstamos previos en MiBanco |
| `tasa_pago_puntual` | Numérica (%) | % de cuotas pagadas a tiempo históricamente |
| `ingreso_mensual_declarado` | Numérica | Ingreso declarado (no verificado) |
| `deuda_actual` | Numérica | Monto total de deuda en el sistema |
| `sector_negocio` | Categórica | Comercio, servicios, manufactura, agro |
| `departamento` | Categórica | Lima, Arequipa, Cusco, etc. |
| `num_dependientes` | Numérica | Personas a cargo |
| `tiene_cuenta_ahorro` | Binaria | 1=Sí, 0=No |
| **`impago_futuro`** | **Binaria (Y)** | **1=No pagó / 0=Pagó** |

**Preguntas del caso (responder en grupo en 20 min):**

1. ¿Qué tipo de ML es este problema? ¿Clasificación o regresión? ¿Cuál es el Y?

2. Para el objetivo del banco (mantener mora < 5%), ¿optimizarían Precision o Recall para la clase "impago_futuro=1"? ¿Por qué?

3. Identifica 2 variables que podrían generar sesgo en el modelo (discriminar injustamente a algún grupo). ¿Cómo lo mitigarías?

4. El gerente propone: "Entrenemos el modelo con los últimos 6 meses de datos". ¿Es suficiente? ¿Qué problema tendría un modelo entrenado solo con datos de COVID-2020?

5. Diseña una métrica de negocio (no de ML) para evaluar si el modelo está funcionando bien en producción después de 3 meses. *(Pista: no es accuracy, es algo que el gerente financiero pueda entender)*

**Preguntas de andamiaje del docente:**

- *"¿El departamento del cliente debería ser una variable del modelo? ¿Puede ser un proxy de algo?"*
- *"Si el modelo aprueba el 60% automáticamente, ¿cómo saben que esos 60% son los MÁS seguros y no cualquier 60%?"*
- *"¿El 'ingreso declarado' es una variable confiable? ¿Qué sesgos introduce?"*

**Respuesta modelo — puesta en común:**

1. Clasificación binaria. Y = `impago_futuro` (1=impagó, 0=pagó). Variables X = todo lo demás.

2. **Precision** para "impago=1". Si el banco aprueba un crédito que luego no se paga, pierde dinero (FP es muy costoso). El banco prefiere rechazar algunos buenos clientes (FN) antes que aprobar un mal deudor. Dicho de otra forma: **en crédito, el Error Tipo I (FP: aprobar a quien no pagará) es más costoso que el Error Tipo II (FN: rechazar a quien sí pagaría)**.

3. Variables con riesgo de sesgo: **`departamento`** (puede discriminar por región geográfica, que en Perú correlaciona con etnia) y **`sector_negocio`** (puede discriminar contra el sector agropecuario aunque sus deudores sean tan confiables como los comerciantes). Mitigación: análisis de paridad de métricas por grupo, incluir variables de pago histórico que sean más directas (tasa_pago_puntual), testear el modelo separadamente para cada grupo demográfico.

4. No es suficiente. Los últimos 6 meses pueden no incluir ciclos económicos adversos, estacionalidad ni eventos excepcionales. Un modelo entrenado con datos de 2020 (COVID) aprendería que casi nadie paga (todos estaban en cuarentena y sin ingresos) → sobre-predicaría impago en condiciones normales. Recomendación: al menos 3 años de datos con balanceo de periodos normales y adversos.

5. Métrica de negocio: **Tasa de mora real del portafolio aprobado automáticamente** medida a los 90 días de aprobación. Si el modelo aprueba el 60% automáticamente y esos créditos tienen mora de 3% (< 5% objetivo), el modelo funciona. Si la mora sube a 8%, el modelo está aprobando créditos riesgosos. Esta métrica es entendible por el gerente financiero sin saber nada de ML.

---

### b) EJERCICIO INDIVIDUAL: Identificar sesgo en el modelo (15 min)

**Escenario:**

El modelo de MiBanco fue evaluado y los resultados por grupo son:

| Grupo | N solicitantes | Precision (impago) | Recall (impago) | Tasa aprobación |
|-------|---------------|-------------------|----------------|----------------|
| Hombres | 1,800 | 0.82 | 0.74 | 68% |
| Mujeres | 1,200 | 0.61 | 0.45 | 54% |
| Lima | 2,100 | 0.85 | 0.78 | 71% |
| Provincias | 900 | 0.58 | 0.42 | 48% |

**Responde en el espacio indicado:**

1. ¿Existe evidencia de sesgo en este modelo? ¿Para qué grupos y en qué métricas?

2. ¿Cuál es el impacto concreto de este sesgo para una emprendedora de Ayacucho que solicita un crédito de S/5,000?

3. Propón 2 acciones técnicas concretas (no éticas en abstracto, sino cambios en el proceso de ML) que el equipo de Data Science de MiBanco debería implementar para reducir este sesgo.

**Criterio de éxito:**
- Sí identifica el sesgo: menciona diferencias de > 20% en métricas entre grupos
- Sí conecta con impacto real: describe consecuencia para persona específica
- Sí propone acciones técnicas: oversampling, rebalanceo del dataset, fairness constraints, métricas de paridad

---

## 5. CIERRE (10 min) {#cierre}

### a) SÍNTESIS COLABORATIVA (4 min)

**Pregunta cierre 1:** *"En una frase: ¿cuál es la diferencia entre supervisado y no supervisado?"*

> **Respuesta esperada:** Supervisado: el dataset tiene etiquetas (Y conocida) y el modelo aprende a predecirlas. No supervisado: no hay etiquetas — el modelo encuentra estructura en los datos por sí solo (grupos, anomalías, patrones).

**Pregunta cierre 2:** *"¿Por qué accuracy puede ser una métrica engañosa?"*

> **Respuesta esperada:** Con clases desbalanceadas, un modelo que predice siempre la clase mayoritaria obtiene alta accuracy sin haber aprendido nada útil. Ejemplo: 95% no fraude, 5% fraude → predecir siempre "no fraude" = 95% accuracy, pero 0% de utilidad para detectar fraudes.

**Pregunta cierre 3:** *"Nombren 2 tipos de sesgo en ML y en qué etapa del pipeline ocurren."*

> **Respuesta esperada:** (1) Sesgo histórico: ocurre en los DATOS (paso 1) — los datos reflejan discriminación pasada del mundo real. (2) Sesgo de proxy: ocurre en la SELECCIÓN DE FEATURES (paso 4) — variables aparentemente neutras que correlacionan con características protegidas.

---

### b) METACOGNICIÓN (3 min)

*"En silencio, respondan internamente:"*

1. *"¿Puedo explicar la diferencia entre Precision y Recall con un ejemplo propio — sin mirar el apunte?"*
2. *"¿Cuál de los tipos de sesgo me pareció más sorprendente? ¿Por qué?"*
3. *"En el proyecto de mi grupo, ¿podría existir sesgo en los datos que vamos a usar? ¿Qué grupo podría estar sub-representado?"*

---

### c) TAREA / PUENTE (3 min)

**Tarea para el laboratorio:**

> *"Para el laboratorio en casa van a construir un modelo completo de predicción de churn para Movistar Perú en Google Colab. El laboratorio tiene el dataset generado y el código esqueleto — ustedes completan las partes de preprocesamiento, el Random Forest, las métricas y el análisis de sesgo por región. El Google Colab no necesita instalación — solo necesitan una cuenta de Google."*

**Puente con S7:**

> *"La próxima semana veremos scraping y limpieza de datos. Hoy asumimos que los datos llegan limpios. En la realidad, el 80% del tiempo de un Data Scientist se gasta en limpiar datos. La semana siguiente aprenderán exactamente cómo hacer ese proceso."*

---

## GUION VERBAL SUGERIDO {#guion}

**Al introducir la Matriz de Confusión:**
> *"Imaginen que soy el modelo y ustedes son los clientes de Claro. Yo predigo: 'Ana se va a ir'. Si Ana se va y yo predije correcto: Verdadero Positivo. Si Ana NO se va y yo predije que sí: Falso Positivo — le llamo innecesariamente. Si Ana SÍ se va pero yo predije que no: Falso Negativo — la dejé escapar. El cliente de retención quiere minimizar los Falsos Negativos."*

**Al hablar de sesgo:**
> *"El sesgo en ML no es intencional en la mayoría de los casos. El algoritmo no discrimina 'a propósito'. Pero reproduce las desigualdades que ya existen en los datos históricos. Es como preguntarle a 1,000 personas de Lima quiénes son los mejores chefs del Perú y asumir que la respuesta aplica para todo el Perú."*

**Al comparar scikit-learn vs MLlib:**
> *"scikit-learn es como una moto: rápido, ágil, perfecto para la ciudad. Spark MLlib es como un camión: más lento para distancias cortas, pero puede cargar 1,000 veces más. ¿Para qué distancia necesitas un camión? Cuando los datos no caben en 1 máquina."*

---

## CASOS REALES RECOMENDADOS {#casos}

1. **Amazon Recruiting Tool (2018):** Sistema de IA para filtrar CVs penalizaba a mujeres porque fue entrenado con CVs históricos donde el 90% de los contratados eran hombres. Amazon descartó el proyecto. Fuente: Reuters, 2018.

2. **COMPAS — Sistema de Justicia Criminal EE.UU. (2016):** Modelo usado por jueces para predecir reincidencia. ProPublica demostró que era 2x más propenso a etiquetar afroamericanos como alto riesgo. Fuente: ProPublica, "Machine Bias", mayo 2016.

3. **BCP y scoring crediticio Perú:** BCP implementó un modelo de ML para aprobar créditos de consumo en 3 segundos (antes: 5 días). El modelo evalúa 150 variables incluyendo comportamiento de pago histórico. Resultado: 40% más de aprobaciones con la misma tasa de mora. Fuente: Presentación BCP, DataLatam 2023.

4. **Spotify Discover Weekly:** Modelo de ML que genera una playlist personalizada de 30 canciones cada lunes para 170M usuarios. Combinación de collaborative filtering (qué escuchan personas similares a ti) y audio features (tempo, energía, valencia). Fuente: Spotify Engineering Blog, 2015.

5. **MINSA y predicción de dengue (Perú, 2022):** El MINSA Perú implementó un modelo predictivo para anticipar brotes de dengue por región usando datos históricos de casos, temperatura, precipitaciones y densidad poblacional. Permite anticipar brotes 3 semanas antes. Fuente: El Comercio, 2022.

---

## EVALUACIÓN FORMATIVA

| Momento | Indicador | Señal de comprensión |
|---------|-----------|---------------------|
| Inicio | Diagnóstico oral | Puede distinguir clasificación de regresión con ejemplo |
| Transformación 3.2 | Mini ejercicio Google Colab | `classification_report` ejecutado con valores visibles |
| Transformación 3.4 | Pregunta P5 (Precision vs Recall) | Justifica según el costo del error para el negocio |
| Transformación 3.5 | Pregunta P6 (sesgo MiBanco) | Menciona al menos 2 tipos de sesgo con causa específica |
| Práctica grupal | Producto del grupo | Propone métrica de negocio (no solo de ML) |
| Ejercicio individual | Análisis de la tabla | Identifica diferencia > 20% entre grupos |

---

## REFERENCIAS APA 7 {#referencias}

Géron, A. (2022). *Hands-on machine learning with scikit-learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

Hastie, T., Tibshirani, R., & Friedman, J. (2017). *The elements of statistical learning: Data mining, inference, and prediction* (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016, May 23). Machine bias. *ProPublica*. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and machine learning: Limitations and opportunities*. MIT Press. https://fairmlbook.org

Meng, X., Bradley, J., Yavuz, B., Sparks, E., Venkataraman, S., Liu, D., Freeman, J., Tsai, D. B., Amde, M., Owen, S., Xin, D., Xin, R., Franklin, M. J., Zadeh, R., Zaharia, M., & Smola, A. (2016). MLlib: Machine learning in Apache Spark. *Journal of Machine Learning Research*, *17*(1), 1235–1241.

Scikit-learn developers. (2024). *scikit-learn: Machine learning in Python*. https://scikit-learn.org/stable/documentation.html

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 6 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay*
