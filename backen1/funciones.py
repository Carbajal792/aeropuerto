from datetime import datetime, timezone
from flask import Flask, jsonify, make_response
import requests
from db_connection import get_connection
from flask_cors import CORS
import logging

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"


def configurar_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

def conteo():
    """Obtiene el número de preguntas contestadas y no contestadas desde la API de Stack Overflow."""
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        respuestas = list(map(lambda x: x.get("is_answered", False), datos["items"]))
        
        contestadas = respuestas.count(True)
        no_contestadas = respuestas.count(False)
        
        return contestadas, no_contestadas
    else:
        return None, None
    
def reputacion(): 
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        preguntas = [
            {
                "title": dato.get("title", "No disponible"),
                "tags": dato.get("tags", []),
                "is_answered": dato.get("is_answered", False),
                "view_count": dato.get("view_count", "N/A"),
                "score": dato.get("score", "N/A"),
                "owner": dato.get("owner", {}),
                "link": dato.get("link", "No disponible")
            }
            for dato in datos["items"]
        ]
        mayorReputacion = max(preguntas, key=lambda x: x["owner"].get("reputation", 0), default=None)
        
        return mayorReputacion
    else:
        return None
    
def menosVistas(): 
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        preguntas = [
            {
                "title": dato.get("title", "No disponible"),
                "tags": dato.get("tags", []),
                "is_answered": dato.get("is_answered", False),
                "view_count": dato.get("view_count", "N/A"),
                "score": dato.get("score", "N/A"),
                "owner": dato.get("owner", {}),
                "link": dato.get("link", "No disponible")
            }
            for dato in datos["items"]
        ]
        menosVistas = min(preguntas, key=lambda x: x["owner"].get("view_count", 0), default=None)
        
        return menosVistas
    else:
        return None

def antigua(): 
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        preguntas = [
            {
                "title": dato.get("title", "No disponible"),
                "tags": dato.get("tags", []),
                "is_answered": dato.get("is_answered", False),
                "view_count": dato.get("view_count", "N/A"),
                "score": dato.get("score", "N/A"),
                "owner": dato.get("owner", {}),
                "link": dato.get("link", "No disponible"),
                "last_activity_date": dato.get("last_activity_date", 0)
            }
            for dato in datos["items"]
        ]
        antigua = min(
            (pregunta for pregunta in preguntas if pregunta.get("is_answered", False)), 
            key=lambda x: x["last_activity_date"],
            default=None
        )
        antigua["last_activity_date"] = convertir_fecha(antigua["last_activity_date"])
        return antigua
    else:
        return None

def actual(): 
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        preguntas = [
            {
                "title": dato.get("title", "No disponible"),
                "tags": dato.get("tags", []),
                "is_answered": dato.get("is_answered", False),
                "view_count": dato.get("view_count", "N/A"),
                "score": dato.get("score", "N/A"),
                "owner": dato.get("owner", {}),
                "link": dato.get("link", "No disponible"),
                "last_activity_date": dato.get("last_activity_date", 0)
            }
            for dato in datos["items"]
        ]

        actual = max(
            (pregunta for pregunta in preguntas if pregunta.get("is_answered", False)),
            key=lambda x: x["last_activity_date"],
            default=None
        )
        actual["last_activity_date"] = convertir_fecha(actual["last_activity_date"])
        return actual
    else:
        return None

def convertir_fecha(timestamp):
    try:
        return datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return f"Error: {str(e)}"
    
# Ejecutar la consulta y retornar el resultado
def ejecutar(query):
    connection = get_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultado
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

def obtenerResultados(tupla):
    if not tupla:
        return []
    comp = tupla[0][1]
    resultados = [fila for fila in tupla if fila[1] == comp]
    return resultados

# ¿Cuál es el nombre del aeropuerto que ha tenido mayor movimiento durante el año?
def masMovimiento():
    query = """
    SELECT a.nombre_aeropuerto, COUNT(v.id_movimiento) AS total_movimientos
    FROM vuelos v
    JOIN aeropuertos a ON v.id_aeropuerto = a.id_aeropuerto
    GROUP BY a.nombre_aeropuerto
    ORDER BY total_movimientos DESC
    """
    resultado = ejecutar(query)
    resultado = obtenerResultados(resultado)

    aeropuertos = [{"Aeropuerto": fila[0], "Total Movimientos": fila[1]} for fila in resultado]
    return aeropuertos

#2\. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?
def masVuelos():
    query = """
        SELECT a.nombre_aerolinea, COUNT(v.id_aerolinea) AS total_vuelos
        FROM vuelos v
        JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
        GROUP BY a.nombre_aerolinea
        ORDER BY total_vuelos DESC;
    """
    resultado = ejecutar(query)
    resultado = obtenerResultados(resultado)

    vuelos = [{"Aerolinea": fila[0], "Total Vuelos":fila[1]} for fila in resultado]
    return vuelos

def dia():
    query = """
            SELECT dia, COUNT(dia) FROM vuelos
			GROUP BY dia;
            """
    resultado = ejecutar(query)
    resultado = obtenerResultados(resultado)

    dia = [{"Dia": fila[0], "Total Vuelos":fila[1]} for fila in resultado]
    return dia
    

def mayor2():
    query = """
            SELECT a.nombre_aerolinea,v.dia, COUNT(v.id_aerolinea) AS total_vuelos
            FROM vuelos v
			JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
           	GROUP BY a.nombre_aerolinea,v.dia
			HAVING COUNT(v.id_aerolinea) >= 2
			ORDER BY total_vuelos DESC;
            """
    resultado = ejecutar(query)
    resultado = obtenerResultados(resultado)
    
    mayor = [{"Aerolinea": fila[0], "Cantidad":fila[2],"Fecha":fila[1]} for fila in resultado]
    return mayor