"""
THE OFFICE GAME/// toda semejanza con la realidad es pura coincidencia by BADORIUS
"""
#############################
# IMPORT LIB
#############################

import sys, time, random, os
from datetime import date

#############################
# VARS
#############################

today = date.today()
empleado_id = random.randint(1, 1000000)
correos_pendientes = random.randint(1, 1000000)

correos_pendientes = 5

#############################
# FUNCTIONS
#############################

#Printing starting services funct
def loading_system(statusa, statusb):
    """opcion = input("Hola, estas seguro que quiere jugar a THE OFFICE? [S/N]: ")
    if opcion != "S":
        print("Estas de suerte, hasta la próxima.")
        exit()"""

    print(statusa + "services:")
    servicios = ["NETWORK", "BIND", "SQUID", "MYSQL", "HTTPD", "SSHD", "NFSD", "CUPSD", "DOCKER", "THE OFFICE SOFTWARE"]
    for n in range(10):
        mensaje=statusa + " {} service.".format(servicios[n])
        print(mensaje, end="")

        #GET STRING LEN TO KEEP OK MESSAGE ON THE SAME POSITION IN THE SCREEN.
        largomax = 50
        largo = len(mensaje)
        largorest = largomax - largo

        #PRINT POINTS SERVICE STARTING OK
        for n in range(10+largorest):
            print(".", end="")
            time.sleep(0.01)
        print (" [" + statusb +"]")

    print()

# FUNC BORRAR PANTALLA
def borrarpantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# FUNC PRINT BANNER
def banner_print():
    print()
    print("█████████████████████████████████████████████████████████████████████")

    banner = """▄▄▄█████▓ ██░ ██ ▓█████     ▒█████    █████▒ █████▒██▓ ▄████▄  ▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▒  ██▒▓██   ▒▓██   ▒▓██▒▒██▀ ▀█  ▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░  ██▒▒████ ░▒████ ░▒██▒▒▓█    ▄ ▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██   ██░░▓█▒  ░░▓█▒  ░░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░ ████▓▒░░▒█░   ░▒█░   ░██░▒ ▓███▀ ░░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▒░▒░  ▒ ░    ▒ ░   ░▓  ░ ░▒ ▒  ░░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░     ░ ▒ ▒░  ░      ░      ▒ ░  ░  ▒    ░ ░  ░
  ░       ░  ░░ ░   ░      ░ ░ ░ ▒   ░ ░    ░ ░    ▒ ░░           ░   
          ░  ░  ░   ░  ░       ░ ░                 ░  ░ ░         ░  ░
                                                      ░               """
    print(banner)
    print("█████████████████████████████████████████████████████████████████████")
    print()
    print("Buenos días empleado {}, hoy es {}, esperemos que sea un gran día para todos.\n ".format(str(empleado_id), today))
    print()
# MENU 1
def menu_print(titulo, opciones_menu_principal):
    mensaje_principal = "█ {} // {} // {} // [THE OFFICE] █".format(titulo, empleado_id, today)
    print("█" * len(mensaje_principal))
    print(mensaje_principal)
    print("█" * len(mensaje_principal))

    #opciones_menu_principal = ["Leer correos pendientes", "Gestion de usuarios", "Getion de servicios", "Deeploy TheOffice software", "Iniciar shell"]

    for i in opciones_menu_principal:
        print("█ " + i + "." * int(len(mensaje_principal) - len(i) - 7) + "[{}] █".format(int(opciones_menu_principal.index(i))))

    print("█" * len(mensaje_principal))
    opciones_menu_principal = input("Elija una opción: ")
    return opciones_menu_principal

def despedido():
    print("Usted ha sido nominado empleado del mes (malo). Recoja sus cosas y pase por RRHH, le están esperando."
          "Gracias por su servicio.")
    input("Presione [ENTER] tecla para continuar...")
    loading_system("Shutting down ", "DONE")
    exit(1)

#############################
# MAIN
#############################

#loading_system("Starting", "OK")
borrarpantalla()
banner_print()


menu = "CORPORATE MENU"
opciones_menu = ["Leer correos pendientes", "Gestion de usuarios", "Getion de servicios", "Deeploy TheOffice software", "Iniciar shell", "Apagar sistema"]
opcion = menu_print(menu, opciones_menu)

if opcion == "0":
    menu = "CORPORATE MAIL"
    opciones_menu = ["Marcar todos los correos como leidos", "Borrar todos los correos", "Borrar todos los correos de todo los usuarios",
                     "Out of office", "salir"]
    opcion_mail = menu_print(menu, opciones_menu)

    if opcion_mail == "0":
        print("{} correos marcados como leidos".format(correos_pendientes))
        despedido()
    elif opcion_mail== "1":
        print("{} correos marcados borrados".format(correos_pendientes))
        despedido()

    elif opcion_mail == "2":
        gestion_servicios()
    elif opcion_mail == "3":
        gestion_servicios()
    elif opcion_mail == "4":
        gestion_servicios()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion = menu_print(opciones_menu)


elif opcion == "1":
    gestion_usuarios()
elif opcion == "2" :
    gestion_servicios()
elif opcion == "3":
    gestion_servicios()
elif opcion == "4":
    gestion_servicios()
elif opcion == "5":
    apagar_sistema()
else:
    print("Opción incorrecta!")
    time.sleep(1)
    borrarpantalla()
    banner_print()
    opcion = menu_print(opciones_menu)

print(opcion)