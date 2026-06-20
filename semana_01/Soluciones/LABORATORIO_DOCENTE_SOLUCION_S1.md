# LABORATORIO S1 — SOLUCIÓN COMPLETA PARA EL DOCENTE
## CONFIDENCIAL — Solo para uso del docente
### Big Data (DD283) | Universidad Autónoma del Perú

---

## GUÍA DE CORRECCIÓN Y SOLUCIONES COMPLETAS

### ERRORES COMUNES QUE VERÁS EN LOS ENTREGABLES

**Error 1: ModuleNotFoundError**
```
Error: ModuleNotFoundError: No module named 'pandas'
Solución para el estudiante:
  En Colab: !pip install pandas matplotlib seaborn
  En local: conda install pandas matplotlib seaborn
```

**Error 2: El gráfico no se muestra**
```
Causa: Olvidaron agregar plt.show() o están en modo script
Solución: Agregar %matplotlib inline al inicio del notebook (magia de Jupyter)
```

**Error 3: Encoding con texto en español**
```
Error: UnicodeDecodeError al leer archivos CSV con acentos
Solución: pd.read_csv('archivo.csv', encoding='utf-8')
         O: pd.read_csv('archivo.csv', encoding='latin-1')
```

---

## SOLUCIÓN COMPLETA — CÓDIGO VERIFICADO

### PARTE 2: Dataset de transacciones — Outputs esperados

```
Dataset creado con 10,000 registros
Columnas: ['id_transaccion', 'fecha', 'cliente_id', 'departamento', 'categoria', 
            'monto_soles', 'metodo_pago', 'es_fraude']

=== INFORMACIÓN GENERAL DEL DATASET ===
Tamaño del dataset: (10000, 8)
Filas: 10,000
Columnas: 8

=== ANÁLISIS DE VOLUMEN ===
Registros: 10,000
Tamaño en memoria: ~2,847.9 KB
Si escalamos a 100 millones de registros: ~27.8 GB

=== ANÁLISIS DE VELOCIDAD ===
Promedio de transacciones por día: ~27
Máximo de transacciones en un día: varía (aprox. 40-60)

=== ANÁLISIS DE VERACIDAD ===
Transacciones normales: ~9,800
Transacciones sospechosas (fraude): ~200
Tasa de fraude: ~2.00%
```

### Respuesta esperada para la Arquitectura (Parte 5)

**Arquitectura correcta** para una empresa retail peruana:

```python
arquitectura = {
    "empresa": "Supermercados Wong / Plaza Vea / Tottus",
    "problema_principal": "Analizar millones de transacciones diarias para detectar fraude, personalizar ofertas y optimizar stock",
    
    "fuentes_de_datos": {
        "estructuradas": [
            "Base de datos POS (puntos de venta) - registros de tickets",
            "Sistema ERP (SAP/Oracle) - inventario y compras",
            "Base de datos de clientes - CRM"
        ],
        "semi_estructuradas": [
            "API de pagos Yape/Plin - JSON con transacciones móviles",
            "Logs de app móvil - JSON de comportamiento de usuario",
            "Datos de tarjetas de fidelidad - XML"
        ],
        "no_estructuradas": [
            "Videos de cámaras de seguridad - detección de comportamiento",
            "Comentarios en redes sociales - análisis de sentimiento",
            "Imágenes de tickets para OCR"
        ]
    },
    
    "estimacion_volumen": {
        "registros_por_dia": "500,000 transacciones × 8 columnas = 4 millones de campos",
        "tamaño_estimado_por_año": "~500 GB solo en transacciones, ~5 TB con videos e imágenes"
    },
    
    "tecnologias_propuestas": {
        "ingesta": "Apache Kafka (streaming de transacciones en tiempo real)",
        "almacenamiento": "HDFS / AWS S3 (datos históricos) + MongoDB (datos de clientes)",
        "procesamiento": "Apache Spark (análisis batch) + Spark Streaming (tiempo real)",
        "visualizacion": "Power BI / Tableau con dashboards de gerencia"
    },
    
    "casos_uso_principales": [
        "Detección de fraude en tiempo real (< 2 segundos por transacción)",
        "Recomendación personalizada de productos por cliente",
        "Predicción de demanda para optimizar inventario y evitar quiebres de stock",
        "Análisis de sentimiento en redes sociales para gestión de reputación"
    ]
}
```

---

## RÚBRICA DE CORRECCIÓN DETALLADA

### Criterio 1: Notebook ejecutado sin errores (30 pts)
| Condición | Puntos |
|-----------|--------|
| Todas las celdas ejecutadas con output visible | 30 |
| La mayoría de celdas ejecutadas (1-2 errores) | 20 |
| Solo la mitad de celdas ejecutadas | 10 |
| No ejecutó el notebook | 0 |

