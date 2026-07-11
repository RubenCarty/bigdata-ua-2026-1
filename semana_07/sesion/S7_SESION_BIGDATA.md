# S7 — SESIÓN DE CLASE COMPLETA: Scraping, Limpieza y Normalización de Datos
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 7: Del Web al Dataset Limpio — Extracción, Depuración y Normalización

---

| Campo | Detalle |
|-------|---------|
| **Curso** | Big Data DD283 |
| **Semana** | 7 de 8 |
| **Tema** | Técnicas de Scraping, Limpieza y Normalización de Datos |
| **Logro** | El estudiante obtiene información estructurada de sitios web y realiza limpieza de datos corruptos e imprecisos con integridad |
| **Duración** | 3 horas (180 min + 20 min receso) |
| **Herramientas** | Google Colab · requests · BeautifulSoup4 · pandas |
| **Valor** | Integridad al normalizar datos sin alterar su esencia original |

---

## TABLA DE CONTENIDOS

1. [Cronograma](#cronograma)
2. [INICIO — Diagnóstico y contexto](#inicio)
3. [UTILIDAD — El dato sucio cuesta millones](#utilidad)
4. [TRANSFORMACIÓN — De HTML a datos limpios](#transformacion)
5. [PRÁCTICA — Caso INDECOPI](#practica)
6. [CIERRE](#cierre)
7. [Guion verbal](#guion)
8. [Casos reales](#casos)
9. [Referencias APA 7](#referencias)

---

## CRONOGRAMA {#cronograma}

| Bloque | Actividad | Duración | Responsable |
|--------|-----------|----------|-------------|
| **INICIO** | Rompe-hielo + Logro + Revisión S6 + Diagnóstico | 20 min | Docente |
| **UTILIDAD** | Por qué limpiar datos importa más que modelarlos | 10 min | Docente |
| **TRANSFORMACIÓN 1** | HTTP, HTML y cómo funciona un scraper | 20 min | Docente + Grupo |
| **TRANSFORMACIÓN 2** | BeautifulSoup: navegar, buscar, extraer | 20 min | Docente + Grupo |
| **TRANSFORMACIÓN 3** | robots.txt, ética y legalidad del scraping | 10 min | Docente |
| ☕ **RECESO** | | 20 min | — |
| **TRANSFORMACIÓN 4** | Tipos de datos sucios + diagnóstico con pandas | 20 min | Docente + Grupo |
| **TRANSFORMACIÓN 5** | Técnicas de limpieza: nulls, duplicados, formatos | 25 min | Docente + Grupo |
| **TRANSFORMACIÓN 6** | Normalización: fechas, teléfonos, texto, categorías | 15 min | Docente + Grupo |
| **PRÁCTICA GRUPAL** | Caso INDECOPI — precios de canasta básica | 25 min | Grupos |
| **EJERCICIO INDIVIDUAL** | Identificar y corregir datos sucios en un dataset | 15 min | Individual |
| **CIERRE** | Síntesis + Metacognición + Tarea | 10 min | Docente |
| **TOTAL** | | **200 min** | |

---

## 1. INICIO (20 min) {#inicio}

### a) ROMPE-HIELO: "El precio del dato sucio" (5 min)

**Instrucción verbal exacta:**

> *"Voy a darles un dato real y quiero que me digan cuánto creen que costó el error."*
>
> *"En 1999, la NASA perdió la sonda Mars Climate Orbiter — una inversión de 327 millones de dólares. El sistema de propulsión de la nave transmitía datos en unidades del sistema imperial (libras-fuerza). El software de navegación los interpretaba como unidades métricas (newtons). Un solo dato con formato incorrecto. La nave entró a la atmósfera de Marte en el ángulo equivocado y se destruyó."*
>
> *"Pregunta para grupos de 3: si en 1999 una discrepancia de unidades costó 327 millones de dólares, ¿cuánto creen que le cuesta a una empresa mediana de Lima tener su base de datos de clientes con RUC duplicados, teléfonos en formato incorrecto y fechas en 3 formatos distintos? ¿Problema técnico o problema de negocio?"*
>
> *(Escuchar 3-4 respuestas)*
>
> *"Hoy vamos a aprender exactamente cómo extraer datos de la web y cómo limpiarlos antes de que ese dato sucio llegue a un modelo de ML, a un reporte gerencial o a una decisión de negocio."*

---

### b) LOGRO DE APRENDIZAJE (3 min)

**Guion verbal textual:**

> *"Al terminar hoy van a poder hacer tres cosas concretas:"*
>
> *"Uno: usar Python con requests y BeautifulSoup para extraer información estructurada de una página web, respetando las reglas éticas y legales del scraping."*
>
> *"Dos: diagnosticar un dataset con datos sucios — identificar nulos, duplicados, formatos inconsistentes, outliers y errores de encoding — y cuantificar qué porcentaje del dato es confiable antes de limpiar."*
>
> *"Tres: limpiar y normalizar ese dataset usando pandas, asegurando que la calidad mejore sin alterar la información original. El principio clave de hoy es: normalizar no es inventar datos, es estandarizar la forma en que se representan."*

---

### c) REVISIÓN SESIÓN ANTERIOR (7 min)

**Pregunta 1:** *"La semana pasada vieron ML. ¿Cuál es la diferencia entre Precision y Recall? ¿Cuándo importa más Recall que Precision?"*

> **Respuesta esperada:** Precision: de los que el modelo predijo como positivos, ¿cuántos realmente lo son? (TP / (TP+FP)). Recall: de todos los positivos reales, ¿cuántos detectó el modelo? (TP / (TP+FN)). Recall importa más cuando el costo del Falso Negativo es muy alto: diagnóstico de cáncer (no detectar un tumor), detección de fraude (no detectar la transacción fraudulenta), alerta de abandono escolar (no detectar al alumno en riesgo antes de que abandone).
>
> **Si responde mal:** *"Imagina que eres el modelo de salud. Predict = qué tan confiables son tus alarmas. Recall = qué tan pocas alarmas te pierdes. ¿Para qué caso el costo de no detectar es mayor que el costo de falsa alarma?"*

**Pregunta 2:** *"¿Qué tipo de sesgo encontraron en el modelo de churn de Movistar del laboratorio? ¿Qué región tenía el F1 más bajo?"*

> **Respuesta esperada:** Sesgo geográfico (sesgo de selección + sesgo histórico). El modelo tenía mejor F1 para Lima (más datos de entrenamiento, 45% del dataset) y peor F1 para regiones como Iquitos o Tacna (menos representación en el dataset histórico). El dataset fue generado intencionalmente con ese sesgo para que el análisis de equidad de la Celda 6 lo detectara. Consecuencia: un cliente de Iquitos puede ser incorrectamente clasificado como "churn" o "no churn" porque el modelo no aprendió bien sus patrones de comportamiento.

**Pregunta 3:** *"¿Por qué se usa `scaler.fit_transform(X_train)` pero solo `scaler.transform(X_test)` — sin el `fit` en el test? ¿Qué problema ocurriría si también hacemos `fit` en el test?"*

> **Respuesta esperada:** El `fit` calcula la media y la desviación estándar de los datos para normalizar. Si se hace `fit` en el test set, el escalador "aprende" estadísticas de los datos de prueba → el modelo tiene información implícita sobre cómo son los datos de prueba antes de predecir → data leakage (fuga de datos). Las métricas de evaluación serían artificialmente buenas porque el modelo indirectamente ya "vio" los datos de prueba. El `transform` solo aplica la misma escala que aprendió del entrenamiento sin ver las estadísticas del test.

---

### d) DIAGNÓSTICO INICIAL (5 min)

**Pregunta 1:** *"¿Alguien ha 'bajado información de internet' de forma automática? ¿Cómo lo hicieron?"*

> **Respuesta esperada (nivel entrada):** Descargar archivos CSV/Excel de páginas web manualmente es la forma más básica. El scraping automatizado usa código para leer el HTML de la página y extraer datos estructurados sin hacer clic manualmente. Algunos pueden mencionar que usaron Ctrl+C de una tabla de una web — eso también es un tipo de extracción manual.

**Pregunta 2:** *"Si abren una página de LinkedIn o de Mercado Libre y hacen 'Ver código fuente' (Ctrl+U), ¿qué ven? ¿Cómo está organizado?"*

> **Respuesta esperada:** Ven HTML — un lenguaje de marcado con etiquetas como `<div>`, `<p>`, `<table>`, `<a href="...">`. Los datos (precios, nombres, descripciones) están dentro de esas etiquetas. El scraping es el proceso de leer ese HTML programáticamente y extraer los datos que nos interesan de dentro de las etiquetas correctas.

**Pregunta 3:** *"¿Han tenido alguna vez un Excel donde los datos venían de distintas personas y el formato era un desastre? ¿Qué tipo de inconsistencias aparecen normalmente?"*

> **Respuesta esperada:** Fechas en formatos distintos (01/05/2024 vs 2024-05-01 vs "1 de mayo"), nombres con mayúsculas/minúsculas inconsistentes (JUAN vs Juan vs juan), teléfonos con y sin código de país (+51 vs 51 vs vacío), montos con y sin puntos de miles (1.500,00 vs 1500 vs S/. 1,500), celdas vacías donde debería haber un valor, duplicados con pequeñas variaciones. Estos son exactamente los problemas que veremos hoy.

---

## 2. UTILIDAD (10 min) {#utilidad}

### Por qué limpiar datos es más importante que elegir el algoritmo

**El dato más citado en Data Science:**

> "Los Data Scientists gastan entre el 60% y el 80% de su tiempo en tareas de preparación de datos (limpieza, normalización, integración), y solo el 20-40% en modelado y análisis." — CrowdFlower Data Science Report, 2017 (actualizado: sigue siendo válido en 2025)

**Casos reales de impacto:**

| Empresa/Organismo | Problema de datos sucios | Impacto |
|-------------------|--------------------------|---------|
| NHS (Reino Unido, 2016) | 500,000 registros de pacientes con fechas de nacimiento erróneas | Pacientes recibieron tratamientos equivocados por edad incorrecta |
| Target (EE.UU., 2012) | Datos limpios y bien usados → predijo embarazos de clientas | Polémica de privacidad: reveló embarazo a adolescente a su padre |
| RENIEC Perú | DNIs duplicados en padrones de votación | Ciudadanos que no podían votar por duplicados en el sistema |
| SUNAT Perú | Empresas con mismo RUC y datos contradictorios | Fiscalizaciones incorrectas, devoluciones de impuestos a empresas equivocadas |
| SBS Perú | Centrales de riesgo con deudas asignadas a personas equivocadas | Ciudadanos con historial crediticio negativo por errores de normalización de nombres |

**El scraping como fuente de datos:**

El 73% de los datos que alimentan modelos de ML en empresas de e-commerce, finanzas y retail peruano provienen de alguna forma de extracción web (scraping de competidores, monitoreo de precios, extracción de datos públicos del gobierno). Las fuentes incluyen: SEACE (contrataciones públicas), datos.gob.pe, SUNAT RUC público, registros de Sunarp, precios de Mercado Libre.

**Pregunta retadora:**

*"Un Data Scientist recibe un dataset de 100,000 registros de clientes de Ripley. Sin limpiar: 15% de nulos en el campo ingreso, 8% de duplicados, fechas en 4 formatos distintos. ¿Debería limpiar primero o entrenar el modelo directamente y ver si la accuracy es suficiente?"*

> **Respuesta esperada (tensión cognitiva):** Nunca entrenar con datos sucios sin diagnosticar. El 15% de nulos en ingreso podría no ser aleatorio — puede que los clientes con ingresos muy altos o muy bajos sean quienes no declararon. Si se imputa la media, se introduce sesgo sistemático. El 8% de duplicados puede inflar artificialmente la representación de ciertos patrones. Las fechas en 4 formatos generarán errores o mezclas incorrectas de períodos. Un modelo entrenado con datos sucios puede tener accuracy aparentemente buena pero estará aprendiendo ruido. La limpieza es parte del pipeline, no opcional.

---

## 3. TRANSFORMACIÓN (70 min) {#transformacion}

### SUBTEMA 3.1 — Cómo funciona el scraping: HTTP y HTML (20 min)

**Explicación conceptual:**

```
EL CICLO REQUEST-RESPONSE
════════════════════════════════════════════════════════

Tu script Python          Internet             Servidor Web
      │                                              │
      │  GET /precios HTTP/1.1                       │
      │──────────────────────────────────────────────▶│
      │                                              │
      │                             HTML + CSS + JS  │
      │◀──────────────────────────────────────────── │
      │                                              │
      │  BeautifulSoup parsea el HTML                │
      │  y extrae los datos que necesitas            │
      │                                              │

Status codes importantes:
200 OK         → Página devuelta correctamente
404 Not Found  → La URL no existe
403 Forbidden  → El servidor rechaza tu request (anti-scraping)
429 Too Many   → Demasiadas solicitudes (rate limit)
     Requests
503 Service    → Servidor sobrecargado
     Unavailable
```

**Estructura del HTML — lo que parsea BeautifulSoup:**

```html
<!-- Ejemplo: ficha de producto en una tienda online peruana -->
<div class="producto" data-id="SKU-2847">
    <h2 class="nombre-producto">Laptop HP 15-ef2127wm</h2>
    <span class="precio" itemprop="price">S/ 1,899.00</span>
    <span class="precio-anterior">S/ 2,299.00</span>
    <div class="rating">
        <i class="fa-star">★★★★</i>
        <span class="num-reviews">(128 reseñas)</span>
    </div>
    <a href="/producto/laptop-hp" class="btn-comprar">Comprar</a>
</div>
```

**Código de scraping básico con requests + BeautifulSoup:**

```python
# ============================================================
# DEMO: Scraping básico en Google Colab
# Sitio de práctica oficial: books.toscrape.com
# (Diseñado explícitamente para practicar scraping)
# ============================================================
!pip install requests beautifulsoup4 -q

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# PASO 1: Hacer el request HTTP
url = "https://books.toscrape.com/catalogue/page-1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (educational-scraper/1.0)",
    # Identificarse como scraper educativo es buena práctica
}

response = requests.get(url, headers=headers, timeout=10)
print(f"Status code: {response.status_code}")  # 200 = OK
print(f"Encoding: {response.encoding}")         # utf-8 o similar
print(f"Tamaño del HTML: {len(response.text):,} caracteres")

# PASO 2: Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# PASO 3: Encontrar todos los libros en la página
libros = soup.find_all("article", class_="product_pod")
print(f"\nLibros en esta página: {len(libros)}")

# PASO 4: Extraer datos de cada libro
datos = []
for libro in libros:
    titulo  = libro.find("h3").find("a")["title"]     # atributo title
    precio  = libro.find("p", class_="price_color").text  # texto del párrafo
    rating  = libro.find("p", class_="star-rating")["class"][1]  # 2do class
    disponible = libro.find("p", class_="instock availability").text.strip()
    
    datos.append({
        "titulo":     titulo,
        "precio":     precio,
        "rating":     rating,
        "disponible": disponible
    })

df = pd.DataFrame(datos)
print(f"\n=== LIBROS EXTRAÍDOS ===")
print(df)
```

**Output esperado:**
```
Status code: 200
Encoding: utf-8
Tamaño del HTML: 50,362 caracteres

Libros en esta página: 20

=== LIBROS EXTRAÍDOS ===
                    titulo   precio   rating disponible
0     A Light in the Attic  £51.77     Three  In stock
1       Tipping the Velvet  £53.74      One  In stock
...
```

**Pregunta al grupo 1:**

*"El campo `precio` tiene el símbolo `£` y el campo `rating` dice 'Three' en inglés en lugar de un número. ¿Este dataset está listo para análisis? ¿Qué hay que hacer primero?"*

> **Respuesta esperada:** No está listo. Hay que limpiarlo:
> - `precio`: remover el `£` y convertir el string `"£51.77"` al float `51.77`
> - `rating`: convertir "One", "Two", "Three", "Four", "Five" a números 1, 2, 3, 4, 5 — es un campo categórico ordinal que debe ser numérico para análisis y modelos
> Esta es exactamente la fase de limpieza que sigue al scraping. El scraping extrae datos brutos; la limpieza los hace utilizables.

**Mini actividad:** *(3 min)* "¿Qué etiqueta HTML usarían para encontrar los precios si en lugar de `class_='price_color'` el desarrollador hubiera usado `id='precio-principal'`? ¿Cuál sería el método BeautifulSoup correcto?"

> **Respuesta:** `soup.find(id="precio-principal")` o `soup.select("#precio-principal")` (CSS selector con `#` para IDs, `.` para clases).

---

### SUBTEMA 3.2 — BeautifulSoup: navegar, buscar, extraer (20 min)

**Los 4 métodos más importantes:**

```python
# ============================================================
# MÉTODOS PRINCIPALES DE BEAUTIFULSOUP
# ============================================================

# 1. find() → primer elemento que coincide
titulo = soup.find("h1")                    # Primera etiqueta <h1>
titulo = soup.find("div", class_="header")  # Primera <div> con esa clase
titulo = soup.find("a", href=True)          # Primera <a> que tenga href

# 2. find_all() → lista de todos los elementos que coinciden
todos_links    = soup.find_all("a")
todos_precios  = soup.find_all("span", class_="precio")
# Limitar resultados:
primeros_5     = soup.find_all("li", limit=5)

# 3. select() → CSS selectors (más potente, más flexible)
# .clase → por clase
precios   = soup.select(".price_color")
# #id → por ID
header    = soup.select("#main-header")
# etiqueta.clase → etiqueta específica con clase
items     = soup.select("article.product_pod")
# Jerarquía: padre > hijo
precios2  = soup.select("div.product-info > span.price")

# 4. Navegar por el árbol HTML
elemento = soup.find("div", class_="producto")
padre     = elemento.parent           # un nivel arriba
hermanos  = elemento.find_next_siblings()   # mismos nivel, después
hijo      = elemento.find("h2")       # primer hijo h2

# Extraer datos del elemento encontrado
texto      = elemento.text              # todo el texto interior
texto_limpio = elemento.get_text(strip=True)  # sin espacios extras
atributo   = elemento["href"]          # valor del atributo href
atributo2  = elemento.get("class", []) # sin error si no existe
```

**Scraping de múltiples páginas — paginación:**

```python
# ============================================================
# SCRAPING MULTI-PÁGINA: extraer las 5 primeras páginas
# de books.toscrape.com
# ============================================================
import time

todos_libros = []
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

for pagina in range(1, 6):           # páginas 1 a 5
    url = BASE_URL.format(pagina)
    
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code != 200:
        print(f"⚠️  Página {pagina}: error {response.status_code}")
        break
    
    soup = BeautifulSoup(response.text, "html.parser")
    libros = soup.find_all("article", class_="product_pod")
    
    for libro in libros:
        titulo = libro.find("h3").find("a")["title"]
        precio = libro.find("p", class_="price_color").text
        rating = libro.find("p", class_="star-rating")["class"][1]
        todos_libros.append({"titulo": titulo, "precio": precio,
                             "rating": rating, "pagina": pagina})
    
    print(f"✅ Página {pagina}: {len(libros)} libros extraídos")
    time.sleep(1)   # PAUSA ENTRE REQUESTS — buena práctica de respeto al servidor

df_libros = pd.DataFrame(todos_libros)
print(f"\nTotal extraído: {len(df_libros)} libros de 5 páginas")
df_libros.head()
```

**Pregunta al grupo 2:**

*"¿Por qué ponemos `time.sleep(1)` entre cada request? ¿Qué pasaría si hacemos 50 requests por segundo al mismo servidor?"*

> **Respuesta esperada:** `time.sleep(1)` agrega una pausa de 1 segundo entre cada solicitud al servidor. Sin la pausa, el script puede hacer decenas de requests por segundo, lo que puede: (1) sobrecargar el servidor de la víctima, interrumpiendo el servicio para usuarios reales — equivalente a un pequeño ataque DoS, (2) activar los sistemas anti-scraping del sitio que detectan patrones de acceso no humano y bloquean la IP, (3) en casos extremos, constituir una violación de los términos de servicio con consecuencias legales. La regla general: no hacer más de 1-2 requests por segundo en sitios de terceros.

---

### SUBTEMA 3.3 — Ética y legalidad del scraping (10 min)

**El archivo robots.txt — las reglas del juego:**

```
EJEMPLO: robots.txt de un portal peruano (hipotético)
══════════════════════════════════════════════════════

User-agent: *          ← aplica a todos los bots
Disallow: /admin/      ← NO se puede scrapear /admin/
Disallow: /usuario/    ← NO se puede scrapear perfiles privados
Disallow: /api/privada/← NO se puede scrapear la API privada
Allow: /catalogo/      ← SÍ se puede scrapear el catálogo
Allow: /precios-publicos/ ← SÍ se puede scrapear precios públicos

Crawl-delay: 10        ← esperar 10 segundos entre requests

Sitemap: https://ejemplo.com/sitemap.xml
```

**Cómo leer robots.txt con Python:**

```python
# Verificar robots.txt ANTES de scrapear cualquier sitio
import urllib.robotparser

def puede_scrapear(url_sitio, url_objetivo):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url_sitio + "/robots.txt")
    rp.read()
    return rp.can_fetch("*", url_objetivo)

# Verificar si podemos scrapear books.toscrape.com
sitio = "http://books.toscrape.com"
pagina = "http://books.toscrape.com/catalogue/page-1.html"
print(f"¿Podemos scrapear? {puede_scrapear(sitio, pagina)}")
# → True (books.toscrape.com permite el scraping — es un sitio de práctica)
```

**Tabla de semáforo: cuándo scrapear y cuándo no:**

| ✅ VERDE — Se puede | 🟡 AMARILLO — Revisar ToS | 🔴 ROJO — No se debe |
|-------------------|--------------------------|---------------------|
| Sitios oficiales del gobierno (datos.gob.pe, SUNAT RUC público) | Sitios de noticias (depende del ToS) | Datos protegidos por login privado |
| Sitios diseñados para scraping (books.toscrape.com, quotes.toscrape.com) | Precios de e-commerce (algunos lo prohíben) | Datos personales sensibles (DNI, salud, dirección) |
| APIs públicas con documentación | LinkedIn, redes sociales (suelen prohibirlo en ToS) | Sitios con robots.txt que lo prohíbe |
| Datos que el propio dueño ha publicado como abiertos | | Datos con copyright explícito |

**Pregunta al grupo 3:**

*"Un estudiante quiere scrapear todos los precios de Saga Falabella para un proyecto de comparación de precios. ¿Qué pasos previos debe hacer ANTES de escribir una sola línea de código?"*

> **Respuesta esperada:**
> 1. Leer el archivo robots.txt de Saga Falabella (`sagafalabella.com.pe/robots.txt`) — verificar si permite o prohíbe el scraping
> 2. Leer los Términos de Servicio del sitio — buscar la sección sobre extracción automatizada de datos
> 3. Verificar si Saga tiene una API pública oficial para acceder a los datos de precio de forma autorizada (muchas empresas las ofrecen para afiliados)
> 4. Si el robots.txt prohíbe el scraping pero los datos son necesarios para investigación académica: contactar a la empresa por email solicitando los datos directamente (muchas empresas los comparten para proyectos universitarios)
> 5. Si todo lo anterior está permitido: scrapear con rate limiting (mínimo 1 seg entre requests), identificarse con un User-Agent descriptivo

---

## RECESO (20 min) ☕

---

### SUBTEMA 3.4 — Tipos de datos sucios: el diagnóstico (20 min)

**Los 7 tipos de suciedad más comunes en datasets peruanos:**

```
TAXONOMÍA DE DATOS SUCIOS
══════════════════════════════════════════════════════════════

1. VALORES NULOS / FALTANTES
   - NaN, None, "", "N/A", "null", "sin dato", 0 donde no corresponde
   - Ejemplo: df["telefono"] = ["987654321", None, "N/A", "", "000000000"]

2. DUPLICADOS
   - Filas exactamente iguales (duplicados exactos)
   - Filas casi iguales (mismo cliente, nombre con/sin tilde)
   - Ejemplo: "Juan Garcia" vs "Juan García" vs "JUAN GARCIA"

3. INCONSISTENCIA DE FORMATOS
   - Fechas: "2024-01-15" vs "15/01/2024" vs "15 de enero 2024"
   - Teléfonos: "987654321" vs "+51987654321" vs "51 987 654 321"
   - Montos: "S/. 1,500.00" vs "1500" vs "1.500,00" (europeo)

4. ERRORES DE TIPO DE DATO
   - Número almacenado como string: "1500" (str) en lugar de 1500 (int)
   - Fecha almacenada como texto: "2024-01-15" (str) en lugar de datetime
   - Booleano como texto: "Si" / "No" / "True" / "1" / "X"

5. OUTLIERS
   - Valores fuera del rango esperado: edad = 200, precio = -50, DNI = 0
   - Pueden ser errores de entrada o eventos extremos reales

6. ERRORES DE ENCODING
   - "Señor" → "Se±or" (ISO-8859-1 leído como ASCII)
   - Caracteres especiales de otros idiomas en campos de texto
   - ñ, á, é, í, ó, ú que aparecen como caracteres extraños

7. DATOS ESTRUCTURALMENTE INCORRECTOS
   - RUC con 10 dígitos en lugar de 11
   - DNI con 7 en lugar de 8 dígitos
   - Email sin @ o sin dominio
   - Coordenadas GPS invertidas (lat/lon swapped)
```

**Código — diagnóstico completo de un dataset:**

```python
# ============================================================
# DIAGNÓSTICO PROFESIONAL DE CALIDAD DE DATOS
# ============================================================
import pandas as pd
import numpy as np

# Dataset sintético con problemas reales de datos peruanos
data_cruda = {
    "nombre":    ["CARLOS MENDOZA", "carlos mendoza", "María García",
                  "MARIA GARCIA", "Pedro López", None, "Ana Rios", "ANA RIOS"],
    "dni":       ["45678901", "45678901", "32145678", "87654321",
                  "9876543", "12345678", None, "12345678"],
    "telefono":  ["+51987654321", "987654321", "51 912 345 678",
                  "912345678", "000000000", "987111222", "N/A", "987111222"],
    "fecha_reg": ["2024-01-15", "15/01/2024", "2024/01/20",
                  "20 de enero 2024", "2024-01-25", "2024-01-30",
                  "2024-02-01", "2024-02-01"],
    "ingreso":   [2500, 2500, 3800, -500, 150000, 2200, 1800, 1800],
    "email":     ["carlos@gmail.com", "carlos@gmail.com",
                  "maria.garcia", "maria@empresa.pe",
                  "pedro@correo", "ana@outlook.com", None, None],
}
df_crudo = pd.DataFrame(data_cruda)

print("="*60)
print("REPORTE DE CALIDAD DE DATOS")
print("="*60)
print(f"\n1. DIMENSIONES: {df_crudo.shape[0]} filas × {df_crudo.shape[1]} columnas")

print("\n2. VALORES NULOS POR COLUMNA:")
nulos = df_crudo.isnull().sum()
pct_nulos = (nulos / len(df_crudo) * 100).round(1)
reporte_nulos = pd.DataFrame({"Nulos": nulos, "Porcentaje": pct_nulos})
print(reporte_nulos[reporte_nulos["Nulos"] > 0])

print("\n3. DUPLICADOS:")
print(f"   Filas exactamente duplicadas: {df_crudo.duplicated().sum()}")

print("\n4. TIPOS DE DATO:")
print(df_crudo.dtypes)

print("\n5. ESTADÍSTICAS BÁSICAS (columnas numéricas):")
print(df_crudo.describe())
```

**Output esperado:**
```
REPORTE DE CALIDAD DE DATOS
============================================================
1. DIMENSIONES: 8 filas × 6 columnas

2. VALORES NULOS POR COLUMNA:
         Nulos  Porcentaje
nombre       1        12.5
dni          1        12.5
telefono     0         0.0
email        2        25.0

3. DUPLICADOS:
   Filas exactamente duplicadas: 1

4. ESTADÍSTICAS BÁSICAS:
         ingreso
count    8.000000
mean  16537.500000   ← promedio distorsionado por outlier 150000
min    -500.000000   ← valor negativo imposible para ingreso
max  150000.000000   ← outlier probable
```

**Pregunta al grupo 4:**

*"El diagnóstico muestra que `ingreso` tiene un valor mínimo de -500 y un máximo de 150,000. El promedio es 16,537 pero la mayoría de valores están entre 1,800 y 3,800. ¿Qué harían con el -500 y con el 150,000? ¿Los eliminan o los corrigen?"*

> **Respuesta esperada:** Depende del contexto:
> - **-500**: claramente un error de digitación (el ingreso no puede ser negativo). Opciones: (a) eliminar la fila si no hay forma de conocer el valor real, (b) convertirlo a NaN y luego imputar la mediana del grupo similar, (c) contactar a la fuente para verificar. NO se debe cambiar a 500 asumiendo que faltó el signo positivo — eso sería inventar datos.
> - **150,000**: puede ser un outlier real (una persona con ingreso alto) o un error (debía ser 15,000). Sin contexto adicional, se mantiene y se documenta como outlier. Si el análisis es para scoring crediticio de clientes de ingreso medio, se puede excluir del modelo pero no borrar del dataset.
> - **Principio fundamental:** normalizar no es inventar. Si no se puede verificar el valor correcto, se marca como NaN, no se reemplaza con un valor asumido.

---

### SUBTEMA 3.5 — Técnicas de limpieza con pandas (25 min)

```python
# ============================================================
# LIMPIEZA COMPLETA PASO A PASO
# ============================================================

# PASO 1: Manejar duplicados
print("=== PASO 1: DUPLICADOS ===")
# Duplicados exactos
df_sin_dup = df_crudo.drop_duplicates()
print(f"Antes: {len(df_crudo)} | Después de drop_duplicates: {len(df_sin_dup)}")

# Duplicados por DNI (mismo DNI = misma persona aunque los demás campos difieran)
df_sin_dup = df_sin_dup.drop_duplicates(subset=["dni"], keep="first")
print(f"Después de deduplicar por DNI: {len(df_sin_dup)}")
```

```python
# PASO 2: Limpiar y normalizar NOMBRES
print("\n=== PASO 2: NORMALIZACIÓN DE NOMBRES ===")
df_sin_dup["nombre_limpio"] = (
    df_sin_dup["nombre"]
    .str.strip()                    # eliminar espacios al inicio y fin
    .str.title()                    # Capitalizar Cada Palabra (no ALL CAPS ni all lower)
    .str.replace(r"\s+", " ", regex=True)  # múltiples espacios → uno solo
)
print(df_sin_dup[["nombre", "nombre_limpio"]])
```

```python
# PASO 3: Limpiar TELÉFONOS
print("\n=== PASO 3: NORMALIZACIÓN DE TELÉFONOS ===")
import re

def normalizar_telefono(tel):
    if pd.isna(tel) or tel in ["N/A", "000000000", ""]:
        return None                 # marcar como nulo real
    # Remover todo excepto dígitos
    tel_limpio = re.sub(r"[^\d]", "", str(tel))
    # Remover código de país peruano (51) si tiene 11 dígitos
    if len(tel_limpio) == 11 and tel_limpio.startswith("51"):
        tel_limpio = tel_limpio[2:]
    # Validar: teléfono celular peruano tiene 9 dígitos y empieza con 9
    if len(tel_limpio) == 9 and tel_limpio.startswith("9"):
        return tel_limpio
    return None   # formato inválido → nulo

df_sin_dup["telefono_limpio"] = df_sin_dup["telefono"].apply(normalizar_telefono)
print(df_sin_dup[["telefono", "telefono_limpio"]])
```

```python
# PASO 4: Normalizar FECHAS
print("\n=== PASO 4: NORMALIZACIÓN DE FECHAS ===")

def normalizar_fecha(fecha_str):
    if pd.isna(fecha_str):
        return pd.NaT
    # Lista de formatos posibles (orden importa: más específico primero)
    formatos = [
        "%Y-%m-%d",       # 2024-01-15
        "%d/%m/%Y",       # 15/01/2024
        "%Y/%m/%d",       # 2024/01/20
        "%d de %B %Y",    # 20 de enero 2024 (requiere locale en español)
    ]
    for fmt in formatos:
        try:
            return pd.to_datetime(fecha_str, format=fmt)
        except (ValueError, TypeError):
            continue
    # Último recurso: pandas infiere el formato
    try:
        return pd.to_datetime(fecha_str, dayfirst=True)
    except:
        return pd.NaT  # si nada funciona → fecha inválida

df_sin_dup["fecha_limpia"] = df_sin_dup["fecha_reg"].apply(normalizar_fecha)
print(df_sin_dup[["fecha_reg", "fecha_limpia"]])
```

```python
# PASO 5: Validar y limpiar DNI
print("\n=== PASO 5: VALIDACIÓN DE DNI ===")
def validar_dni(dni):
    if pd.isna(dni):
        return None
    dni_str = str(dni).strip()
    # DNI peruano: exactamente 8 dígitos numéricos
    if re.match(r"^\d{8}$", dni_str):
        return dni_str
    return None  # formato inválido

df_sin_dup["dni_valido"] = df_sin_dup["dni"].apply(validar_dni)
invalidos = df_sin_dup["dni_valido"].isna().sum()
print(f"DNIs inválidos encontrados: {invalidos}")

# PASO 6: Manejar outliers en ingreso
print("\n=== PASO 6: TRATAMIENTO DE OUTLIERS ===")
Q1 = df_sin_dup["ingreso"].quantile(0.25)
Q3 = df_sin_dup["ingreso"].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
print(f"Rango válido por IQR: {limite_inferior:.0f} a {limite_superior:.0f}")
outliers = df_sin_dup[
    (df_sin_dup["ingreso"] < limite_inferior) |
    (df_sin_dup["ingreso"] > limite_superior)
]
print(f"Outliers detectados: {len(outliers)}")
print(outliers[["nombre", "ingreso"]])
# Los marcamos como NaN para análisis manual, no los eliminamos
df_sin_dup["ingreso_limpio"] = df_sin_dup["ingreso"].where(
    (df_sin_dup["ingreso"] >= 0) & (df_sin_dup["ingreso"] <= limite_superior)
)
```

**Pregunta al grupo 5:**

*"Para los valores nulos en `ingreso` después de marcar los outliers, se propone: opción A) imputar con la media del ingreso, opción B) imputar con la mediana. ¿Cuál es mejor para este dataset y por qué?"*

> **Respuesta esperada:** La **mediana** es más robusta. La media es muy sensible a outliers — incluso después de marcar 150,000 como outlier, si hay otros valores extremos, la media sigue siendo alta y no representa al cliente típico. La mediana (el valor del medio cuando se ordenan todos) no se afecta por los valores extremos. En distribuciones de ingreso que son asimétricas a la derecha (pocos ricos, muchos con ingreso moderado), la mediana es siempre más representativa que la media. Las organizaciones de estadística oficial (INEI, Banco Mundial) usan la mediana de ingreso, no la media, por esta razón.

---

### SUBTEMA 3.6 — Normalización: estándares de representación (15 min)

**Normalizar no es transformar — es estandarizar la forma:**

```python
# ============================================================
# NORMALIZACIÓN DE CATEGORÍAS Y TEXTO
# ============================================================

# Ejemplo: campo "distrito" con múltiples formas del mismo valor
distritos_sucios = pd.Series([
    "San Juan de Lurigancho", "SJL", "S.J.L.", "san juan de lurigancho",
    "Miraflores", "MIRAFLORES", "miraflores",
    "San Isidro", "San  Isidro", "san isidro"  # doble espacio
])

# Tabla de mapeo de variantes → nombre canónico
mapeo_distritos = {
    "sjl": "San Juan de Lurigancho",
    "s.j.l.": "San Juan de Lurigancho",
    "san juan de lurigancho": "San Juan de Lurigancho",
    "miraflores": "Miraflores",
    "san isidro": "San Isidro",
}

def normalizar_distrito(nombre):
    if pd.isna(nombre):
        return None
    # Estandarizar: minúsculas + sin espacios extras
    clave = " ".join(nombre.lower().split())
    return mapeo_distritos.get(clave, nombre.title())  # title() si no está en el mapeo

distritos_normalizados = distritos_sucios.apply(normalizar_distrito)
print(pd.DataFrame({"Original": distritos_sucios,
                    "Normalizado": distritos_normalizados}))
```

**Normalización de precios en diferentes formatos:**

```python
# ============================================================
# NORMALIZACIÓN DE PRECIOS (caso de scraping peruano)
# ============================================================
precios_sucios = pd.Series([
    "S/. 1,500.00",     # formato Banco de la Nación
    "S/ 1500",          # formato SUNAT
    "1.500,00",         # formato europeo
    "1500.50",          # número limpio
    "PEN 1,500",        # código ISO
    "S/1,500.00",       # sin espacio
    "mil quinientos",   # texto (error de entrada)
    None
])

def normalizar_precio(precio_str):
    if pd.isna(precio_str):
        return None
    precio_str = str(precio_str).strip()
    # Remover prefijos de moneda
    for prefijo in ["S/. ", "S/ ", "S/", "PEN ", "PEN"]:
        precio_str = precio_str.replace(prefijo, "")
    # Detectar formato europeo (punto como separador de miles, coma como decimal)
    if re.match(r"^\d{1,3}(\.\d{3})*(,\d{2})?$", precio_str):
        precio_str = precio_str.replace(".", "").replace(",", ".")
    else:
        # Formato americano/peruano: remover comas de miles
        precio_str = precio_str.replace(",", "")
    try:
        return float(precio_str)
    except ValueError:
        return None  # "mil quinientos" y similares → NaN

precios_normalizados = precios_sucios.apply(normalizar_precio)
print(pd.DataFrame({"Original": precios_sucios,
                    "Normalizado S/": precios_normalizados}))
```

**Pregunta al grupo 6:**

*"Al normalizar el campo `nombre` a `str.title()`, 'CARLOS MENDOZA' se convierte en 'Carlos Mendoza'. ¿Eso altera la esencia del dato? ¿Cuándo sería un problema cambiar la capitalización?"*

> **Respuesta esperada:** Para la mayoría de análisis no altera la esencia — Carlos Mendoza y CARLOS MENDOZA representan la misma persona. Pero hay casos donde sí importa: (1) datos de programas con abreviaciones en mayúsculas que tienen significado específico ('BC' como abreviatura de Banco Central vs 'Bc'), (2) nombres propios que el titular escribe en minúsculas intencionalmente (ej: nombre de marca como "iPhone" donde el 'i' minúsculo es parte de la identidad), (3) códigos alfanuméricos donde mayúscula y minúscula distinguen (identificadores de sistemas, códigos de producto). La regla: normalizar capitalización es seguro para nombres de personas y lugares; ser más cuidadoso con códigos y nombres de marcas.

**Pregunta al grupo 7:**

*"¿Cuál es la diferencia entre ELIMINAR una fila con datos inválidos y MARCAR esa fila como inválida (convertirla a NaN)? ¿Cuándo usarías cada enfoque?"*

> **Respuesta esperada:** Eliminar: la fila desaparece permanentemente del dataset. Útil cuando el dato inválido afecta al análisis y no es recuperable (ej: duplicado exacto con toda la información idéntica). Marcar como NaN (o flag): la fila permanece pero el campo queda marcado como desconocido. Útil cuando: (1) la fila tiene otros campos válidos valiosos, (2) el análisis puede funcionar con datos parciales, (3) quieres mantener trazabilidad de cuántos datos eran inválidos (para reportes de calidad). Principio general: preferir marcar sobre eliminar — la eliminación es irreversible y puede reducir el tamaño del dataset más de lo necesario. Siempre trabajar en un DataFrame nuevo, nunca destruir el original.

---

## 4. PRÁCTICA (40 min) {#practica}

### a) CASO PRÁCTICO GRUPAL: INDECOPI — Vigilancia de precios (25 min)

**Escenario:**

El INDECOPI (Instituto Nacional de Defensa de la Competencia y de la Protección de la Propiedad Intelectual) quiere implementar un sistema automatizado de monitoreo de precios de la canasta básica familiar en Lima. El objetivo: detectar empresas que publicitan un precio en su web pero cobran un precio diferente en tienda.

El equipo de IT ha extraído datos de 4 fuentes distintas durante el mes de enero 2024:

**Muestra del dataset combinado (datos sucios):**

| producto | tienda | precio_web | precio_tienda | fecha | distrito |
|---------|--------|-----------|--------------|-------|---------|
| Arroz Costeño 1kg | Wong | "S/. 3,80" | 3.80 | 2024-01-10 | Miraflores |
| arroz costeño 1kg | wong | "S/ 3.80" | 3.80 | 10/01/2024 | MIRAFLORES |
| Arroz Costeño 1kg | Metro | "3,80" | 4.20 | 2024-01-11 | San Isidro |
| Aceite Primor 1L | Tottus | "S/8.50" | 8.50 | 2024/01/12 | SJL |
| aceite primor 1l | Tottus | None | 8.90 | 2024-01-12 | San Juan de Lurigancho |
| Azúcar Cartavio 1kg | Plaza Vea | "S/. 2,90" | -2.90 | 2024-01-15 | san isidro |
| Leche Gloria 1L | Wong | "S/ 4,20" | 4.50 | "15 ene 2024" | Miraflores |

**Preguntas del caso (responder en grupo en 20 min):**

1. Identifica TODOS los problemas de calidad de datos en este dataset (menciona el tipo de problema y el campo afectado).

2. ¿Cuáles son los pasos de limpieza que aplicarías en orden? Escribe el pseudocódigo o la lógica (no necesitas código real).

3. Tras limpiar, ¿cómo identificarías automáticamente los productos donde `precio_tienda > precio_web`? ¿Qué consulta de pandas usarías?

4. El INDECOPI quiere saber el porcentaje de casos donde se cobra más de lo anunciado. Con el dataset limpio, ¿qué métrica calcularían y cómo la presentarían?

5. ¿Qué problema ético existe si publican directamente los datos scrapeados de las webs de los supermercados sin avisar a las empresas?

**Preguntas de andamiaje del docente:**

- *"¿Las dos filas de Arroz Costeño Wong son duplicados exactos? ¿O son registros distintos? ¿Cómo lo sabes?"*
- *"Si 'precio_web' es string y 'precio_tienda' es float, ¿pueden compararlos directamente?"*
- *"¿Qué harían con el precio_tienda = -2.90? ¿Eliminan la fila o marcan el campo?"*

**Respuesta modelo — puesta en común:**

**Problemas identificados:**
1. **Duplicados no exactos** (misma fila pero con capitalización diferente): Arroz Costeño 1kg / arroz costeño 1kg en Wong
2. **Formato inconsistente de precio_web**: "S/. 3,80", "S/ 3.80", "3,80", "S/8.50", "S/. 2,90" (6 formatos distintos para el mismo tipo de dato)
3. **Formato inconsistente de fechas**: 4 formatos diferentes
4. **Inconsistencia de distrito**: MIRAFLORES, Miraflores, SJL, San Juan de Lurigancho, san isidro
5. **Valor nulo en precio_web**: None en aceite Primor Tottus
6. **Outlier / error en precio_tienda**: -2.90 (precio negativo = imposible)

**Pasos de limpieza en orden:**
1. Normalizar texto (producto → lower + strip, distrito → mapeo canónico)
2. Eliminar duplicados (basados en producto + tienda + fecha, después de normalizar)
3. Normalizar precio_web (remover S/., S/, aplicar función de precio)
4. Normalizar fechas a `datetime`
5. Marcar precio_tienda negativo como NaN
6. Marcar precio_web nulo como NaN

**Query para detectar precio mayor en tienda:**
```python
df_limpio[df_limpio["precio_tienda"] > df_limpio["precio_web_num"]][
    ["producto", "tienda", "precio_web_num", "precio_tienda", "fecha"]
]
```

**Métrica para INDECOPI:**
```python
casos_con_precio_superior = (df_limpio["precio_tienda"] > df_limpio["precio_web_num"]).sum()
total_validos = df_limpio[["precio_tienda", "precio_web_num"]].notna().all(axis=1).sum()
porcentaje = casos_con_precio_superior / total_validos * 100
print(f"Casos con precio en tienda > web: {casos_con_precio_superior} ({porcentaje:.1f}%)")
```

**Problema ético:** Publicar datos de precios extraídos de webs privadas de supermercados sin notificación previa puede violar los Términos de Servicio, generar demandas legales por competencia desleal, o divulgar información que las empresas consideran confidencial. El INDECOPI, como entidad reguladora gubernamental, tiene facultades especiales para acceder a esta información — pero una empresa privada que haga lo mismo podría enfrentar consecuencias legales.

---

### b) EJERCICIO INDIVIDUAL: Diagnosticar un dataset (15 min)

**Instrucción:**

Analiza el siguiente fragmento de dataset de una empresa de logística de Lima y responde:

```python
data_logistica = {
    "id_envio":      ["ENV001", "ENV002", "ENV001", "ENV003", "ENV004", "ENV005"],
    "destinatario":  ["José Torres", "JOSE TORRES", "María Lima", "pedro garcia", None, "Ana Ríos"],
    "telefono":      ["987654321", "987654321", "+51912345", "01-4567890", "999", "912345678"],
    "distrito":      ["Surco", "surco", "SJL", "San Isidro", "CALLAO", "Miraflores"],
    "peso_kg":       [2.5, 2.5, -1.0, 0.3, 850.0, 1.8],
    "fecha_envio":   ["2024-03-01", "01/03/2024", "2024-03-05", "2024-03-07", "2024-03-10", None],
    "estado":        ["entregado", "entregado", "PENDIENTE", "Pendiente", "En camino", "entregado"],
}
df_log = pd.DataFrame(data_logistica)
```

**Preguntas:**

1. Lista todos los problemas de calidad que identificas (tipo de problema + campo + fila).
2. Escribe el código pandas para: (a) eliminar el duplicado, (b) normalizar la columna `estado` a minúsculas con `.str.lower()`, (c) marcar como None los teléfonos con menos de 9 dígitos.
3. ¿El peso_kg = -1.0 lo eliminarías o lo marcarías como NaN? Justifica.

**Criterio de éxito:**
- Identificó al menos 5 problemas distintos (hay más de 7)
- El código de (b) es correcto: `df_log["estado"] = df_log["estado"].str.lower()`
- Justifica correctamente la decisión para el outlier

---

## 5. CIERRE (10 min) {#cierre}

### a) SÍNTESIS COLABORATIVA (4 min)

**Pregunta cierre 1:** *"¿Cuáles son los 3 pasos mínimos que debe tener cualquier pipeline de limpieza de datos?"*

> **Respuesta esperada:** (1) Diagnóstico: cuantificar nulos, duplicados, tipos de dato y outliers antes de tocar nada, (2) Limpieza: eliminar duplicados, corregir formatos, marcar valores inválidos como NaN, (3) Normalización: estandarizar representación (capitalización, fechas en formato único, precios como float, categorías con nombre canónico). Opcional pero recomendado: (4) Validación post-limpieza: verificar que las métricas de calidad mejoraron.

**Pregunta cierre 2:** *"¿Cuál es la diferencia entre `dropna()` y `fillna()`? ¿Cuándo usarías cada una?"*

> **Respuesta esperada:** `dropna()`: elimina las filas (o columnas) que contienen al menos un NaN. Se usa cuando hay pocas filas con nulos o cuando los nulos indican datos completamente inválidos. `fillna()`: reemplaza los NaN con un valor específico (media, mediana, moda, valor de negocio por defecto, valor del registro anterior/siguiente). Se usa cuando la eliminación reduciría demasiado el dataset o cuando el nulo puede imputarse de forma razonable. Regla general: `fillna` para columnas importantes con pocos nulos, `dropna` para filas donde más de la mitad de los campos son nulos.

**Pregunta cierre 3:** *"¿Por qué el `robots.txt` es importante antes de hacer scraping? ¿Es una obligación legal?"*

> **Respuesta esperada:** El `robots.txt` es el estándar de la industria para que los sitios web indiquen a los scrapers automatizados qué páginas pueden y no pueden acceder. No es una ley en sí mismo, pero ignorarlo puede: (1) violar los Términos de Servicio del sitio, dando lugar a demandas por daños; (2) constituir acceso no autorizado a sistemas informáticos según leyes de delitos informáticos; (3) en la UE, potencialmente violar el GDPR si se extraen datos personales. En Perú, la Ley N° 30096 (delitos informáticos) puede aplicar si el scraping interfiere con sistemas o accede a datos privados.

---

### b) METACOGNICIÓN (3 min)

> *"En silencio, respondan internamente:"*
>
> *"¿Podría explicarle a un compañero que llegó tarde la diferencia entre `find()` y `find_all()` en BeautifulSoup?"*
>
> *"¿Si me dan un dataset de 10,000 filas mañana, sé cómo diagnosticar cuántos datos son confiables antes de empezar el análisis?"*
>
> *"¿En el proyecto de mi grupo, hay algún campo que probablemente tenga datos sucios? ¿Qué tipo de suciedad esperaría?"*

---

### c) TAREA / PUENTE (3 min)

**Tarea para el laboratorio en casa:**

> *"En el laboratorio en casa van a construir un pipeline completo: primero scrapearán datos de books.toscrape.com, luego limpiarán y normalizarán el dataset completo, y finalmente harán un análisis básico de precios por categoría. Todo en Google Colab. El código esqueleto está en el laboratorio."*

**Puente con S8:**

> *"La próxima semana es la última sesión: Casos de Estudio Empresariales y Evaluación Final. Van a ver cómo Google, Facebook, Uber y LinkedIn aplican TODO lo que aprendieron en el curso. Es también cuando defenderán sus proyectos grupales. Vengan con los datasets limpios — la semana 8 no habrá tiempo para limpiar datos."*

---

## GUION VERBAL SUGERIDO {#guion}

**Al presentar `robots.txt`:**
> *"Imaginen que llegan a una biblioteca. Hay un letrero: 'Los estudiantes solo pueden acceder a las salas 1, 2 y 3. La sala 4 es solo para investigadores'. Ustedes, como visitantes educados, respetan eso. El `robots.txt` es ese letrero para los scrapers. No ignorarlo no es solo una cuestión legal — es una cuestión de respeto hacia quienes mantienen los servidores."*

**Al explicar la regla de no alterar la esencia:**
> *"Normalizar es como limpiar monedas antiguas para que se vean bien, sin cambiar su valor ni raspar el grabado. Si una fecha dice '15 de enero 2024', puedo cambiarla a '2024-01-15' — eso es normalización. Pero si dice '15 de enero 2024' y yo la cambio a '16 de enero 2024' porque creo que era un error, eso ya no es normalización — es alteración de datos. La integridad implica respetar lo que el dato dice, solo cambiar cómo se representa."*

**Al cerrar el tema de limpieza:**
> *"Un modelo de ML entrenado con datos sucios es como una brújula calibrada con imanes equivocados — siempre apunta, parece funcionar, pero te lleva en la dirección equivocada. La calidad del dato determina la calidad de la decisión."*

---

## CASOS REALES RECOMENDADOS {#casos}

1. **NASA Mars Climate Orbiter (1999):** Pérdida de 327M USD por inconsistencia de unidades (imperial vs métrico) entre dos módulos de software. El dato llegó correcto pero en formato incompatible. Fuente: NASA Report, 1999. Lección: la normalización de unidades/formatos es crítica en sistemas críticos.

2. **SUNAT Perú — Fiscalización de RUCs fantasma:** La SUNAT detectó en 2022 más de 15,000 RUCs activos con inconsistencias (dirección fiscal en terrenos baldíos, razón social con caracteres especiales inválidos, fechas de constitución en el futuro). Los scrapers de auditoría compararon datos del Registro de Empresas con registros de la Sunarp. Fuente: El Comercio, 2022.

3. **Booking.com — scraping de competidores:** Booking.com fue demandada en 2020 por hoteles que alegaban que la empresa usaba scrapers para extraer sus precios y condiciones y luego los usaba para ofrecer mejores condiciones a los clientes. El caso puso en debate los límites legales del price scraping. Fuente: Reuters, 2020.

4. **hiQ Labs vs LinkedIn (EE.UU., 2022):** El Tribunal de Apelaciones del 9° Circuito dictaminó que el scraping de datos PÚBLICOS de perfiles de LinkedIn no viola la ley de Computer Fraud and Abuse Act. Sentencia clave para entender los límites legales del scraping de datos públicos vs privados.

5. **datos.gob.pe — Portal de Datos Abiertos Perú:** El portal oficial del gobierno peruano publica datasets en CSV, JSON y a través de APIs. Incluye datos del MINSA, MIDIS, MEF, MINEDU. Es la fuente más segura y legal para extracción de datos peruanos con fines académicos y de investigación. URL: https://www.datosabiertos.gob.pe

---

## EVALUACIÓN FORMATIVA

| Momento | Indicador | Señal de comprensión |
|---------|-----------|---------------------|
| Diagnóstico inicial | Respuesta sobre "inspeccionar código fuente" | Reconoce HTML, menciona etiquetas |
| Transformación 3.1 | Mini actividad CSS selectors | Usa `#` para ID, `.` para clase correctamente |
| Transformación 3.4 | Pregunta P4 (outliers -500 y 150K) | Diferencia entre error de digitación y outlier real |
| Transformación 3.5 | Pregunta P5 (media vs mediana) | Justifica con distribución asimétrica |
| Práctica grupal | Producto del grupo | Identifica 5+ problemas, propone orden de limpieza |
| Ejercicio individual | Código de normalización `estado` | `df["estado"].str.lower()` correcto |

---

## REFERENCIAS APA 7 {#referencias}

Mitchell, R. (2018). *Web scraping with Python: Collecting more data from the modern web* (2nd ed.). O'Reilly Media.

Richardson, L. (2023). *Beautiful Soup documentation* (Version 4.12). Crummy.com. https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

Wickham, H. (2014). Tidy data. *Journal of Statistical Software*, *59*(10), 1–23. https://doi.org/10.18637/jss.v059.i10

Osborne, J. W. (2013). *Best practices in data cleaning: A complete guide to everything you need to do before and after collecting your data*. SAGE Publications.

Batini, C., & Scannapieco, M. (2016). *Data and information quality: Dimensions, principles and techniques*. Springer. https://doi.org/10.1007/978-3-319-24106-7

---

## RECURSOS

- **Sitio de práctica scraping:** https://books.toscrape.com | https://quotes.toscrape.com
- **Documentación BeautifulSoup:** https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Documentación requests:** https://docs.python-requests.org/en/latest/
- **pandas limpieza oficial:** https://pandas.pydata.org/docs/user_guide/missing_data.html
- **Portal datos abiertos Perú:** https://www.datosabiertos.gob.pe
- **Repositorio GitHub — web scraping cookbook:** https://github.com/realpython/web-scraping-in-python-course
- **Google Colab para este lab:** https://colab.research.google.com

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 7 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay*
