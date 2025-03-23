from funciones import *
import time
opcion=0
datos=cargar_datos('premier-league-points-table.json')
while opcion != 6:
    opcion=Menu()
    if opcion == 1:
        temporada=input('Introduzca una temporada(1992/1993---2018/2019): ')
        mostrar_clasificacion(datos,temporada)
    elif opcion == 2:
        contar_goles_totales_por_equipo(datos)
    elif opcion == 3:
        subcadena=input('Introduzca la subcadena de la que se buscaran coincidencias: ')
        filtrar_equipos_por_subcadena(datos,subcadena)
    elif opcion == 4:
        nombre=input('Introduzca el nombre de un equipo: ')
        obtener_posiciones_por_equipo(datos,nombre)
    elif opcion == 5:
        contar_titulos_por_equipo(datos)
    time.sleep(2)