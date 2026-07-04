from pymongo import MongoClient

# PEGA TU CONNECTION STRING
CONNECTION_STRING = "mongodb+srv://admin:yape2026@cluster0.9ewuanc.mongodb.net/?appName=Cluster0"
client = MongoClient(CONNECTION_STRING)

db = client["yape_db"]

comerciantes = db["comerciantes"]

print("Conexion correcta")

lista = [

{
"nombre_comercio":"Bodega Mario",
"tipo":"bodega",
"calificacion":4.2,
"yape_activo":True,
"monto_mensual_soles":4500
},

{
"nombre_comercio":"Restaurante Peru",
"tipo":"restaurante",
"calificacion":4.8,
"yape_activo":True,
"monto_mensual_soles":28000
},

{
"nombre_comercio":"Farmacia Lima",
"tipo":"farmacia",
"calificacion":4.5,
"yape_activo":True,
"monto_mensual_soles":12000
},

{
"nombre_comercio":"Taxi Express",
"tipo":"taxi",
"calificacion":4.0,
"yape_activo":True,
"monto_mensual_soles":3200
},

{
"nombre_comercio":"Empresa Norte",
"tipo":"empresa",
"calificacion":3.9,
"yape_activo":True,
"monto_mensual_soles":85000
}

]

resultado = comerciantes.insert_many(lista)

print("Insertados:", len(resultado.inserted_ids))