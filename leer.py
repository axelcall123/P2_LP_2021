import lineaLineaM as lineaLineaM
import lineaLineaO as lineaLineaO
from tkinter import filedialog
from tkinter import *
def read(TF):
    array_salida=[]
    root = Tk()#
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P2_LP_2021",title = "Select file",filetypes = (("lfp files","*.lfp"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    unir=''
    contador=0
    for linea in archivo.readlines():#LEE LINEA POR LINEA
        unir=unir+linea
        contador+=1
    if TF==True:#CARGAR MENU|ORDEN
        array_salida=lineaLineaM.afd(unir)#MENU
    else:
        array_salida=lineaLineaO.afd(unir)#MENU
    return array_salida 
    