# S7 — LABORATORIO EN CASA: Scraping + Limpieza de Datos en Google Colab
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 7: Pipeline Completo — Del Sitio Web al Dataset Limpio

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha de entrega** | ______________________________________________ |
| **Duración estimada** | 2 horas |
| **Modalidad** | Individual o en pareja |
| **Herramienta principal** | Google Colab (gratuito) |
| **Entrega** | PR a `semana_07/Soluciones/TuNombre_TuCodigo/` en GitHub |

---

## OBJETIVO DEL LABORATORIO

Construir un pipeline completo de extracción, limpieza y normalización de datos: scrapear el catálogo de libros de `books.toscrape.com` (sitio de práctica oficial), limpiar y normalizar el dataset resultante, y generar un análisis de precios y valoraciones por categoría.

**Competencia que desarrolla:** Implementa un pipeline end-to-end de obtención y limpieza de datos con integridad, aplicando validaciones que preservan la esencia del dato original.

---

## SOFTWARE Y HERRAMIENTAS

### Google Colab (herramienta principal)

| Detalle | Información |
|---------|-------------|
| **Acceso** | colab.research.google.com |
| **Instalación** | Ninguna — 100% en el navegador |
| **Librerías a instalar** | requests, beautifulsoup4 (via `!pip install`) |
| **Librerías preinstaladas** | pandas, numpy, matplotlib, seaborn, re |

### Verificación del entorno (ejecutar en Celda 0):

```python
!pip install requests beautifulsoup4 -q

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import time
import matplotlib.pyplot as plt
import seaborn as sns

print(f"✅ requests: {requests.__version__}")
print(f"✅ bs4: {BeautifulSoup.__module__}")
print(f"✅ pandas: {pd.__version__}")
print("✅ Todas las librerías listas")
```

### Alternativa offline (si no hay internet para scrapear)

Si no puedes conectarte a `books.toscrape.com`, se provee un dataset de respaldo al final de la Celda 1 que puedes usar directamente. Sin embargo, se recomienda intentar el scraping real.

---

## CONTEXTO DEL CASO

`Books to Scrape` (`books.toscrape.com`) es una librería online ficticia diseñada específicamente para practicar web scraping de forma ética y legal — su robots.txt permite el acceso de scrapers y fue creado con ese propósito. Tiene 1,000 libros en 50 páginas, organizados en 50 categorías (Mystery, Travel, Science, etc.).

Tu misión: construir el catálogo completo de las primeras 10 páginas (200 libros), limpiar los datos y generar reportes de precios por categoría.

---

## PARTE 1 — EXPLORACIÓN: Entender el sitio y primer scraping (30 min)

### Celda 1: Inspeccionar y scrapear la primera página

```python
# ============================================================
# CELDA 1: Inspección + Primer Scraping
# Ejecutar y observar el output antes de continuar
# ============================================================
import urllib.robotparser

# PASO 0: Verificar que podemos scrapear (ética primero)
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://books.toscrape.com/robots.txt")
rp.read()
puede_scrapear = rp.can_fetch("*", "http://books.toscrape.com/catalogue/page-1.html")
print(f"¿robots.txt permite el scraping? {puede_scrapear}")

# PASO 1: Request a la primera página
HEADERS = {"User-Agent": "Mozilla/5.0 (UA-BigData-Lab/1.0 educational)"}
url_p1 = "http://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url_p1, headers=HEADERS, timeout=15)
print(f"\nStatus: {response.status_code}")
print(f"Tamaño HTML: {len(response.text):,} caracteres")

# PASO 2: Parsear con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# PASO 3: Explorar la estructura — ¿cómo están organizados los libros?
# Cada libro está en un <article class="product_pod">
articulos = soup.find_all("article", class_="product_pod")
print(f"\nLibros encontrados en la página 1: {len(articulos)}")

# PASO 4: Extraer datos del PRIMER libro para inspeccionar
primer_libro = articulos[0]
print("\n=== ESTRUCTURA DEL PRIMER LIBRO ===")
print(f"HTML:\n{primer_libro.prettify()[:500]}")  # ver los primeros 500 chars

# PASO 5: Extraer cada campo del primer libro
titulo    = primer_libro.find("h3").find("a")["title"]
precio    = primer_libro.find("p", class_="price_color").text
rating_cl = primer_libro.find("p", class_="star-rating")["class"]  # lista de clases
rating    = rating_cl[1]  # 2da clase: "One", "Two", "Three", "Four", "Five"
stock     = primer_libro.find("p", class_="instock availability").text.strip()

# URL de la ficha individual del libro (para obtener la categoría después)
url_ficha = "http://books.toscrape.com/catalogue/" + primer_libro.find("h3").find("a")["href"]

print(f"\nTítulo: {titulo}")
print(f"Precio (raw): {precio}")
print(f"Rating (raw): {rating}")
print(f"Stock: {stock}")
print(f"URL ficha: {url_ficha}")
```

