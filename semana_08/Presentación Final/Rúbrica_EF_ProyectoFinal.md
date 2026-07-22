# RÚBRICA — EVALUACIÓN FINAL DE PROYECTOS BIG DATA
## Curso: BIG DATA (DD283) · Ciclo VIII · 2026-1
### Docente: Mg. Rubén Quispe Llacctarimay — Universidad Autónoma del Perú
### Fecha: Sábado 26 de julio de 2026 · Modalidad: Presencial con demo técnica

---

## GRUPOS Y PROYECTOS

| Grupo | Proyecto | GitHub |
|-------|----------|--------|
| G1 | Churn Telecom B2B | github.com/RubenCarty/bigdata-g1-churn-telecom-b2b |
| G2 | Telcom Prediction | github.com/RubenCarty/bigdata-g2-telcom-prediction |
| G3 | Demanda Hospitalaria | github.com/RubenCarty/bigdata-g3-demanda-hospitalaria |
| G4 | Doctor Data | github.com/RubenCarty/bigdata-g4-Doctor-Data |
| G5 | Fraude Bancario | github.com/RubenCarty/bigdata-g5-fraude-bancario |
| G6 | ITSM Analytics | github.com/RubenCarty/bigdata-g6-itsm-analytics |

---

## DISTRIBUCIÓN DE PUNTOS (ESCALA 0 – 20)

| # | Dimensión de Evaluación | Puntaje | Peso |
|---|-------------------------|---------|------|
| 1 | Repositorio GitHub (estructura + código + docs + PR) | **4.0 pts** | 20% |
| 2 | Presentación técnica oral — 12 minutos | **7.0 pts** | 35% |
| 3 | ⭐ Defensa técnica ante el docente — 8 minutos | **8.0 pts** | 40% |
| 4 | Presentación profesional (vestimenta + actitud) | **1.0 pt** | 5% |
| — | **TOTAL BASE** | **20.0 pts** | 100% |
| ★ | Bonificación: preguntas del salón (suma sobre el total, tope 20) | **+1.0 pt** | — |

> **⭐ CRITERIO DE MAYOR PESO:** La defensa técnica (8 min / 8 pts) representa el 40% de la nota.
> Una presentación impecable NO compensa la incapacidad de responder preguntas técnicas precisas.
> El docente evaluará si los estudiantes realmente implementaron y comprenden su solución.

---

## DIMENSIÓN 1 — REPOSITORIO GITHUB `(4.0 puntos)`

### Estructura requerida para todos los grupos

Cada repositorio **DEBE** cumplir con la siguiente estructura antes del PR:

```
bigdata-g[N]-[nombre-proyecto]/
│
├── README.md                          ← OBLIGATORIO (ver plantilla abajo)
├── requirements.txt                   ← OBLIGATORIO (o package.json / go.mod)
├── .gitignore                         ← OBLIGATORIO
├── LICENSE                            ← OBLIGATORIO
│
├── docs/
│   ├── arquitectura/
│   │   ├── as-is.png                 ← OBLIGATORIO (diagrama del estado actual)
│   │   └── to-be.png                 ← OBLIGATORIO (diagrama de la solución)
│   └── [G{N}]-documentacion-tecnica.pdf   ← OBLIGATORIO (o link al campus si >25MB)
│
├── data/
│   ├── raw/
│   │   └── README.md o .gitkeep + link al dataset original
│   └── processed/
│       └── muestra del dataset procesado (máx. 5 MB) o README con link
│
├── notebooks/
│   ├── 01_eda_exploracion.ipynb      ← OBLIGATORIO
│   ├── 02_pipeline_procesamiento.ipynb ← OBLIGATORIO
│   └── 03_modelo_entrenamiento.ipynb  ← OBLIGATORIO si hay ML
│
├── src/
│   └── [módulos Python / Go / JS / Scala organizados por función]
│       ├── ingestion/
│       ├── processing/
│       └── modeling/ o api/ o dashboard/
│
└── CONTRIBUTING.md                    ← RECOMENDADO (o incluido en README)
```

### Plantilla mínima del README.md

```markdown
# [Nombre del Proyecto] — Big Data DD283

## Descripción
[2-3 párrafos explicando el problema y la solución]

## Arquitectura
![AS-IS](docs/arquitectura/as-is.png)
![TO-BE](docs/arquitectura/to-be.png)

## Stack tecnológico
| Tecnología | Rol en el proyecto |
|------------|--------------------|

## Cómo ejecutar
[Instrucciones paso a paso]

## Dataset
[Fuente, tamaño, características]

## Resultados
[Métricas clave obtenidas]

## Integrantes
| Nombre | Rol |
|--------|-----|

## Documentación técnica
[Link al PDF en docs/ o al campus virtual]
```

