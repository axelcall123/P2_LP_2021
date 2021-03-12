import Html as Html
#if txt[n]=='':
#Tokens.append([unir,fila,columna,'T_ID','Restaurante'])
#Errores.append([fila,columna,txt[n],"SE ESPERABA:"])
def afd(txt):
    array_salida=[]
    fila=1#/n
    columna=0#PARA CONTAR BIEN LAS COLUMNAS# 1==/n
    state=0
    unir=''
    Tokens=[]
    Errores=[]
    tres=1
    for n in range(len(txt)):   
        if txt[n]=='\n':
            fila+=1
            columna=-1#PARA CONTAR BIEN LAS COLUMNAS
        if txt[n]!='\n':
            columna+=1
        print(state,'||',txt[n],n,fila,columna,len(txt))
        if state==0:
            if txt[n]=="'":
                state=1
        if state==1:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=2
        elif state==2:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=2
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_CADENA','NOMBRE'])
                unir=''
                state=3          
        elif state==3:
            if txt[n]==' ':
                state=3
            if txt[n]==",":
                state=4

        elif state==4:
            if txt[n]==' ':
                state=4
            elif txt[n]=="'":
                state=5
        elif state==5:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=6
        elif state==6:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=6
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_CADENA','NIT'])
                unir=''
                state=7
        elif state==7:
            if txt[n]==' ':
                state=7
            elif txt[n]==",":
                state=8
        elif state==8:
            if txt[n]==' ':
                state=8
            elif txt[n]=="'":
                state=9
        elif state==9:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=10
        elif state==10:
            if txt[n]!="'":
                unir=unir+txt[n]
                state=10
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_CADENA','FECHA'])
                unir=''
                state=11
        elif state==11:
            if txt[n]==' ':
                state=11
            elif txt[n]==',':
                state=12
        elif state==12:
            if txt[n]==' ':
                state=12
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13



        elif state==13:#. %
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
            elif txt[n]==".":
                unir=unir+txt[n]
                state=14
            elif txt[n]=="%":
                num=float(unir)/100#8->0.08
                unir=str(num)#0.08->str 0.08
                Tokens.append([unir,fila,columna,'T_NUMERO','PORCENTAJE'])
                unir=''
                state=15
        elif state==14:
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=14
            elif txt[n]=="%":
                num=float(unir)/100#8->0.08
                unir=num#0.08->str 0.08
                Tokens.append([unir,fila,columna,'T_NUMERO','PORCENTAJE'])
                unir=''
                state=15
        elif state==15:#0-9
            if txt[n]=='\n' or txt[n]==' ':
                state=15
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9:
                unir=unir+txt[n]
                state=16
        elif state==16:#' ' ,
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9:
                unir=unir+txt[n]
                state=16
            elif txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_NUMERO','CANTIDAD'])
                unir=''
                state=17
            elif txt[n]==",":
                Tokens.append([unir,fila,columna,'T_NUMERO','CANTIDAD'])
                unir=''
                state=18
        elif state==17:#,
            if txt[n]==' ':
                state=17
            elif txt[n]==",":
                state=18
        elif state==18:#a-z
            if txt[n]==' ':
                state=18
            elif ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=19
        elif state==19:#0-9 _
            if ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=19
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9:
                unir=unir+txt[n]
                state=20
            elif txt[n]=="_":
                unir=unir+txt[n]
                state=21
        elif state==20:#' ' \n
            if int(len(txt)-1)==n:
                unir=unir+txt[n]
                Tokens.append([unir,fila,columna,'T_ID','ID'])
                unir=''
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9:
                unir=unir+txt[n]
                state=20
            elif txt[n]=='\n' or txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_ID','ID'])
                unir=''
                state=15           
        elif state==21:#0-9
            if txt[n]=="_":
                unir=unir+txt[n]
                state=21
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9:
                unir=unir+txt[n]
                state=20
    Html.tokenHtml(Tokens)
    array_salida.append(Tokens)
    array_salida.append(Errores)
    return array_salida
                
        
                
