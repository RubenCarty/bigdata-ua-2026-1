# S6 — Predicción de Churn Movistar Perú | Junior Emerzon Ortiz Andrade (2221895332)

- **Mejor modelo:** Regresión Logística (AUC-ROC 0.7861, F1-Churn **0.4146**) — superó al Random Forest (AUC 0.7726, F1 0.3743) que la guía asumía como ganador. El Árbol de Decisión tuvo la mejor accuracy (0.843) pero un recall de churn de solo 0.06: la accuracy engaña con clases desbalanceadas (14.5% churn).
- **F1-Score del churn:** 0.4146 (Regresión Logística) / 0.3743 (Random Forest, usado en las visualizaciones por proveer `feature_importances_`).
- **Región con más sesgo:** **Trujillo** (F1 = 0.250, la única bajo el umbral de 0.30). Disparidad máxima de F1 entre regiones: **0.264** (> 0.15 → alerta de sesgo geográfico). Dato relevante: Lima, con 4x más datos, también quedó bajo (F1 0.311).
- **Mitigación aplicada:** ajuste del threshold de decisión solo para Trujillo, de 0.50 → 0.35, elevando su F1 de 0.250 a 0.302 (+0.052). El barrido de thresholds mostró que 0.45 optimiza el F1 (0.368) y 0.30 maximiza el recall (0.714).
- **Trade-off:** bajar el threshold sube el recall y baja la precision. En Movistar el falso negativo es el error caro (adquirir un cliente cuesta 5x más que retenerlo), por lo que priorizar recall es la decisión correcta de negocio.