**PUNTO DE VERIFICACIÓN 1:** ¿Ves 20 libros en la página 1? ¿El primer libro tiene precio con `£` y rating como texto ("One", "Two", etc.)? → Estos son exactamente los problemas que limpiarás en la Parte 2.

**Reflexión 1:** Observa el `precio` — tiene el símbolo `£` y usa `.` como separador decimal. Observa el `rating` — es una palabra en inglés. ¿Qué tipo de transformación necesita cada campo para ser útil en un análisis?

```python
# Reflexión 1 — escribe tu respuesta:
"""
El campo precio necesita:
_______________________________________________

El campo rating necesita:
_______________________________________________
"""
```

---

### Celda 2: Obtener la categoría del libro (visitar la ficha individual)

```python
# ============================================================
# CELDA 2: Extraer la categoría del primer libro
# (la categoría está en la ficha individual, no en el listado)
# ============================================================

# Visitar la ficha del primer libro
response_ficha = requests.get(url_ficha, headers=HEADERS, timeout=15)
soup_ficha = BeautifulSoup(response_ficha.text, "html.parser")

# La categoría está en el breadcrumb: Home > [Categoría] > [Título]
breadcrumb = soup_ficha.select("ul.breadcrumb li a")
# El 2do elemento del breadcrumb es la categoría
categoria = breadcrumb[1].text.strip()
print(f"Categoría del primer libro: {categoria}")

# También podemos extraer la descripción
descripcion_el = soup_ficha.find("div", id="product_description")
if descripcion_el:
    descripcion = descripcion_el.find_next_sibling("p").text.strip()
    print(f"Descripción (primeros 100 chars): {descripcion[:100]}...")
    
time.sleep(1)  # siempre esperar entre requests
```

---

## PARTE 2 — APLICACIÓN: Scraping completo + Limpieza (60 min)

### Celda 3: Scraping de 10 páginas completo

```python
# ============================================================
# CELDA 3: Scraping de las primeras 10 páginas
# (200 libros en total)
# IMPORTANTE: Ejecuta y espera ~15-20 segundos (hay pausas)
# ============================================================

BASE_URL    = "http://books.toscrape.com/catalogue/page-{}.html"
FICHA_BASE  = "http://books.toscrape.com/catalogue/"
NUM_PAGINAS = 10    # 10 páginas × 20 libros = 200 libros

todos_los_libros = []
errores = 0

print(f"Iniciando scraping de {NUM_PAGINAS} páginas...")

for num_pagina in range(1, NUM_PAGINAS + 1):
    url_pagina = BASE_URL.format(num_pagina)
    
    try:
        resp = requests.get(url_pagina, headers=HEADERS, timeout=15)
        
        if resp.status_code != 200:
            print(f"⚠️  Página {num_pagina}: código {resp.status_code}")
            errores += 1
            continue
        
        soup_pagina = BeautifulSoup(resp.text, "html.parser")
        libros_pagina = soup_pagina.find_all("article", class_="product_pod")
        
        for libro in libros_pagina:
            titulo     = libro.find("h3").find("a")["title"]
            precio_raw = libro.find("p", class_="price_color").text
            rating_raw = libro.find("p", class_="star-rating")["class"][1]
            stock_raw  = libro.find("p", class_="instock availability").text.strip()
            href       = libro.find("h3").find("a")["href"]
            
            # Obtener categoría de la ficha individual
            # (esto hace el scraping más lento — necesario para la categoría)
            url_ficha_i = FICHA_BASE + href
            try:
                resp_f = requests.get(url_ficha_i, headers=HEADERS, timeout=10)
                soup_f = BeautifulSoup(resp_f.text, "html.parser")
                bc = soup_f.select("ul.breadcrumb li a")
                categoria = bc[1].text.strip() if len(bc) > 1 else "Desconocida"
                time.sleep(0.5)   # pausa entre requests de fichas
            except Exception:
                categoria = "Desconocida"
            
            todos_los_libros.append({
                "titulo":     titulo,
                "precio_raw": precio_raw,
                "rating_raw": rating_raw,
                "stock_raw":  stock_raw,
                "categoria":  categoria,
                "pagina":     num_pagina,
            })
        
        print(f"✅ Página {num_pagina}/10: {len(libros_pagina)} libros extraídos")
        time.sleep(1)  # pausa entre páginas del listado
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en página {num_pagina}: {e}")
        errores += 1

print(f"\n{'='*50}")
print(f"Total libros extraídos: {len(todos_los_libros)}")
print(f"Errores: {errores}")

df_raw = pd.DataFrame(todos_los_libros)
print(f"Shape del dataset raw: {df_raw.shape}")
df_raw.head()
```

