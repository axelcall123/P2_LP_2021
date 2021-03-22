import graphviz
def arbol(Tu):
    #SE PUDE BORRAR DESDE AQUI XDXD
    cont=0
    array_sup=[]#[[SECCION],[ID],[NOMBRE],[PRECIO],[DESCRIPCION]]
    array_ayuda=[]#TEMPORAMENTE LA SECCION
    array_seccion=[]#ARRAY SECCION
    for a in range(2,len(Tu)):#CREA LA MATRIZ SUP
        if Tu[a][4]=='SECCION':
            array_ayuda=Tu[a]
            array_seccion.append(array_ayuda)
        elif Tu[a][4]=='ID' or Tu[a][4]=='NOMBRE' or Tu[a][4]=='NUMERO' or Tu[a][4]=='DESCRIPCION':
            cont+=1  
            if cont%4==0:
                array_sup.append([array_ayuda,Tu[a-3],Tu[a-2],Tu[a-1],Tu[a]])
                cont=0

    array_uno=[]#AYUDA1
    array_dos=[]##AYUDA2
    for a in range(len(array_sup)):
        for b in range(len(array_sup)):
            if b+1<len(array_sup):#PARA MIRAR ANTES DEQUE CREO UN ERROR AL TOMAR LA ULTIMA MATRIZ
                if float(array_sup[b][3][0])<float(array_sup[b+1][3][0]):
                    continue
                else:#SI !5<4 CAMBIA LA POSICION DE LA MATRIZ
                    array_uno=array_sup[b]
                    array_dos=array_sup[b+1]
                    array_sup[b]=array_dos
                    array_sup[b+1]=array_uno
    T=[]
    T.append(Tu[0])#UNE EL restaurante
    T.append(Tu[1])#UNE EL 'LFP restaurante'
    for a in array_seccion:#RECREA LA MATRIZ ANTERIOR ORDENADA
        T.append(a)
        for b in range(len(array_sup)):
            if array_sup[b][0][0]==a[0]:
                T.append(array_sup[b][1])
                T.append(array_sup[b][2])
                T.append(array_sup[b][3])
                T.append(array_sup[b][4])
            else:
                continue
    #------------------------------------------

    array_nod=[]#PARA UNIR LOS NODOS
    nod = graphviz.Digraph(comment='SI')
    nod
    nod.node('A','RESTAURANTE'+'\n'+T[1][0])#TITULO PRINCIPAL
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
                numDosD=T[a-1][0]
                nod.node(caracter,T[a-2][0]+'   '+"Q"+str(f"{numDosD:.2f}")+'\n'+T[a][0])#
                array_nod.append(nod_principal+caracter)#UNIR PRINCIPAL CON LOS SUB-SUB
                cont_nod+=1#NUEVO NODO
                cont=0#CONT = 0 PARA MULTIPLO DE 4
    nod.edges(array_nod)#UNE LOS NODOS
    nod.render('PDF/arbol', view=True)#IMPRIME EL PDF
    #print(nod)#IMPRIME EL NODO EN CONSOLA
