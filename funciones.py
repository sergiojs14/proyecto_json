import json

def cargar_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def Menu():
    menu='''
Menu:
    1. Listar información: Mostrar la clasificacion de una temporada específica.
    2. Contar información: Contar el número total de goles marcados por cada equipo en todas las temporadas.
    3. Buscar o filtrar información: Filtrar los equipos que contienen una subcadena.
    4. Buscar información relacionada: Dado un equipo, mostrar sus estadísticas de rendimiento en diferentes temporadas.
    5. Ejercicio libre: Determinar el numero de titulos de cada equipo.
    6. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input('Opcion:'))
            while opcion < 1 or opcion > 6:
                print('Opcion incorrecta')
                opcion=int(input('Opcion:'))
            return opcion
        except:
            print('Opcion incorrecta')

def mostrar_clasificacion(datos, temporada):
    temporadas_encontradas = [item for item in datos if item["season"] == temporada]
    if not temporadas_encontradas:
        print(f"No se encontraron datos para la temporada {temporada}.")
        return
    temporada_datos = temporadas_encontradas[0]
    equipos_temporada = temporada_datos["table"]
    equipos_ordenados = sorted(equipos_temporada, key=lambda x: int(x["position"]))
    print(f"Clasificación de la temporada {temporada}")
    print(f"{'Pos':<4}{'Equipo':<25}{'PJ':<4}{'G':<4}{'E':<4}{'P':<4}{'GF':<4}{'GC':<4}{'DG':<6}{'Puntos':<7}")
    for equipo in equipos_ordenados:
        print(f"{equipo['position']:<4}{equipo['team']:<25}{equipo['played']:<4}{equipo['won']:<4}"
              f"{equipo['draw']:<4}{equipo['loss']:<4}{equipo['goals_scored']:<4}"
              f"{equipo['goals_against']:<4}{equipo['goal_difference']:<6}{equipo['points']:<7}")

def contar_goles_totales_por_equipo(datos):
    goles_por_equipo = {}
    for temporada_datos in datos:
        for equipo in temporada_datos["table"]:
            equipo_nombre = equipo["team"]
            goles = int(equipo["goals_scored"])
            if equipo_nombre not in goles_por_equipo:
                goles_por_equipo[equipo_nombre] = goles
            else:
                goles_por_equipo[equipo_nombre] += goles
    equipos_ordenados = sorted(goles_por_equipo.items(), key=lambda x: x[1], reverse=True)
    print(f"Goles totales marcados por cada equipo en todas las temporadas")
    print(f"{'Equipo':<25}{'Goles Totales':<15}")
    for equipo, goles in equipos_ordenados:
        print(f"{equipo:<25}{goles:<15}")

def filtrar_equipos_por_subcadena(datos, subcadena):
    equipos_filtrados = []
    for temporada_datos in datos:
        for equipo in temporada_datos["table"]:
            if subcadena.lower() in equipo["team"].lower() and equipo["team"] not in equipos_filtrados:
                equipos_filtrados.append(equipo["team"])
    if equipos_filtrados:
        print(f"Equipos cuyo nombre contiene '{subcadena}':")
        for equipo in equipos_filtrados:
            print(equipo)
    else:
        print(f"No se encontraron equipos que contengan '{subcadena}' en su nombre.")

def obtener_posiciones_por_equipo(datos, equipo_nombre):
    posiciones = []
    for temporada_datos in datos:
        temporada = temporada_datos["season"]
        for equipo in temporada_datos["table"]:
            if equipo["team"].lower() == equipo_nombre.lower():
                posiciones.append((temporada, equipo["position"]))
    if posiciones:
        print(f"Posiciones de {equipo_nombre} en cada temporada:")
        print('Temporada Posición')
        for temporada, posicion in posiciones:
            print(temporada,posicion)
    else:
        print(f"No se encontraron registros para el equipo '{equipo_nombre}'.")

def contar_titulos_por_equipo(datos):
    titulos_por_equipo = {}
    for temporada_datos in datos:
        for equipo in temporada_datos["table"]:
            if equipo["position"] == "1":
                equipo_nombre = equipo["team"]
                if equipo_nombre not in titulos_por_equipo:
                    titulos_por_equipo[equipo_nombre] = 1
                else:
                    titulos_por_equipo[equipo_nombre] += 1
    print("Número de títulos ganados por cada equipo")
    print(f"{'Equipo':<25}{'Títulos':<10}")
    for equipo, titulos in sorted(titulos_por_equipo.items(), key=lambda x: x[1], reverse=True):
        print(f"{equipo:<25}{titulos:<10}")