**PUNTO DE VERIFICACIÓN 2:** ¿Tienes 200 filas (o cerca de 200)? ¿Las columnas `precio_raw` y `rating_raw` tienen símbolos `£` y textos en inglés respectivamente? → Continúa.

---

### Celda 4: Diagnóstico de calidad del dataset raw

```python
# ============================================================
# CELDA 4: Diagnóstico completo — ¿qué tan sucio está el dato?
# ============================================================
print("="*55)
print("REPORTE DE CALIDAD — DATOS CRUDOS (Books to Scrape)")
print("="*55)

print(f"\n📊 Dimensiones: {df_raw.shape[0]} libros × {df_raw.shape[1]} columnas")

print("\n📋 Primeras filas:")
print(df_raw.head(3).to_string())

print("\n🔍 Tipos de dato:")
print(df_raw.dtypes)

print("\n❓ Valores nulos por columna:")
print(df_raw.isnull().sum())

print("\n📈 Valores únicos por columna:")
for col in df_raw.columns:
    print(f"   {col}: {df_raw[col].nunique()} valores únicos")

print("\n🏷️  Muestras de precio_raw (primeros 10):")
print(df_raw["precio_raw"].head(10).tolist())

print("\n⭐ Valores únicos de rating_raw:")
print(df_raw["rating_raw"].value_counts())

print("\n📦 Valores únicos de stock_raw:")
print(df_raw["stock_raw"].value_counts())
```

---

### Celda 5: Pipeline de limpieza y normalización — COMPLETA LOS ___

```python
# ============================================================
# CELDA 5: Pipeline de limpieza — COMPLETA LOS ___
# ============================================================

df_limpio = df_raw.copy()   # NUNCA modificar el original

# --- LIMPIEZA 1: Precio ---
# precio_raw: "£51.77" → precio_gbp: 51.77 (float)
df_limpio["precio_gbp"] = (
    df_limpio["precio_raw"]
    .str.replace("___", "", regex=False)  # ← COMPLETA: símbolo a remover (£)
    .astype(___)                           # ← COMPLETA: tipo de dato (float)
)

# Verificar que la limpieza funcionó
print("Precios limpios (primeros 5):", df_limpio["precio_gbp"].head().tolist())
print(f"Tipo de dato: {df_limpio['precio_gbp'].dtype}")

# --- LIMPIEZA 2: Rating ---
# rating_raw: "Three" → rating_num: 3 (int)
mapeo_rating = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}
df_limpio["rating_num"] = df_limpio["___"].map(mapeo_rating)  # ← COMPLETA: columna origen

# Verificar
print("\nRating limpio:")
print(df_limpio["rating_num"].value_counts().sort_index())
invalidos_rating = df_limpio["rating_num"].isna().sum()
print(f"Ratings no mapeados (NaN): {invalidos_rating}")

# --- LIMPIEZA 3: Stock ---
# stock_raw: "In stock" o "In stock (2 available)" → en_stock: True/False
df_limpio["en_stock"] = df_limpio["stock_raw"].str.contains(
    "___",                # ← COMPLETA: texto que indica que hay stock
    case=False,           # no sensible a mayúsculas/minúsculas
    na=False
)

print(f"\nLibros en stock: {df_limpio['en_stock'].sum()}")
print(f"Libros sin stock: {(~df_limpio['en_stock']).sum()}")

# --- LIMPIEZA 4: Normalizar categoría ---
df_limpio["categoria_limpia"] = (
    df_limpio["categoria"]
    .str.strip()          # eliminar espacios
    .str.title()          # Capitalizar Cada Palabra
)

# Verificar
print(f"\nCategorías únicas: {df_limpio['categoria_limpia'].nunique()}")
print(df_limpio["categoria_limpia"].value_counts().head(10))

# --- LIMPIEZA 5: Eliminar duplicados por título ---
antes = len(df_limpio)
df_limpio = df_limpio.drop_duplicates(subset=["titulo"], keep="first")
print(f"\nDuplicados eliminados: {antes - len(df_limpio)}")
print(f"Dataset limpio final: {df_limpio.shape[0]} libros")
```

