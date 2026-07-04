# Parcial Big Data - Hidgar Orellano Huerta

| Campo | Detalle |
|---|---|
| Estudiante | Hidgar Orellano Huerta |
| Codigo | 2221892872 |
| Curso | Big Data |
| Repositorio personal | https://github.com/HidgarO/yape-orellano-hidgar |
| Video de sustentacion | https://youtu.be/EnequVsewIc |

## Enlaces de entrega

- Repositorio personal con implementacion: <https://github.com/HidgarO/yape-orellano-hidgar>
- Video de sustentacion: <https://youtu.be/EnequVsewIc>

## Parte A - Arquitectura Big Data para Yape

### 1. Propuesta general

Para una billetera digital tipo Yape propongo una arquitectura separada por responsabilidades. El nucleo de pagos debe estar aislado de la capa analitica, porque las transacciones financieras requieren consistencia fuerte, mientras que los reportes pueden trabajar con datos historicos o consistencia eventual.

La arquitectura propuesta considera los siguientes componentes:

| Necesidad | Tecnologia propuesta | Justificacion |
|---|---|---|
| Pagos y saldos | Base NewSQL como CockroachDB | Permite transacciones ACID, consistencia fuerte y escalamiento horizontal. |
| Sesiones y consultas rapidas | Redis | Entrega baja latencia para datos temporales, tokens, cache y sesiones. |
| Comercios afiliados | MongoDB Atlas | Permite almacenar documentos flexibles con datos variables de comercios. |
| Analitica de transacciones | Databricks / Delta Lake | Permite procesar datos con arquitectura Medallion: Bronze, Silver y Gold. |
| Analisis de fraude | Base de grafos como Neo4j o TigerGraph | Facilita detectar relaciones sospechosas entre usuarios, cuentas y comercios. |
| Visualizacion | Dashboard sobre tablas Gold | Permite mostrar indicadores como volumen, comisiones, zonas activas y tendencias. |

### 2. Decisiones principales

Para el nucleo transaccional se propone NewSQL porque combina propiedades ACID con escalamiento distribuido. En pagos digitales no se puede permitir doble descuento, confirmaciones inconsistentes o saldos incorrectos. Por eso, la base principal debe priorizar consistencia y tolerancia a fallos.

Para los comercios se propone MongoDB Atlas porque cada comercio puede tener atributos distintos. Por ejemplo, un restaurante puede manejar delivery, horarios y categorias, mientras que una farmacia o bodega puede tener otros campos operativos. Un modelo documental permite guardar esta informacion sin forzar una estructura relacional fija.

Para la analitica se propone Databricks con arquitectura Medallion. La capa Bronze conserva datos crudos, Silver aplica limpieza y enriquecimiento, y Gold genera metricas listas para reportes y dashboards. Esta separacion permite mantener trazabilidad y ordenar el procesamiento.

### 3. CAP

En el modulo de pagos se debe priorizar consistencia y tolerancia a particiones. Si ocurre una falla de red, es preferible rechazar temporalmente una operacion antes que confirmar una transaccion incorrecta. En este escenario, el sistema sacrifica disponibilidad para proteger la consistencia financiera.

En cambio, para dashboards, historial o analitica, se puede aceptar consistencia eventual. Un reporte puede actualizarse con algunos segundos o minutos de retraso sin afectar directamente el saldo ni la confirmacion del pago. En este caso se prioriza disponibilidad y rendimiento de consulta.

### 4. NewSQL

NewSQL resuelve el problema de escalar sistemas transaccionales sin perder propiedades ACID. En una billetera digital, esto permite procesar pagos de forma consistente aunque existan muchos usuarios y alto volumen de transacciones.

MongoDB no seria la mejor opcion para el core de pagos porque es mas adecuado para documentos flexibles que para un libro contable transaccional financiero. En cambio, MongoDB si es adecuado para perfiles de comercios, configuraciones, catalogos y datos semiestructurados.

Un mecanismo comun en bases NewSQL distribuidas es el consenso, como Raft, que permite replicar datos y mantener acuerdo entre nodos antes de confirmar operaciones criticas.

## Parte D - Docker y comparacion con MongoDB Atlas

### 1. Implementacion local con Docker

Para validar MongoDB en un entorno local se utilizo Docker Desktop. Se levanto un contenedor de MongoDB con la imagen oficial `mongo:7`, usando el nombre `mongodb-yape` y exponiendo el puerto local `27017`.

Luego se valido que el contenedor estuviera activo desde Docker Desktop y desde terminal. Despues se ejecuto un script de Python que se conecto al MongoDB local, inserto un documento de prueba de comercio, recupero ese documento y mostro el total de documentos almacenados.

Esta prueba confirma que MongoDB puede ejecutarse localmente de forma aislada y reproducible para desarrollo o validacion.

### 2. Diferencia entre Docker y Atlas

Docker es conveniente cuando se necesita un entorno local de desarrollo o pruebas. Permite levantar una base de datos rapidamente, probar scripts, validar conexiones y eliminar el entorno cuando ya no se necesita. Es util para trabajar sin afectar una base cloud o datos compartidos.

MongoDB Atlas es una solucion administrada en la nube. Es mas adecuada cuando se necesita acceso remoto, persistencia administrada, monitoreo, interfaz web, gestion de usuarios y colaboracion. En un contexto academico tambien facilita evidenciar los documentos insertados desde Browse Collections.

### 3. Persistencia de datos

Si se detiene y elimina el contenedor `mongodb-yape` sin haber configurado un volumen persistente, los datos locales se pierden junto con el contenedor. Docker permite persistencia, pero debe configurarse explicitamente mediante volumenes.

En MongoDB Atlas, los datos permanecen en la nube aunque se apague la computadora local o se cierre la sesion. Por eso Atlas es mas conveniente para una entrega demostrable y para escenarios cercanos a produccion.

## Resumen

La implementacion completa de las partes practicas se encuentra en el repositorio personal. Alli se incluyen los scripts, capturas y README de ejecucion para Databricks, MongoDB Atlas y Docker.
