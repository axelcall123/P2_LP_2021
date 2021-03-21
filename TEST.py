from tkinter import filedialog
from tkinter import *
import graphviz
from datetime import date#teimpo
from datetime import datetime#teimpo
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
        print(linea_texto,contador_lineas)
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

        ['BEBIDA',fila,columna,'T_SEC'],
        ['BEBIDA 1',fila,columna,'T_ID'],['PAPAYA',fila,columna,'T_NOM'],['10.0',fila,columna,'T_PRE'],['---',fila,columna,'T_DES'],
        ['BEBIDA 2',fila,columna,'T_ID'],['SANDIA',fila,columna,'T_NOM'],['20.0',fila,columna,'T_PRE'],['???',fila,columna,'T_DES'],

        ['PASTEL',fila,columna,'T_SEC'],
        ['PASTEL 1',fila,columna,'T_ID'],['FRAMBUESA',fila,columna,'T_NOM'],['5.0',fila,columna,'T_PRE'],['***',fila,columna,'T_DES'],
        ['PASTEL 2',fila,columna,'T_ID'],['F RESA',fila,columna,'T_NOM'],['10.0',fila,columna,'T_PRE'],['¨¨',fila,columna,'T_DES'],

        ['PIZZA',fila,columna,'T_SEC'],
        ['PIZZA 1',fila,columna,'T_ID'],['PIÑA',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES'],

        ['HELAODS',fila,columna,'T_SEC'],
        ['HELAODS 1',fila,columna,'T_ID'],['A',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES'],
        ['HELAODS 2',fila,columna,'T_ID'],['B',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES'],
        ['HELAODS 3',fila,columna,'T_ID'],['C',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES'],
        ['HELAODS 4',fila,columna,'T_ID'],['D',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES'],
        ['HELAODS 5',fila,columna,'T_ID'],['E',fila,columna,'T_NOM'],['25.0',fila,columna,'T_PRE'],['##',fila,columna,'T_DES']

        ]
    
    array_nod=[]#PARA UNIR LOS NODOS
    nod = graphviz.Digraph(comment='SI')
    nod
    nod.node('A','RESTAURANTE'+'\n'+T[0][0])#TITULO PRINCIPAL
    letra='B'#COMIENZA EN B POR A->RESTAURANTE
    cont_nod=0#CUENTA LA CREACION DE UN NUEVO NODO
    cont=0#PARA SI ES MULTIPLO DE 4
    nod_principal=''
    for a in range(1,len(T)):
        caracter=chr(ord(letra)+cont_nod)#LETRA A-Z CONTADOR SUMATORIA
        if T[a][3]=='T_SEC':#VE SI ES LA SECCION
            nod_principal=caracter#TOMA EL NODO PRINCIPAL
            array_nod.append('A'+nod_principal)#UNE EL TITULO CON LOS PRINCIPALES
            nod.node(caracter,T[a][0])#BEBIDA,PASTEL,PIZZA
            cont_nod+=1#NUEVO NODO
        elif T[a][3]=='T_ID' or T[a][3]=='T_NOM' or T[a][3]=='T_PRE' or T[a][3]=='T_DES':
            cont+=1  
            if cont%4==0:
                nod.node(caracter,T[a-2][0]+'   '+T[a-1][0]+'\n'+T[a][0])#
                array_nod.append(nod_principal+caracter)#UNIR PRINCIPAL CON LOS SUB-SUB
                cont_nod+=1#NUEVO NODO
                cont=0#CONT = 0 PARA MULTIPLO DE 4
    nod.edges(array_nod)#UNE LOS NODOS
    nod.render('PDF/Hola', view=True)#IMPRIME EL PDF
    print(nod)#IMPRIME EL NODO EN CONSOLA

    cont=0
    for a in range(len(T)):
        if T[a][3]=='T_SEC':
            #div 12 
            print(T[a][0],':')
        elif T[a][3]=='T_ID' or T[a][3]=='T_NOM' or T[a][3]=='T_PRE' or T[a][3]=='T_DES':
            cont+=1  
            if cont%4==0:
                #div varios
                print(T[a-3][0],T[a-2][0],T[a-1][0],T[a][0],'||')
                #hr
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

def grap():
    dot = graphviz.Digraph(comment='SI')
    dot
    dot.node('A', 'Restaurante')
    dot.node('B', 'Bebidas')
    dot.node('C', 'Desayunos')
    dot.node('D', 'Postres')
    dot.node('E', 'BEBIDA 1')
    dot.node('F', 'BEBIDA 2')
    dot.node('G', 'POSTRES 1')
    dot.node('H', 'POSTRES 2')
    dot.edges(['AB', 'AC','AD','BE','BF','DG','DH'])
    #dot.edge('B', 'L', constraint='false')
    print(dot.source) 
    dot.render('PDF/Hola', view=True)

def xd():
    fecha=date.today()
    num="9.5"
    numDosD=float(num)
    print(str(fecha)+" "+f"{numDosD:.2f}")

xd()