### Criterio 2: Análisis datos estructurados (20 pts)
| Condición | Puntos |
|-----------|--------|
| Dataset creado correctamente + todas las métricas calculadas + gráficos | 20 |
| Dataset creado + métricas pero sin gráficos | 15 |
| Solo el dataset creado, sin análisis | 8 |
| No lo hizo | 0 |

### Criterio 3: Análisis JSON (15 pts)
| Condición | Puntos |
|-----------|--------|
| JSON parseado + convertido a DataFrame + resumen de completitud | 15 |
| JSON parseado + convertido a DataFrame | 10 |
| Solo cargó el JSON sin analizar | 5 |
| No lo hizo | 0 |

### Criterio 4: Análisis de texto (15 pts)
| Condición | Puntos |
|-----------|--------|
| Análisis de sentimiento correcto con resultados visualizados | 15 |
| Análisis correcto sin visualización | 10 |
| Intentó pero con errores parciales | 5 |
| No lo hizo | 0 |

### Criterio 5: Arquitectura (15 pts)
| Condición | Puntos |
|-----------|--------|
| Arquitectura coherente con tecnologías correctas para cada capa | 15 |
| Arquitectura coherente pero tecnologías incompletas | 10 |
| Template llenado pero sin reflexión real | 5 |
| No lo hizo | 0 |

### Criterio 6: README (5 pts)
| Condición | Puntos |
|-----------|--------|
| README completo con reflexión genuina personal | 5 |
| README con texto copiado o muy genérico | 2 |
| No hay README | 0 |

---

## FEEDBACK TIPO PARA EL DOCENTE

### Feedback positivo modelo:
> "Excelente trabajo! Tu análisis de datos de transacciones es correcto y el gráfico muestra claramente la distribución por departamento. Nota importante: en tu arquitectura mencionas 'usar una base de datos' pero en Big Data necesitamos ser más específicos — ¿qué base de datos? ¿Para qué tipo de datos? Te invito a revisar la diferencia entre HDFS, MongoDB y Redis para la siguiente sesión."

### Feedback de mejora modelo:
> "Tu notebook tiene errores de ejecución en las Partes 3 y 4. Te recomiendo revisar la importación del módulo JSON (línea 2) — asegúrate de que la cadena JSON esté correctamente formateada con comillas dobles. El análisis de texto que intentaste es el enfoque correcto, solo necesitas corregir el error de sintaxis. Puedes usar el chat de soporte para resolver esto antes de la próxima entrega."

---

## SOLUCIÓN RÁPIDA PARA MOSTRAR EN CLASE (si un estudiante está trabado)

```python
# SOLUCIÓN MÍNIMA VERIFICADA — Para mostrar en clase si es necesario
import pandas as pd
import matplotlib.pyplot as plt

# 1. DATOS ESTRUCTURADOS
df = pd.read_csv('https://raw.githubusercontent.com/datasets/co2-fossil-global/master/global.csv')
print("Datos cargados:", df.shape)
print(df.head())
df['Total'].plot(title='Emisiones CO2 en el Tiempo')
plt.show()

# 2. DATOS SEMI-ESTRUCTURADOS (JSON)
import json
dato = '{"empresa": "BCP", "clientes": 5000000, "ciudad": "Lima"}'
d = json.loads(dato)
print("Empresa:", d['empresa'])
print("Clientes:", d['clientes'])

# 3. DATO NO ESTRUCTURADO (texto)
texto = "Excelente servicio del BCP, muy rápido y eficiente"
palabras = texto.lower().split()
positivas = ['excelente', 'rápido', 'eficiente']
score = sum(1 for p in positivas if p in palabras)
print(f"Score positivo: {score}")
```

---

## DATASET ALTERNATIVO SI COLAB TIENE PROBLEMAS DE RED

Incluir este dataset hardcodeado como fallback:

```python
# Dataset de backup - no requiere descarga
data_backup = {
    'producto': ['Arroz', 'Aceite', 'Leche', 'Pan', 'Azucar'],
    'ventas_lima': [1500, 890, 1200, 2300, 670],
    'ventas_arequipa': [450, 230, 380, 780, 210],
    'precio_sol': [3.50, 8.90, 4.50, 0.30, 2.80]
}
df_backup = pd.DataFrame(data_backup)
df_backup['total_ventas'] = df_backup['ventas_lima'] + df_backup['ventas_arequipa']
df_backup['ingreso_total'] = df_backup['total_ventas'] * df_backup['precio_sol']
print(df_backup)
```

---

*CONFIDENCIAL — No distribuir a estudiantes*
