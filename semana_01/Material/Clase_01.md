# SEMANA 1 — GUÍA DE SESIÓN 
## Introducción a Big Data | Arquitectura y Organización de Sistemas Big Data

**Duración**: 3 horas teoría  
**Resultado de aprendizaje**: El estudiante analiza un caso reconociendo los tipos de datos y elabora la arquitectura de un proyecto de Big Data con integridad.

---

## ANTES DE LA CLASE — Checklist del docente

- [ ] Preparar las slides con casos reales (Netflix Perú, BCP, Claro Perú)
- [ ] Tener abierto Google Colab con el notebook de la semana
- [ ] Preparar un dataset de ejemplo (recomendado: datos del Banco Central de Reserva del Perú o SUNAT)
- [ ] Verificar acceso a draw.io (diagrams.net) en línea
- [ ] Asignar grupos de proyecto en la lista de clase

---

## APERTURA — Warm-Up (15 minutos)

### Actividad "Big Data en tu empresa"
**Objetivo**: Conectar con la experiencia real de los estudiantes (son working adults)

**Pregunta para el grupo**:
> "Levanten la mano: ¿En su empresa actual manejan datos? ¿Cuántos registros tiene su base de datos principal?"

**Preguntas de sondeo socráticas**:
1. ¿Qué hace tu empresa cuando la base de datos se llena?
2. ¿Han tenido lentitud en consultas? ¿Por qué creen que pasa?
3. ¿Han escuchado que Netflix sabe qué serie verás mañana? ¿Cómo creen que hace eso?

**Dato impactante para abrir la mente**:
> "En 2026, cada minuto se crean: 500 horas de video en YouTube, 6 millones de búsquedas en Google, 350,000 tweets, 65,000 fotos en Instagram. Todo eso son datos. ¿Quién los procesa?"

---

## BLOQUE 1 — TEORÍA (45 minutos)

### Tema 1: ¿Qué es Big Data? (15 min)

**Las 5 V's del Big Data** — explicar con analogías del mundo real:

| V | Definición | Analogía peruana |
|---|-----------|-----------------|
| **Volumen** | Cantidad masiva de datos (TB, PB, ZB) | SUNAT tiene 28M+ contribuyentes con historial de 20 años |
| **Velocidad** | Rapidez de generación y procesamiento | Yape procesa 10,000 transacciones por segundo en picos |
| **Variedad** | Múltiples formatos: texto, imagen, video, sensor | ONPE: votos + fotos de actas + tweets de candidatos |
| **Veracidad** | Confiabilidad de los datos | Datos del padrón electoral vs. datos de redes sociales |
| **Valor** | El dato tiene valor de negocio | BCP predice fraudes y ahorra millones |

**Pregunta socrática**:
> "¿Cuál de las 5 V's creen que es la más difícil de manejar? ¿Por qué?"
*(Respuesta esperada: Veracidad — los datos sucios son el mayor problema real)*

### Tema 2: Tipos de Datos (15 min)

**Clasificación con ejemplos reales**:

```
DATOS ESTRUCTURADOS
├── Bases de datos relacionales (SQL)
├── Hojas de cálculo Excel
└── Ejemplo: Tabla de ventas de una tienda retail

DATOS SEMI-ESTRUCTURADOS
├── JSON (respuestas de APIs)
├── XML
├── Logs de servidores
└── Ejemplo: Respuesta de la API de Reniec

DATOS NO ESTRUCTURADOS (80% de todos los datos del mundo)
├── Imágenes y videos
├── Emails y documentos
├── Audio
├── Posts de redes sociales
└── Ejemplo: Fotos de DNI, llamadas de call center de Claro
```

**Demo rápida en Colab** (5 min):
```python
import pandas as pd
import json

# Dato estructurado
df = pd.DataFrame({'cliente': ['Juan','Maria'], 'compra': [150, 320]})
print("ESTRUCTURADO:")
print(df)

# Dato semi-estructurado
dato_json = '{"cliente": "Juan", "compras": [150, 200, 320], "ciudad": "Lima"}'
dato = json.loads(dato_json)
print("\nSEMI-ESTRUCTURADO (JSON):")
print(dato)

# Dato no estructurado
print("\nNO ESTRUCTURADO: Una imagen satelital de Lima")
print("No podemos leerlo directamente — necesitamos procesamiento especial")
```

### Tema 3: Requisitos y Retos del Big Data (5 min)

**Los 5 grandes retos** (explica con casos):
1. **Almacenamiento**: No cabe en un solo servidor → solución: distribuir
2. **Procesamiento**: Un CPU no alcanza → solución: procesar en paralelo  
3. **Seguridad y privacidad**: GDPR, Ley 29733 de Perú
4. **Calidad de datos**: basura entra = basura sale
5. **Talento humano**: escasez de ingenieros de datos en Perú

### Tema 4: Arquitectura y Clusters (10 min)

**Arquitectura típica de un sistema Big Data**:

```
[FUENTES DE DATOS]          [INGESTA]           [ALMACENAMIENTO]
  └─ APIs                     └─ Kafka              └─ HDFS / S3
  └─ Bases de datos           └─ Flume              └─ Data Lake
  └─ Sensores IoT             └─ Sqoop              └─ Data Warehouse
  └─ Redes sociales
                          [PROCESAMIENTO]         [ANÁLISIS/VISUALIZACIÓN]
                            └─ MapReduce             └─ Tableau / Power BI
                            └─ Spark                 └─ Jupyter Notebooks
                            └─ Hive                  └─ Dashboards
```

