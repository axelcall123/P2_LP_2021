import webbrowser#pag
def tokenHtml(array):
    texto=''
    IR= '<tr>'
    FR='</tr>'
    FD='</td>'
    ID='<td>'
    ih='<th scope="row">'
    fh='</th>'
    cont=1
    for a in array:
      if a[0]!=' ' or a[0]!='':
        if a[4]=='PORCENTAJE':
          texto=texto+IR  +ih+str(cont)+fh   +ID+str(float(a[0])*100)+'%'+FD   +ID+str(a[1])+FD  +ID+str(a[2])+FD  +ID+a[3]+';'+a[4]+FD+   FR
        else:
          texto=texto+IR  +ih+str(cont)+fh   +ID+str(a[0])+FD   +ID+str(a[1])+FD  +ID+str(a[2])+FD  +ID+a[3]+';'+a[4]+FD+   FR
        cont+=1
    Tokens(texto)

def Tokens(txt):
    f = open('Tokens.html','w')
    principal = """
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
    cuerpos=txt
    fin= """
                </tbody>
        </table>
    </body>
    <script src="boos/bootstrap.js"></script>
    </html>"""
    f.write(principal)#inicio
    f.write(cuerpos)#medio
    f.write(fin)#final
    f.close()#cerar
    webbrowser.open_new_tab('Tokens.html')

'''
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">No.</th>
      <th scope="col">Lexema</th>
      <th scope="col">Fila</th>
      <th scope="col">Columna</th>
      <th scope="col">Token</th>
    </tr>
  </thead>
  <tbody>


    <tr>
      <th scope="row">1</th>
      <td>9.50</td>
      <td>10</td>
      <td>10</td>
      <td>numero</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>nombre_1 </td>
      <td>2</td>
      <td>12 </td>
      <td>Identificador</td>
    </tr>


  </tbody>
</table>
'''