# S5 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 5: MapReduce + Apache Spark (Core, SQL, Streaming, GraphX)

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Sección** | ______________________________________________ |
| **Fecha** | ______________________________________________ |
| **Tiempo estimado** | 90 minutos |
| **Puntaje total** | 100 puntos |

---

### INSTRUCCIONES GENERALES

- Esta guía evalúa los temas de la Semana 5: MapReduce, Spark Core, Spark SQL, Structured Streaming y GraphX.
- Tiempo recomendado: 90 minutos.
- Las secciones van de menor a mayor dificultad — responde en orden.
- En preguntas abiertas: responde con oraciones completas y argumentos técnicos precisos.
- No hay respuestas en este documento.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts c/u)

*Marca con X la alternativa correcta. Solo una es válida.*

---

**1.** ¿Cuál es la principal limitación de MapReduce que motivó el desarrollo de Apache Spark?

a) MapReduce solo puede ejecutarse en clústeres con más de 100 nodos, lo que lo hace inaccesible para empresas pequeñas  
b) MapReduce escribe los resultados intermedios en disco entre cada etapa Map y Reduce, generando alta latencia especialmente en algoritmos iterativos  
c) MapReduce no puede procesar datos en formato JSON o Parquet, solo archivos de texto plano  
d) MapReduce no soporta el lenguaje Python, obligando a los desarrolladores a usar Java exclusivamente  

---

**2.** En la arquitectura de Apache Spark, ¿cuál es la función del componente llamado "Driver Program"?

a) Almacena los datos distribuidos en bloques de 128MB en los nodos del clúster  
b) Gestiona los recursos físicos del clúster (CPU, RAM) y asigna nodos a los trabajos  
c) Contiene el código del usuario, crea el SparkContext y el DAG de ejecución, y coordina los Executors  
d) Ejecuta las tareas individuales sobre particiones de datos en cada nodo Worker  

---

**3.** ¿Cuál es la diferencia entre una "Transformación" y una "Acción" en Apache Spark?

a) Las transformaciones escriben datos en disco y las acciones los leen; es la diferencia entre escritura y lectura  
b) Las transformaciones son operaciones lazy que definen el plan de ejecución pero no se ejecutan; las acciones disparan la ejecución del DAG y devuelven un resultado  
c) Las transformaciones solo aplican a RDDs de la primera versión de Spark; las acciones son exclusivas de DataFrames  
d) Las transformaciones usan Python y las acciones usan Scala; es una diferencia de lenguaje de programación  

---

**4.** Una empresa de e-commerce peruano tiene 500 millones de registros de navegación web en HDFS y necesita calcular las 20 páginas más visitadas del mes. ¿Cuál es la secuencia correcta de operaciones Spark?

a) `read → orderBy → groupBy → count → limit(20)`  
b) `read → filter → select → write → sort`  
c) `read → groupBy(url) → count() → orderBy(desc) → limit(20) → show()`  
d) `read → map → reduce → collect → sort`  

---

**5.** En Spark SQL, cuando se usa `createOrReplaceTempView("ventas")`, ¿qué se crea exactamente?

a) Una tabla permanente en el metastore de Hive que persiste después de cerrar la sesión  
b) Una copia de los datos en disco en formato Parquet para consultas posteriores  
c) Una vista temporal en memoria que permite consultar el DataFrame con sintaxis SQL estándar, disponible solo en la sesión actual  
d) Un índice distribuido sobre el DataFrame para acelerar consultas con filtros WHERE  

---

**6.** ¿Cuál es la desventaja principal de usar UDFs (User Defined Functions) en Python dentro de Spark comparado con las funciones nativas como `F.sum()` o `F.when()`?

