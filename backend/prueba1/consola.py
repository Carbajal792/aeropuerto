import funciones

def main():
    print("\nResultados de la primera parte de la prueba\n")

    contestadas, no_contestadas = funciones.conteo()
    print(f"Preguntas contestadas: {contestadas}")
    print(f"Preguntas no contestadas: {no_contestadas}\n")

    reputacion = funciones.reputacion()
    print("Pregunta con mayor reputación:")
    if reputacion:
        print(f"Título: {reputacion['title']}")
        print(f"Reputación: {reputacion['owner'].get('reputation', 'N/A')}")
        print(f"Enlace: {reputacion['link']}\n")
    else:
        print("No se pudo obtener la información.\n")

    vista = funciones.menosVistas()
    print("Pregunta con menos vistas:")
    if vista:
        print(f"Título: {vista['title']}")
        print(f"Vistas: {vista['view_count']}")
        print(f"Enlace: {vista['link']}\n")
    else:
        print("No se pudo obtener la información.\n")

    antigua = funciones.antigua()
    print("Pregunta contestada más antigua:")
    if antigua:
        print(f"Título: {antigua['title']}")
        print(f"Última actividad: {antigua['last_activity_date']}")
        print(f"Enlace: {antigua['link']}\n")
    else:
        print("No se pudo obtener la información.\n")

    reciente = funciones.actual()
    print("Pregunta contestada más reciente:")
    if reciente:
        print(f"Título: {reciente['title']}")
        print(f"Última actividad: {reciente['last_activity_date']}")
        print(f"Enlace: {reciente['link']}\n")
    else:
        print("No se pudo obtener la información.\n")

if __name__ == "__main__":
    main()
