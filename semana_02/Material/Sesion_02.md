# S2 — SESIÓN COMPLETA: COMPUTACIÓN EN LA NUBE PARA BIG DATA
## Universidad Autónoma del Perú | Curso: Big Data DD283 | 2026-1

---

| Campo | Detalle |
|-------|---------|
| **Curso** | Big Data DD283 |
| **Semana** | 2 |
| **Tema** | Computación en la Nube para Big Data: Virtualización, Clústeres, Hadoop, HDFS, MapReduce, HBase |
| **Logro de aprendizaje** | El estudiante describe una propuesta de arquitectura Big Data para la nube y procesa un archivo distribuido usando Hadoop con integridad |
| **Duración** | 3 horas (180 min) + 20 min receso |
| **Herramienta principal** | Databricks Community Edition (gratuito) + Google Colab |
| **Valor** | Integridad en el uso transparente de recursos de almacenamiento compartido |

---

## TABLA DE CONTENIDOS

1. [Cronograma de la sesión](#cronograma)
2. [Bloque 1 — Inicio y Utilidad](#bloque-1)
3. [Bloque 2 — Transformación](#bloque-2)
4. [Receso](#receso)
5. [Bloque 3 — Práctica y Cierre](#bloque-3)
6. [Guion verbal sugerido](#guion)
7. [Casos reales recomendados](#casos-reales)
8. [Evaluación formativa](#evaluacion)
9. [Stack tecnológico gratuito](#stack-gratuito)
10. [Referencias APA 7](#referencias)

---

## CRONOGRAMA DE LA SESIÓN {#cronograma}

| Bloque | Actividad | Duración | Responsable |
|--------|-----------|----------|-------------|
| **Bloque 1** | INICIO: Rompe-hielo + Logro + Revisión S1 + Diagnóstico | 20 min | Docente |
| **Bloque 1** | UTILIDAD: ¿Por qué cloud + Hadoop hoy? | 10 min | Docente |
| **Bloque 2** | TRANSFORMACIÓN: Virtualización → Clústeres → HDFS → MapReduce → HBase | 70 min | Docente + Estudiantes |
| **RECESO** | Descanso | 20 min | — |
| **Bloque 3** | PRÁCTICA: Caso grupal + Ejercicio individual | 40 min | Estudiantes |
| **Bloque 3** | CIERRE: Síntesis + Metacognición + Tarea | 10 min | Docente + Estudiantes |

---

## BLOQUE 1 — INICIO (20 min) {#bloque-1}

### 1. ROMPE-HIELO (5 min)

**Dinámica: "¿Cuánto pesa tu vida digital?"**



---

### 2. LOGRO DE APRENDIZAJE (3 min)

> **Guion verbal textual:**
>
> *"El logro de hoy tiene dos partes muy concretas. Primera: que al terminar esta sesión puedan describir una arquitectura Big Data en la nube — con nombres, componentes y justificación. No solo decir 'uso Hadoop', sino explicar POR QUÉ y CÓMO se conectan las piezas.*
>
> *Segunda: que procesen un archivo distribuido usando el ecosistema Hadoop. Eso significa que van a correr código real en Databricks —que ya está en sus pantallas— y van a ver datos moviéndose entre nodos como lo haría Netflix o el Banco de la Nación.*
>
> *Al final de la clase, si alguien les pregunta en una entrevista: '¿Sabes Big Data?', van a poder decir: 'Sí, diseñé una arquitectura y procesé datos con Hadoop en la nube'. Eso es lo que construimos hoy."*

---

### 3. REVISIÓN SESIÓN ANTERIOR (7 min)

**Pregunta 1:**
> *"La semana pasada definimos las 5 V's del Big Data. ¿Quién me da un ejemplo REAL de empresa donde se vean las 5 V's juntas?"*

**Respuesta esperada detallada:**
Un estudiante que entendió bien debería mencionar una empresa como Uber o una red social, y explicar: **Volumen** (millones de viajes por día), **Velocidad** (precio dinámico calculado en milisegundos), **Variedad** (GPS, pagos, calificaciones, mensajes), **Veracidad** (señales GPS perdidas o falsas) y **Valor** (previsión de demanda, optimización de conductores). Si el estudiante solo menciona una o dos V's, pedir que piense en las otras: *"Bien, ya tienes Volumen y Velocidad. ¿Cómo encaja la Variedad en Uber?"*

**Si responde mal:** *"Interesante. Analicemos juntos — ¿qué tipos de datos genera Uber por minuto? GPS, pagos, chats... eso ya nos da Variedad. ¿Qué más?"*

---

**Pregunta 2:**
> *"¿Cuál es la diferencia entre datos estructurados, semiestructurados y no estructurados? Den un ejemplo de cada uno que pueda existir en un hospital peruano."*

**Respuesta esperada detallada:**
- **Estructurados:** datos en tablas relacionales con esquema fijo. Ejemplo hospital: tabla de pacientes (ID, nombre, fecha nacimiento, DNI) en Oracle o SQL Server.
- **Semiestructurados:** tienen estructura pero flexible, sin esquema fijo obligatorio. Ejemplo: archivo JSON de un diagnóstico de laboratorio donde algunos campos son opcionales.
- **No estructurados:** sin esquema, difíciles de analizar con SQL. Ejemplo: imágenes de rayos X, audios de consultas médicas, videos de endoscopías, notas de enfermería escritas a mano y escaneadas.

**Si responde mal:** *"Pensemos en una historia clínica digital. ¿Qué parte puede buscarse fácilmente con un SELECT de SQL? Esa parte es estructurada. ¿Qué parte no?"*

---

**Pregunta 3:**
> *"¿Qué es un pipeline de datos y por qué es importante que sea automatizado en Big Data?"*

**Respuesta esperada detallada:**
Un pipeline de datos es una secuencia automatizada de etapas que transforma datos desde su fuente original hasta un destino de análisis: ingesta → limpieza → transformación → carga → análisis. Es crítico que sea automatizado porque en Big Data los volúmenes son imposibles de procesar manualmente (millones de registros por hora), los datos llegan continuamente (streaming), y cualquier fallo manual en el procesamiento compromete la integridad del análisis. Ejemplos: el pipeline ETL que procesa transacciones bancarias en tiempo real para detectar fraudes no puede depender de que alguien ejecute scripts manualmente a las 3 AM.

**Si responde mal:** *"Piensen en una fábrica de autos. ¿Qué pasaría si cada operario decidiera de forma manual cuándo pasar la pieza al siguiente? El pipeline es la línea de ensamblaje, pero para datos."*

---

### 4. DIAGNÓSTICO INICIAL (5 min)

> *"Antes de continuar, necesito saber desde dónde partimos hoy. Levanten la mano si han escuchado la palabra 'virtualización' antes de esta clase. Bien. Ahora levanten la mano si pueden explicarla. Perfecto — eso me dice dónde empezamos."*

**Pregunta diagnóstica 1:**
> *"¿Qué entienden por 'nube' en tecnología? ¿Es un servidor físico en el cielo? ¿De quién es ese hardware?"*

**Respuesta esperada:** La nube es una infraestructura de servidores físicos ubicados en centros de datos de empresas como Amazon (AWS), Google (GCP) o Microsoft (Azure), que se ofrece como servicio a través de internet. El usuario no ve ni toca el hardware — solo paga por el uso. No es literalmente el cielo; es un edificio lleno de servidores con refrigeración industrial en Iowa, São Paulo o Singapur.

---

**Pregunta diagnóstica 2:**
> *"¿Alguien sabe qué es un clúster en computación? ¿Lo han visto en algún contexto?"*

**Respuesta esperada:** Un clúster es un conjunto de computadoras (nodos) interconectadas que trabajan juntas como si fueran una sola máquina más potente. Se usa para distribuir carga de procesamiento. Pueden haberlo visto en videojuegos (servidores de juego en clúster), en universidades (clúster de cómputo científico) o en empresas (clúster de base de datos).

---

**Pregunta diagnóstica 3:**
> *"¿Han escuchado 'Hadoop' o 'MapReduce'? ¿Qué imagen les viene a la mente?"*

**Respuesta esperada:** Cualquier respuesta es válida aquí (es diagnóstico). Lo importante es registrar el punto de partida. Algunos dirán "Facebook lo usa", otros "es un framework de Java", otros no sabrán nada. Esto determina la velocidad de la Transformación.

---

## UTILIDAD (10 min)

### ¿Por qué este tema importa ahora mismo?

**Dato real:** En 2025, el 94% de las empresas del Fortune 500 usa alguna forma de computación en la nube para procesar datos (Gartner, 2024). En Perú, el BCP, Interbank, Claro, Telefónica y el propio gobierno (RENIEC, SUNAT) procesan millones de registros diarios usando tecnologías que vamos a ver hoy.

**El problema concreto que resuelve:**

Imaginen que son el equipo de datos de SUNAT. Cada año, al 31 de marzo, millones de peruanos presentan su declaración de renta. ¿Cómo procesan 3 millones de declaraciones en 72 horas para detectar inconsistencias y generar cartas de cobranza? No pueden comprar 3 millones de computadoras. Necesitan distribuir ese procesamiento en cientos de máquinas trabajando en paralelo — eso es exactamente para lo que nació Hadoop.

**Aplicación real hoy:**

| Empresa | Uso de Hadoop/Cloud | Escala |
|---------|---------------------|--------|
| Netflix | Análisis de comportamiento de 280M usuarios para recomendaciones | 500 TB de datos nuevos/día |
| Spotify | Procesamiento de streams para Discover Weekly | 100M canciones analizadas/semana |
| Yape (BCP) | Detección de fraudes en tiempo real en transacciones | 5M transacciones/día en Perú |
| MINSA Perú | Vigilancia epidemiológica COVID-19 | Datos de 33 regiones en tiempo real |

**Pregunta retadora de apertura:**

> *"Si un banco tiene 10 millones de transacciones del día de ayer en un archivo de 500 GB, y necesita encontrar todas las transacciones sospechosas en menos de 1 hora, ¿cuántas computadoras de escritorio normales necesitarían? ¿O existe una mejor forma?"*

**Respuesta esperada:** Una computadora normal procesa esos 500 GB en aproximadamente 6-8 horas (sin optimización). Si dividen el archivo en 100 partes iguales de 5 GB y las procesan en paralelo en 100 máquinas, el tiempo teórico baja a 4-5 minutos. Eso es el principio de Hadoop: divide el problema, distribúyelo, junta los resultados. La "mejor forma" no es una supercomputadora cara — es cientos de máquinas baratas trabajando juntas.

---

## BLOQUE 2 — TRANSFORMACIÓN (70 min) {#bloque-2}

---

### SUBTEMA 1: VIRTUALIZACIÓN — EL FUNDAMENTO DE LA NUBE (12 min)

#### Explicación conceptual

**Virtualización** es la tecnología que permite ejecutar múltiples sistemas operativos independientes (llamados **máquinas virtuales** o VMs) sobre un único servidor físico, compartiendo sus recursos de hardware (CPU, RAM, disco) mediante una capa de software llamada **hipervisor**.

```
SERVIDOR FÍSICO (32 cores, 256 GB RAM, 10 TB disco)
┌─────────────────────────────────────────────────────┐
│                   HIPERVISOR                        │
│  (VMware ESXi / KVM / Hyper-V / Xen)               │
├─────────────┬─────────────┬─────────────────────────┤
│   VM #1     │   VM #2     │        VM #3            │
│ Ubuntu 22   │ Windows     │     CentOS              │
│ 4 cores     │ 8 cores     │     20 cores            │
│ 32 GB RAM   │ 64 GB RAM   │     160 GB RAM          │
│ Hadoop Node │ App Server  │     Database Server     │
└─────────────┴─────────────┴─────────────────────────┘
```

**Tipos de virtualización:**

| Tipo | Qué virtualiza | Ejemplo de uso | Herramienta |
|------|---------------|----------------|-------------|
| **Full virtualization** | Hardware completo | Correr Windows dentro de Linux | VirtualBox, VMware |
| **Paravirtualización** | Hardware modificado, mejor rendimiento | Servidores de producción | Xen, KVM |
| **Contenedores** | Solo el sistema operativo (no hardware) | Microservicios, Spark workers | Docker, Podman |
| **Virtualización de red** | Redes lógicas sobre infraestructura física | VPCs en AWS, clústeres Hadoop aislados | VMware NSX |

#### Ejemplo real

AWS EC2 (Elastic Compute Cloud) es el servicio de virtualización más grande del mundo. Cuando una startup peruana contrata un servidor en AWS, en realidad está arrendando una VM que corre en un servidor físico en São Paulo compartido con decenas de otras empresas. AWS cobra por segundo de uso. Netflix, Airbnb y Rappi nacieron sobre VMs de AWS sin comprar un solo servidor propio.

#### Pregunta al grupo #1

> *"¿Por qué creen que Amazon, Google y Microsoft invierten miles de millones en construir data centers propios, en lugar de vender el hardware directamente a las empresas?"*

**Respuesta esperada detallada:** El modelo de negocio de la nube es superior al de venta de hardware porque: (1) las empresas prefieren gasto operativo (pagar mensual) vs. gasto de capital (comprar hardware); (2) el proveedor puede hacer economía de escala: 1,000 empresas que no usan el 100% de sus VMs comparten el mismo servidor físico; (3) el proveedor ofrece valor agregado (backups automáticos, escalado, seguridad) que ninguna empresa mediocre puede implementar sola; (4) ingresos recurrentes y predecibles. AWS genera más de $90 mil millones al año solo con este modelo.

#### Mini actividad (3 min)

> *"En parejas: dibujen en papel el esquema de un servidor físico virtualizado que aloja 3 VMs — una para un clúster Hadoop, una para una base de datos, una para la aplicación web. Cada VM debe tener asignado cuántos cores, RAM y disco. El total no puede superar los recursos del servidor: 16 cores, 64 GB RAM, 2 TB disco. Tienen 2 minutos."*

---

### SUBTEMA 2: GESTIÓN DE CLÚSTERES — ORCHESTRAR LA POTENCIA DISTRIBUIDA (12 min)

#### Explicación conceptual

Un **clúster** para Big Data es un conjunto de nodos (máquinas físicas o virtuales) interconectados, donde cada nodo tiene un rol específico en el procesamiento distribuido. La **gestión de clústeres** es el proceso de asignar recursos, monitorear nodos, recuperarse de fallos y escalar la capacidad.

**Arquitectura típica de un clúster Hadoop:**

```
                    ┌─────────────────────┐
                    │   NODO MAESTRO       │
                    │  (Master/NameNode)   │
                    │  - Coordina todo     │
                    │  - No procesa datos  │
                    │  - Mantiene el índice│
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
  │  NODO TRABAJADOR │ │  NODO TRABAJADOR │ │  NODO TRABAJADOR │
  │  (DataNode #1)  │ │  (DataNode #2)  │ │  (DataNode #3)  │
  │  Almacena datos │ │  Almacena datos │ │  Almacena datos │
  │  Procesa locales│ │  Procesa locales│ │  Procesa locales│
  └─────────────────┘ └─────────────────┘ └─────────────────┘
```

**Herramientas de gestión de clústeres:**

| Herramienta | Función | Uso en Big Data |
|-------------|---------|-----------------|
| **YARN** (Apache) | Gestiona recursos dentro del clúster Hadoop | Asigna CPU/RAM a cada job MapReduce/Spark |
| **Kubernetes** | Orquestación de contenedores a escala | Desplegar Spark en la nube |
| **Apache Mesos** | Sistema operativo distribuido | Twitter, Airbnb usaron esto |
| **Databricks Runtime** | Gestión automática de clúster Spark | Lo que usamos hoy en clase |

#### Concepto crítico: Tolerancia a fallos

**¿Qué pasa si un nodo muere en el clúster?**

En un sistema tradicional (base de datos en un solo servidor): **DESASTRE** — el sistema cae completo.

En Hadoop: **NADA visible para el usuario** — el nodo maestro detecta que un DataNode no responde en 10 segundos, redirige el trabajo a los otros nodos, y los datos están replicados (3 copias por defecto), así que no se pierde nada.

#### Pregunta al grupo #2

> *"Si tienen un clúster de 10 nodos y el nodo maestro (NameNode) falla, ¿qué pasa con el sistema? ¿Y si falla uno de los 9 DataNodes?"*

**Respuesta esperada detallada:** 
- Si falla el **NameNode** (maestro): el clúster completo queda inaccesible porque el NameNode es quien tiene el mapa de dónde están todos los datos — es el índice central. Por eso Hadoop tiene **NameNode secundario** y configuraciones de **Alta Disponibilidad (HA)** con dos NameNodes (activo/standby). Este es el famoso "Single Point of Failure" de Hadoop 1.x que se corrigió en Hadoop 2.x.
- Si falla un **DataNode**: absolutamente nada desde el punto de vista del usuario. Los datos estaban replicados (factor 3 por defecto), así que los otros nodos tienen copias. YARN reasigna el trabajo del nodo caído a otros nodos disponibles. El NameNode marca ese nodo como inactivo y empieza a re-replicar los bloques que solo tiene ese nodo para volver al factor de replicación 3.

**Concepto que el docente debe enfatizar:** "**Diseñar para el fallo**" — en Big Data no se asume que las máquinas son confiables. Se diseña el sistema para que los fallos sean invisibles. Esto cambia completamente la mentalidad de arquitectura.

#### Mini actividad (2 min)

> *"¿Cuántos nodos mínimos necesitarían para que un clúster sea tolerante a fallos si el factor de replicación es 3? Justifiquen en una oración."*

**Respuesta:** Mínimo 3 DataNodes. Si tienes solo 2 y uno falla, el bloque replicado 3 veces ya no tiene 3 copias. Con 3 nodos y factor 3, cada bloque está en los 3 nodos, así que si uno cae, todavía hay 2 copias en los otros 2 nodos.

---

### SUBTEMA 3: COMPUTACIÓN EN LA NIEBLA (FOG COMPUTING) (8 min)

#### Explicación conceptual

**Fog Computing** (computación en la niebla) es una arquitectura que procesa los datos **en el borde de la red** — en dispositivos cercanos a donde se generan los datos — en lugar de enviarlos todos a un data center centralizado en la nube.

```
ARQUITECTURA CLOUD vs FOG vs EDGE

CLOUD (clásico):
  Sensor → → → → → → → → → → → → Data Center → Respuesta (latencia: 200-500ms)

FOG COMPUTING:
  Sensor → → Nodo Fog (gateway local) → Procesa localmente
                    ↓ (solo resumen)
              Data Center Central (latencia: 5-20ms local)

EDGE COMPUTING (extremo):
  Sensor ← → Proceso en el propio dispositivo (latencia: < 1ms)
```

**¿Cuándo usar Fog y no Cloud puro?**

| Escenario | ¿Por qué Fog? |
|-----------|--------------|
| Semáforos inteligentes en Lima | No puedes esperar 500ms para cambiar el semáforo |
| Sensores de calidad de aire (Grupo 4 del curso) | Datos cada segundo, si mandas todo a la nube: colapso de red |
| Cámara de seguridad con detección de personas | El análisis de video ocurre localmente, solo alertas van a la nube |
| Vehículos autónomos | Una decisión de freno no puede esperar respuesta de un servidor en São Paulo |

#### Ejemplo real peruano

El **COES (Comité de Operación Económica del Sistema)** que regula la red eléctrica peruana usa sensores distribuidos en todo el país que procesan datos localmente (fog) antes de enviar resúmenes al centro de control en Lima. Si esperaran que todos los datos viajen a Lima antes de tomar decisiones, el tiempo de reacción ante una falla sería inaceptable.

#### Pregunta al grupo #3

> *"En el proyecto del Grupo 4 (sensores de calidad del aire en Lima), ¿usarían Cloud puro o Fog Computing? ¿Por qué? ¿Qué procesarían en el fog y qué enviarían a la nube?"*

**Respuesta esperada detallada:** Deberían usar **Fog Computing**. En el nodo fog (el gateway del sensor en cada parque o esquina): calcular el promedio de los últimos 5 minutos de PM2.5, detectar si supera el umbral de alerta, generar la alerta local y activar la señal visual del semáforo ambiental. A la nube enviarían: los promedios por hora, las alertas generadas, y los datos históricos para análisis de tendencias. Enviar cada lectura raw (1 lectura/segundo × 150 sensores = 150 registros/segundo, 13 millones al día) a la nube sería costoso e innecesario si el procesamiento local es suficiente para las decisiones en tiempo real.

---

### SUBTEMA 4: HADOOP — EL ECOSISTEMA BIG DATA (20 min)

#### Origen histórico (dato que engancha)

> *"Hadoop nació de un problema de Google. En 2003, Google publicó un paper sobre cómo almacenaban archivos en miles de servidores (Google File System). En 2004, publicaron otro sobre cómo los procesaban (MapReduce). Un ingeniero de Yahoo! llamado Doug Cutting leyó esos papers y dijo: 'Voy a construir una versión open source de esto.' Lo llamó Hadoop — el nombre de juguete de su hijo. Hoy Hadoop es usado por empresas que Google mismo usa como competencia."*

#### Componentes del ecosistema Hadoop

```
┌─────────────────────────────────────────────────────────────────┐
│                    ECOSISTEMA HADOOP                             │
├─────────────────────────────────────────────────────────────────┤
│  ANÁLISIS Y ACCESO                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │  Hive    │ │   Pig    │ │  Spark   │ │ Impala   │           │
│  │ (SQL)    │ │(Script)  │ │(In-Memory│ │ (Fast SQL│           │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘           │
│       └────────────┴────────────┴────────────┘                  │
│                              │                                  │
│  PROCESAMIENTO               │                                  │
│  ┌───────────────────────────▼──────────────────────────────┐   │
│  │              MAPREDUCE / YARN                            │   │
│  │  (El motor que distribuye y ejecuta los trabajos)        │   │
│  └───────────────────────────┬──────────────────────────────┘   │
│                              │                                  │
│  ALMACENAMIENTO              │                                  │
│  ┌───────────────────────────▼──────────────────────────────┐   │
│  │                     HDFS                                 │   │
│  │        (Hadoop Distributed File System)                  │   │
│  │   Bloques de 128 MB | Replicación x3 | Tolerante fallos  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SERVICIOS ADICIONALES                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ZooKeeper │ │  HBase   │ │  Kafka   │ │  Sqoop   │           │
│  │(Coordin.)│ │(NoSQL)   │ │(Streaming│ │(DB→HDFS) │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

#### HDFS — Hadoop Distributed File System

**Concepto clave: los bloques**

Cuando subes un archivo de 500 MB a HDFS con tamaño de bloque predeterminado de 128 MB:

```
Archivo: ventas_2025.csv (500 MB)

HDFS lo divide en:
  Bloque 1: 128 MB → guardado en DataNode 1, 2, 3 (3 copias)
  Bloque 2: 128 MB → guardado en DataNode 2, 4, 5 (3 copias)
  Bloque 3: 128 MB → guardado en DataNode 1, 3, 5 (3 copias)
  Bloque 4: 116 MB → guardado en DataNode 2, 3, 4 (3 copias)

NameNode guarda el mapa: "ventas_2025.csv = Bloques 1,2,3,4 en estos nodos"
```

**Pregunta al grupo #4:**

> *"¿Por qué HDFS usa bloques grandes (128 MB) en lugar de bloques pequeños como los sistemas de archivos normales (4 KB)? ¿Qué ventaja y qué desventaja tiene?"*

**Respuesta esperada detallada:**
- **Ventaja de bloques grandes:** Reduce el número de entradas en el NameNode (índice). Si el bloque fuera 4 KB, un archivo de 500 MB tendría 125,000 entradas en el índice — el NameNode (que guarda todo en RAM) se saturaría rápidamente. Con bloques de 128 MB, el mismo archivo tiene solo 4 entradas. Además, bloques grandes reducen el overhead de red al trasladar datos.
- **Desventaja de bloques grandes:** Para archivos muy pequeños (< 128 MB, como logs de 1 MB), cada archivo igual ocupa una entrada en el NameNode Y el DataNode guarda el bloque casi vacío — se desperdicia espacio de metadatos. Por eso el "problema de los archivos pequeños" en HDFS es real y conocido. La solución es empaquetar muchos archivos pequeños en un HAR (Hadoop Archive) o SequenceFile.

---

#### MapReduce — El Modelo de Procesamiento

**MapReduce** es un modelo de programación que divide el procesamiento en dos fases:
- **MAP**: cada nodo procesa su porción local de datos y emite pares `(clave, valor)`
- **REDUCE**: se agrupan todos los pares con la misma clave y se aplica una función de agregación

**Ejemplo clásico en código Python (PySpark compatible):**

```python
# PROBLEMA: contar cuántas transacciones hubo por tipo en un archivo de 1 TB

# Fase MAP: cada DataNode procesa SU bloque local
# Input: líneas del CSV
# Output: (tipo_transaccion, 1) por cada línea

def mapper(linea):
    """
    Recibe una línea del CSV y emite (tipo, 1)
    Esto corre EN PARALELO en cada DataNode con SU porción del archivo
    """
    campos = linea.split(',')
    tipo_transaccion = campos[2]  # columna 3: "compra", "retiro", "transferencia"
    return (tipo_transaccion, 1)

# Ejemplo de output del mapper (cada DataNode emite esto para sus líneas):
# ("compra", 1)
# ("retiro", 1)
# ("compra", 1)
# ("transferencia", 1)
# ...

# SHUFFLE & SORT (automático en Hadoop/Spark):
# Hadoop agrupa todos los pares por clave:
# ("compra", [1, 1, 1, 1, ...])
# ("retiro", [1, 1, 1, ...])
# ("transferencia", [1, 1, ...])

# Fase REDUCE: un reducer por clave, suma los valores
def reducer(clave, lista_valores):
    """
    Recibe una clave y todos sus valores, los agrega
    """
    return (clave, sum(lista_valores))

# Output final:
# ("compra", 50000)
# ("retiro", 30000)
# ("transferencia", 20000)
```

**El mismo ejemplo en PySpark (lo que usamos en Databricks):**

```python
from pyspark.sql import SparkSession

# Iniciar sesión Spark (ya disponible en Databricks como 'spark')
spark = SparkSession.builder.appName("ContarTransacciones").getOrCreate()

# Leer archivo desde HDFS o S3 o DBFS (Databricks File System)
df = spark.read.csv("/FileStore/tables/transacciones.csv", 
                    header=True, 
                    inferSchema=True)

# MAP equivalente: seleccionar la columna tipo
# REDUCE equivalente: groupBy + count()
resultado = df.groupBy("tipo_transaccion").count()

# Spark internamente distribuye esto en todos los nodos del clúster
resultado.show()

# Output esperado:
# +-------------------+-------+
# |tipo_transaccion   | count |
# +-------------------+-------+
# |compra             | 50000 |
# |retiro             | 30000 |
# |transferencia      | 20000 |
# +-------------------+-------+
```

**Pregunta al grupo #5:**

> *"En el ejemplo de MapReduce de contar transacciones, ¿qué ventaja tiene procesar en paralelo en 100 DataNodes versus en 1 computadora? ¿La respuesta es 100 veces más rápida? Justifiquen."*

**Respuesta esperada detallada:** La aceleración teórica sería 100x, pero en la práctica es menor porque: (1) existe overhead de red para el paso **Shuffle & Sort** donde Hadoop mueve los pares clave-valor entre nodos para agruparlos — esto toma tiempo; (2) el NameNode tiene que coordinar todos los nodos; (3) si los datos no están distribuidos uniformemente (un DataNode tiene 80% del archivo), ese nodo se convierte en cuello de botella. En la práctica, el speedup para 100 nodos suele ser 60-80x, que de todas formas es extraordinario. Para un archivo de 1 TB que tarda 10 horas en una sola máquina, con 100 nodos puede tardar 8-10 minutos.

---

#### HBase — La Base de Datos NoSQL sobre HDFS

**HBase** es una base de datos NoSQL distribuida construida sobre HDFS, modelada sobre Google Bigtable. Es ideal para acceso aleatorio y en tiempo real a grandes volúmenes de datos.

**Diferencia fundamental:**

| Característica | HDFS | HBase |
|----------------|------|-------|
| **Tipo de acceso** | Secuencial (lee todo el archivo) | Aleatorio (busca una fila específica) |
| **Latencia** | Alta (segundos o minutos) | Baja (milisegundos) |
| **Escritura** | Append-only (solo agregar al final) | Lectura/Escritura/Actualización |
| **Uso típico** | Análisis batch (reportes, ML) | Aplicaciones en tiempo real |
| **Ejemplo** | Procesar logs de todo el mes | Buscar el saldo de un cliente |

**Modelo de datos HBase:**

```
TABLA: clientes_transacciones

Row Key: "1234567890" (DNI del cliente)
─────────────────────────────────────────────────────────────────────
Column Family: "info_personal"     Column Family: "transacciones"
  nombre: "García López Ana"         2025-01-15T10:23: "retiro:500"
  email:  "ana@email.com"            2025-01-15T11:45: "compra:150"
  zona:   "Lima"                     2025-01-16T09:00: "deposito:2000"
─────────────────────────────────────────────────────────────────────
```

**¿Por qué Row Key es crítico en HBase?**

> *"Si buscas las transacciones de un cliente por DNI, el Row Key debe ser el DNI. Si lo buscas por fecha, el Row Key debe incluir la fecha. HBase no tiene índices secundarios como SQL — el Row Key ES el índice. Diseñar mal el Row Key = sistema lento."*

**Pregunta al grupo #6:**

> *"El Banco Falabella tiene 5 millones de clientes. ¿Usarías HDFS puro o HBase para el sistema que muestra el saldo de un cliente cuando hace login en la app? ¿Por qué?"*

**Respuesta esperada detallada:** **HBase**. Cuando un cliente hace login, el sistema necesita buscar UN cliente específico (por DNI o ID) y devolverle su saldo en menos de 200 milisegundos — o la app se percibe lenta y el cliente cierra sesión. HDFS no puede hacer eso: para encontrar un registro específico, tendría que leer todo el archivo secuencialmente (minutos). HBase, con su Row Key indexado, localiza el registro en milisegundos incluso con 5 millones de filas. HDFS se usaría para los reportes nocturnos: "dame todas las transacciones del mes de todos los clientes para calcular el estado de cuenta".

---

#### Error común #1: Confundir Hadoop con Spark

> *"Muchos estudiantes y hasta profesionales dicen 'uso Hadoop' cuando en realidad usan Spark. Vamos a clarificar:"*

| Aspecto | Hadoop MapReduce | Apache Spark |
|---------|-----------------|--------------|
| **Velocidad** | Lento (lee/escribe en disco en cada paso) | 100x más rápido (procesa en RAM) |
| **Programación** | Java verboso (200 líneas para contar palabras) | Python/Scala conciso (5 líneas) |
| **Streaming** | No soportado nativamente | Spark Streaming integrado |
| **ML** | Mahout (poco usado) | MLlib (muy popular) |
| **¿Quién lo usa hoy?** | Legado (pocos nuevos proyectos) | Netflix, Uber, Databricks, todos |
| **¿Por qué aprenderlo?** | Los conceptos (HDFS, YARN) siguen vigentes | El lenguaje de implementación moderno |

**La metáfora:**
> *"Hadoop MapReduce es como un camión que va al almacén, carga mercancía, va al destino, descarga, regresa al almacén... en cada etapa. Spark es como un camión que carga TODO de una vez en la RAM y no vuelve al almacén hasta terminar. Si el almacén es el disco y el destino es el resultado, ¿cuál es más rápido?"*

**Pregunta al grupo #7:**

> *"Si Spark es 100x más rápido que Hadoop MapReduce, ¿por qué las empresas todavía tienen HDFS? ¿Por qué no lo reemplazaron completamente con S3 o Google Cloud Storage?"*

**Respuesta esperada detallada:** HDFS sigue vigente porque: (1) **Localidad de datos** — en Hadoop, el procesamiento va DONDE están los datos (el DataNode también tiene Spark worker), eliminando transferencia de red. En S3/GCS, los datos y el cómputo están separados, generando tráfico de red (aunque la tendencia actual es separar storage de cómputo). (2) **Inversión existente** — las empresas tienen petabytes en HDFS y migrar cuesta millones. (3) **Integración del ecosistema** — HBase, Hive, Pig están diseñados sobre HDFS. (4) **Costo** — HDFS en hardware propio puede ser más barato que S3 a escala masiva (petabytes). La tendencia moderna (2023-2025) es **Data Lakehouse** (Delta Lake, Apache Iceberg) que combina lo mejor de ambos mundos.

---

### SUBTEMA 5: ARQUITECTURAS CLOUD PARA BIG DATA (8 min)

#### Los 3 modelos de servicio cloud para Big Data

```
IaaS (Infrastructure as a Service)
  → Te doy servidores virtuales. Tú instalas Hadoop.
  → Ejemplo: AWS EC2 + instalar HDP manualmente
  → Control total, responsabilidad total

PaaS (Platform as a Service)  
  → Te doy Hadoop/Spark ya instalado y configurado.
  → Ejemplo: Amazon EMR, Google Dataproc, Azure HDInsight
  → Tú solo corres tus jobs. Ellos gestionan el clúster.

SaaS (Software as a Service)
  → Te doy una plataforma completa con notebooks, colaboración, APIs.
  → Ejemplo: Databricks, Snowflake, BigQuery
  → Tú solo escribes código SQL/Python. Ellos hacen todo lo demás.
```

**Databricks (lo que usan en clase):**
- Es SaaS sobre Spark optimizado
- Creado por los mismos creadores de Apache Spark (Berkeley AMPLab)
- Gestiona automáticamente el clúster (auto-scaling, auto-termination)
- Community Edition: gratuito, 1 clúster simultáneo, hasta 6 GB RAM

**Pregunta al grupo #8:**

> *"Un startup peruano con 3 ingenieros de datos quiere construir un pipeline para analizar ventas de 50 tiendas en tiempo real. ¿Elegiría IaaS (instalar Hadoop en EC2), PaaS (Amazon EMR), o SaaS (Databricks)? Justifiquen considerando tiempo, costo y expertise."*

**Respuesta esperada detallada:** **SaaS (Databricks o similar)**, porque: (1) Con solo 3 ingenieros, no tienen tiempo ni expertise para configurar y mantener un clúster Hadoop completo (NameNode HA, YARN tuning, seguridad Kerberos, parches de seguridad) — eso requeriría al menos 2 ingenieros de infraestructura dedicados. (2) La velocidad de llegar al mercado es crítica en una startup; con Databricks pueden tener su primer notebook funcionando en 30 minutos. (3) El costo de PaaS/SaaS parece alto en tarjeta de crédito pero es más barato que el salario de 2 ingenieros de infraestructura. (4) Con IaaS, si el clúster falla a las 3 AM, ¿quién lo arregla? El SaaS tiene SLA de 99.9% y soporte 24/7. La respuesta cambia para una empresa grande con 50 ingenieros y petabytes: allí IaaS o PaaS es más económico a escala.

---

## RECESO (20 min) {#receso}

> *"Perfecto — descansamos 20 minutos. Al regresar, vamos directamente al laboratorio práctico en Databricks. Asegúrense de tener la sesión abierta en: dbc-xxxxxxxx.cloud.databricks.com"*

---

## BLOQUE 3 — PRÁCTICA Y CIERRE (50 min) {#bloque-3}

### 4. PRÁCTICA (40 min)

#### a) CASO PRÁCTICO GRUPAL (25 min)

**Escenario:**

> *"Son el equipo de datos de la empresa RIMAC Seguros. Tienen 2.5 millones de pólizas activas y reciben 15,000 siniestros por mes. Cada siniestro genera: formulario de denuncia (texto libre, 2 KB), fotos del accidente (promedio 15 fotos × 5 MB = 75 MB), audio de la llamada al call center (10 min × 1 MB = 10 MB), datos del vehículo de la SUNARP (JSON, 5 KB), historial del cliente en su base de datos (SQL, 2 KB). Total por siniestro: ~87 MB. Total mensual: 15,000 × 87 MB = 1.3 TB/mes.*
>
> *El directorio de RIMAC quiere un sistema que detecte siniestros fraudulentos en menos de 2 horas de recibido el caso."*

**Preguntas de análisis para los grupos:**

1. ¿Qué tipo de datos genera cada fuente? (¿estructurado, semiestructurado, no estructurado?)
2. ¿Qué componentes del ecosistema Hadoop/Cloud usarían para almacenar cada tipo?
3. ¿Qué arquitectura de nube elegirían (IaaS, PaaS, SaaS)? Justifiquen.
4. ¿Cómo aplicarían MapReduce o Spark para buscar patrones de fraude?
5. ¿Necesitan Fog Computing para alguna parte del proceso?

**Producto esperado del grupo:** Un diagrama de arquitectura (en papel o en la pizarra) con los componentes identificados y justificados, más un párrafo de respuesta a cada pregunta.

**Preguntas de andamiaje del docente mientras recorre grupos:**
- *"¿Las fotos del accidente irían a HDFS o a HBase? ¿Por qué?"* (HDFS — son archivos grandes no estructurados, acceso batch)
- *"Si quieren buscar si el mismo vehículo apareció en 3 siniestros distintos, ¿qué base de datos usarían?"* (HBase — acceso aleatorio por Row Key = placa del vehículo)
- *"¿El call center puede esperar a que el análisis de audio termine para darle una respuesta al cliente?"* (No — necesitan procesar en tiempo real o near-real-time)

**Puesta en común — Respuesta modelo:**

```
ARQUITECTURA RIMAC ANTI-FRAUDE:

INGESTA:
  Formulario texto → Kafka topic: siniestros-texto
  Fotos → HDFS /siniestros/fotos/2025/01/ (archivos grandes, batch)
  Audio → HDFS /siniestros/audio/ (batch, procesado nocturnamente)
  SUNARP JSON → MongoDB Atlas (semiestructurado, acceso por placa)
  Historial SQL → HBase (acceso rápido por DNI del asegurado)

PROCESAMIENTO:
  PySpark Streaming: detecta patrones en tiempo real (mismo vehículo, mismo taller)
  PySpark ML: modelo de clasificación fraude/no-fraude (Random Forest)
  
ALMACENAMIENTO RESULTADOS:
  HBase: score de fraude por siniestro (acceso rápido por ID siniestro)
  HDFS: archivos fuente para auditoría y re-entrenamiento del modelo

CLOUD: SaaS (Databricks) — equipo pequeño, velocidad crítica, datos sensibles con compliance

FOG: No necesario — los datos ya llegan digitales y no tienen restricciones de latencia extrema
```

---

#### b) EJERCICIO INDIVIDUAL (15 min)

**Tarea:**

> *"En Databricks (o en papel si no tienen acceso ahora), escriban el pseudocódigo o código PySpark para resolver este problema:*
>
> *Tienen un archivo CSV con el historial de accidentes del SOAT: columnas = [ID_siniestro, placa_vehiculo, fecha, departamento, monto_siniestro, tipo_siniestro]. El archivo tiene 5 millones de filas (3 años de datos).*
>
> *Calcular: ¿Cuál es el departamento con mayor monto total de siniestros?"*

**Código esperado:**

```python
# En Databricks: Shift+Enter para ejecutar cada celda

# 1. Leer el archivo
df = spark.read.csv("/FileStore/tables/soat_siniestros.csv",
                    header=True,
                    inferSchema=True)

# 2. Agrupar por departamento y sumar montos
resultado = df.groupBy("departamento") \
              .sum("monto_siniestro") \
              .orderBy("sum(monto_siniestro)", ascending=False)

# 3. Mostrar el top 5
resultado.show(5)

# Output esperado:
# +------------+---------------------+
# |departamento|sum(monto_siniestro) |
# +------------+---------------------+
# |Lima        |    245000000.0      |
# |Arequipa    |     45000000.0      |
# |La Libertad |     38000000.0      |
# |Piura       |     29000000.0      |
# |Cusco       |     25000000.0      |
# +------------+---------------------+
```

**Criterio de éxito:** El estudiante puede explicar verbalmente qué hace cada línea y por qué `groupBy` es el equivalente a la fase REDUCE de MapReduce.

---

### 5. CIERRE (10 min)

#### a) SÍNTESIS COLABORATIVA (4 min)

> *"Vamos a construir juntos el resumen de la sesión. Yo pregunto, ustedes responden:"*

**Pregunta de cierre 1:**
> *"¿Cuál es la diferencia más importante entre HDFS y una base de datos relacional como Oracle?"*

**Respuesta esperada:** HDFS está diseñado para almacenar archivos masivos de forma distribuida con acceso secuencial y tolerancia a fallos automática — pero no puede actualizar registros individuales ni responder consultas en tiempo real. Oracle está diseñado para transacciones ACID, acceso aleatorio rápido y consultas SQL complejas — pero escala verticalmente (comprando un servidor más caro) y no distribuye nativamente. Son complementarios, no sustitutos.

**Pregunta de cierre 2:**
> *"¿En qué fase de MapReduce se distribuye el trabajo a los DataNodes: en Map, en Shuffle, o en Reduce?"*

**Respuesta esperada:** En todas, pero el principio fundamental es que la fase **Map** se ejecuta donde están los datos (localidad de datos) — el código va al nodo, no los datos al código. Shuffle mueve los pares key-value entre nodos para agruparlos. Reduce opera sobre los grupos. La clave es "mover el código, no los datos" — eso es lo que hace eficiente a Hadoop para archivos de TB.

**Pregunta de cierre 3:**
> *"¿Cuándo es mejor HBase que HDFS?"*

**Respuesta esperada:** HBase es mejor cuando necesitas acceso aleatorio en tiempo real por una clave específica (Row Key). HDFS es mejor para procesamiento secuencial de grandes archivos en batch. Regla práctica: si dices "dame el registro de este cliente específico en menos de 100ms" → HBase. Si dices "procesa todos los registros del mes y dame un reporte" → HDFS.

---

#### b) METACOGNICIÓN (3 min)

> *"En silencio, en su cuaderno o en el mismo notebook de Databricks, respondan honestamente estas preguntas — no se entregan, son para ustedes:"*
>
> 1. ¿Qué concepto de hoy me quedó más claro? ¿Por qué creo que lo entendí bien?
> 2. ¿Qué concepto todavía me genera confusión? ¿Qué necesito hacer para aclararlo?
> 3. Si tuviera que explicar MapReduce a un amigo que no estudia sistemas, ¿qué analogía usaría?

---

#### c) TAREA Y PUENTE (3 min)

> *"Para la próxima semana vemos Apache Spark en profundidad y procesamiento de datos en streaming. La tarea de esta semana es:*
>
> *1. Completar el Laboratorio en Casa (S2_LAB_CASA_BIGDATA.md) — 2 horas*
> *2. Leer: Capítulo 2 de 'Learning Spark' (O'Reilly) — disponible gratuito en databricks.com/resources*
> *3. OPCIONAL pero recomendado: ver el video de YouTube 'MapReduce - Computerphile' (8 min) — link en el laboratorio*
>
> *Para quienes lograron correr el código en Databricks hoy: el lab va a ser mucho más fluido. Para quienes no pudieron, el laboratorio en casa tiene instrucciones paso a paso.*
>
> *Una última cosa: el nombre de usuario que eligieron en Databricks es el que voy a usar para calificar los notebooks. Asegúrense de que sea profesional."*

---



---

## CASOS REALES RECOMENDADOS {#casos-reales}

1. **Facebook y el "cold storage" en HDFS:** En 2014, Facebook tenía 300 PB en HDFS y anunció que migraba datos "fríos" (poco accedidos) a sistemas de cinta magnética para reducir costos — pero el índice seguía en HDFS. Enseña: no todo dato necesita estar caliente. Fuente: Facebook Engineering Blog, 2014.

2. **Twitter y el "Retweet problem":** El algoritmo de Twitter tiene que propagar un tweet viral a 100 millones de seguidores en segundos — usaron Storm (streaming) sobre Hadoop para esto. Cuando Elon Musk compró Twitter (2022), uno de los primeros problemas fue que el código de "For You" que recomendaba tweets usaba un clúster Hadoop de 1,000 nodos. Fuente: Twitter Engineering Blog.

3. **SUNAT Perú y la detección de evasión:** SUNAT implementó un sistema de análisis de riesgo tributario usando Big Data que cruza facturas electrónicas, declaraciones de renta, y movimientos bancarios. En 2023 detectaron S/ 2,800 millones en evasión con este sistema. Fuente: SUNAT Informe Anual 2023.

4. **Uber y los "surge" prices:** El algoritmo de precio dinámico de Uber procesa posición GPS de millones de usuarios y conductores en tiempo real con Kafka + Spark Streaming sobre infraestructura en la nube. Un fallo de 5 minutos en este sistema en una noche de lluvia generó pérdidas de $2M. Fuente: Uber Engineering Blog.

5. **HBase en la banca peruana:** El BCP (Banco de Crédito del Perú) usa arquitecturas similares a HBase para el historial de transacciones de Yape. Cada consulta de saldo debe responder en < 300ms para 5 millones de usuarios activos simultáneos. Fuente: BCP Tech Blog (LinkedIn).

---

## EVALUACIÓN FORMATIVA {#evaluacion}

| Momento | Técnica | Indicador de logro |
|---------|---------|-------------------|
| Durante Transformación | Preguntas orales al grupo | El 70%+ da respuestas que incluyen los elementos esperados |
| Mini actividades | Revisión rápida del docente caminando | El estudiante puede justificar verbalmente su respuesta |
| Caso práctico grupal | Observación del diagrama producido | Incluye mínimo: tipo de dato + componente Hadoop + justificación |
| Ejercicio individual | Revisión del código/pseudocódigo | Usa groupBy (reduce) y puede explicar la lógica MapReduce |
| Cierre | Respuestas orales a preguntas de síntesis | Diferencia HDFS vs HBase correctamente |

---

## STACK TECNOLÓGICO GRATUITO PARA ESTUDIANTES {#stack-gratuito}

| Herramienta | Función | Link | Límites gratuitos |
|-------------|---------|------|-------------------|
| **Databricks Community Edition** | Spark + Notebooks + DBFS | community.cloud.databricks.com | 1 clúster, 6 GB RAM, 15 GB DBFS |
| **Google Colab** | Python + PySpark simulado | colab.research.google.com | 12 GB RAM, GPU gratis |
| **Docker Desktop** | Hadoop local en contenedores | docker.com | Gratis para uso personal/educativo |
| **Apache Hadoop Docker** | Clúster Hadoop local | hub.docker.com/r/sequenceiq/hadoop-docker | Sin límite |
| **MongoDB Atlas M0** | HBase alternativo en la nube | mongodb.com/atlas | 512 MB gratis permanente |
| **Hue** | Interfaz web para HDFS/Hive | gethue.com | Open source |
| **Apache Zeppelin** | Notebooks para Hadoop/Spark | zeppelin.apache.org | Open source, instalar local |
| **AWS Academy** | Créditos AWS para estudiantes | aws.amazon.com/education/awsacademy | Solicitar con email universitario |
| **GitHub Student Pack** | Créditos Azure + herramientas | education.github.com | Con email .edu |
| **Play with Docker** | Docker en el navegador sin instalar | labs.play-with-docker.com | 4 horas por sesión |

---

## REFERENCIAS APA 7 {#referencias}

White, T. (2015). *Hadoop: The definitive guide* (4th ed.). O'Reilly Media. https://www.oreilly.com/library/view/hadoop-the-definitive/9781491901687/

Chambers, B., & Zaharia, M. (2018). *Spark: The definitive guide*. O'Reilly Media. https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/

Dean, J., & Ghemawat, S. (2008). MapReduce: Simplified data processing on large clusters. *Communications of the ACM, 51*(1), 107–113. https://doi.org/10.1145/1327452.1327492

Ghemawat, S., Gobioff, H., & Leung, S.-T. (2003). The Google file system. *ACM SIGOPS Operating Systems Review, 37*(5), 29–43. https://doi.org/10.1145/1165389.945450

Chang, F., Dean, J., Ghemawat, S., Hsieh, W. C., Wallach, D. A., Burrows, M., Chandra, T., Fikes, A., & Gruber, R. E. (2008). Bigtable: A distributed storage system for structured data. *ACM Transactions on Computer Systems, 26*(2), Article 4. https://doi.org/10.1145/1365815.1365816

Bonomi, F., Milito, R., Zhu, J., & Addepalli, S. (2012). Fog computing and its role in the internet of things. *Proceedings of the First Edition of the MCC Workshop on Mobile Cloud Computing*, 13–16. https://doi.org/10.1145/2342509.2342513

Kleppmann, M. (2017). *Designing data-intensive applications*. O'Reilly Media. https://dataintensive.net/

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