*Pistas para los `___`:*
- `str.replace("___", ...)` → `"£"` (símbolo de libra esterlina)
- `.astype(___)` → `float`
- `df_limpio["___"].map(mapeo_rating)` → `"rating_raw"`
- `str.contains("___", ...)` → `"in stock"` (o `"stock"`)

**PUNTO DE VERIFICACIÓN 3:** ¿`precio_gbp` es de tipo `float64`? ¿`rating_num` tiene valores 1-5? ¿`en_stock` es boolean? → Pipeline de limpieza correcto.

---

### Celda 6: Análisis y visualización del dataset limpio

```python
# ============================================================
# CELDA 6: Análisis de precios y valoraciones por categoría
# ============================================================
print("="*55)
print("ANÁLISIS DEL CATÁLOGO — BOOKS TO SCRAPE")
print("="*55)

# Estadísticas generales
print("\n📊 ESTADÍSTICAS GENERALES:")
print(df_limpio[["precio_gbp", "rating_num"]].describe().round(2))

# Top 5 categorías más caras
print("\n💰 TOP 5 CATEGORÍAS POR PRECIO PROMEDIO:")
cat_precios = (df_limpio.groupby("categoria_limpia")["precio_gbp"]
               .agg(["mean", "count", "min", "max"])
               .round(2)
               .rename(columns={"mean": "precio_prom", "count": "num_libros",
                                "min": "precio_min", "max": "precio_max"})
               .sort_values("precio_prom", ascending=False))
print(cat_precios.head(5))

# Categorías con mejor rating
print("\n⭐ TOP 5 CATEGORÍAS POR RATING PROMEDIO:")
cat_rating = (df_limpio.groupby("categoria_limpia")["rating_num"]
              .agg(["mean", "count"])
              .round(2)
              .rename(columns={"mean": "rating_prom", "count": "num_libros"})
              .sort_values("rating_prom", ascending=False))
print(cat_rating.head(5))

# Visualizaciones
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Análisis del Catálogo Books to Scrape — Web Scraping Lab",
             fontsize=13, fontweight='bold')

# Distribución de precios
df_limpio["precio_gbp"].hist(bins=20, ax=axes[0,0], color="steelblue", edgecolor="white")
axes[0,0].set_title("Distribución de Precios")
axes[0,0].set_xlabel("Precio (£)")
axes[0,0].set_ylabel("Número de libros")
axes[0,0].axvline(df_limpio["precio_gbp"].median(), color='red',
                   linestyle='--', label=f'Mediana: £{df_limpio["precio_gbp"].median():.2f}')
axes[0,0].legend()

# Distribución de ratings
df_limpio["rating_num"].value_counts().sort_index().plot(
    kind="bar", ax=axes[0,1], color="coral", edgecolor="white")
axes[0,1].set_title("Distribución de Ratings")
axes[0,1].set_xlabel("Rating (1-5 estrellas)")
axes[0,1].set_ylabel("Número de libros")
axes[0,1].tick_params(axis='x', rotation=0)

# Precio promedio por top 10 categorías
top10_cat = cat_precios.head(10)
top10_cat["precio_prom"].sort_values().plot(
    kind="barh", ax=axes[1,0], color="steelblue")
axes[1,0].set_title("Precio Promedio (£) — Top 10 Categorías")
axes[1,0].set_xlabel("Precio promedio (£)")

# Relación precio vs rating
axes[1,1].scatter(df_limpio["rating_num"],
                   df_limpio["precio_gbp"],
                   alpha=0.4, color="steelblue", s=30)
axes[1,1].set_xlabel("Rating (estrellas)")
axes[1,1].set_ylabel("Precio (£)")
axes[1,1].set_title("¿Los libros más caros son mejor valorados?")
axes[1,1].set_xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("books_analisis.png", dpi=150, bbox_inches='tight')
plt.show()
print("✅ Gráfico guardado como books_analisis.png")
```

