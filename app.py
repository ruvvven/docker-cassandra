import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener credenciales desde el .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SECURE_CONNECT_BUNDLE = os.getenv("SECURE_CONNECT_BUNDLE")

# Configurar la conexión a Cassandra
cloud_config = {"secure_connect_bundle": SECURE_CONNECT_BUNDLE}
auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Probar conexión
row = session.execute("SELECT release_version FROM system.local").one()
if row:
    print(f"Conectado a Cassandra, versión: {row[0]}")
else:
    print("Error en la conexión a Cassandra")
