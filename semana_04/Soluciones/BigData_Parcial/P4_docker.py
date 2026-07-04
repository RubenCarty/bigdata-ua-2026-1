from pymongo import MongoClient

client = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin"
)

db_local = client["yape_local"]

col = db_local["comerciantes_test"]

col.insert_one({
    "nombre_comercio":"Bodega Test Docker",
    "tipo":"bodega",
    "entorno":"docker_local"
})

print("Docker funcionando")