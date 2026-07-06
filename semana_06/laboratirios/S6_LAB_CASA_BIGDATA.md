# S6 — LABORATORIO EN CASA: Pipeline de ML con Google Colab
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 6: Predicción de Churn en Movistar Perú

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha de entrega** | ______________________________________________ |
| **Duración estimada** | 2 horas |
| **Modalidad** | Individual o en pareja |
| **Herramienta principal** | Google Colab (gratuito, solo requiere cuenta Google) |
| **Entrega** | PR a `semana_06/Soluciones/TuNombre_TuCodigo/` en GitHub |

---

## OBJETIVO DEL LABORATORIO

Construir un pipeline completo de Machine Learning — desde los datos crudos hasta la evaluación y análisis de equidad — usando Google Colab y scikit-learn, aplicado al caso de predicción de churn (abandono de clientes) de Movistar Perú.

**Competencia que desarrolla:** Implementa pipelines de ML aplicando métricas de evaluación apropiadas e identifica sesgos en el modelo con enfoque ético.

---

## SOFTWARE Y HERRAMIENTAS

### Herramienta principal — Google Colab

| Detalle | Información |
|---------|-------------|
| **Acceso** | colab.research.google.com (requiere cuenta Google) |
| **Instalación** | No requiere instalación — 100% en el navegador |
| **Librerías** | scikit-learn, pandas, numpy, matplotlib, seaborn ya preinstaladas |
| **GPU gratis** | Activar en Entorno de ejecución → Cambiar tipo de entorno → GPU T4 |

### Verificación del entorno (ejecutar en la primera celda):

```python
import sklearn
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
print(f"✅ scikit-learn: {sklearn.__version__}")
print(f"✅ pandas: {pd.__version__}")
print(f"✅ numpy: {np.__version__}")
print(f"✅ matplotlib: {matplotlib.__version__}")
print("✅ Todos los paquetes listos")
```

**Si ves ✅ en todas las líneas → el entorno está listo para trabajar.**

### Alternativa sin internet — Jupyter local

```bash
pip install scikit-learn pandas numpy matplotlib seaborn jupyter
jupyter notebook
```

---

## CONTEXTO DEL CASO

**Movistar Perú** tiene 12 millones de clientes. Cada mes, aproximadamente el 8% de los clientes cancela su servicio (churn). Adquirir un cliente nuevo cuesta 5 veces más que retener uno existente. El equipo de analítica quiere un modelo predictivo para identificar, con 30 días de anticipación, cuáles clientes tienen alta probabilidad de cancelar — y así intervenir con ofertas de retención personalizadas.

**Dataset sintético:** 5,000 clientes de Movistar Perú con 12 variables de comportamiento.

---

## PARTE 1 — EXPLORACIÓN Y COMPRENSIÓN (30 min)

### Celda 1: Generar y cargar el dataset

