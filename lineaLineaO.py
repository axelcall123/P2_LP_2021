#if txt[n]=='':
#Tokens.append([unir,fila,columna,'T_ID','Restaurante'])
#Errores.append([fila,columna,txt[n],"SE ESPERABA: restaurante"])
def afd(txt):
    array_salida=[]
    fila=1#/n
    columna=-1#PARA CONTAR BIEN LAS COLUMNAS# 1==/n
    state=0
    unir=''
    Tokens=[]
    Errores=[]
    for n in range(len(txt)):   
        if txt[n]=='\n':
            fila+=1
            columna=-1#PARA CONTAR BIEN LAS COLUMNAS
        if txt[n]!='\n':
            columna+=1
        print(state,'||',txt[n],n,':::')
        if state==0:#'
            if txt[n]=="'":
                state=1
        if state==1:#!'
            if txt[n]!="'":
                unir=unir+txt[n]
                state=2
        elif state==2:#'
            if txt[n]!="'":
                unir=unir+txt[n]
                state=2
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_CADENA','Nombre'])
                unir=''
                state=3          
        elif state==3:#,
            if txt[n]==' ':
                state=3
            elif txt[n]==",":
                state=4
        elif state==4:#' 0-9
            if txt[n]==' ':
                state=4
            elif txt[n]=="'":
                state=1
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=5

        elif state==5:#. %
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=5
            elif txt[n]==".":
                unir=unir+txt[n]
                state=6
            elif txt[n]=="%":
                num=float(unir)/100#8->0.08
                unir=str(num)#0.08->str 0.08
                Tokens.append([unir,fila,columna,'T_CADENA','Nombre'])
                unir=''
                state=7
        elif state==6:
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=6
            elif txt[n]=="%":
                num=float(unir)/100#8->0.08
                unir=str(num)#0.08->str 0.08
                Tokens.append([unir,fila,columna,'T_CADENA','Nombre'])
                unir=''
                state=7
        elif state==7:
            if txt[n]==" ":
            elif txt[n]==
    print(Tokens)
                
        
                
