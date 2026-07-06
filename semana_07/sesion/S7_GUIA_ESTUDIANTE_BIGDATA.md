# S7 — GUÍA DE TRABAJO DEL ESTUDIANTE: Scraping, Limpieza y Normalización
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 7: Del Dato Sucio al Dataset Confiable

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

- Responde con tus propias palabras. Las respuestas copiadas anulan el puntaje.
- Tienes 1.5 horas para completar todas las secciones.
- Para la Sección A, marca con **X** la alternativa correcta.
- Para las secciones C y D, justifica siempre con argumentos técnicos concretos.
- Entrega en PDF en el aula virtual o como PR en el repositorio del curso.

> **No incluye respuestas** — las respuestas están en el documento del docente.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts c/u)

### Preguntas básicas (1-4)

**1.** ¿Qué hace la librería `requests` de Python en el contexto del web scraping?

- a) Parsea el HTML de una página web para encontrar etiquetas y atributos específicos
- b) Realiza solicitudes HTTP al servidor web y devuelve el contenido de la respuesta (HTML, JSON, etc.)
- c) Descarga imágenes y archivos multimedia de sitios web de forma automática
- d) Genera automáticamente el código Python para scrapear cualquier sitio web

**Respuesta:** [ ]

---

**2.** ¿Cuál de los siguientes métodos de BeautifulSoup retorna UNA LISTA con TODOS los elementos que coinciden con el criterio de búsqueda?

- a) `soup.find("p")`
- b) `soup.select_one(".precio")`
- c) `soup.find_all("p", class_="descripcion")`
- d) `soup.get("href")`

**Respuesta:** [ ]

---

**3.** Un dataset tiene la columna `telefono` con los valores: `"987654321"`, `None`, `"N/A"`, `"+51912345678"`. ¿Qué función de pandas convierte los textos "N/A" a NaN de forma automática al leer un CSV?

- a) `pd.read_csv("archivo.csv", na_values=["N/A"])`
- b) `pd.read_csv("archivo.csv").fillna("N/A")`
- c) `pd.read_csv("archivo.csv").dropna()`
- d) `pd.read_csv("archivo.csv", dtype={"telefono": float})`

**Respuesta:** [ ]

---

**4.** ¿Cuál es el propósito del archivo `robots.txt` en el contexto del scraping web?

- a) Especifica el código de programación que deben usar los scrapers para acceder al sitio
- b) Indica a los scrapers automatizados qué partes del sitio pueden o no pueden acceder
- c) Bloquea técnicamente el acceso de cualquier script Python al servidor web
- d) Contiene la clave de API necesaria para autorizar el scraping del sitio

**Respuesta:** [ ]

---

### Preguntas intermedias (5-7)

**5.** Un Data Scientist recibe un dataset con la columna `fecha_nacimiento` con estos valores: `"1990-05-15"`, `"15/05/1990"`, `"May 15, 1990"`. ¿Cuál es la acción correcta para normalizarlos?

- a) Eliminar todas las filas con fechas en formato diferente al primero (`"1990-05-15"`)
- b) Convertir todos los valores a un único formato datetime estándar usando `pd.to_datetime()` con múltiples formatos
- c) Reemplazar todos los valores con la fecha actual usando `pd.Timestamp.now()`
- d) Almacenar las fechas como texto sin cambios, ya que pandas no puede convertir múltiples formatos

**Respuesta:** [ ]

---

**6.** Al analizar la columna `ingreso_mensual` de 1,000 trabajadores, se obtiene: mínimo = S/ -200, máximo = S/ 950,000, media = S/ 45,000, mediana = S/ 2,800. ¿Qué indican estos estadísticos?

- a) Los datos son correctos y representan la distribución normal del ingreso en Lima
- b) Existen errores (valor negativo) y outliers (950,000) que distorsionan la media; la mediana es más representativa
- c) El dataset tiene demasiados valores nulos que distorsionan los estadísticos
- d) La columna fue mal importada y todos los valores deben multiplicarse por 0.001

**Respuesta:** [ ]

---

**7.** ¿Cuál es la diferencia entre `df.dropna()` y `df.fillna(df.median())`?