```python
# ============================================================
# CELDA 1: Dataset Movistar Perú — ejecutar sin modificar
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(2026)
N = 5000

planes = ["Básico 29", "Estándar 39", "Plus 59", "Premium 79", "Elite 99"]
regiones = ["Lima", "Arequipa", "Cusco", "Trujillo", "Piura",
            "Iquitos", "Tacna", "Huancayo"]
canales = ["Tienda física", "App móvil", "Web", "Call center", "Promotor"]

df = pd.DataFrame({
    "id_cliente":       [f"MOV{i:06d}" for i in range(1, N+1)],
    "plan":             np.random.choice(planes, N, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    "precio_plan":      np.random.choice([29, 39, 59, 79, 99], N, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    "meses_cliente":    np.random.randint(1, 85, N),
    "gb_consumidos_mes":np.round(np.random.exponential(18, N), 1),
    "llamadas_mes":     np.random.poisson(45, N),
    "quejas_6meses":    np.random.poisson(0.7, N),
    "pagos_tardios":    np.random.randint(0, 8, N),
    "num_productos":    np.random.randint(1, 6, N),
    "region":           np.random.choice(regiones, N, p=[0.45, 0.10, 0.08, 0.10, 0.08, 0.07, 0.05, 0.07]),
    "canal_adquisicion":np.random.choice(canales, N),
    "tiene_descuento":  np.random.choice([0, 1], N, p=[0.65, 0.35]),
})

# Variable objetivo: churn (probabilidad basada en comportamiento real)
prob_churn = (
    0.03 +
    df["quejas_6meses"] * 0.12 +
    df["pagos_tardios"] * 0.06 -
    df["meses_cliente"] * 0.002 -
    df["num_productos"] * 0.03 -
    df["tiene_descuento"] * 0.05 +
    (df["precio_plan"] == 29).astype(int) * 0.04
).clip(0.01, 0.92)

# Introducir sesgo geográfico: clientes de Lima tienen 30% menos probabilidad de churn
# (representan más datos de calidad en el sistema histórico)
prob_churn_ajustada = prob_churn.copy()
mask_lima = df["region"] == "Lima"
prob_churn_ajustada[mask_lima] = prob_churn[mask_lima] * 0.70
prob_churn_ajustada[~mask_lima] = prob_churn[~mask_lima] * 1.10

df["churn"] = (np.random.random(N) < prob_churn_ajustada).astype(int)

print(f"✅ Dataset Movistar Perú: {len(df):,} clientes")
print(f"📊 Churn rate global: {df['churn'].mean():.1%}")
print(f"📊 Churn rate Lima: {df[mask_lima]['churn'].mean():.1%}")
print(f"📊 Churn rate otras regiones: {df[~mask_lima]['churn'].mean():.1%}")
print(f"\nEstructura del dataset:")
print(df.dtypes)
df.head()
```

**Punto de verificación 1:** ¿Ves aproximadamente 8-10% churn global? ¿Ves diferencia entre Lima y otras regiones? → Continúa.

---

### Celda 2: Exploración de datos (EDA)

```python
# ============================================================
# CELDA 2: Análisis Exploratorio de Datos (EDA)
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("Exploración del Dataset Movistar Perú", fontsize=14, fontweight='bold')

# Distribución de la variable objetivo
df["churn"].value_counts().plot(kind="bar", ax=axes[0,0], color=["steelblue", "coral"])
axes[0,0].set_title("Distribución Churn")
axes[0,0].set_xticklabels(["No churn (0)", "Churn (1)"], rotation=0)
axes[0,0].set_ylabel("Clientes")

# Churn rate por plan
churn_plan = df.groupby("plan")["churn"].mean() * 100
churn_plan.sort_values().plot(kind="barh", ax=axes[0,1], color="steelblue")
axes[0,1].set_title("Churn Rate por Plan (%)")
axes[0,1].set_xlabel("% de clientes que hacen churn")

# Distribución de quejas por grupo (churn vs no churn)
df[df["churn"]==0]["quejas_6meses"].hist(ax=axes[0,2], alpha=0.7, label="No churn", color="steelblue")
df[df["churn"]==1]["quejas_6meses"].hist(ax=axes[0,2], alpha=0.7, label="Churn", color="coral")
axes[0,2].set_title("Quejas por grupo")
axes[0,2].legend()

# Meses como cliente vs churn
df.groupby("meses_cliente")["churn"].mean().rolling(5).mean().plot(ax=axes[1,0], color="steelblue")
axes[1,0].set_title("Churn rate por antigüedad (suavizado)")
axes[1,0].set_xlabel("Meses como cliente")
axes[1,0].set_ylabel("Probabilidad de churn")

# Churn por región
churn_region = df.groupby("region")["churn"].mean() * 100
churn_region.sort_values(ascending=False).plot(kind="bar", ax=axes[1,1], color="steelblue")
axes[1,1].set_title("Churn Rate por Región (%)")
axes[1,1].set_xlabel("")
axes[1,1].tick_params(axis='x', rotation=45)

# Correlación de variables numéricas
correlaciones = df[["meses_cliente", "quejas_6meses", "pagos_tardios",
                     "num_productos", "tiene_descuento", "churn"]].corr()
sns.heatmap(correlaciones, annot=True, fmt=".2f", cmap="coolwarm",
            ax=axes[1,2], center=0)
axes[1,2].set_title("Correlación con Churn")

plt.tight_layout()
plt.savefig("movistar_eda.png", dpi=150, bbox_inches='tight')
plt.show()
print("✅ EDA guardado como movistar_eda.png")
```

