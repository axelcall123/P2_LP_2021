import cadenas
def nombreRestaurante(texto,contador):
    texto=texto.replace('\n','')
    texto=texto+'='
    igual=texto.split('=')
    if len(igual)==3:#MIRAR SI TIEN = separaracion
        restaurante(igual[0])#RESTAURANTE
        AfdNombreRestaurante(igual[1])
    else:#[FILA,COLUMNA,CARACTER,DESCRIPCION]
        print('')

def restaurante(texto):#SI ES RESTAURANTE
    if texto.lower()=='restaurante':
        print('SI res')
    else:
        print('NO res')

def AfdNombreRestaurante(texto):
    print()
    #if texto[0].lower