**Reflexión 2:** Observa el gráfico de precio vs rating. ¿Existe correlación entre precio y rating? ¿Qué dice eso sobre el valor percibido de los libros en este catálogo?

```python
# Reflexión 2:
"""
Correlación precio vs rating:
_______________________________________________
¿Qué significa eso para un comprador que asume que más caro = mejor?
_______________________________________________
"""
```

---

## PARTE 3 — DESAFÍO: Pipeline completo de reporte (30 min)

### Celda 7: Reporte de calidad automatizado

```python
# ============================================================
# CELDA 7: DESAFÍO — Generar un reporte de calidad profesional
# 
# Completa la función `reporte_calidad()` que evalúa
# cualquier DataFrame y genera métricas de calidad
# ============================================================

def reporte_calidad(df, nombre_dataset="Dataset"):
    """
    Genera un reporte de calidad de datos profesional.
    
    Parámetros:
    - df: DataFrame a evaluar
    - nombre_dataset: nombre descriptivo del dataset
    
    Devuelve:
    - dict con las métricas de calidad calculadas
    """
    print(f"\n{'='*55}")
    print(f"REPORTE DE CALIDAD: {nombre_dataset}")
    print(f"{'='*55}")
    
    metricas = {}
    
    # 1. Dimensiones básicas
    metricas["total_filas"] = len(df)
    metricas["total_columnas"] = len(df.columns)
    print(f"\n📐 Dimensiones: {metricas['total_filas']:,} filas × {metricas['total_columnas']} columnas")
    
    # 2. Análisis de nulos
    nulos_por_col = df.isnull().sum()
    pct_nulos_por_col = (nulos_por_col / len(df) * 100).round(2)
    metricas["columnas_con_nulos"] = (nulos_por_col > 0).sum()
    metricas["pct_celdas_nulas"] = round(df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100, 2)
    
    print(f"\n❓ Completitud:")
    print(f"   Columnas con nulos: {metricas['columnas_con_nulos']}")
    print(f"   % de celdas nulas en el dataset: {metricas['pct_celdas_nulas']}%")
    if metricas["columnas_con_nulos"] > 0:
        print("   Detalle por columna:")
        for col in nulos_por_col[nulos_por_col > 0].index:
            print(f"   - {col}: {nulos_por_col[col]} nulos ({pct_nulos_por_col[col]}%)")
    
    # 3. Duplicados
    metricas["duplicados_exactos"] = df.duplicated().sum()
    print(f"\n🔁 Duplicados exactos: {metricas['duplicados_exactos']}")
    
    # 4. Columnas numéricas: outliers con IQR
    cols_num = df.select_dtypes(include=[np.number]).columns.tolist()
    metricas["outliers"] = {}
    print(f"\n📊 Outliers (método IQR) en columnas numéricas:")
    for col in cols_num:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR
        n_outliers = ((df[col] < lim_inf) | (df[col] > lim_sup)).sum()
        metricas["outliers"][col] = n_outliers
        flag = "⚠️" if n_outliers > 0 else "✅"
        print(f"   {flag} {col}: {n_outliers} outliers (rango válido: {lim_inf:.2f} - {lim_sup:.2f})")
    
    # 5. Índice de calidad global (0-100)
    puntos = 100
    puntos -= metricas["pct_celdas_nulas"] * 2       # -2 pts por cada 1% de nulos
    puntos -= min(metricas["duplicados_exactos"] / metricas["total_filas"] * 100, 20)  # máx -20 pts
    total_outliers = sum(metricas["outliers"].values())
    puntos -= min(total_outliers / metricas["total_filas"] * 100, 20)  # máx -20 pts
    puntos = max(0, round(puntos, 1))
    metricas["indice_calidad"] = puntos
    
    print(f"\n{'='*55}")
    estado = "EXCELENTE ✅" if puntos >= 90 else ("ACEPTABLE ✅" if puntos >= 70 else "REQUIERE ATENCIÓN ⚠️")
    print(f"🏆 ÍNDICE DE CALIDAD GLOBAL: {puntos}/100 — {estado}")
    print(f"{'='*55}")
    
    return metricas

# Aplicar el reporte al dataset CRUDO y al dataset LIMPIO
print("EVALUANDO DATASET CRUDO:")
metricas_raw   = reporte_calidad(df_raw, "Books to Scrape — RAW")

print("\n\nEVALUANDO DATASET LIMPIO:")
metricas_limp  = reporte_calidad(df_limpio[["titulo", "precio_gbp",
                                             "rating_num", "en_stock",
                                             "categoria_limpia", "pagina"]],
                                  "Books to Scrape — LIMPIO")

print(f"\n📈 MEJORA DE CALIDAD:")
print(f"   Raw:   {metricas_raw['indice_calidad']}/100")
print(f"   Limpio: {metricas_limp['indice_calidad']}/100")
print(f"   Mejora: +{metricas_limp['indice_calidad'] - metricas_raw['indice_calidad']:.1f} puntos")
```