**Reflexión 1:** Observa el gráfico de churn por región. ¿Qué diferencia ves entre Lima y las demás regiones? ¿Por qué ocurre esa diferencia (pista: mira cómo se generó el dataset en la Celda 1)?

*Tu respuesta aquí (en comentarios Python):*
```python
# Reflexión 1:
# Lo que observé en el gráfico de churn por región:
# _______________________________________________
# Por qué ocurre esa diferencia:
# _______________________________________________
```

---

## PARTE 2 — CONSTRUCCIÓN DEL MODELO (60 min)

### Celda 3: Preprocesamiento

```python
# ============================================================
# CELDA 3: Preprocesamiento — COMPLETA LOS ___
# ============================================================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Codificar variables categóricas (texto → número)
df_modelo = df.copy()

# Encoding de columnas categóricas
for col in ["plan", "region", "canal_adquisicion"]:
    le = LabelEncoder()
    df_modelo[col + "_cod"] = le.fit_transform(df_modelo[col])

# Seleccionar features (X) y variable objetivo (y)
features = ["precio_plan", "meses_cliente", "gb_consumidos_mes",
            "llamadas_mes", "quejas_6meses", "pagos_tardios",
            "num_productos", "tiene_descuento",
            "plan_cod", "region_cod", "canal_adquisicion_cod"]

X = df_modelo[features]
y = df_modelo["___"]           # ← COMPLETA: variable objetivo

print(f"Features utilizadas: {features}")
print(f"Shape de X: {X.shape}")
print(f"Distribución de y: {y.value_counts().to_dict()}")

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=___,             # ← COMPLETA: proporción de prueba
    random_state=2026,
    stratify=y                 # mantiene proporción de churn en ambos sets
)
print(f"\nEntrenamiento: {len(X_train):,} clientes")
print(f"Prueba: {len(X_test):,} clientes")

# Normalizar: escalar al mismo rango
# IMPORTANTE: fit SOLO en entrenamiento para no espiar los datos de prueba
scaler = ___()                 # ← COMPLETA: clase del escalador
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)   # solo transform, no fit

print("\n✅ Preprocesamiento completo")
print(f"Media de X_train_scaled: {X_train_scaled.mean():.4f} (debe ser ≈ 0)")
print(f"Std  de X_train_scaled: {X_train_scaled.std():.4f} (debe ser ≈ 1)")
```

*Pistas para los `___`:*
- `y = df_modelo["___"]` → `"churn"`
- `test_size=___` → `0.2` (20% para prueba)
- `scaler = ___()` → `StandardScaler`

**Punto de verificación 2:** La media de `X_train_scaled` debe ser ≈ 0 y la std ≈ 1 → normalización correcta.

---

### Celda 4: Entrenar y comparar modelos

