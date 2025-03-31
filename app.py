import os
from flask import Flask, render_template
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Obtener credenciales desde el .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SECURE_CONNECT_BUNDLE = os.getenv("SECURE_CONNECT_BUNDLE")

# Conectar a Cassandra
cloud_config = {"secure_connect_bundle": SECURE_CONNECT_BUNDLE}
auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


session.set_keyspace("prueba")


@app.route("/")
def index():
    # Obtener los clientes de la base de datos
    clientes = session.execute("SELECT * FROM cliente").all()

    return render_template("index.html", clientes=clientes)


if __name__ == "__main__":
    app.run(debug=True)
