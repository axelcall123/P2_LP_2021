def numero(numero):
    unir=''
    state=0
    numero=numero.replace(' ','')
    for n in range(len(numero)):
        if state==0:
            if ord(numero[n])>47 and ord(numero[n])<58:
                unir=unir+numero[n]
            elif numero[n]=='.':#estado 1
                unir=unir+numero[n]
                state=1
            else:
                print('ERROR',numero[n])
                return
        elif state==1:
            if ord(numero[n])>47 and ord(numero[n])<58:
                unir=unir+numero[n]
            else:
                print('ERROR',numero[n])
                return         
    print(str(float(unir)))
# numero('11')
# numero('10.50')
# numero('45.00')
# numero('40.')
# numero('35')
# numero('25')
# numero('0123456789.987654388')