- a) `dropna()` elimina columnas vacías; `fillna()` agrega nuevas columnas con los valores faltantes
- b) `dropna()` elimina las filas con valores nulos; `fillna()` reemplaza los nulos con un valor especificado
- c) Son equivalentes — ambos producen el mismo resultado final en el DataFrame
- d) `dropna()` solo funciona en columnas numéricas; `fillna()` solo funciona en columnas de texto

**Respuesta:** [ ]

---

### Preguntas avanzadas (8-10)

**8.** Un scraper extrae la siguiente tabla de una web de finanzas:

```
precio_str = ["S/. 1,500.00", "S/ 2.800", "1500", "dos mil soles", None]
```

Al aplicar `pd.to_numeric(precios, errors='coerce')`, ¿cuál es el resultado esperado?

- a) `[1500.0, 2800.0, 1500.0, 2000.0, NaN]`
- b) `[NaN, NaN, 1500.0, NaN, NaN]` porque los strings con "S/" son inválidos para `to_numeric`
- c) Lanza un `ValueError` porque hay strings mezclados con números
- d) `[1500.0, 2.8, 1500.0, NaN, NaN]` porque el punto en "2.800" se interpreta como decimal

**Respuesta:** [ ]

---

**9.** Un equipo está limpiando un dataset de 500,000 clientes de Claro Perú. Detectan que el 23% de los RUCs tienen 10 dígitos en lugar de 11 (estándar de SUNAT). ¿Cuál es la acción técnica más responsable?

- a) Agregar un "0" al inicio de todos los RUCs de 10 dígitos, ya que la mayoría de RUCs inician con cero
- b) Eliminar las 115,000 filas con RUC inválido, ya que no se puede recuperar la información correcta
- c) Marcar los RUCs inválidos como NaN, reportar la incidencia y escalar a la fuente original para corrección
- d) Rellenar con ceros al final hasta completar 11 dígitos, ya que es el método más utilizado en la industria

**Respuesta:** [ ]

---

**10.** Un scraper automatizado hace 500 requests por minuto al sitio de Saga Falabella para monitorear precios. El servidor responde con código HTTP 429. ¿Qué debe hacer el scraper?

- a) Continuar con el scraping ignorando el código 429, ya que los datos de precio son públicos
- b) Cambiar de IP (usar una VPN) y continuar con los 500 requests por minuto
- c) Reducir la velocidad de requests, implementar pausas y respetar los encabezados `Retry-After` del servidor
- d) Interpretar el 429 como una falla del servidor y reintentar el mismo request inmediatamente

**Respuesta:** [ ]

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### Parte 1: Completa los espacios en blanco (10 puntos | 2 pts c/u)

**1.** En BeautifulSoup, el método `soup.find("div", class_="_____")` busca el **primer** elemento `<div>` con esa clase, mientras que `soup._____("div", class_="precio")` devuelve una **lista** con todos los elementos que coinciden.

**2.** Antes de hacer scraping de cualquier sitio web, el profesional ético debe verificar el archivo `_____` en la raíz del dominio, que especifica qué rutas están permitidas o prohibidas para scrapers. Además, debe leer los _____ del sitio para confirmar que la extracción automatizada está permitida.

**3.** El método `df.drop_duplicates(subset=["_____"], keep="_____")` elimina filas duplicadas basándose solo en la columna especificada, conservando la primera aparición y descartando las siguientes.

**4.** Para detectar la presencia y cantidad de valores nulos en cada columna de un DataFrame, se usa la combinación `df._____().sum()`, que devuelve un entero por columna indicando cuántos valores son nulos.

**5.** El principio ético de la normalización de datos establece que solo se debe cambiar la _____ en que se representa el dato, nunca su _____ original. Por ejemplo, convertir "LIMA" a "Lima" es normalización, pero cambiar "Lima" por "Lima Metropolitana" cuando el campo solo decía "Lima" es _____ de datos.

---

### Parte 2: Relaciona las columnas (10 puntos | 1 pt c/par)

