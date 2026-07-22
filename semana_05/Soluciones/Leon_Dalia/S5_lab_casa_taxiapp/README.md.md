# S5 — LABORATORIO EN CASA: Pipeline Spark Completo
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: PySpark + Spark SQL + Streaming simulado en Databricks Community

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | DALIA NANCY LEON AGUILAR |
| **Código** | 2221895373|
| **Fecha de entrega** | 11 JULIO 2026 |
| **Tiempo estimado** | 2 horas |
| **Modalidad** | Individual |
| **Entorno** | Databricks Community Edition (principal) · Google Colab (alternativa) |

---


---

## CONTEXTO DEL LABORATORIO

**Dataset:** 10,000 viajes de taxi en Lima Metropolitana (datos sintéticos basados en patrones reales de taxis por aplicativo).


```

**Pregunta de reflexión 1:** ¿Qué distribución de estados encontraste? ¿Qué porcentaje de viajes terminó en "incidente"? ¿Cómo afecta esto a los ingresos netos de TaxiApp?

```python
# R1: Se puede observar que hay tres estados, Completado con 87%, cancelado con 10% e incidente con 2%.Y con respecto  del porcentaje de incidente  de 2,2 nos indica que  no generaningresos  pero sí consumieron recursos  como el tiempo del conductor , atencion al cliente , posibles reembolsos, por lo que se reduce la eficiencia operativa  y los ingresos netos de  taxiapp. 

```

---

## PARTE 2 — APLICACIÓN: Pipeline Bronze → Silver → Gold (60 min)


**Pregunta de reflexión 2:** ¿Qué pasaría si aumentas `rowsPerSecond` a 1000? ¿El sistema de alertas seguiría funcionando igual? ¿Cuál sería el cuello de botella en Databricks Community (1 clúster)?

```python
# R2: Se observa que el volumen de los eventos por ventana de los 30 segundo crecio drasticamente , que hizo que aumnetara la presión de memoria  en el outputMode, ya que  el spark debe mantnerse en estado completo de las ventanas y el de los conductoresne memoria state store, para poder recalcular  la agregación  en cada microbatch. Y con respecto al cello botella seria principalmente en la memora del drive/executor único y el shuffle para el groupBy, loque esto ocasioanria  demoras e creceintes del backpressure o incluso  de errores de OOM out of memory si la ventana no se recorta con watermarking.

```

**Pregunta de reflexión 3 (conexión con proyecto grupal):** ¿Tu grupo podría aplicar Structured Streaming para detectar patrones en tiempo real en su proyecto? ¿Cuál sería la ventana temporal más adecuada?

```python
# R3: Realmente si se podria, se aplica en  dataspace o gestión institucional,  detecta picos  anómalos de solicitudes  o eventos (como transacciones Yape sospechosas o caídas repentinas de un servicio) casi en tiempo real. Una ventana temporal razonable dependería de la frecuencia natural de los eventos: para monitoreo transaccional se recomendaría una ventana corta (1-5 minutos) para detectar anomalías rápido sin generar demasiado ruido estadístico, mientras que para métricas de uso institucional (por ejemplo accesos a un portal) una ventana de 15-30 minutos sería suficiente para suavizar la variabilidad y aun así reaccionar a tiempo.

```

---

## ENTREGABLES

### Estructura del PR en GitHub:

```
semana_05/Soluciones/TuNombre_TuCodigo/
├── S5_lab_casa_taxiapp.ipynb       ← Notebook exportado con outputs visibles
│   o S5_lab_casa_taxiapp.py
├── screenshots/
│   ├── celda1_bronze_output.png    ← Output de la Celda 1
│   ├── celda3_silver_output.png    ← Output de la Celda 3 (tabla con nuevas columnas)
│   ├── celda4_gold_rutas.png       ← Top 10 rutas
│   ├── celda4_gold_conductores.png ← Conductores estrella
│   ├── celda5_dashboard.png        ← Los 3 gráficos del dashboard
│   └── celda6_alertas.png          ← Output del streaming con alertas
└── README.md                        ← Reflexiones 1, 2 y 3 respondidas
```

**Rama del PR:** `semana05-lab-TuNombre`

### Rúbrica básica

| Criterio | Pts |
|----------|-----|
| Celda 1: dataset generado con output visible | 10 |
| Celda 3: Silver completada con los ___ correctos y output | 25 |
| Celda 4: Gold completada con los ___ correctos, 3 tablas visibles | 30 |
| Celda 5: Dashboard con 3 gráficos guardado | 15 |
| Celda 6: Stream ejecutado al menos 2 ciclos con alertas | 15 |
| Reflexiones 1, 2 y 3 respondidas con argumento técnico | 5 |
| **TOTAL** | **100** |

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Laboratorio en casa — Databricks Community Edition*
