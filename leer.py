import lineaLinea as lineaLinea
from tkinter import filedialog
from tkinter import *
def leer():
    root = Tk()#
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P2_LP_2021",title = "Select file",filetypes = (("lfp files","*.lfp"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    contador_lineas=1
    for linea in archivo.readlines():#LEE LINEA POR LINEA
        lineaLinea.leerLinea(linea,contador_lineas)
        contador_lineas+=1
leer()