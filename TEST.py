from tkinter import filedialog
from tkinter import *
def leer():
    root = Tk()
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P2_LP_2021",title = "Select file",filetypes = (("lfp files","*.lfp"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    contador_lineas=1
    for linea in archivo.readlines():
        #print(linea,contador_lineas)
        restaurante(linea,contador_lineas)
        contador_lineas+=1


def restaurante(linea_texto,contador_lineas):
    texto={}
    texto[contador_lineas]=linea_texto
    if(contador_lineas==1):
        print(linea_texto,'UNO')
    else:
        print(texto[contador_lineas])

def numero():#COMO SE MUESTRAN LOS NUMEROS
    uno=40.
    dos=40
    tres=40.000
    print(uno,dos,tres)
    
#imprimir()
def wuamos():
    fila=0
    columna=0
    T=[
        ['BLABLA',fila,columna,'T_RES'],

        ['UNO',fila,columna,'T_SEC'],
        ['a',fila,columna,'T_ID'],['b',fila,columna,'T_NOM'],['c',fila,columna,'T_PRE'],['d',fila,columna,'T_DES'],
        ['e',fila,columna,'T_ID'],['f',fila,columna,'T_NOM'],['g',fila,columna,'T_PRE'],['h',fila,columna,'T_DES'],

        ['DOS',fila,columna,'T_SEC'],
        ['A',fila,columna,'T_ID'],['B',fila,columna,'T_NOM'],['C',fila,columna,'T_PRE'],['D',fila,columna,'T_DES'],
        ['E',fila,columna,'T_ID'],['F',fila,columna,'T_NOM'],['G',fila,columna,'T_PRE'],['H',fila,columna,'T_DES'],

        ['TRES',fila,columna,'T_SEC'],
        ['1',fila,columna,'T_ID'],['2',fila,columna,'T_NOM'],['3',fila,columna,'T_PRE'],['4',fila,columna,'T_DES']
        ]
    cont=0
    for a in range(len(T)):
        if T[a][3]=='T_SEC':
            print(T[a][0],':')
        elif T[a][3]=='T_ID' or T[a][3]=='T_NOM' or T[a][3]=='T_PRE' or T[a][3]=='T_DES':
            cont+=1  
            if cont%4==0:
                print(T[a-3][0],T[a-2][0],T[a-1][0],T[a][0],'||')
                cont=0
                
        #print(T[a][3],'***')
#wuamos()

def tilde(letra):
    if letra=='á':
        return 'a'
    elif letra=='é':
        return 'e'
    elif letra=='í':
        return 'i'
    elif letra=='ó':
        return 'o'
    elif letra=='ú':
        return 'u'  
    elif letra=='ñ':
        return 'n'
    else:
        return letra
    
def textos(txt):#Á->á->a
    unir=''
    for a in txt:
        #print(a,a.lower(),ord(a.lower()),tilde(a.lower()),ord(tilde(a.lower())))
        if ord(tilde(a.lower()))>96 and ord(tilde(a.lower()))<123 or a==' ':#a-z
            unir=unir+a
    print(unir)

def numeros():
    a='1'
    b='1.'
    c='1.0'
    print(str(float(a))+'0',str(float(b)),str(float(c)))

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
                state=13