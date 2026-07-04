# Asegurar que la librería pymongo esté instalada en Cloud Shell
import os
try:
    from pymongo import MongoClient
except ImportError:
    os.system('pip install -q pymongo')
    from pymongo import MongoClient

# Conexión directa (Aquí sí funciona localhost al 100% porque el script corre al lado de Docker)
client_docker = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin"
)

db_local = client_docker["yape_local"]
col_local = db_local["comerciantes_test"]

# Limpiar ejecuciones previas para tener un conteo limpio
col_local.delete_many({})

# Insertar el comerciante de Yape
col_local.insert_one({
    "nombre_comercio": "Bodega Test Docker",
    "tipo": "bodega",
    "distrito": "Lima",
    "monto_mensual_soles": 1500.00,
    "yape_activo": True,
    "entorno": "docker_local"
})

# Verificar la inserción
doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
print("✅ Documento guardado en MongoDB Docker:")
print(f"   Nombre:   {doc['nombre_comercio']}")
print(f"   Entorno:  {doc['entorno']}")
print(f"   ID:       {doc['_id']}")