### Celda 8: Reflexión final

```python
# ============================================================
# CELDA 8: REFLEXIÓN FINAL — responde en los comentarios
# ============================================================
reflexion_final = """
1. En este laboratorio scrapeaste 200 libros y los limpiaste.
   ¿Cuál fue el paso más difícil del pipeline y por qué?
   (No digas "el más difícil fue el código" — explica qué 
   problema de datos encontraste que no esperabas)
   
   Respuesta: _______________________________________________

2. El Índice de Calidad del dataset crudo vs el limpio mejoró
   en X puntos. ¿Qué cambio específico contribuyó más a 
   esa mejora? ¿Fue la limpieza del precio, del rating, 
   los duplicados, o algo más?
   
   Respuesta: _______________________________________________

3. Si en lugar de 200 libros necesitaras scrapear los 1,000 
   libros completos (50 páginas), ¿qué cambiarías en el 
   código de la Celda 3? ¿Qué nuevo problema podría aparecer
   con 50 páginas que no ocurrió con 10?
   
   Respuesta: _______________________________________________

4. Conecta este laboratorio con tu proyecto grupal:
   ¿Hay alguna fuente pública web que podrías scrapear para
   enriquecer el dataset de tu proyecto? (Menciona la URL 
   o el tipo de sitio y qué datos obtendría)
   
   Respuesta: _______________________________________________
"""
print(reflexion_final)
```

---

## ENTREGABLES

Sube al repositorio `semana_07/Soluciones/TuNombre_TuCodigo/` los siguientes archivos:

| # | Archivo | Descripción |
|---|---------|-------------|
| 1 | `books_scraping.ipynb` | Notebook completo con todas las celdas ejecutadas y reflexiones respondidas |
| 2 | `books_raw.csv` | Dataset crudo tal como fue extraído (`df_raw.to_csv("books_raw.csv", index=False)`) |
| 3 | `books_limpio.csv` | Dataset limpio y normalizado |
| 4 | `books_analisis.png` | Gráfico de análisis de la Celda 6 |
| 5 | `README.md` | 5 líneas: cuántos libros extraíste, cuántas categorías, mejora del índice de calidad raw→limpio, hallazgo más interesante del análisis |

**Formato del PR:**
- Título: `S7 Books Scraping — TuNombre (TuCódigo)`
- Branch: `semana07-scraping-TuNombre`

---

## RÚBRICA DE EVALUACIÓN

| Criterio | Excelente (100%) | Suficiente (60%) | Insuficiente (0%) | Pts |
|----------|-----------------|-----------------|-------------------|-----|
| **Celda 1-2: Scraping básico** | 20 libros extraídos correctamente, verificación robots.txt visible | Extrae libros pero sin verificar robots.txt | Error que impide continuar | 15 |
| **Celda 3: 10 páginas** | 180-200 libros con categoría | 100-179 libros o sin categoría | < 100 libros o no ejecutó | 25 |
| **Celda 5: Limpieza** | Los 3 `___` correctos, tipos de dato verificados, 0 duplicados | 2/3 transformaciones correctas | Sin completar o error en tipos | 25 |
| **Celda 6: Visualizaciones** | 4 gráficos con datos reales + PNG guardado | 2-3 gráficos | Sin visualizaciones | 15 |
| **Celda 7: Reporte de calidad** | Función ejecuta correctamente en raw Y limpio, mejora visible | Ejecuta en uno de los dos | Sin ejecutar | 10 |
| **Reflexiones (4)** | Respuestas técnicas específicas con ejemplos del lab | Respuestas genéricas de 1 línea | Sin respuestas | 10 |

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 7 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay | github.com/RubenCarty/bigdata-ua-2026-1*
