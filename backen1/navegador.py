import funciones
funciones.logging.basicConfig(level=funciones.logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
app = funciones.Flask(__name__)
funciones.CORS(app)
@app.route("/stack/contar", methods=["GET"])
def contar():
    contestadas, no_contestadas = funciones.conteo()
    if contestadas is not None and no_contestadas is not None:
        response =  funciones.make_response(funciones.jsonify({
            "Contestadas": contestadas,
            "No contestadas": no_contestadas
        }))
        return funciones.configurar_cors(response)
    else:
        response = funciones.make_response(funciones.jsonify({"error": "Error al obtener los datos"}), 500)
        return funciones.configurar_cors(response)

@app.route("/stack/reputacion", methods=["GET"])
def reputacion():
    mayor = funciones.reputacion()
    if mayor is not None:
        response = funciones.make_response(funciones.jsonify({
            "Titulo": mayor.get("title", "No disponible"),
            "Etiquetas": ", ".join(mayor.get("tags", [])),
            "Respondida": "Si" if mayor.get("is_answered") else "No",
            "Vistas": mayor.get("view_count", "N/A"),
            "Puntaje": mayor.get("score", "N/A"),
            "Usuario": mayor.get("owner", {}).get("display_name", "Desconocido"),
            "Reputacion del usuario": mayor.get("owner", {}).get("reputation", "N/A"),
            "Link a la pregunta": mayor.get("link", "No disponible")
        }))
       
        return funciones.configurar_cors(response)
    else:
        response = funciones.make_response(funciones.jsonify({"error": "Error al obtener los datos"}), 500)
        return funciones.configurar_cors(response)
    
@app.route("/stack/vistas", methods=["GET"])
def vistas():
    menos = funciones.menosVistas()
    print(menos)
    if menos is not None:
        response = funciones.make_response(funciones.jsonify({
            "Titulo": menos.get("title", "No disponible"),
            "Etiquetas": ", ".join(menos.get("tags", [])),
            "Respondida": "Si" if menos.get("is_answered") else "No",
            "Vistas": menos.get("view_count", "N/A"),
            "Puntaje": menos.get("score", "N/A"),
            "Usuario": menos.get("owner", {}).get("display_name", "Desconocido"),
            "Reputacion del usuario": menos.get("owner", {}).get("reputation", "N/A"),
            "Link a la pregunta": menos.get("link", "No disponible")
        }))
        return funciones.configurar_cors(response)
    else:
        response = funciones.make_response(funciones.jsonify({"error": "Error al obtener los datos"}), 500)
        return funciones.configurar_corsres(response)

@app.route("/stack/fecha", methods=["GET"])
def antiguaActual():
    try:
        antigua = funciones.antigua()
        print(antigua)
        actual= funciones.actual()
        print(actual)
        if antigua is not None and actual is not None:
            response = funciones.make_response(funciones.jsonify({  
                "Pregunta mas antigua": {
                    "Titulo": antigua.get("title", "No disponible"),    
                    "Etiquetas": ", ".join(antigua.get("tags", [])),
                    "Respondida": "Si" if antigua.get("is_answered") else "No",
                    "Vistas": antigua.get("view_count", "N/A"),
                    "Puntaje": antigua.get("score", "N/A"),
                    "Usuario": antigua.get("owner", {}).get("display_name", "Desconocido"),
                    "Reputacion del usuario": antigua.get("owner", {}).get("reputation", "N/A"),
                    "Link a la pregunta": antigua.get("link", "No disponible"),
                    "Fecha": antigua.get("last_activity_date","N/A")
                },
                    "Pregunta mas actual":{
                    "Titulo": actual.get("title", "No disponible"),
                    "Etiquetas": ", ".join(actual.get("tags", [])),
                    "Respondida": "Si" if actual.get("is_answered") else "No",
                    "Vistas": actual.get("view_count", "N/A"),
                    "Puntaje": actual.get("score", "N/A"),
                    "Usuario": actual.get("owner", {}).get("display_name", "Desconocido"),
                    "Reputacion del usuario": actual.get("owner", {}).get("reputation", "N/A"),
                    "Link a la pregunta": actual.get("link", "No disponible"),
                    "Fecha": actual.get("last_activity_date","N/A")
                }}))
            
            return funciones.configurar_cors(response)
        else:
            response = funciones.make_response(funciones.jsonify({"error": "Error al obtener los datos"}), 500)
            return funciones.configurar_cors(response)
    except Exception as e:

        response = funciones.make_response(funciones.jsonify({"error": str(e)}), 500)
    return funciones.configurar_cors(response)        

@app.route('/vuelos/masMovimiento', methods=['GET'])
def movimiento():
    try:
        resultado = funciones.masMovimiento()
        
        if resultado:

            response = funciones.make_response(funciones.jsonify(resultado))
            return funciones.configurar_cors(response)
        else:

            response = funciones.make_response(funciones.jsonify({"error": "No se encontraron resultados"}), 404)
            return funciones.configurar_cors(response)
    except Exception as e:
        
        response = funciones.make_response(funciones.jsonify({"error": str(e)}), 500)
        return funciones.configurar_cors(response)


@app.route('/vuelos/masVuelos', methods=['GET'])
def vuelos():
    try:
        resultado = funciones.masVuelos()
        
        if resultado:
            
            response = funciones.make_response(funciones.jsonify(resultado))
            return funciones.configurar_cors(response)
        else:
            
            response = funciones.make_response(funciones.jsonify({"error": "No se encontraron resultados"}), 404)
            return funciones.configurar_cors(response)
    except Exception as e:
    
        response = funciones.make_response(funciones.jsonify({"error": str(e)}), 500)
        return funciones.configurar_cors(response)

@app.route("/vuelos/dia", methods=['GET'])
def dia():
    try:
        resultado = funciones.dia()
        if resultado:
            
            response = funciones.make_response(funciones.jsonify(resultado))
            return funciones.configurar_cors(response)
        else:
            
            response = funciones.make_response(funciones.jsonify({"error": "No se encontraron resultados"}), 404)
            return funciones.configurar_cors(response)
    except Exception as e:
    
        response = funciones.make_response(funciones.jsonify({"error": str(e)}), 500)
        return funciones.configurar_cors(response)

@app.route("/vuelos/mayor2", methods=['GET'])
def mayor():
    try:
        resultado = funciones.mayor2()
        if resultado:
            
            response = funciones.make_response(funciones.jsonify(resultado))
            return funciones.configurar_cors(response)
        else:
            
            response = funciones.make_response(funciones.jsonify({"error": "No se encontraron resultados"}), 404)
            return funciones.configurar_cors(response)
    except Exception as e:
        
        response = funciones.make_response(funciones.jsonify({"error": str(e)}), 500)
        return funciones.configurar_cors(response)
    
if __name__ == "__main__":
    app.run(debug=True)