a) Las UDFs no pueden recibir más de un argumento de entrada, limitando su utilidad  
b) Las UDFs rompen la ejecución vectorizada de Spark porque se ejecutan fila por fila en el proceso Python, impidiendo que el optimizador Catalyst las optimice  
c) Las UDFs solo funcionan con datos de tipo String y no soportan tipos numéricos o fechas  
d) Las UDFs requieren reiniciar el clúster Spark para que sean reconocidas por todos los Executors  

---

**7.** En Structured Streaming, ¿qué significa el output mode `complete`?

a) El stream ha terminado y no habrá más datos — es la señal de cierre del stream  
b) Solo las filas nuevas desde el último micro-batch se escriben al destino  
c) El resultado completo acumulado se re-escribe en cada trigger — usado cuando el resultado depende de todos los eventos históricos  
d) Todos los micro-batches se procesan en paralelo en lugar de secuencialmente  

---

**8.** Una startup fintech peruana necesita detectar transferencias sospechosas en tiempo real: específicamente, cuando una cuenta envía dinero a más de 5 cuentas diferentes en menos de 2 minutos. ¿Qué tecnología de Spark es más apropiada?

a) Spark SQL con una vista temporal — porque es la más sencilla de implementar y no requiere configuración adicional  
b) Spark Batch con Delta Lake — porque la persistencia de Delta Lake garantiza que no se pierdan transacciones  
c) Structured Streaming con ventanas de tiempo deslizantes — porque procesa cada transacción en tiempo real y puede acumular conteos por cuenta en ventanas de 2 minutos  
d) GraphX con PageRank — porque PageRank identifica las cuentas más centrales que son las más sospechosas  

---

**9.** En GraphX/GraphFrames, ¿para qué tipo de problema es más eficiente comparado con JOINs en SQL tradicional?

a) Para calcular totales y promedios sobre millones de registros — GraphX paraleliza la agregación mejor que GROUP BY  
b) Para detectar patrones de relaciones entre entidades a múltiples saltos (ej: ciclos A→B→C→A, amigos de amigos) — SQL requiere JOINs que crecen exponencialmente con la profundidad  
c) Para filtrar registros con condiciones complejas — GraphX puede aplicar múltiples filtros en una sola pasada  
d) Para ordenar globalmente grandes volúmenes de datos — el algoritmo de sort de GraphX supera al sort distribuido de SQL  

---

**10.** En el contexto de Big Data para una empresa peruana de 10 empleados con 50 GB de datos históricos de ventas en Excel, ¿cuál es la recomendación técnica correcta?

a) Implementar Apache Spark en AWS EMR inmediatamente — siempre es mejor usar tecnología de última generación  
b) Usar PostgreSQL o DuckDB en un servidor local — Spark agrega complejidad innecesaria cuando los datos caben en una sola máquina y el equipo es pequeño  
c) Usar HDFS + MapReduce — porque los datos de Excel necesitan el ecosistema Hadoop para ser procesados correctamente  
d) Implementar Structured Streaming — porque las ventas se generan continuamente y necesitan procesamiento en tiempo real  

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts c/u)

**11.** En Spark, la propiedad de evaluación ______________________ significa que las transformaciones no se ejecutan inmediatamente cuando son definidas, sino que Spark acumula el plan de ejecución hasta que se llama una _______________________, momento en el que ejecuta todo el DAG optimizado.

**12.** La abstracción más usada en Spark moderno es el ______________________, que organiza los datos en columnas nombradas con tipos definidos, permitiendo tanto la API de Python como el ______________________ para consultarlos — internamente Spark usa el optimizador ______________________ para generar el plan físico más eficiente.

**13.** En Structured Streaming, los datos de entrada se modelan como una tabla que crece infinitamente. Spark procesa los nuevos datos en intervalos llamados ______________________, y puede escribir el resultado en tres modos: `append` (solo filas nuevas), `update` (filas modificadas) y ______________________ (toda la tabla de resultados re-calculada).

**14.** GraphX y GraphFrames permiten representar relaciones entre entidades usando dos estructuras: los ______________________ (nodos) que representan las entidades (ej: cuentas bancarias), y las ______________________ (conexiones) que representan las relaciones (ej: transferencias entre cuentas).

