def identificadores(identificador):
    identificador=identificador.replace(' ','')
    state=0
    unir=''
    for n in range(len(identificador)):
        if state==0:#a-z
            if (ord(identificador[n].lower())>96 and ord(identificador[n].lower())<123) and n==0:#a-z
                unir=unir+identificador[n]
                state=1
            else:
                print('mal 0')
                return
        elif state==1:
            if (ord(identificador[n].lower())>96 and ord(identificador[n].lower())<123):#a-z
                unir=unir+identificador[n]
            elif (ord(identificador[n].lower())>47 and ord(identificador[n].lower())<58):#0-9
                unir=unir+identificador[n]
                state=2
            elif identificador[n]=='_':
                unir=unir+identificador[n]
                state=3
            else:
                print('mal 1')
                return
        elif state==2:
            if (ord(identificador[n].lower())>47 and ord(identificador[n].lower())<58):#0-9
                unir=unir+identificador[n]
            else:
                print('mal 2')
                return
        elif state==3:
            if identificador[n]=='_':
                unir=unir+identificador[n]
            elif (ord(identificador[n].lower())>47 and ord(identificador[n].lower())<58):#0-9
                unir=unir+identificador[n]
                state=4
            else:
                print('mal 3')
                return
        elif state==4:
            if (ord(identificador[n].lower())>47 and ord(identificador[n].lower())<58):#0-9
                unir=unir+identificador[n]
            else:
                print('mal 4')
                return

    print(unir,'xd')
            # if ord(identificador[n].lower())>96 and ord(identificador[n].lower())<123:
            #     unir=unir+identificador[n]
            # elif identificador[n]=='_'

identificadores('Abcd___000123')