import webbrowser#pag
from datetime import date#teimpo
from datetime import datetime#teimpo
def tokenHtml(array,tf):
    texto=''
    IR= '<tr>'
    FR='</tr>'
    FD='</td>'
    ID='<td>'
    ih='<th scope="row">'
    fh='</th>'
    cont=1
    #HTML NORMAL
    if tf==True:#SI ES TOKENS
      for a in array:
        if a[0]!=' ' or a[0]!='':
          if a[4]=='PORCENTAJE':#CONVETIR DE 0.08 A 8%
            texto=texto+IR  +ih+str(cont)+fh   +ID+str(float(a[0])*100)+'%'+FD   +ID+str(a[1])+FD  +ID+str(a[2])+FD  +ID+str(a[3])+FD+   FR
          else:
            texto=texto+IR  +ih+str(cont)+fh   +ID+str(a[0])+FD   +ID+str(a[1])+FD  +ID+str(a[2])+FD  +ID+str(a[3])+FD+   FR
          cont+=1
    else:
       for a in array:
          texto=texto+IR  +ih+str(cont)+fh   +ID+str(a[0])+FD   +ID+str(a[1])+FD  +ID+str(a[2])+FD  +ID+str(a[3])+FD+   FR
          cont+=1

    Tokens(texto,tf)
def Tokens(txt,tf):
  if tf==True:
    f = open('Tokens.html','w')
  else:
     f = open('Errores.html','w')
  principalT = """
  <!DOCTYPE html>
      <html lang="es">
      <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      
      <link rel="stylesheet" href="css/css.css">
      <link rel="stylesheet" href="boos/bootstrap.css">
      <title>Document</title>
      </head>
      <body>
        <table class="table">
              <thead class="thead-dark">
                  <tr class="menu">
                      <th scope="col">No.</th>
                      <th scope="col">Lexema</th>
                      <th scope="col">Fila</th>
                      <th scope="col">Columna</th>
                      <th scope="col">Token</th>
                  </tr>
              </thead>
              <tbody>
      """
  principalE = """
  <!DOCTYPE html>
      <html lang="es">
      <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      
      <link rel="stylesheet" href="css/css.css">
      <link rel="stylesheet" href="boos/bootstrap.css">
      <title>Document</title>
      </head>
      <body>
        <table class="table">
              <thead class="thead-dark">
                  <tr class="menu">
                      <th scope="col">No.</th>
                      <th scope="col">Fila</th>
                      <th scope="col">Columna</th>
                      <th scope="col">Caracter</th>
                      <th scope="col">Descripcion</th>
                  </tr>
              </thead>
              <tbody>
      """
  cuerpos=txt
  fin= """
              </tbody>
      </table>
  </body>
  <script src="boos/bootstrap.js"></script>
  </html>"""
  if tf==True:
    f.write(principalT)#inicio
  else:
    f.write(principalE)#inicio
  f.write(cuerpos)#medio
  f.write(fin)#final
  f.close()#cerar
  if tf==True:
    webbrowser.open_new_tab('Tokens.html')
  else:
    webbrowser.open_new_tab('Errores.html')
#---------------------
def menuHtml(array,limite):
  texto=""
  nombreRestI="""
        <div class="collapse" id="navbarToggleExternalContent">
            <div class="bg-dark p-4">
              <h5 class="text-white h4">RESTAURANTE</h5>
              <span class="text-muted">
  """
  nombreRestF="""</span>
            </div>
          </div>
          <nav class="navbar navbar-dark bg-dark">
            <div class="container-fluid">
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            </div>
          </nav>
          <div class="container body">
            <div class="row">
                <div class="col-md-1">*</div>
                <div class="col-md-10 catalogo">
  """
  #SIERVE PARA BEBIDAS:
  seccionI="""<div class="col-md-12"><p class="Titulo">"""
  seccionF="""</p></div>"""
  #SIRVE PARA todo BEBIDAS|Q11.0|JSDFKLSDÑJFA
  productoI="""<div class="container"><div class="row cuadros">"""
  productoF="""</div></div>"""
  
  colMd6="""<div class="col-md-6">"""

  divF="""</div>"""

  subTitulo="""<div class="col-md-12"><p class="sub-titulo">"""
  precio="""<div class="col-md-12"><p class="precio">"""
  textoS="""<div class="col-md-12"><p class="texto">"""

  sptF="""</p></div>"""

  #TOKENS:
  texto=texto+nombreRestI+array[1][0]+nombreRestF#menuThtml
  contCuatro=0
  parImpar=0
  for a in range(2,len(array)):
    if array[a][4]=="SECCION":
      texto=texto+seccionI+array[a][0]+seccionF
      #print(array[a][0])
    elif array[a][4]=="ID" or array[a][4]=="NOMBRE" or array[a][4]=="NUMERO" or array[a][4]=="DESCRIPCION":
      contCuatro+=1
      if contCuatro%4==0:#PARA CONTAR SECCION|NOMBRE|NUMERO|DESCRIPCION
        if limite>=float(array[a-1][0]):#LIMITE DE LOS OBJETOS
          #ID|NOMBRE|NUMERO|DESCRIPCION
          subPrecio=subTitulo+str(array[a-3][0])+sptF+  precio+'Q'+str(array[a-1][0])+sptF#ID|PRECIO
          textoM=textoS+str(array[a][0])+sptF#TEXTO
          if parImpar%2==0:
            texto=texto+productoI+colMd6+  subPrecio +divF+ colMd6+ textoM +divF+productoF
          else:
            texto=texto+productoI+colMd6+  textoM  +divF+ colMd6+  subPrecio  +divF+productoF
          parImpar+=1
          #print(' ',array[a-3][0],array[a-2][0],str(float(array[a-1][0])),array[a][0])
        contCuatro=0
  Menu(texto)
