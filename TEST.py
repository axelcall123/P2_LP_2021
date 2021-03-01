from tkinter import filedialog
from tkinter import *
def leer():
    root = Tk()
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P2_LP_2021",title = "Select file",filetypes = (("lfp files","*.lfp"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    contador_lineas=1
    for linea in archivo.readlines():
        #print(linea,contador_lineas)
        txt=restaurante(linea,contador_lineas)
        contador_lineas+=1
    print(txt)

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

def array_test():
    array_catalogo1=[]
    #[ID,NOMBRE,PRECIO,DESCRIPCION]
    array_catalogo1.append('POS_1')
    array_catalogo1.append('POSTRE LOL')
    array_catalogo1.append('88.88')
    array_catalogo1.append('ULU LULUL')
    array_catalogo1.append(' ')
    #print(array_catalogo1)
    return array_catalogo1    
    
def retornoUno():
    arrayA_catalogo=[]
    array=array_test()
    #[[B1][B2][B3]] B ALIMENTO#N
    arrayA_catalogo.append(array)
    arrayA_catalogo.append(array)
    #print(arrayA_catalogo)
    return arrayA_catalogo

def retornoDos():
    array_alimento_bebidas=[]
    array=retornoUno()
    #[ALIMENTO,arrayA_catalogo,ERROR]
    array_alimento_bebidas.append('POSTRE CABRON')
    array_alimento_bebidas.append(array)
    array_alimento_bebidas.append(' ')
    #print(array_alimento_bebidas)
    return array_alimento_bebidas    

def retornoTres():
    arrayA_alimento_bebidas=[]
    array=retornoDos()
    #[[ALIMENTOS][ALIMENTOS]
    arrayA_alimento_bebidas.append(array)
    arrayA_alimento_bebidas.append(array)
    #print(arrayA_alimento_bebidas)
    return arrayA_alimento_bebidas

def retornoCuatro():
    array_menu_restaurante=[]
    array=retornoTres()
    # [NOMBRE RESTAURANTE,array_alimento_bebidas]
    array_menu_restaurante.append('RESTAURANTE JEEJ')
    array_menu_restaurante.append(array)
    array_menu_restaurante.append(' ')
    return array_menu_restaurante

def imprimir():
    FF=retornoCuatro()
    #print(A)
    if FF[2]==' ':
        print('nombre del restaurante:',FF[0])
        for BB in FF[1]:
            if BB[2]==' ':
                print(' nombre del alimento:',BB[0])
                for CC in BB[1]:
                    if CC[4]==' ':
                        print('     ID:',CC[0],'||NOMBRE:',CC[1],'||PRECIO:',CC[2],'||DESCRIPCION:',CC[3])
        
imprimir()