### Formato del Pull Request

- **Rama de origen:** `feature/entrega-final` → `main`
- **Título del PR:** `[G{N}] {Nombre Proyecto} — Entrega Final EF | DD283 | 2026-1`
- **Descripción debe incluir:**
  1. Resumen de lo implementado (3-5 bullets)
  2. Tecnologías principales usadas
  3. Resultado/métrica principal obtenida
  4. Link a la documentación PDF (si está en el campus)

---

### Tabla de evaluación — Repositorio (4.0 pts)

| Criterio | 0 pts | 0.5 pts | 1.0 pt | 1.5 pts |
|----------|-------|---------|--------|---------|
| **R1. Estructura de carpetas requeridas** (1.5 pts) | Sin estructura / solo archivos en raíz | Estructura parcial: faltan 3+ carpetas o README básico | La mayoría de carpetas presentes, README incompleto | Todas las carpetas presentes, README completo con diagrama y tabla de stack |
| **R2. Código fuente funcional y comentado** (1.0 pt) | No hay código o solo `.gitkeep` vacíos | Código incompleto o sin ejecutar | Código ejecutable pero sin comentarios técnicos | Código ejecutable, organizado, con comentarios explicando decisiones técnicas |
| **R3. Documentación técnica en PDF** (1.0 pt) | No existe PDF ni link | PDF referenciado pero inaccesible | PDF en campus con link en README | PDF en `docs/` (o campus con link claro) que incluye: metodología, arquitectura, resultados y conclusiones |
| **R4. Pull Request correctamente enviado** (0.5 pts) | PR no enviado o sin descripción | PR enviado sin título estándar ni descripción | PR con título correcto y descripción mínima | PR con título estándar, descripción completa, commits limpios y descriptivos |

---

## DIMENSIÓN 2 — PRESENTACIÓN TÉCNICA ORAL `(7.0 puntos)` · 12 minutos

> **Guía de tiempo sugerida:**
> - 0:00 – 1:00 → Título + problema + impacto social/económico
> - 1:00 – 3:00 → Solución: ¿qué construyeron? ¿por qué es Big Data?
> - 3:00 – 5:00 → Arquitectura AS-IS y TO-BE (el corazón técnico)
> - 5:00 – 8:00 → Stack tecnológico: ¿qué usaron y por qué?
> - 8:00 – 12:00 → Demo en vivo del sistema funcionando + métricas

> **Sobre el uso de PPT:**
> La presentación es principalmente técnica y práctica.
> El PPT se usa SOLO para mostrar: arquitectura, diagramas, métricas finales.
> NO leer diapositivas. La demo en vivo tiene más valor que cualquier slide.

---

### Tabla de evaluación — Presentación (7.0 pts)

#### B1 — Planteamiento del problema y justificación Big Data `(1.0 pt)`

| 0 pts | 0.5 pts | 1.0 pt |
|-------|---------|--------|
| No define el problema o es demasiado vago para entenderse | Describe el problema pero no justifica por qué requiere Big Data (las 5Vs) | Problema claramente delimitado con datos reales. Justifica con al menos 2 de las 5Vs del Big Data. Muestra el impacto cuantificable |

#### B2 — Solución propuesta y valor generado `(1.0 pt)`

| 0 pts | 0.5 pts | 1.0 pt |
|-------|---------|--------|
| No explica la solución construida | Describe la solución a nivel superficial sin conectar con los datos | Explica claramente QUÉ construyeron, QUÉ problema resuelve, y CÓMO los datos son el centro de la solución. Menciona el valor para el usuario final |

#### B3 — Arquitectura AS-IS y TO-BE `(2.0 pts)` ← CRÍTICO

| 0 pts | 0.5 pts | 1.0 pt | 1.5 pts | 2.0 pts |
|-------|---------|--------|---------|---------|
| No presenta arquitectura o es una imagen sin explicación | Muestra un diagrama pero no explica ningún componente | Presenta ambas arquitecturas pero la explicación es superficial o una no está | Ambas arquitecturas claras, explica las diferencias y mejoras del TO-BE | Ambas arquitecturas con explicación técnica precisa de cada capa: ingesta → procesamiento → almacenamiento → análisis → visualización. Señala con claridad qué tecnologías van en cada capa |

