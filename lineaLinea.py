#print(txt)
#ord(txt[n])>47 and ord(txt[n])<58:#0-9
#ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
#unir=unir+txt[n]
#columna+=1
#LEXEMA,FILA,COLUMNA||TOKEN#9.5,10,10,numero
#FILA,COLUNA,CARACTER,DESCRIPCION||1,1,%,algo
#txt[n]==' '
def afd(txt):
    fila=1#/n
    columna=0# 1==/n
    state=1
    unir=''
    for n in range(len(txt)):
        if txt[n]=='\n':
            fila+=1
            columna=1
        if txt[n]!='\n':
            columna+=1
        print(state,'||',txt[n],n,':::')
        if state==0:#a-z
            if ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=0             
            elif txt[n]=='=':
                print(unir,fila,columna,'T_res')
                unir=''
                state=1
                #unir=unir+txt[n]
        elif state==1:#=
            if txt[n]=="'":
                state=2
                #unir=unir+txt[n]
        elif state==2:#'
            if txt[n]!="'":
                state=3
                unir=unir+txt[n]
        elif state==3:# cualquier !'
            if txt[n]!="'":
                state=3
                unir=unir+txt[n]
            elif txt[n]=="'":
                state=4
                print(unir,fila,columna,'T_Cadena')
                unir=''
                #unir=unir+txt[n]
        elif state==4:#'
            if txt[n]=='\n' or txt[n]==' ':
                state=4
            elif txt[n]=="'":
                state=5
        elif state==5:#' '|/n
            if txt[n]!="'":
                unir=unir+txt[n]
                state=5
            elif txt[n]=="'":
                state=6
                print(unir,fila,columna,'T_Cadena')
                unir=''
        elif state==6:#'
            if txt[n]==' ':
                state=7
        elif state==7:#' '
            if txt[n]==' ':
                state=7
            elif txt[n]==':':
                state=8
        elif state==8:#:
            if txt[n]==' ' or txt[n]=='\n':
                state=9
        elif state==9:#' '|\n
            if txt[n]==' ' or txt[n]=='\n':
                state=9
            elif txt[n]=='[':
                state=10
        elif state==10:#[
            if txt[n]==' ':
                state=11
            elif ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=12
        elif state==11:#' '
            if txt[n]==' ':
                state=11
            elif ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=12
        #[l][a-z][0-9]|[l][a-z][_][0][0-9]:
        elif state==12:#a-z
            if ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=12
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
            elif txt[n]=='_':
                unir=unir+txt[n]
                state=14
        elif state==13:#0-9
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
            elif txt[n]==';':#;
                print(unir,fila,columna,'T_Id')
                unir=''
                state=15
        elif state==14:#_
            if txt[n]=='_':#_
                unir=unir+txt[n]
                state=14
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
        elif state==15:#'
            if txt[n]==' ':
                state=16
        elif state==16:#' '
            if txt[n]==' ':
                state=16
            elif txt[n]=="'":
                print()
    #print(txt,linea,columna)
    

        