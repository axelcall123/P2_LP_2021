#'->a-z->{a-z| }->a-z->'
#LEXEMA,FILA,COLUMNA,TOKEN#9.5,10,10,numero
#FILA,COLUNA,CARACTER,DESCRIPCION#1,1,%,algo
def cadenasT(texto,fila):
    unir=''
    state=0
    palabra=''
    for n in range(len(texto)):#NO TOMAR EN CUENTA ‘a1d’ 
        if state==0:
            if texto[n]!="’":#DIF DE ’
                unir=unir+texto[n]
            elif texto[n]=="’" and (len(texto)-1)!=n:
                palabra=unir
                print(palabra+'||'+str(fila)+'||'+str(n+1)+'||'+'T_SECCION')  
                state=1
            else:
                print(str(fila)+'||'+str(n+1)+'||'+' '+'||'+'E:SE ESPERABA :')
        elif state==1:
            if texto[n]==' ':
                continue
            elif texto[n]==':' and len(texto)-1==n:
                print(':'+'||'+str(fila)+'||'+str(n+1)+'||'+'T_:')
            else:
                print(str(fila)+'||'+str(n+1)+'||'+texto[n]+'||'+'E:CARACTER NO VALIDO')
                

cadenasT("hola como le va’  :",0)