**Memoria distribuida vs. compartida**:

| Tipo | Descripción | Cuándo usar |
|------|-------------|------------|
| **Memoria Compartida** | Múltiples CPUs comparten la misma RAM | 1 servidor potente (scale-up) |
| **Memoria Distribuida** | Cada nodo tiene su propia RAM, se comunican por red | Clúster de muchas máquinas baratas (scale-out) |

**La filosofía Hadoop**: "En lugar de mover datos al cómputo, mover el cómputo a los datos"

---

## BREAK (10 minutos)

---

## BLOQUE 2 — DEMO EN VIVO (50 minutos)

### Demo: Visualizar arquitecturas con Draw.io

**URL**: https://www.drawio.com/

**El docente diseña EN VIVO** una arquitectura de Big Data para el siguiente caso:

**Caso de negocio**: "Supermercados Wong quiere analizar en tiempo real qué productos se compran juntos para optimizar sus ofertas"

**Componentes a diagramar**:
1. Fuentes: POS (punto de venta), app móvil, cámara de seguridad
2. Ingesta: Apache Kafka
3. Almacenamiento: HDFS + MongoDB
4. Procesamiento: Apache Spark
5. Visualización: Dashboard Power BI
6. Acción: Sistema de recomendación en cajas self-checkout

**Mientras dibuja, preguntar**:
- "¿Qué pasa si el sistema de POS falla? ¿Perdemos datos?"
- "¿Dónde guardaríamos las imágenes de las cámaras?"
- "¿Qué tan rápido necesitamos el análisis? ¿Real-time o batch?"

---

## BLOQUE 3 — TRABAJO COLABORATIVO (30 minutos)

### Actividad: "Diseño de Ecosistema de Datos"

**Instrucción para grupos** (grupos de 3-4 personas):

> Seleccionen UNA empresa peruana o latinoamericana real. Diseñen una arquitectura de Big Data para resolver un problema específico de esa empresa. Deben identificar:
> 1. ¿Qué tipos de datos tienen? (estructurado, semi, no estructurado)
> 2. ¿Cuál es el volumen aproximado?
> 3. ¿Qué velocidad de procesamiento necesitan?
> 4. ¿Qué arquitectura proponen? (usar Draw.io)

**Empresas sugeridas** (una por grupo):
- Interbank / BCP / BBVA → fraud detection
- Claro Perú / Movistar → churn prediction
- InRetail (Plaza Vea, Oechsle) → recommendation engine
- MiBanco → credit scoring para microempresas
- EsSalud → predicción de enfermedades
- SUNAT → detección de evasión fiscal

**Al finalizar**: Cada grupo expone su diagrama en 3 minutos

---

## BLOQUE 4 — REVISIÓN DE PROYECTOS Y CIERRE (20 minutos)

### Formación de grupos de proyecto (10 min)
- Presentar los 10 proyectos innovadores del semestre
- Que cada grupo elija su proyecto
- Registrar en lista: Grupo → Integrantes → Proyecto elegido
- Crear repositorio en GitHub Classroom

### Cierre de sesión (10 min)
**Preguntas de metacognición**:
1. "¿Qué concepto de hoy te sorprendió más?"
2. "¿Cómo se conecta lo de hoy con tu trabajo actual?"
3. "¿Qué pregunta te queda sin responder?"

**Tarea para la semana 2**:
1. Completar la Guía de Trabajo S1 (preguntas teóricas)
2. Instalar Docker Desktop en su laptop
3. Crear cuenta en MongoDB Atlas y Databricks Community
4. Leer: Capítulos 1-2 del libro "Big Data: técnicas, herramientas y aplicaciones"
5. Avanzar en la descripción del problema de su proyecto (1 párrafo)

---

## PUNTOS CRÍTICOS PARA NO OLVIDAR

⚠️ **Errores comunes del docente en esta sesión**:
- Quedarse solo en teoría sin demo → siempre mostrar algo concreto funcionando
- No conectar con el mundo real de los estudiantes → siempre preguntar "¿en tu empresa...?"
- Asumir que todos saben Python → verificar el nivel del grupo en la apertura
- No dejar tiempo para preguntas → el cierre debe incluir espacio para dudas

✅ **Indicadores de éxito de la sesión**:
- Los estudiantes pueden nombrar las 5 V's con ejemplos propios
- Cada grupo tiene un diagrama de arquitectura básico hecho
- Todos los grupos tienen proyecto asignado y repo en GitHub
- Los estudiantes saben qué software instalar para la siguiente semana

---

## MATERIALES DE LA SESIÓN

| Material | Dónde está |
|---------|-----------|
| Slides S1 | /Semana_1/slides/ |
| Notebook demo | /Semana_1/notebooks/demo_s1_tipos_datos.ipynb |
| Template Draw.io | /Semana_1/recursos/arquitectura_template.drawio |
| Guía trabajo estudiante | /Semana_1/GUIA_TRABAJO_ESTUDIANTE_S1.md |
| Lab estudiante | /Semana_1/LABORATORIO_ESTUDIANTE_S1.md |

---

*Docente: revisar este material 24h antes de la clase*
