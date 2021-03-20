from colorama import init, Fore, Back, Style
import leer as leer
import Html as Html
import arbol as arbol
cargarMenu = []
cargarOrden=[]
numeroF=0#cuenta el numero de la factura echa en html
def menu():
	print("\x1b[1;33m"+"Proyectos 1- LFP")
	print("\033[;36m"+"Lenguajes|B|AXEL CALDERON|201901458")
	print("""
	SELECCIONA UNA OPCION
	t1 - CARGAR MENU
	t2 - CARGAR ORDEN
	t3 - GENERAR MENU
	t4 - GENERAR FACTURA
	t5 - GENERAL ARBOL
	t6 - SALIR
	""")


while True:
	menu()
	opcionMenu = input('INSERTE UNA OPCION >>')
	if opcionMenu == '1':
		cargarMenu = leer.read(True)
	elif opcionMenu == '2':
		cargarOrden = leer.read(False)
	elif opcionMenu == '3':
		if cargarMenu:#LLENO cargar
			opcionLimite= input('desea poner un límite en los precios de las distintas opciones que tiene el menú >>,SI|NO\n')
			if opcionLimite=="SI":
				numLimite=input('producto menores al precio>>')
				Html.menuHtml(cargarMenu,float(numLimite))
			elif opcionLimite=="NO":
				Html.menuHtml(cargarMenu,999999)
		else: 
			print('No ha selecciona a un el menu, o hubo error en archivo.lfp. Seleccione un archivo correcto Gracias :3')
	elif opcionMenu == '4':
		if cargarOrden and cargarMenu:
			if float(cargarOrden[3][0])>=0 and float(cargarOrden[3][0])<=1:
				numero=Html.facturaHtml(cargarMenu,cargarOrden,numeroF)
				numeroF=numero#no factura en html
			else:
				print('La propina excede el limite')
		else:
			print('No ha selecciona una orden o un menu, o hubo error en archivo.lfp. Seleccione un archivo correcto Gracias :3')
	elif opcionMenu == '5':
		if cargarMenu:#Leeno cargar
			arbol.arbol(cargarMenu)
		else:
			print('No ha selecciona a un el menu, o hubo error en archivo.lfp. Seleccione un archivo correcto Gracias :3')
	elif opcionMenu == '6':
		break
	elif opcionMenu=='9':
		print(cargarMenu,'||',cargarOrden)
	elif opcionMenu=='7':
		print()
	else:
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')