| # | CONCEPTO / MÉTODO | Letra | DESCRIPCIÓN / USO |
|---|------------------|-------|-------------------|
| 1 | `requests.get(url)` | ___ | A. Convierte strings de fecha con formatos mixtos a objetos datetime |
| 2 | `BeautifulSoup(html, "html.parser")` | ___ | B. Identifica valores estadísticamente extremos usando el rango intercuartílico |
| 3 | `soup.select(".clase > span")` | ___ | C. Reemplaza los valores nulos con un valor especificado (media, mediana, texto) |
| 4 | `pd.to_datetime()` | ___ | D. Realiza la solicitud HTTP GET y devuelve el objeto response con el contenido |
| 5 | `df.fillna()` | ___ | E. Aplica expresiones regulares para buscar o reemplazar patrones en strings |
| 6 | `df.str.strip()` | ___ | F. Parsea el HTML crudo y crea el árbol de objetos navegable |
| 7 | Método del IQR | ___ | G. Usa selectores CSS para encontrar elementos por jerarquía y clase |
| 8 | `re.sub()` | ___ | H. Elimina espacios en blanco al inicio y al final de un string |
| 9 | `df.describe()` | ___ | I. Muestra estadísticas descriptivas (count, mean, std, min, percentiles, max) |
| 10 | `robots.txt` | ___ | J. Archivo en la raíz del dominio que especifica las reglas de acceso para scrapers |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

### Pregunta C1 (8 puntos)

El equipo de analítica de SUNAT quiere construir un sistema que scrappe diariamente el Registro de Empresas público para detectar empresas con información desactualizada o inconsistente.

a) Describe el pipeline técnico completo (desde la URL hasta el dataset limpio) en al menos 5 pasos con el componente tecnológico que usarías en cada paso. *(4 puntos)*

b) El equipo detecta que el 15% de los teléfonos de las empresas tienen formatos distintos: `"01-4567890"` (fijo Lima), `"(01) 456-7890"`, `"014567890"`, `"+51 1 456 7890"`. Escribe la lógica (pseudocódigo o Python) de una función que normalice todos estos formatos al estándar `"014567890"` (9 dígitos, código de ciudad incluido). *(4 puntos)*

**Tu respuesta:**

---

### Pregunta C2 (8 puntos)

**Mini caso:** El MIDIS (Ministerio de Desarrollo e Inclusión Social) tiene un dataset de 2.3 millones de beneficiarios del programa Juntos con los siguientes problemas detectados:

| Columna | Problema | % afectado |
|---------|---------|------------|
| nombre | Mezcla de mayúsculas/minúsculas + caracteres especiales incorrectos | 34% |
| dni | DNIs con 7 dígitos (anterior a 1990) y 8 dígitos (actual) | 12% |
| ubigeo | Códigos de ubigeo de 5 dígitos cuando el estándar es 6 | 8% |
| ingreso_familiar | Valores negativos + valores > S/50,000 en familias registradas como "extrema pobreza" | 3% |
| fecha_inscripcion | 5 formatos distintos de fecha | 18% |

**C2a.** Para el campo `nombre`, ¿aplicarías `str.title()` directamente? ¿Qué caso especial peruano debe manejarse que `str.title()` no resuelve correctamente? Da un ejemplo específico. *(2 puntos)*

**C2b.** Para los DNIs de 7 dígitos, ¿cuál es la acción técnica correcta según el principio de integridad del dato? ¿Por qué no se recomienda agregar un "0" al inicio para completar 8 dígitos? *(3 puntos)*

**C2c.** Para los ingresos > S/50,000 en familias de extrema pobreza, el equipo propone dos opciones: (A) eliminar esas filas y (B) marcarlas como outliers sospechosos y auditarlas manualmente. ¿Cuál es más apropiada para un programa social? Justifica con un argumento ético y uno técnico. *(3 puntos)*

**Tu respuesta:**

---

### Pregunta C3 — Mini caso con análisis (14 puntos)

**Escenario — UrbanData Lima:**

Una startup de proptech (tecnología inmobiliaria) quiere construir un comparador de precios de departamentos en Lima scrapeando los portales Urbania, Adondevivir e InLima. El modelo de negocio es mostrar al comprador cuál portal tiene el mismo departamento más barato.

**C3a.** Identifica 3 desafíos técnicos específicos del scraping que enfrentaría esta startup (no menciones solo "el sitio puede bloquear" — explica el desafío técnico específico y su solución). *(4 puntos)*

**C3b.** Al consolidar datos de 3 portales del mismo departamento, el equipo obtiene:
- Urbania: `"Miraflores · 2 dorm. · 85 m² · S/ 320,000"`  
- Adondevivir: `"Miraflores, 2 dormitorios, 85.00 m2, USD 88,000"`  
- InLima: `"MFL | 2D | 85M2 | PEN 320000"`