#### B4 — Stack tecnológico y decisiones técnicas `(1.5 pts)`

| 0 pts | 0.5 pts | 1.0 pt | 1.5 pts |
|-------|---------|--------|---------|
| Solo listan nombres de herramientas sin contexto | Mencionan tecnologías pero no explican por qué las eligieron | Explican las tecnologías principales con justificación básica | Explican CADA tecnología, por qué la eligieron vs alternativas, y cómo se integra en la arquitectura. Mencionan costos, limitaciones o trade-offs |

#### B5 — Demo en vivo del sistema `(1.0 pt)`

| 0 pts | 0.3 pts | 0.7 pts | 1.0 pt |
|-------|---------|---------|--------|
| No hay demo / solo muestran código estático | Demo pregrabada (video) o solo capturas de pantalla | Demo en vivo pero parcial (no muestra el flujo completo de datos) | Demo en vivo funcional que muestra el flujo completo: ingesta de datos → procesamiento → resultado/predicción → visualización |

#### B6 — Manejo del tiempo y participación del equipo `(0.5 pt)`

| 0 pts | 0.3 pts | 0.5 pts |
|-------|---------|---------|
| Se pasa más de 3 min del tiempo o no termina / solo expone 1 persona | Termina a tiempo pero solo 1-2 personas exponen activamente | Termina dentro de los 12 min (±1 min), todos los integrantes participan en la exposición y la demo |

---

## DIMENSIÓN 3 — DEFENSA TÉCNICA ANTE EL DOCENTE `(8.0 puntos)` · 8 minutos

> ⭐ **DIMENSIÓN DE MAYOR PESO — 40% de la nota total**
>
> El docente realizará **4 preguntas técnicas** (2 pts c/u) durante 8 minutos.
> Las preguntas buscan verificar que los estudiantes REALMENTE implementaron y comprenden su proyecto.
> No se aceptan respuestas genéricas del tipo "usamos Spark porque es rápido" sin detalles técnicos.

### Escala de calificación por pregunta (× 4 preguntas = 8 pts)

| Nivel | Puntos | Descriptor |
|-------|--------|-----------|
| **Excelente** | 2.0 | Respuesta técnica precisa, cita código propio, ejemplifica con datos reales del proyecto, muestra comprensión profunda |
| **Bueno** | 1.5 | Respuesta correcta pero general, sin ejemplificar con código o datos específicos del proyecto |
| **Regular** | 1.0 | Respuesta parcialmente correcta, confunde conceptos o da información incompleta |
| **Insuficiente** | 0.5 | Intenta responder pero comete errores conceptuales graves |
| **No responde** | 0.0 | No responde, responde algo completamente distinto, o dice "no sé" |

---

### BANCO DE PREGUNTAS TÉCNICAS POR GRUPO

> El docente seleccionará 4 de las siguientes preguntas por grupo.
> Algunas preguntas aplican a todos los grupos.

---

#### GRUPO 1 — Churn Telecom B2B
`github.com/RubenCarty/bigdata-g1-churn-telecom-b2b`

1. ¿Cómo manejaron el desbalance de clases en el dataset de churn? ¿Usaron SMOTE, class_weight o submuestreo? ¿Por qué eligieron ese enfoque?
2. Explica el pipeline completo de preprocesamiento: ¿qué transformaciones aplicaron a las variables categóricas? ¿Cómo trataron los valores nulos?
3. ¿Cuáles son las 3 variables más importantes según Feature Importance de su modelo? ¿Qué significa eso para el negocio de telecomunicaciones?
4. ¿Cuál es el AUC-ROC de su modelo? ¿Por qué eligieron ese umbral de decisión (threshold) para la clasificación? ¿Qué pasa si lo bajan a 0.3?
5. Si un nuevo cliente entra al sistema hoy, ¿cuál es el flujo de datos exacto desde que llega el dato hasta que se genera la predicción de churn?
6. ¿Cómo validaron que su modelo no tiene data leakage? Explica qué medidas tomaron en el train/test split.

---

#### GRUPO 2 — Telcom Prediction
`github.com/RubenCarty/bigdata-g2-telcom-prediction`

