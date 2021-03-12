from colorama import init, Fore, Back, Style
import leer as leer
cargarMenu = []
cargarOrden=[]

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
		print()
	elif opcionMenu == '4':
		print()
	elif opcionMenu == '5':
		print()
	elif opcionMenu == '6':
		break
	elif opcionMenu=='9':
		print(cargarMenu,'||',cargarOrden)
	elif opcionMenu=='7':
		print()
	else:
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')
