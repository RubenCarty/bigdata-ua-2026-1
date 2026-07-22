# S5 — Laboratorio en Casa: Pipeline Spark Completo (TaxiApp Lima)

**Estudiante:** Junior Emerzon Ortiz Andrade
**Código:** 2221895332
**Curso:** Big Data DD283 | Universidad Autónoma del Perú | 2026-1
**Entorno:** Google Colab (PySpark 3.5)

## Contenido

| Archivo | Descripción |
|---------|-------------|
| `S5_LAB_CASA_BIGDATA.md` | Guía resuelta con código y resultados documentados |
| `S5_lab_casa_taxiapp.ipynb` | Notebook ejecutado con outputs visibles |
| `screenshots/` | Capturas de las 6 celdas ejecutadas |

## Nota sobre el entorno

El laboratorio se desarrolló en **Google Colab** (opción B de la guía) porque Databricks Free Edition —que reemplazó a Community Edition— tiene DBFS/FileStore deshabilitado en su entorno serverless. Todas las rutas `/FileStore/...` fueron adaptadas a rutas locales, manteniendo intacta la lógica del pipeline Bronze → Silver → Gold.

## Resultados del pipeline

- **Bronze:** 10,000 viajes generados (13 columnas)
- **Silver:** 8,767 viajes válidos (se eliminaron 1,233 = 12.3%)
- **Gold 1:** Top 10 rutas — lidera Surco → Comas (S/595.59)
- **Gold 2:** Conductores estrella — 0 resultados (ver diagnóstico)
- **Gold 3:** Mayor facturación: turno tarde + Yape (S/12,574.99)
- **Streaming:** alertas detectadas en los ciclos 3 y 4

> **Nota sobre Gold 2:** La consulta de conductores estrella (rating > 4.5, > 20 viajes) devuelve una tabla vacía. No es un error: el rating se genera con media 4.15, y el máximo promedio entre conductores con más de 20 viajes es 4.36. Se agregó una consulta de diagnóstico con umbral realista (rating > 4.2) que sí devuelve los 10 mejores conductores disponibles.

---

## Reflexión 1 — Distribución de estados e impacto en ingresos

La distribución fue: 87.7% completados (8,767), 10.2% cancelados (1,017) y 2.2% incidentes (216). Solo los completados generan ingresos, así que el 12.4% restante es demanda no monetizada. El 2.2% de incidentes es el más costoso: además de no facturar, puede implicar reembolsos, soporte y daño reputacional, afectando el ingreso neto más de lo que sugiere su porcentaje. Reducir cancelaciones e incidentes es una palanca directa de rentabilidad.

## Reflexión 2 — Escalar `rowsPerSecond` a 1000

Al pasar de 20 a 1000 viajes/segundo, el sistema seguiría funcionando lógicamente, pero el cuello de botella sería la capacidad de cómputo de un solo clúster (en Databricks Community o el entorno local de Colab hay un único nodo). Con 1000 filas/seg, el procesamiento de las ventanas y las agregaciones podría no completarse antes de que lleguen los siguientes datos, generando retraso acumulado (latencia creciente) y presión de memoria. En producción se resolvería escalando horizontalmente (más nodos) o particionando el stream, algo que un solo clúster no permite.

## Reflexión 3 — Structured Streaming en el proyecto grupal

Sí. Nuestro proyecto (Grupo 3 — pronóstico de demanda hospitalaria en EsSalud) tiene un caso natural para Structured Streaming: el **monitoreo en tiempo real de la ocupación de camas** por establecimiento. Hoy el pipeline es batch (Prophet predice a 4 semanas), pero la ocupación cambia hora a hora, y nuestra arquitectura ya define la regla `BRECHA = demanda − oferta → si BRECHA > 0, activar protocolo de contingencia`. Esa lógica es idéntica al patrón del laboratorio: agregar en ventana temporal y filtrar por umbral. En vez de `rating < 3.5`, la alerta sería `tasa_ocupacion > 1.0` (sobreocupación, el caso que en enero llegó a 112%), disparando la redistribución de pacientes a otro establecimiento de la red.

**Ventanas temporales según el fenómeno** (no habría una sola, sino tres niveles):

- **Ocupación de camas y emergencias → ventana de 1 hora** (deslizante cada 15 min). Fenómeno operativo que cambia rápido y requiere reacción inmediata del Director de Hospital.
- **Vigilancia de brotes epidemiológicos → ventana de 1 semana**, alineada con la semana epidemiológica (SE) que ya usamos como campo del dataset y con el boletín MINSA. Detectar un brote no tiene sentido en minutos: se necesita acumular casos.
- **Clima (SENAMHI) → ventana diaria**, porque nuestras hipótesis usan rezagos de 2-3 semanas (`temperatura_max_lag2`), no lecturas instantáneas.

**Conclusión de diseño:** la ventana debe coincidir con la **velocidad del fenómeno**, no con la velocidad del dato. Los datos de camas llegan continuamente, pero un brote de dengue se manifiesta en semanas. Usar una ventana de 30 segundos para vigilancia epidemiológica generaría ruido y falsos positivos; usar una ventana semanal para la ocupación de camas haría inútil la alerta, porque el colapso ya habría ocurrido.