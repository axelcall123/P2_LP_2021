#'->a-z->{a-z| }->a-z->'
def cadenas(texto):
    if texto[0]=="'" and texto[len(texto)-1]=="'":
        for n in range(1,len(texto)-1):#NO TOMAR EN CUENTA 'a1d'
            if texto[n]!="'": 
                if len(texto)-2==n:#NO TOMAR EN CUENTA  a1d' comilla final
                    print(texto,'|final')
                    return
            else:
                print('posicion '+str(n),texto[n],'|nop|',texto)        
                return
cadenas("'hola 'como le va'")