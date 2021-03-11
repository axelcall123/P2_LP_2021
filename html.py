import webbrowser#pag
def htmlTokensDes(array):
    texto=''
        


def htmlTokens(txt):
    f = open('HTML/Tokens.html','w')
    principal = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="css/css.css">
        <link rel="stylesheet" href="boos/bootstrap.css">
        <title>Document</title>
        </head>
        <body>
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
    webbrowser.open_new_tab('HTML/Tokens.html')

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