def Menu(txt):
  f = open('Menu.html','w')
  principal= """
  <!DOCTYPE html>
  <html lang="es">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

  <link rel="stylesheet" href="css/cssM.css">
  <link rel="stylesheet" href="boos/bootstrap.css">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Cinzel&family=Raleway:wght@500&family=Ranchers&display=swap" rel="stylesheet">
  <title>Document</title>
  </head>
  <body>"""
  fin="""
  </body>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </html>
  </html>
  """
  cuerpos=txt
  f.write(principal)
  f.write(cuerpos)#medio
  f.write(fin)#final
  f.close()#cerar
  webbrowser.open_new_tab('Menu.html')
#---------------------
def facturaHtml(menu,orden):
  contCuatro=0
  contPar=0
  listaMenu=[]
  listaOrden=[]
  despacho=[]
  for a in range(len(menu)):#TUPLA[ID,NOMBRE,PRECIO]{-3,-2,-1}
    if menu[a][4]=="ID" or menu[a][4]=="NOMBRE" or menu[a][4]=="NUMERO" or menu[a][4]=="DESCRIPCION":
      contCuatro+=1
      if contCuatro%4==0:
        listaMenu.append([menu[a-3][0],menu[a-2][0],menu[a-1][0]])
        contCuatro=0
  for a in range(len(orden)):#TUPLA[ID,CANTIDAD]{0,-1}
    if orden[a][0]!='':
      if orden[a][4]=="ID" or orden[a][4]=="CANTIDAD":
        contPar+=1
        if contPar%2==0:
          listaOrden.append([orden[a][0],orden[a-1][0]])
          contPar=0
  total=0
  for a in listaOrden:#si id(menu)=id(orden)
    for b in listaMenu:
      if a[0].lower()==b[0].lower():
        #CANITDAD|NOMBRE|PRECIO|PRECIO*CANTIDAD
        subtotal=float(b[2])*float(a[1])
        total=total+subtotal
        despacho.append([a[1],b[1],b[2],subtotal])
  propina=total*(float(orden[3][0]))
  #print(listaMenu,listaOrden)
  TotalMasPropina=total+propina
  numeroF=0
  fecha=date.today()
  #print(despacho,total,propina,TotalMasPropina)
  texto=""
  div12="""<div class="col-12">"""
  divf="""</div>"""
  br="""<br>"""
  #                   restaurante          factura No.1         12-02-12
  texto=texto+div12+menu[1][0]+br+"factura No."+str(numeroF)+br+"Fecha: "+str(fecha)+divf
  div12Datos="""<div class="col-12 datos">"""
  #                                               nombre:pepe               Nit:123               direccion: ciudad               descripcion   
  texto=texto+div12Datos+"Datos del cliente"+br+"Nombre: "+orden[0][0]+br+"Nit:"+orden[1][0]+br+"Direccion: "+orden[2][0]+br+br+"Descripcion"+divf
  incioTablaD="""
    <div class="col-12">
      <table class="table table-borderless">
          <thead>
            <tr>
              <th scope="col">cantidad</th>
              <th scope="col">Concepto</th>
              <th scope="col">Precio</th>
              <th scope="col">Total</th>
            </tr>
          </thead>
          <tbody>
  """
  inicioTablaG="""
    <hr>
    <div class="col-12">
      <table class="table table-borderless">
        <tbody>
  """

  fintTabla="""
        </tbody>
      </table>
    </div>
  """
  tri="<tr>"
  trf="</tr>"
  tdi="<td>"
  tdf="</td>"
  tdL="""<td class="left">"""
  tdR="""<td class="rigth">"""
  texto=texto+incioTablaD
  for a in despacho:
    #                    cantidad             concepto              precio                total
    #                   1                       bebida 1              Q10.0                 Q10.0   
    texto=texto+tri+tdi+str(a[0])+tdf  +tdi+str(a[1])+tdf  +tdi+'Q'+str(a[2])+tdf   +tdi+'Q'+str(a[3])+tdf+trf
  texto=texto+fintTabla
  texto=texto+inicioTablaG
  #                       subtotal     ->        5                         porpina(8%)            ->                                 25
  texto=texto+tri+tdL+"sub total"+tdf   +tdR+str(total)+tdf+trf    +tri+tdL+"Propina:("+str(float(orden[3][0])*100)+"%)"+tdf   +tdR+"Q"+str(propina)+tdf+trf
  texto=texto+tri+tdL+"Total"+tdf   +tdR+"Q"+str(TotalMasPropina)+tdf+trf     +fintTabla


  factura(texto)


  


def factura(txt):
  f = open('Factura.html','w')
  principal= """
  <!DOCTYPE html>
  <html lang="es">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link rel="stylesheet" href="css/cssF.css">
  <link rel="stylesheet" href="boos/bootstrap.css">
  <title>Document</title>
  </head>
    <body class="cuerpo">
      <div class="container">
            <div class="row">
                <div class="col-2 f">*</div>
                <div class="col-8 factura">
                    <div class="container"><div class="row">
  """
  fin="""
                  </div></div>      
                </div>
                <div class="col-2">*</div>
            </div>
        </div>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </html>
  </html>
  """
  cuerpo=txt
  f.write(principal)
  f.write(cuerpo)#medio
  f.write(fin)#final
  f.close()#cerar
  webbrowser.open_new_tab('Factura.html')
