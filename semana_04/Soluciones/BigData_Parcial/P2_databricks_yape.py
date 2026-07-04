# CELDA 1 BRONZE
import numpy as np
import pandas as pd
from pyspark.sql import functions as F

np.random.seed(42)

n = 2000

distritos = [
    "Miraflores","San Isidro","SJL","Comas",
    "Villa El Salvador","Los Olivos",
    "Surco","Ate","Callao","Independencia"
]

tipos = [
    "persona_a_persona",
    "persona_a_comercio",
    "retiro_bcp",
    "recarga"
]

estados = [
    "completada",
    "completada",
    "completada",
    "rechazada",
    "pendiente"
]

data = {
    "id_transaccion":[f"YP{i:07d}" for i in range(1,n+1)],
    "fecha":pd.date_range("2025-01-01",periods=n,freq="1h").strftime("%Y-%m-%d"),
    "hora":[f"{h:02d}:{m:02d}" for h,m in zip(np.random.randint(0,24,n),np.random.randint(0,60,n))],
    "monto_soles":np.round(np.random.exponential(45,n),2),
    "tipo":np.random.choice(tipos,n),
    "distrito_origen":np.random.choice(distritos,n),
    "estado":np.random.choice(estados,n,p=[0.75,0.10,0.05,0.07,0.03]),
    "id_usuario":[f"USR{np.random.randint(1000,9999)}" for _ in range(n)],
    "es_comercio":np.random.choice([True,False],n,p=[0.4,0.6])
}

df_pandas = pd.DataFrame(data)

df_bronze = spark.createDataFrame(df_pandas)

display(df_bronze)

print(df_bronze.count())

# CELDA 2 SILVER
from pyspark.sql import functions as F

df_silver = (
    df_bronze
    .filter(F.col("estado") == "completada")
    .filter(F.col("monto_soles") > 0)
    .withColumn(
        "categoria_monto",
        F.when(F.col("monto_soles") < 20, "micro")
         .when(F.col("monto_soles") < 100, "medio")
         .otherwise("alto")
    )
    .withColumn(
        "es_hora_pico",
        F.when(F.col("hora").between("12:00","14:00"), True)
         .when(F.col("hora").between("18:00","22:00"), True)
         .otherwise(False)
    )
    .withColumn(
        "comision_yape",
        F.when(
            F.col("tipo")=="persona_a_comercio",
            F.round(F.col("monto_soles")*0.015,2)
        ).otherwise(0.0)
    )
)

display(df_silver)

print("Total registros:", df_silver.count())
# CELDA 3 GOLD
from pyspark.sql import functions as F

gold_distritos = (
    df_silver.groupBy("distrito_origen")
    .agg(
        F.count("*").alias("total_transacciones"),
        F.round(F.sum("monto_soles"),2).alias("volumen_total_soles"),
        F.round(F.avg("monto_soles"),2).alias("ticket_promedio"),
        F.sum(F.when(F.col("es_comercio")==True,1).otherwise(0)).alias("transacciones_comercio")
    )
    .orderBy(F.desc("total_transacciones"))
    .limit(5)
)

gold_comisiones = (
    df_silver
    .filter(F.col("comision_yape")>0)
    .groupBy(F.substring("hora",1,2).alias("hora_dia"))
    .agg(
        F.count("*").alias("num_transacciones"),
        F.round(F.sum("comision_yape"),2).alias("ingresos_yape_soles")
    )
    .orderBy(F.desc("ingresos_yape_soles"))
)

print("TOP 5 DISTRITOS")
display(gold_distritos)

print("INGRESOS POR HORA")
display(gold_comisiones)

# CELDA 4 DASHBOARD
import matplotlib.pyplot as plt

gold_distritos_pd = gold_distritos.toPandas()

plt.figure(figsize=(8,5))
plt.bar(
    gold_distritos_pd["distrito_origen"],
    gold_distritos_pd["volumen_total_soles"]
)

plt.title("Top 5 Distritos")
plt.xlabel("Distrito")
plt.ylabel("Volumen (S/)")
plt.xticks(rotation=30)

plt.show()