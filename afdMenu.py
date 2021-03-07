import acortadorEspacios as acortadorEspacios
def menu(texto,fila):
    textoN=''
    textoN=acortadorEspacios.principal(texto)
    if textoN[0]=='’':
        print()#CADENA
    elif ord(textoN[0])>47 and ord(textoN[0])<58:#0-9
        print()#NUMERO
    elif ord(textoN[0].lower())>96 and ord(textoN[0].lower())<123:#a-<:
        print()#IDENTIFICADOR