```python
# ============================================================
# CELDA 4: Entrenamiento y comparación de modelos
# ============================================================
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                              f1_score, roc_auc_score, accuracy_score)

# Definir los 3 modelos a comparar
modelos = {
    "Regresión Logística": LogisticRegression(
        random_state=2026, max_iter=1000, class_weight="balanced"
    ),
    "Árbol de Decisión":   DecisionTreeClassifier(
        max_depth=5, min_samples_leaf=20, random_state=2026
    ),
    "Random Forest":       RandomForestClassifier(
        n_estimators=100, max_depth=8, random_state=2026, class_weight="balanced"
    )
}

resultados = {}
for nombre, modelo in modelos.items():
    # Entrenar
    modelo.fit(X_train_scaled, y_train)
    
    # Predecir
    y_pred = modelo.predict(X_test_scaled)
    y_prob = modelo.predict_proba(X_test_scaled)[:, 1]  # probabilidad de churn
    
    # Métricas
    resultados[nombre] = {
        "accuracy":  round(accuracy_score(y_test, y_pred), 4),
        "f1_churn":  round(f1_score(y_test, y_pred, zero_division=0), 4),
        "auc_roc":   round(roc_auc_score(y_test, y_prob), 4),
        "modelo":    modelo,
        "y_pred":    y_pred,
    }
    print(f"\n=== {nombre} ===")
    print(classification_report(y_test, y_pred,
                                 target_names=["Se queda", "Hace churn"],
                                 zero_division=0))

# Tabla comparativa
print("\n" + "="*55)
print("TABLA COMPARATIVA DE MODELOS")
print("="*55)
print(f"{'Modelo':<25} {'Accuracy':>9} {'F1-Churn':>9} {'AUC-ROC':>9}")
print("-"*55)
for nombre, r in resultados.items():
    print(f"{nombre:<25} {r['accuracy']:>9.4f} {r['f1_churn']:>9.4f} {r['auc_roc']:>9.4f}")
```

**Punto de verificación 3:** ¿El Random Forest tiene el mayor AUC-ROC? ¿El F1-Churn es mayor que 0.40 en al menos un modelo? Con datos desbalanceados (8% churn), un F1 de 0.40-0.55 en la clase churn es un buen resultado inicial.

---

### Celda 5: Visualización de la matriz de confusión y curva ROC

```python
# ============================================================
# CELDA 5: Visualizar el mejor modelo
# ============================================================
from sklearn.metrics import roc_curve
import warnings
warnings.filterwarnings('ignore')

# Tomar el Random Forest como mejor modelo
mejor_modelo = resultados["Random Forest"]["modelo"]
y_pred_mejor  = resultados["Random Forest"]["y_pred"]
y_prob_mejor  = mejor_modelo.predict_proba(X_test_scaled)[:, 1]

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Evaluación del Modelo Random Forest — Churn Movistar Perú",
             fontsize=13, fontweight='bold')

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred_mejor)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=["Pred: Queda", "Pred: Churn"],
            yticklabels=["Real: Queda", "Real: Churn"])
axes[0].set_title("Matriz de Confusión")

# Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob_mejor)
auc_val = resultados["Random Forest"]["auc_roc"]
axes[1].plot(fpr, tpr, color='steelblue', lw=2, label=f"AUC = {auc_val:.3f}")
axes[1].plot([0, 1], [0, 1], color='gray', linestyle='--', label="Modelo aleatorio")
axes[1].set_xlabel("Tasa de Falsos Positivos")
axes[1].set_ylabel("Tasa de Verdaderos Positivos (Recall)")
axes[1].set_title("Curva ROC")
axes[1].legend()

# Importancia de variables
importancias = pd.Series(
    mejor_modelo.feature_importances_,
    index=features
).sort_values(ascending=True)
importancias.plot(kind="barh", ax=axes[2], color="steelblue")
axes[2].set_title("Importancia de Variables")
axes[2].set_xlabel("Importancia relativa")

plt.tight_layout()
plt.savefig("movistar_evaluacion.png", dpi=150, bbox_inches='tight')
plt.show()
print("✅ Gráficos guardados como movistar_evaluacion.png")
```

---

### Celda 6: Análisis de equidad por región (FAIRNESS)