**15.** La principal ventaja de Spark sobre MapReduce para algoritmos de Machine Learning iterativos es que Spark puede almacenar los datos intermedios en ______________________ usando el método `cache()` o `persist()`, evitando que cada iteración del algoritmo tenga que releer los datos desde ______________________.

---

### B2. Relacionar columnas (10 puntos | 1 pt c/par correcto)

Relaciona cada concepto/herramienta (Columna A) con su descripción correcta (Columna B):

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | `collect()` | | A | Operación Spark que agrupa filas con el mismo valor de una columna para aplicar agregaciones |
| 2 | `cache()` | | B | Convierte un DataFrame en una vista consultable con SQL estándar en la sesión actual |
| 3 | `groupBy()` | | C | Acción que trae todos los datos del clúster al Driver — peligroso con datos grandes |
| 4 | `createOrReplaceTempView()` | | D | Guarda el RDD/DataFrame en memoria para reutilizarlo sin recalcular |
| 5 | DAG | | E | Algoritmo de GraphX que asigna un puntaje de importancia a cada nodo del grafo |
| 6 | Catalyst Optimizer | | F | El plan de ejecución de Spark representado como un grafo dirigido sin ciclos |
| 7 | Structured Streaming | | G | Motor de Spark que transforma el código del usuario en el plan físico más eficiente |
| 8 | PageRank | | H | Procesamiento de datos continuos tratando el stream como una tabla que crece infinitamente |
| 9 | `withColumn()` | | I | Transformación que agrega o reemplaza una columna en un DataFrame |
| 10 | Executor | | J | Proceso en el nodo Worker que ejecuta tareas individuales sobre particiones de datos |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas. Extensión: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El equipo de Data Engineering del Banco Pichincha Perú tiene un pipeline que actualmente usa Hadoop MapReduce para calcular el riesgo crediticio de sus 800,000 clientes. El proceso toma 6 horas cada noche. El banco quiere reducirlo a menos de 1 hora.

a) ¿Por qué el algoritmo de riesgo crediticio se beneficiaría especialmente de migrar a Spark en comparación con un proceso de simple conteo de transacciones? Argumenta con el concepto de evaluación iterativa.

b) ¿Qué componente de Spark les recomendarías usar para el pipeline nocturno (batch) y cuál para alertas de crédito rechazado en tiempo real durante el día? Justifica.

---

**17. (8 puntos)** Compara el procesamiento batch con el procesamiento en streaming para el siguiente escenario: *Rappi Perú necesita mostrar a sus repartidores las zonas de alta demanda de pedidos en Lima en este momento.*

a) Si usaran batch procesando cada hora: ¿qué problema concreto enfrentaría el repartidor Carlos que está decidiendo hacia qué zona moverse a las 12:47 PM?

b) Si usaran Structured Streaming con ventanas de 5 minutos: ¿qué información recibiría Carlos y cómo cambia su decisión?

c) ¿Existe algún caso en el negocio de Rappi donde el batch sería suficiente y el streaming sería sobredimensionado? Justifica con un ejemplo concreto.

---

**18. (6 puntos) — Mini caso:** 

*La empresa "DataPyme" tiene el siguiente código PySpark:*

```python
df = spark.read.csv("/data/ventas.csv", header=True)
df_filtrado = df.filter(df.monto > 100)
df_agrupado = df_filtrado.groupBy("ciudad").count()
df_ordenado = df_agrupado.orderBy("count", ascending=False)
resultado = df_ordenado.collect()
```

a) Identifica cuáles de las líneas 2, 3, 4 y 5 son transformaciones y cuál es la acción. ¿Cuántas veces se leen los datos del CSV?

b) El CEO dice: "Quiero guardar `df_filtrado` porque lo uso 3 veces más adelante en el código." ¿Qué línea agregarías y por qué mejora el rendimiento?