1. Describe el pipeline completo en `pipeline.py`: ¿qué hace cada step? ¿Qué entra y qué sale de cada función?
2. ¿Por qué `StandardScaler` debe ajustarse solo con datos de entrenamiento y no con todo el dataset? ¿Qué ocurriría si no lo hicieran?
3. ¿Qué diferencias hay entre su arquitectura AS-IS (sistema actual de la telco) y la TO-BE que proponen? ¿Cuánto mejorarían los tiempos de procesamiento?
4. En `modelo.py`, ¿qué algoritmo de ML usaron? ¿Por qué ese y no una Regresión Logística o un árbol de decisión simple?
5. ¿Cómo evaluarían si su modelo sigue siendo preciso después de 3 meses? ¿Tienen algún mecanismo de monitoreo de data drift?
6. Si les piden poner el modelo en producción con Spark MLlib en lugar de scikit-learn, ¿qué cambios serían necesarios en el código?

---

#### GRUPO 3 — Demanda Hospitalaria
`github.com/RubenCarty/bigdata-g3-demanda-hospitalaria`

1. ¿De qué fuente obtuvieron los datos hospitalarios? ¿Cómo los limpiaron? ¿Cuántos registros tienen y qué período temporal cubren?
2. En `03_mongodb_kpis.ipynb`, ¿cuáles son los 3 KPIs más relevantes que calculan? ¿Cómo los obtienen desde MongoDB con aggregation pipeline?
3. ¿Por qué eligieron MongoDB para almacenar los KPIs hospitalarios en lugar de un RDBMS como PostgreSQL? ¿Qué ventajas tienen con el esquema de datos HIS del MINSA?
4. ¿Qué técnica usan para predecir la demanda futura? ¿Cómo validan que la predicción tiene sentido? ¿Cuál es el MAE o MAPE de su modelo?
5. Si un hospital en Lima quisiera integrar su sistema hoy, ¿cuál sería el proceso de onboarding de datos? ¿Cómo manejan las diferencias de formato entre hospitales?
6. ¿Cómo manejan los datos estacionales en la predicción? (por ejemplo: más atenciones en invierno por enfermedades respiratorias)

---

#### GRUPO 4 — Doctor Data
`github.com/RubenCarty/bigdata-g4-Doctor-Data`

1. ¿Cómo implementaron el cifrado AES-256 en el backend Go? ¿En qué momento del flujo se cifran los datos del paciente? ¿Y cuándo se descifran?
2. Explica la arquitectura del backend Go: ¿qué rutas expone la API? ¿Cómo funciona el acceso por QR/NFC técnicamente (no a nivel usuario, sino a nivel código)?
3. ¿Cómo garantizan cumplimiento con la Ley N° 29733 de Protección de Datos Personales del Perú? ¿Qué medidas técnicas concretas implementaron?
4. ¿Cómo funciona el RBAC (Role Based Access Control)? Si un médico de guardia intenta acceder al historial de un paciente que no le corresponde, ¿qué ocurre exactamente en el sistema?
5. ¿Dónde se almacenan los datos en la arquitectura TO-BE? ¿Por qué eligieron MongoDB Atlas y no un RDBMS relacional para el historial médico?
6. En el frontend React Native, ¿cómo manejan la sincronización offline? Si el médico no tiene internet en la emergencia, ¿puede acceder al historial?

---

#### GRUPO 5 — Fraude Bancario
`github.com/RubenCarty/bigdata-g5-fraude-bancario`

1. ¿Cuál es la arquitectura completa de detección de fraude en tiempo real? ¿Usan Kafka + Spark Structured Streaming? Explica el flujo de datos desde la transacción hasta la alerta.
2. El dataset de fraude bancario es típicamente 99% negativo / 1% positivo. ¿Cómo manejaron este desbalance extremo? ¿Qué métricas usaron para evaluar el modelo?
3. Si hay que detectar una transacción fraudulenta en menos de 2 segundos, ¿qué ventana temporal usan en Structured Streaming? ¿Qué `outputMode` del streaming es el correcto para alertas en tiempo real?
4. ¿Por qué la Accuracy sería engañosa como métrica principal en fraude bancario? ¿Qué métrica priorizaron y por qué?
5. ¿Qué features construyeron para el modelo? ¿Construyeron features de comportamiento temporal (como frecuencia de transacciones en los últimos 30 minutos)?
6. ¿Cómo guardan las alertas de fraude? ¿Qué base de datos eligieron y por qué esa y no MongoDB o HBase?

---

#### GRUPO 6 — ITSM Analytics
`github.com/RubenCarty/bigdata-g6-itsm-analytics`