```python
# ============================================================
# CELDA 6: ANÁLISIS DE EQUIDAD — COMPLETA LOS ___
# ¿El modelo predice igual de bien para todas las regiones?
# ============================================================

print("="*60)
print("ANÁLISIS DE EQUIDAD (FAIRNESS) — MOVISTAR PERÚ")
print("="*60)

# Agregar predicciones al dataset de prueba
X_test_df = pd.DataFrame(X_test_scaled, columns=features, index=X_test.index)
df_eval = df.loc[X_test.index].copy()
df_eval["y_pred"] = y_pred_mejor
df_eval["y_prob"] = y_prob_mejor

# Análisis por región
print("\n📊 MÉTRICAS POR REGIÓN:")
print(f"{'Región':<15} {'N clientes':>12} {'Churn real':>12} {'F1-Score':>10} {'AUC-ROC':>10}")
print("-"*60)

metricas_region = {}
for region in sorted(df_eval["region"].unique()):
    mask = df_eval["region"] == region
    y_real_r = y_test[mask]
    y_pred_r = df_eval.loc[mask, "y_pred"]
    y_prob_r = df_eval.loc[mask, "y_prob"]
    
    n  = mask.sum()
    f1 = f1_score(y_real_r, y_pred_r, zero_division=0)
    auc = roc_auc_score(y_real_r, y_prob_r) if y_real_r.sum() > 0 else float('nan')
    churn_real = y_real_r.mean()
    
    metricas_region[region] = {"f1": f1, "auc": auc, "n": n, "churn_real": churn_real}
    flag = "⚠️" if f1 < 0.30 else "✅"
    print(f"{region:<15} {n:>12,} {churn_real:>11.1%} {f1:>10.3f} {auc:>10.3f} {flag}")

# Detectar disparidad
f1_values = [v["f1"] for v in metricas_region.values()]
disparidad = max(f1_values) - min(f1_values)
print(f"\n📊 Disparidad máxima de F1 entre regiones: {disparidad:.3f}")
if disparidad > 0.15:
    print("⚠️  ALERTA: El modelo no funciona igual para todas las regiones")
    print("   Esto puede indicar SESGO GEOGRÁFICO")
else:
    print("✅ El modelo funciona de forma comparable en todas las regiones")
```

**Reflexión 2:** ¿Qué regiones tienen el F1 más bajo? ¿Qué consecuencia tendría para un cliente de esa región si Movistar usa este modelo para retención?

```python
# Reflexión 2:
# Regiones con F1 más bajo:
# _______________________________________________
# Consecuencia para el cliente de esa región:
# _______________________________________________
```

---

## PARTE 3 — DESAFÍO (30 min)

### Celda 7: Mejorar el modelo para las regiones con sesgo

```python
# ============================================================
# CELDA 7: DESAFÍO — Mitigar el sesgo geográfico
# 
# Investiga y aplica al menos UNA de estas estrategias:
# 1. Entrenar con mayor peso para las regiones sub-representadas
# 2. Ajustar el threshold de decisión para las regiones con peor F1
# 3. Entrenar modelos separados por región
# 
# Documenta qué estrategia elegiste y por qué.
# ============================================================

# OPCIÓN 1 sugerida: ajustar el threshold por región
# (cambiar 0.5 por un umbral más bajo para las regiones con menos datos)

print("=== ESTRATEGIA DE MITIGACIÓN DE SESGO ===")

# Identificar la región con peor F1
peor_region = min(metricas_region, key=lambda r: metricas_region[r]["f1"])
mejor_region = max(metricas_region, key=lambda r: metricas_region[r]["f1"])
print(f"Región con peor F1: {peor_region} ({metricas_region[peor_region]['f1']:.3f})")
print(f"Región con mejor F1: {mejor_region} ({metricas_region[mejor_region]['f1']:.3f})")

# Ajustar el threshold para la región con peor desempeño
# En lugar de 0.5 (default), usar 0.35 para capturar más churners reales
threshold_ajustado = 0.35

mask_peor = df_eval["region"] == peor_region
y_real_peor = y_test[mask_peor]
y_prob_peor = df_eval.loc[mask_peor, "y_prob"]

# Predecir con threshold normal vs ajustado
y_pred_normal  = (y_prob_peor >= 0.50).astype(int)
y_pred_ajustado = (y_prob_peor >= threshold_ajustado).astype(int)

f1_normal   = f1_score(y_real_peor, y_pred_normal, zero_division=0)
f1_ajustado = f1_score(y_real_peor, y_pred_ajustado, zero_division=0)

print(f"\n📊 Resultados para {peor_region}:")
print(f"   F1 con threshold 0.50: {f1_normal:.3f}")
print(f"   F1 con threshold {threshold_ajustado}: {f1_ajustado:.3f}")
mejora = f1_ajustado - f1_normal
print(f"   Mejora: {mejora:+.3f}")

# TU TURNO: ¿Por qué bajar el threshold mejora el Recall pero reduce la Precision?
# Escribe tu explicación aquí:
print("""
¿Por qué bajar el threshold mejora el Recall pero reduce la Precision?
Explicación: _______________________________________________
""")
```