---

**19. (8 puntos)** Explica el concepto de "ventana deslizante" (sliding window) en Structured Streaming y por qué es necesaria para detectar fraude en Yape. Luego, diferencia entre una ventana fija (tumbling window) de 10 minutos y una ventana deslizante de 10 minutos que avanza cada 2 minutos: ¿cuál detectaría antes una transacción fraudulenta que ocurre en el minuto 9? Justifica con un esquema o descripción temporal.

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional (15 puntos)**

*Eres el Lead Data Engineer de InRetail Perú (dueños de Plaza Vea, Oechsle, Promart, Mifarma). La empresa tiene:*

- *3.5 millones de tickets de venta diarios en 460 tiendas a nivel nacional*
- *Datos históricos de 5 años (18 TB) en HDFS en formato Parquet*
- *Sistema de alertas de desabastecimiento: si un producto baja de 50 unidades en una tienda, necesita una alerta en menos de 10 minutos*
- *El modelo de recomendación "Compraron también..." requiere re-entrenarse cada semana sobre los datos de los últimos 30 días*
- *El equipo analítico de 20 personas hace consultas ad-hoc diariamente sobre el historial*

Responde:

a) Para el análisis histórico de los 20 analistas (consultas SQL sobre 18 TB): ¿usarías Spark batch con `spark.sql()` o recomendarías Databricks SQL con Delta Lake? Justifica la diferencia y por qué una opción es mejor para este caso específico. (4 pts)

b) Para las alertas de desabastecimiento en < 10 minutos: diseña el pipeline de Structured Streaming. ¿Qué fuente de datos usarías (Kafka, archivos, rate)? ¿Qué tamaño de ventana? ¿Qué output mode? Justifica cada decisión. (5 pts)

c) Para el modelo de recomendaciones (re-entrenamiento semanal sobre 30 días de datos = ~3 TB): ¿qué ventaja tiene usar Spark MLlib sobre usar scikit-learn en un servidor normal? ¿Qué operación de Spark usarías para evitar leer 3 TB en cada iteración del algoritmo? (3 pts)

d) Un analista junior propone: "En lugar de Spark, usemos pandas en Python — es más fácil y el resultado es el mismo." Refuta este argumento con 3 limitaciones técnicas concretas de pandas para el caso InRetail. (3 pts)

---

**21. Pregunta de diseño (8 puntos)**

*"Diseña el pipeline completo de Spark para el sistema de detección de fraude de Izipay (procesadora de pagos con tarjeta en Perú): 800,000 transacciones diarias, necesita detectar tarjetas clonadas (misma tarjeta usada en dos ciudades diferentes en menos de 30 minutos) y alertar en tiempo real."*

Diseña:
- La fuente de datos del stream y por qué (Kafka, archivos, base de datos)
- La lógica de la ventana temporal (tipo, tamaño, avance)
- Las transformaciones Spark necesarias
- El criterio de detección (cuándo se dispara la alerta)
- El destino del output (dónde va la alerta)
- Por qué GraphFrames o Structured Streaming es más apropiado para este caso específico

---

**22. Pensamiento crítico (7 puntos)**

*"En 2025, empresas como Databricks y Snowflake compiten directamente con Spark nativo. Databricks construyó el Photon Engine que es 5x más rápido que Spark estándar. ¿Significa esto que Apache Spark (open source) quedará obsoleto en los próximos años? ¿O hay razones técnicas y económicas para que coexistan?"*

Analiza:
- ¿Qué ofrece Databricks/Snowflake que Spark open source no tiene?
- ¿Para qué casos una empresa peruana medianas (200 empleados) elegiría Spark open source en lugar de Databricks?
- ¿Cuál es el riesgo de depender completamente de un proveedor como Databricks para toda la infraestructura de datos?
- ¿Cómo se relaciona este debate con el concepto de vendor lock-in?

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 5 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
