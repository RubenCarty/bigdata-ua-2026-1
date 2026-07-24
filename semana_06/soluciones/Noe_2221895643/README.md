

* **Modelo final obtenido:** Random Forest Classifier (con un AUC-ROC aproximado de 0.88).
* **F1-Score del churn:** Se obtuvo un F1-Score general de ~0.52 para la predicción de la clase de abandono.
* **Región con mayor sesgo:** Lima presentó el mayor sesgo debido a la alteración artificial de sus probabilidades en la generación de datos.
* **Estrategia de mitigación:** Se implementó una optimización del umbral de decisión (bajando el threshold a 0.35) para aumentar el Recall en la región afectada.