1. ¿Qué KPIs del ITSM calculan y cuáles son los valores actuales de esos KPIs en los datos que procesaron? Cita un número concreto (no "el tiempo promedio de resolución", sino "es de X horas").
2. ¿De qué sistema de ITSM provienen los datos? ¿ServiceNow, GLPI, Jira Service Management u otro? ¿Cómo extrajeron los datos?
3. Explica el diccionario de datos: ¿qué significa cada campo en el dataset de tickets? ¿Cuáles son los campos más relevantes para los análisis?
4. ¿Qué análisis predictivo hacen? ¿Pueden predecir el tiempo de resolución de un nuevo ticket? ¿Qué algoritmo usaron?
5. ¿Cuál es la arquitectura del dashboard? ¿Con qué herramienta lo construyeron (Power BI, Grafana, Streamlit, Apache Superset)? ¿Cómo se conecta con los datos procesados?
6. Si el volumen de tickets crece 10x, ¿cómo escalaría su arquitectura? ¿Qué cambios harían al pipeline actual?

---

### PREGUNTAS TRANSVERSALES (aplican a cualquier grupo)

El docente puede complementar con estas si las respuestas del grupo son muy superficiales:

- ¿Cuáles son las 5Vs del Big Data y cómo se manifiestan específicamente en su proyecto?
- Si tuvieran que migrar su solución a AWS/Azure/GCP, ¿qué servicios usarían para cada capa?
- ¿Qué es la evaluación lazy (lazy evaluation) en Spark y cómo afectó el rendimiento de su pipeline?
- ¿Qué diferencia hay entre `reduceByKey` y `groupByKey`? ¿Cuál usaron y por qué?
- ¿Cómo manejan los datos nulos en su dataset? ¿Eliminan filas, imputan o tienen otra estrategia?
- ¿Cuál fue el mayor problema técnico que enfrentaron y cómo lo resolvieron?
- Si tuvieran que escalar su solución para procesar 100x más datos, ¿qué cambiarían en la arquitectura?

---

## DIMENSIÓN 4 — PRESENTACIÓN PROFESIONAL `(1.0 punto)`

| Criterio | 0 pts | 0.5 pts |
|----------|-------|---------|
| **P1. Vestimenta formal** | Más de 2 integrantes sin ropa formal (polos, shorts, casual extremo) | Todos los integrantes con vestimenta formal: camisa/blusa, pantalón/falda formal |
| **P2. Actitud y comunicación** | Leen todo del PPT, no mantienen contacto visual, actitud desinteresada | Hablan con seguridad sin leer el PPT, mantienen contacto visual con el salón, demuestran dominio del tema |

---

## BONIFICACIÓN — PARTICIPACIÓN DEL SALÓN `(+1.0 punto extra)`

> Los estudiantes del salón que no están exponiendo pueden hacer preguntas o dar recomendaciones constructivas al grupo expositor. Esto suma puntos al grupo.

| Condición | Bonificación |
|-----------|-------------|
| 3 o más preguntas/recomendaciones del salón al grupo | +1.0 pt |
| 1-2 preguntas del salón al grupo | +0.5 pt |
| Sin preguntas del salón | +0.0 pt |

> **Nota:** La bonificación suma sobre el total, con tope de 20/20.

---

## ESCALA DE CALIFICACIÓN FINAL

| Nota | Calificación | Nivel |
|------|-------------|-------|
| 18.0 – 20.0 | Excelente | Aprobado con distinción |
| 15.0 – 17.9 | Muy Bueno | Aprobado |
| 13.0 – 14.9 | Bueno | Aprobado |
| 10.5 – 12.9 | Suficiente | Aprobado |
| 0.0 – 10.4 | Insuficiente | **Desaprobado** |

> Para aprobar el curso: nota EF ≥ 10.5 sobre 20.
> El peso de la EF en la nota final del curso es **50%** (según sílabo DD283).

---


---

## INSTRUCCIONES PARA LOS GRUPOS — CHECKLIST PRE-PRESENTACIÓN

### Viernes antes de la presentación (hasta las 23:59)

