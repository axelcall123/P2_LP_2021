#print(txt)
#ord(txt[n])>47 and ord(txt[n])<58:#0-9
#ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
#unir=unir+txt[n]
#columna+=1
#txt[n]==' '
#LEXEMA,FILA,COLUMNA||TOKEN#9.5,10,10,numero
#SU MASCARA
#FILA,COLUNA,CARACTER,DESCRIPCION||1,1,%,algo
#Errores.append([fila,columna,txt[n],""])
#ALFA INCIO CADENA
#OMEGA FIN DEL CICLO
array_catalogo=[]
arrayA_catalogo=[]
array_alimento_bebidas=[]
arrayA_alimento_bebidas=[]
array_menu_restaurante=[]
def afd(txt):
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
        if n+1< len(txt):
            if txt[n]=='Ω' and txt[n+1]=='Ω':#FIXME: sirve para terminar la cadena borrarlo
                for a in Tokens:
                    print(a,'T')
                for a in Errores:
                    print(a,'E')
                return
        print(state,'||',txt[n],n,':::')
        if state==0:#a-z
            if ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=0             
            elif txt[n]=='=':
                if unir.lower()=='restaurante':
                    Tokens.append([unir,fila,columna,'T_Restaurante'])#RESTAURANTE               
                else:
                    Errores.append([fila,columna,txt[n],"SE ESPERABA: restaurante"]) 
                unir=''
                state=1
            else:
                if txt[n]=="'":
                    Errores.append([fila,columna,txt[n],"SE ESPERABA: ="])
                    Tokens.append([' ',fila,columna,'T_Restaurante'])
                    unir='' 
                    state=2
        elif state==1:#=
            if txt[n]=="'":
                state=2
            else:
                Errores.append([fila,columna,txt[n],"SE ESPERABA:'"])
                state=-1
        elif state==-1:#Restaurante LFP'
            if txt[n]=="'":
                state=4
                Tokens.append([' ',fila,columna,'T_Res'])
            else:  
                state=-1
        elif state==2:#'
            if txt[n]!="'":
                state=3
                unir=unir+txt[n]
            elif txt[n]=="'":#ADMITE VACIA
                unir=''
                Tokens.append([unir,fila,columna,'T_Res'])
                state=4
        elif state==3:# cualquier !'
            if txt[n]!="'":
                state=3
                unir=unir+txt[n]
            elif txt[n]=="'":
                state=4
                Tokens.append([unir,fila,columna,'T_Res'])#NOMBRE DEL RESTAURANTE
                unir=''
            #else:#DIFIL VER ALGUN ERROR CON ESTO
                #print('ERROR',txt[n])
                #return
        #TODO:COMIENZA SECCION 
        elif state==4:#'
            if txt[n]=='\n' or txt[n]==' ':
                state=4
            elif txt[n]=="'":
                state=5
            else:
                Errores.append([fila,columna,txt[n],"SE ESPERABA: '"])
                state=-4
                #print('ERROR4',txt[n])
        elif state==-4:#ERROR 'Restaurante LFP
            if txt[n]=="'":
                state=6
            else:
                state=-4
        elif state==5:#' '|/n
            if txt[n]!="'":
                unir=unir+txt[n]
                state=5
            elif txt[n]=="'":
                state=6
                Tokens.append([unir,fila,columna,'T_SEC'])#NOMBRE DE SECCION
                unir=''
            else:
                #D
                print('ERROR',txt[n])
                return
        elif state==6:#'
            if txt[n]==' ':
                state=6
            elif txt[n]==':':
                state=8
            else:
                Errores.append([fila,columna,txt[n],"SE ESPERABA: ,:"])
                state=-6
        elif state==-6:#ERROR 'Bebidas1' 2:
            if txt[n]=='[':
                state=10
            else:
                state=-6
        # elif state==7:#' '
        #     if txt[n]==' ':
        #         state=7
        #     elif txt[n]==':':
        #         state=8
        elif state==8:#:
            if txt[n]==' ' or txt[n]=='\n':
                state=8
            elif txt[n]=='[':
                state=10
            else:
                Errores.append([fila,columna,txt[n],"SE ESPERABA: ,salto,["])
                state=-8
        # elif state==9:#' '|\n
        #     if txt[n]==' ' or txt[n]=='\n':
        #         state=9
        #     elif txt[n]=='[':
        #         state=10
        elif state==-8:#ERRRO :2
            if txt[n]=="[":
                state=10
            else:
                state=-8
        elif state==10:#[
            if txt[n]==' ':
                state=11
            elif ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=12
            else:
                print('ERROR10',txt[n])
                return
        elif state==11:#' '
            if txt[n]==' ':
                state=11
            elif ord(txt[n].lower())>96 and ord(txt[n].lower())<123:#a-z
                unir=unir+txt[n]
                state=12
            else:
                print('ERROR')
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
            else:
                print('ERROR')
        elif state==13:#0-9
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
            elif txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_ID'])#IDENTIFICADOR
                unir=''
                state=-14
            elif txt[n]==';':#;
                Tokens.append([unir,fila,columna,'T_ID'])#IDENTIFICADOR
                unir=''
                state=15
            else:
                print('ERROR')
        elif state==-14:
            if txt[n]==' ':
                state=-14
            elif txt[n]==';':
                state=15
        elif state==14:#_
            if txt[n]=='_':#_
                unir=unir+txt[n]
                state=14
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=13
            else:
                print('ERROR')
        elif state==15:#'
            if txt[n]==' ':
                state=15
            elif txt[n]=="'":
                state=17
            else:
                print('ERROR')
        # elif state==16:#' '
        #     if txt[n]==' ':
        #         state=16
        #     elif txt[n]=="'":
        #         state=17
        elif state==17:#'
            if txt[n]!="'":
                unir=unir+txt[n]
                state=18
            else:
                print('ERROR')
        elif state==18:#!'
            if txt[n]!="'":
                unir=unir+txt[n]
                state=18
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_NOMBRE'])#NOMBRE
                unir=''
                state=19
            else:
                print('ERROR')
        elif state==19:#' '
            if txt[n]==' ':
                state=19
            elif txt[n]==';':
                state=21
            else:
                print('ERROR')
        # elif state==20:#';'
        #     if txt[n]==' ':
        #         state=20
        #     elif txt[n]==';':
        #         state=21
        elif state==21:#' '|0-9
            if txt[n]==' ':
                state=21
            elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=23
            else:
                print('ERROR')
        # elif state==22:#0-9
        #     if txt[n]==' ':
        #         state=22
        #     elif ord(txt[n])>47 and ord(txt[n])<58:#0-9
        #         unir=unir+txt[n]
        #         state=23
        elif state==23:#.|;|' '
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=23     
            elif txt[n]=='.':
                unir=unir+txt[n]
                state=24
            elif txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=25
            elif txt[n]==';':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=26
            else:
                print('ERROR')
        elif state==24:#' '|;
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=27
            elif txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=25
            elif txt[n]==';':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=26
            else:
                print('ERROR')
        elif state==25:#;
            if txt[n]==' ':
                state=25
            elif txt[n]==';':
                state=26
            else:
                print('ERROR')
        elif state==26:#' '|'
            if txt[n]==' ':
                state=26
            elif txt[n]=="'":
                state=29
            else:
                print('ERROR')
        elif state==27:#' '|;
            if ord(txt[n])>47 and ord(txt[n])<58:#0-9
                unir=unir+txt[n]
                state=27
            elif txt[n]==' ':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=25
            elif txt[n]==';':
                Tokens.append([unir,fila,columna,'T_NUM'])#PRECIO
                unir=''
                state=26
            else:
                print('ERROR')
        # elif state==28:#'
        #     if txt[n]==' ':
        #         state=28
        #     elif txt[n]=="'":
        #         state=29
        elif state==29:#'
            if txt[n]!="'":
                unir=unir+txt[n]
                state=29
            elif txt[n]=="'":
                Tokens.append([unir,fila,columna,'T_DES'])#DESCRIPCION
                unir=''
                state=30
            else:
                print('ERROR')
        elif state==30:#]
            if txt[n]==' ':
                state=30
            elif txt[n]==']':
                state=31
            else:
                print('ERROR')
        elif state==31:#' '|\n
            if txt[n]==' ' or txt[n]=='\n':
                state=31
            elif txt[n]=='[':
                state=10
            elif txt[n]=="'":
                state=5
    ##CE ACABO EMPIEZA LA RECURSIVIDAD DE 'abc':|[]
    

        