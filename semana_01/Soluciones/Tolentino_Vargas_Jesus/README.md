# Lab Semana 1 — Big Data DD283
**Estudiante**: Tolentino Vargas Jesus Antonio  
**Fecha**: Junio 2026  


## ¿Qué aprendí?
<<<<<<< HEAD
Aprendí a diferenciar en la práctica los tres tipos de datos del Big Data: estructurados (un DataFrame de transacciones con esquema fijo), semi-estructurados (un JSON tipo API que tuve que aplanar a tabla) y no estructurados (comentarios de texto libre que clasifiqué por sentimiento). También comprobé cómo calcular las V's directamente sobre los datos: medí el volumen en memoria y lo proyecté a 100 millones de registros, calculé la velocidad como transacciones por día, y la veracidad mediante la tasa de fraude. Por último, entendí que diseñar una arquitectura Big Data consiste en conectar de forma coherente la ingesta, el almacenamiento, el procesamiento y la visualización según el tipo de dato y el caso de uso.

## ¿Qué fue lo más difícil?
Lo más difícil fue trabajar con el JSON anidado de la Parte 3, porque tuve que recorrer estructuras dentro de estructuras (el campo "contacto" y la lista "compras") y manejar los valores nulos para convertir todo a una tabla plana sin perder información. Manejar los valores `null` y las listas vacías al pasar de JSON a DataFrame requirió cuidado para no romper los cálculos de totales.

## ¿Cómo aplica en mi empresa actual?
En COEZ PERÚ, donde trabajo como Ingeniero de Producción, manejo a diario datos estructurados (metrados y avances de partidas en Excel), semi-estructurados (correos y formatos de submittal) y no estructurados (fotografías de obra y PDFs de planos). Este laboratorio me mostró que podría centralizar todo ese flujo fragmentado en una arquitectura tipo Data Lake para tener control de producción en tiempo real, en lugar de las planillas manuales y desconectadas que usamos hoy. Además, el ejercicio de detección de fraude y predicción conecta directamente con el proyecto de mi grupo sobre predicción de fuga de clientes (churn) en telecomunicaciones.
=======
Durante este laboratorio entendí mejor la diferencia entre los datos estructurados, semiestructurados y no estructurados. Trabajé con tablas, archivos JSON y comentarios de texto, lo que me permitió ver cómo cambia el tratamiento de la información según su formato. También aprendí a calcular algunas de las características del Big Data, como el volumen, la velocidad y la veracidad de los datos. Finalmente, comprendí que una arquitectura Big Data no solo almacena información, sino que organiza todo el proceso desde la captura de los datos hasta la generación de reportes para apoyar la toma de decisiones.

## ¿Qué fue lo más difícil?
La parte que más trabajo me costó fue transformar el archivo JSON en una tabla. Tuve que recorrer información anidada, extraer los datos que necesitaba y manejar correctamente los valores nulos para evitar errores durante el procesamiento. Fue la actividad donde tuve que revisar más el código hasta obtener el resultado esperado.

## ¿Cómo aplica en mi empresa actual?
En mi trabajo utilizamos información que proviene de diferentes fuentes, como hojas de cálculo, documentos, correos, fotografías y planos. Este laboratorio me ayudó a entender que todos esos datos podrían integrarse en una sola plataforma para facilitar su análisis y evitar trabajar con información dispersa. Además, varios de los conceptos vistos también pueden aplicarse al proyecto de mi grupo, donde analizamos datos para predecir la fuga de clientes utilizando técnicas de Big Data.
>>>>>>> c01f654f9a11075fb9f5ec7728accf12406f02b5
