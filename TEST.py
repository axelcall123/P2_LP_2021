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
