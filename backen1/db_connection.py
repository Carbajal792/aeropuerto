import psycopg2
import os
from dotenv import load_dotenv
connection = None
def get_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv(host),        
            port=os.getenv(port),        
            database=os.getenv(database),
            user=os.getenv(user),        
            password=os.getenv(password) 
        )
        print("✅ Conexión exitosa a PostgreSQL")
        return connection
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")