import graphviz
def arbol(T):
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
        if T[a][4]=='SECCION':#VE SI ES LA SECCION
            nod_principal=caracter#TOMA EL NODO PRINCIPAL
            array_nod.append('A'+nod_principal)#UNE EL TITULO CON LOS PRINCIPALES
            nod.node(caracter,T[a][0])#BEBIDA,PASTEL,PIZZA
            cont_nod+=1#NUEVO NODO
        elif T[a][4]=='ID' or T[a][4]=='NOMBRE' or T[a][4]=='NUMERO' or T[a][4]=='DESCRIPCION':
            cont+=1  
            if cont%4==0:#           NOMBRE          NUMERO         DESCRIPCION
                nod.node(caracter,T[a-2][0]+'   '+"Q"+str(T[a-1][0])+'\n'+T[a][0])#
                array_nod.append(nod_principal+caracter)#UNIR PRINCIPAL CON LOS SUB-SUB
                cont_nod+=1#NUEVO NODO
                cont=0#CONT = 0 PARA MULTIPLO DE 4
    nod.edges(array_nod)#UNE LOS NODOS
    nod.render('PDF/arbol', view=True)#IMPRIME EL PDF
    #print(nod)#IMPRIME EL NODO EN CONSOLA
