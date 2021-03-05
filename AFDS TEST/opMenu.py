def acortador(texto):# QUITAR ESPACIOS IZQUIERDA Y DERECHA
    lado=True
    unir=''
    for a in texto:#QUITA LOS ESPACIOS DE LA IZQUIERDA
        if a==' ' and lado==True:
            continue
        else:
            lado=False
            unir=unir+a
    texto=unir
    unir=''
    for n in range(len(texto)-1,-1,-1):#QUITA LOS ESPACIOS DE LA DERECHA
        if texto[n]==' ' and lado==False:
            continue
        else:  
            lado=True
            unir=unir+texto[n]
    texto=unir
    unir=''
    for n in range(len(texto)-1,-1,-1):#CADENA SEA ALREVES
        unir=unir+texto[n]
    return unir

def OpMenu(texto):
    unir=''
    a=''
    b=''
    c=''
    d=''
    if texto[0]=='[':#VERIFICACION DE []
        if texto[len(texto)-1]==']':
            for n in range(1,len(texto)-1):#QUITA LOS []
                unir=unir+texto[n]
            texto=unir
            texto=texto+';;;;'
            unir=''
            array_OpMenu=texto.split(';')#SEPARA POR ;
            a=acortador(array_OpMenu[0])
            b=acortador(array_OpMenu[1])
            c=acortador(array_OpMenu[2])
            d=acortador(array_OpMenu[3])
            array_salida=[a,b,c,d]
            print(array_salida)  
#1;2;3;4
OpMenu('[d1;‘Desayuno 1’;45.00;’Descripción Desayuno 1’]')

