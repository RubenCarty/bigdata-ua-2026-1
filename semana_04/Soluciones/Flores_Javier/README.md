# Proyecto - Semana 04

## Big Data – Evaluación Parcial

### Alumno

* **Nombre:** Javier Flores
* **Código:** 2221897056
* **Curso:** Big Data
* **Tema:** Arquitectura Big Data, Databricks, MongoDB Atlas y Docker

---

# Descripción del Proyecto

Este proyecto tiene como objetivo implementar una solución Big Data basada en un escenario de análisis de transacciones de Yape, utilizando tecnologías modernas para el procesamiento, almacenamiento y despliegue de datos.

La solución contempla el diseño de la arquitectura, el procesamiento de datos mediante Databricks siguiendo la arquitectura **Bronze → Silver → Gold**, el almacenamiento de información en MongoDB Atlas y la ejecución de aplicaciones Python dentro de un contenedor Docker.

---

# Implementación del Proyecto

## 1. Diseño de Arquitectura

Se diseñó una arquitectura orientada a Big Data que integra componentes de ingesta, procesamiento, almacenamiento y visualización.

Las principales decisiones tecnológicas fueron:

* Uso de **Databricks** como plataforma de procesamiento distribuido mediante Apache Spark.
* Uso de **MongoDB Atlas** como base de datos NoSQL para almacenar documentos JSON de forma escalable.
* Uso de **Docker Desktop** para ejecutar la aplicación Python de forma aislada y portable.
* Separación de los datos en capas **Bronze**, **Silver** y **Gold** para garantizar calidad y organización de la información.

---

## 2. Procesamiento de Datos con Databricks

Se desarrolló un notebook que realiza el flujo completo de procesamiento de datos.

### Bronze

* Lectura de los datos originales.
* Almacenamiento sin modificaciones.

### Silver

* Limpieza de registros.
* Eliminación de valores nulos.
* Corrección de tipos de datos.
* Estandarización de la información.

### Gold

* Agregaciones.
* Métricas finales.
* Preparación para dashboards y análisis.

Finalmente se generó un Dashboard con las métricas obtenidas.

---

## 3. Implementación con MongoDB Atlas

Se utilizó MongoDB Atlas para almacenar la información procesada.

Las actividades realizadas fueron:

* Conexión desde Python utilizando PyMongo.
* Inserción de documentos.
* Consulta de registros.
* Visualización de las colecciones desde Atlas UI.
* Ejecución de un Aggregation Pipeline para obtener estadísticas de los datos almacenados.

---

## 4. Implementación con Docker

Se creó un contenedor Docker para ejecutar la aplicación Python.

Las tareas realizadas fueron:

* Creación del Dockerfile.
* Construcción de la imagen.
* Ejecución del contenedor.
* Verificación de la conexión entre Python y MongoDB Atlas.

La ejecución fue validada desde Docker Desktop mostrando el contenedor en estado **Running**.

---

# Evidencias

Las capturas de pantalla del proyecto se encuentran en la carpeta:

```

Databricks/
Docker/
MongoDB_Atlas/

```

Incluyen:

* Databricks
* Dashboard
* MongoDB Atlas
* Aggregation Pipeline
* Docker en Google Cloud Shell

---

# Video de Sustentación

El video muestra:

1. Presentación del estudiante.
2. Explicación de la arquitectura propuesta.
3. Demostración del notebook en Databricks.
4. Visualización de MongoDB Atlas.
5. Ejecución del contenedor Docker.
6. Explicación del uso de Inteligencia Artificial durante el desarrollo.

**Enlace del video:**

> https://drive.google.com/file/d/1zOvud3UT-Dvc_hs0vNYriaBDyCAQ36Mr/view?pli=1

---

# Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó Inteligencia Artificial como herramienta de apoyo para:

* Generar ejemplos de código.
* Resolver dudas sobre PySpark.
* Comprender consultas de MongoDB.
* Optimizar el Dockerfile.
* Mejorar la documentación del proyecto.

Las implementaciones fueron revisadas, adaptadas y validadas manualmente para cumplir con los requerimientos del examen.

---

# Tecnologías Utilizadas

* Python 3
* Apache Spark
* Databricks
* MongoDB Atlas
* Docker Cloud Shell
* GitHub

---

# Conclusión

Este proyecto permitió integrar diferentes herramientas del ecosistema Big Data para desarrollar un flujo completo de procesamiento de información, desde la ingesta y transformación de datos hasta su almacenamiento, visualización y despliegue en un entorno contenerizado, aplicando buenas prácticas de arquitectura y procesamiento distribuido.
