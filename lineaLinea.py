import AFDrestaurante as AFDrestaurante
def leerLinea(linea_texto,contador_lineas):
    texto={}#DICCIONARIO
    texto[contador_lineas]=linea_texto#AGREGA AL DICCIONARIO
    if(contador_lineas==1):#PRIMERA LINEA ES
        AFDrestaurante.nombreRestaurante(linea_texto,contador_lineas)#PASA AL AFD DEL RES
    else:
        print(texto[contador_lineas])

        