**Reflexión final:**

```python
# ============================================================
# REFLEXIÓN FINAL — Responde en los comentarios
# ============================================================
reflexion_final = """
1. ¿Cuál fue el mayor aprendizaje técnico de este laboratorio?
   (Menciona una cosa concreta que puedas aplicar en un proyecto real)
   
   Respuesta: _______________________________________________

2. Si Movistar Perú desplegara este modelo en producción para
   decidir qué clientes reciben una oferta de retención, y solo
   puede llamar a 2,000 clientes por semana, ¿optimizarías 
   Precision o Recall? ¿Con qué threshold comenzarías?
   
   Respuesta: _______________________________________________

3. Describe en 2 líneas cómo usarías el análisis de equidad
   (Celda 6) en tu proyecto de Big Data del curso.
   
   Respuesta: _______________________________________________
"""
print(reflexion_final)
```

---

## ENTREGABLES

Sube al repositorio `semana_06/Soluciones/TuNombre_TuCodigo/` los siguientes archivos:

| # | Archivo | Descripción |
|---|---------|-------------|
| 1 | `movistar_churn.ipynb` | Notebook completo con todas las celdas ejecutadas y reflexiones respondidas |
| 2 | `movistar_eda.png` | Gráfico de EDA de la Celda 2 |
| 3 | `movistar_evaluacion.png` | Gráfico de evaluación de la Celda 5 |
| 4 | `README.md` | 5 líneas máximo: qué modelo obtuviste, F1-Score del churn, qué región tuvo más sesgo y cómo lo mitigaste |

**Formato del PR:**
- Título: `S6 Movistar Churn — TuNombre (TuCódigo)`
- Branch: `semana06-ml-TuNombre`

---

## RÚBRICA DE EVALUACIÓN

| Criterio | Excelente (100%) | Suficiente (60%) | Insuficiente (0%) | Pts |
|----------|-----------------|-----------------|-------------------|-----|
| **Celda 3: Preprocesamiento** | Los 3 `___` correctos, normalización verificada | 2/3 correctos | Sin ejecutar o con error | 20 |
| **Celda 4: 3 modelos comparados** | Tabla comparativa con los 3 modelos + interpretación | 2/3 modelos | Solo 1 modelo o sin tabla | 25 |
| **Celda 5: Visualizaciones** | 3 gráficos con datos reales, guardados como PNG | 2/3 gráficos | Sin visualizaciones | 15 |
| **Celda 6: Análisis de equidad** | Identifica región con sesgo + interpreta consecuencia | Corre el código pero no interpreta | Sin análisis de equidad | 20 |
| **Celda 7: Desafío** | Aplica una estrategia de mitigación y explica el trade-off Precision/Recall | Ajusta threshold sin explicar | Sin desafío | 10 |
| **Reflexiones (3)** | Respuestas técnicas específicas vinculadas al caso | Respuestas genéricas | Sin respuestas | 10 |

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 6 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay | github.com/RubenCarty/bigdata-ua-2026-1*