- [ ] PR enviado con el título correcto: `[G{N}] {Nombre} — Entrega Final EF | DD283 | 2026-1`
- [ ] `README.md` completo con: descripción, arquitectura, stack, instrucciones de ejecución, integrantes
- [ ] Carpeta `docs/arquitectura/` con `as-is.png` y `to-be.png`
- [ ] PDF de documentación técnica en `docs/` (o link al campus si pesa > 25 MB)
- [ ] Al menos 2 notebooks con código ejecutable (no vacíos)
- [ ] Carpeta `src/` con código fuente organizado
- [ ] `requirements.txt` o `package.json` actualizado
- [ ] `.gitignore` que excluye: `.env`, `*.csv` grandes, `__pycache__/`, `node_modules/`

### El día de la presentación (sábado)

- [ ] Laptop con el proyecto funcionando y listo para demo
- [ ] Demo probada sin internet (si usa servicios cloud, verificar que funciona)
- [ ] Diagrama de arquitectura visible para mostrar en el salón
- [ ] Todos los integrantes con vestimenta formal
- [ ] Cronómetro interno para respetar los 12 minutos
- [ ] Cada integrante sabe responder preguntas técnicas de SU PARTE del proyecto
- [ ] Tener a mano: el código en GitHub + el PDF de documentación

---

## ORDEN DE PRESENTACIÓN (Sábado)

| # | Horario | Grupo | Proyecto |
|---|---------|-------|---------|
| 1 | 02:00 – 02:20 | G1 | Churn Telecom B2B |
| 2 | 02:25 – 02:45 | G2 | Telcom Prediction |
| 3 | 02:50 – 03:10 | G3 | Demanda Hospitalaria |
| — | 03:10 – 03:20 | — | *Descanso 10 min* |
| 4 | 03:20 – 03:40 | G4 | Doctor Data |
| 5 | 03:45 – 04:05 | G5 | Fraude Bancario |
| 6 | 04:10 – 04:30 | G6 | ITSM Analytics |
| — | 04:30 – 04:50 | — | *Retroalimentación general* |

> Cada bloque = 12 min exposición + 8 min Q&A docente = **20 min por grupo**

---

## DIAGNÓSTICO DEL ESTADO ACTUAL DE REPOSITORIOS

> Revisión realizada el 2026-07-22. Los grupos deben completar lo pendiente antes del viernes.

| Grupo | README | Código | Notebooks | docs/ | PDF | Estado |
|-------|--------|--------|-----------|-------|-----|--------|
| G1 | ✅ | ⚠️ Por completar | ⚠️ Por completar | ⚠️ Solo semanas | ❌ Falta | Completar código + PDF |
| G2 | ✅ | ✅ pipeline.py / modelo.py | ✅ 4 notebooks | ❌ Sin carpeta docs | ❌ Falta | Agregar docs/ + PDF + arquitectura |
| G3 | ✅ | ⚠️ Por completar | ✅ EDA + MongoDB | ✅ PDF parcial EP | ⚠️ EP (no final) | Actualizar PDF final + completar notebooks |
| G4 | ✅ | ✅ Go backend + React Native | N/A (full-stack) | ⚠️ Solo resumen PDF | ⚠️ Resumen ejecutivo | Agregar docs/arquitectura/ AS-IS y TO-BE |
| G5 | ✅ | ❌ src/ vacío | ❌ notebooks vacíos | ❌ docs/ vacío | ❌ Falta | **URGENTE: Subir TODO el código** |
| G6 | ✅ | ❌ src/ vacío | ❌ notebooks vacíos | ⚠️ Solo KPIs y diccionario | ❌ Falta | **URGENTE: Subir código + notebooks + PDF** |

> 🔴 **G5 y G6:** Sus carpetas `src/`, `notebooks/` y `docs/` están vacías con solo `.gitkeep`.
> Deben subir **todo el código** antes del viernes o perderán los puntos de la Dimensión 1.

---

## CRITERIOS DE DESCALIFICACIÓN AUTOMÁTICA

El grupo obtiene **0 puntos en la Dimensión correspondiente** si:

- **Dimensión 1 (Repo):** No envían PR antes del viernes a las 23:59
- **Dimensión 2 (Presentación):** Presentan íntegramente con PPT leyendo slides sin demo ni explicación técnica
- **Dimensión 3 (Q&A):** Más del 50% del grupo no puede responder ninguna pregunta técnica de su propio proyecto
- **Dimensión 4 (Profesional):** Más de la mitad del grupo sin vestimenta formal

---

*Rúbrica elaborada por: Mg. Rubén Quispe Llacctarimay*
*Curso: Big Data DD283 — Universidad Autónoma del Perú — Ciclo VIII 2026-1*
*Versión: 1.0 — 2026-07-22*
