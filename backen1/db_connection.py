import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
port = os.environ.get("DB_PORT")

connection = None
def get_connection():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        print("✅ Conexión exitosa a PostgreSQL")
        return connection
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")