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

def principal(texto):
    unir=''
    a=''
    b=''
    c=''
    d=''
    #SIRVEN PARA TOMAR O NO TOMAR EN CUENTA LOS [...........]
    num1=1
    num2=1
    if texto[0]!='[':#VERIFICACION DE []
        num1=0
        if texto[len(texto)-1]!=']':
            num1=0
            
    for n in range(num1,len(texto)-num2):#QUITA LOS []
        unir=unir+texto[n]
    texto=unir
    texto=texto+';;;;'#POR SI NO VIENE PONER LOS 4
    unir=''
    array_OpMenu=texto.split(';')#SEPARA POR ;
    a=acortador(array_OpMenu[0])
    b=acortador(array_OpMenu[1])
    c=acortador(array_OpMenu[2])
    d=acortador(array_OpMenu[3])
    txt=a+';'+b+';'+c+';'+d
    print(txt)

#1;2;3;4
principal('[   d1   ;   ‘Desayuno 1’   ;   45.00   ;   Descripción Desayuno 1’   ]')