Describe el proceso de normalización necesario para poder comparar estos 3 registros como si fueran el mismo departamento. *(5 puntos)*

**C3c.** La startup planea publicar los datos de precios en su plataforma pública. ¿Qué problema legal y ético específico existe con publicar precios extraídos de Urbania sin su consentimiento? ¿Cómo podrían los fundadores protegerse legalmente? *(5 puntos)*

**Tu respuesta:**

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

### Caso profesional: Observatorio de Precios del MEF

El Ministerio de Economía y Finanzas (MEF) del Perú lanza el "Observatorio de Precios" — un sistema que monitorea en tiempo real los precios de medicamentos esenciales en 450 farmacias de Lima (InkaFarma, MiFarma, SanaFarma, farmacias independientes). El objetivo: detectar medicamentos con precio superior al precio de referencia del MINSA.

**Datos del sistema:**
- Fuentes: scraping de webs + apps móviles de las cadenas + datos declarados manualmente por farmacias independientes
- Frecuencia: actualización diaria a las 6 AM
- Dataset histórico: 24 meses de precios, 3,200 medicamentos, 450 farmacias
- Problema detectado: 28% de registros con algún tipo de dato sucio

**D1.** Análisis profundo del pipeline *(10 puntos)*

a) El equipo descubre que InkaFarma carga los precios dinámicamente con JavaScript (no en el HTML inicial). Cuando hacen `requests.get(url)`, los precios no aparecen en el response. ¿Qué alternativa técnica existe para este caso? Explica el principio técnico (sin necesidad de saber la sintaxis exacta). *(3 puntos)*

b) Las farmacias independientes reportan precios manualmente en un formulario. El 28% de datos sucios proviene principalmente de este canal. Diseña una estrategia de prevención que reduzca ese porcentaje al momento de la captura (no después de la limpieza). *(4 puntos)*

c) El medicamento "Paracetamol 500mg x 10 tab" aparece con estos nombres en las distintas fuentes:
   - InkaFarma: `"PARACETAMOL 500 MG X 10 TABLETAS"`
   - MiFarma: `"Paracetamol 500mg (10 tabletas)"`
   - SanaFarma: `"PCML 500 10T"`
   - Farmacia independiente: `"Paracetamol x 10"`
   
   ¿Cómo resolvería el sistema que estos 4 registros corresponden al mismo medicamento? Describe la técnica de normalización o coincidencia apropiada. *(3 puntos)*

---

**D2.** Diseño de solución: "¿Cómo implementarías el pipeline de calidad de datos?" *(10 puntos)*

El Director de Analítica del MEF pide un pipeline de calidad que opere diariamente y genere automáticamente un "Reporte de Calidad" antes de que los datos se publiquen.

Diseña el pipeline completo describiendo:
a) Las 4 etapas del pipeline (de scraping a publicación) con las herramientas y decisiones técnicas de cada etapa *(4 puntos)*
b) Las 5 reglas de validación que el sistema debería verificar automáticamente antes de publicar los datos *(3 puntos)*
c) Qué debe contener el "Reporte de Calidad Diario" para que el director pueda tomar la decisión de publicar o retener los datos *(3 puntos)*

---

**D3.** Pensamiento crítico: La paradoja de la imputación *(10 puntos)*

a) "¿Qué pasaría si el equipo del MEF, al tener el 28% de datos sucios, decide imputar todos los nulos con la media del precio de cada medicamento por cadena?" Analiza las consecuencias de esta decisión para el objetivo del sistema (detectar precios por encima del precio de referencia del MINSA). *(4 puntos)*

b) Una cadena de farmacias alega que sus precios fueron scrapeados incorrectamente y que el sistema del MEF está reportando precios distintos a los reales. El MEF debe demostrar que el scraping fue correcto. ¿Qué evidencias técnicas debería haber almacenado el sistema para poder defenderlo? *(3 puntos)*

c) ¿Cuál es el riesgo de publicar un "precio promedio de mercado" calculado con datos que incluyen un 28% de valores imputados o aproximados? Da un ejemplo concreto de cómo esto podría afectar a un ciudadano que confía en ese dato para decidir dónde comprar su medicamento. *(3 puntos)*

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 7 | 2026-1*
*Docente: Mg. Rubén Quispe Llacctarimay | github.com/RubenCarty/bigdata-ua-2026-1*
