"""
THE OFFICE GAME/// toda semejanza con la realidad es pura coincidencia by BADORIUS
"""
#############################
# IMPORT LIB
#############################

import sys, time, random, os, getpass
from datetime import date

#############################
# VARS
#############################

today = date.today()
empleado_id = random.randint(1, 1000000)
correos_pendientes = random.randint(1, 1000000)
correos_usuarios = random.randint(100000, 1000000000)
out_of_office = False
usuario_despedido = False
usuarios_activos = random.randint(1, 1000000)
mi_usuario = "falken"
mi_password = "joshua"
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
    print("Buenos días Sr {}, empleado ID {}, hoy es {}, esperemos que sea un gran día para todos.\n ".format(mi_usuario, str(empleado_id), today))
    print()
# MENU 1
def menu_print(titulo, opciones_menu_principal):
    mensaje_principal = "█ {} // ID: {} // DATE: {} // [THE OFFICE] █".format(titulo, empleado_id, today)
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
    global usuario_despedido
    usuario_despedido = True
    print("Usted ha sido nominado empleado del mes (malo). Recoja sus cosas y pase por RRHH, le están esperando."
          "Gracias por su servicio.")
    input("Presione [ENTER] tecla para continuar...")
    loading_system("Shutting down ", "DONE")
    print("""┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼""")
    exit(1)

def corporatemenu():
    menu = "CORPORATE MENU"
    opciones_menu = ["Corporate mail", "User Management", "Service management",
                     "Deploy The Office software", "Run shell", "Shutdown system"]
    opcion = menu_print(menu, opciones_menu)
    #Corporate mail
    if opcion == "0":
        opcion_mail = corporatemail()
    #User Management
    elif opcion == "1":
        opcion_umanagement=user_management()
    #Service management
    elif opcion == "2":
        opcion_smanagement=service_management()
    #Deploy The Office Software
    elif opcion == "3":
        opcion_office_deploy=office_deploy()
    #Run shell
    elif opcion == "4":
        opcion_run_shell=run_shell()
    #Shutdown system
    elif opcion == "5":
        opcion_sytem_shutdown=system_shutdown()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion = corporatemenu()
    return opcion
def corporatemail():
    global correos_usuarios
    global correos_pendientes
    menu = "CORPORATE MAIL // " + str(correos_pendientes) + " Correos no leidos"
    opciones_menu = ["Marcar todos los correos como leidos", "Borrar todos los correos", "Borrar todos los correos de todo los usuarios",
                     "Out of office", "salir"]
    opcion_mail = menu_print(menu, opciones_menu)

    if opcion_mail == "0":
        print("{} correos marcados como leidos".format(correos_pendientes))
        despedido()
    elif opcion_mail== "1":
        print("{} correos borrados".format(correos_pendientes))
        despedido()
    elif opcion_mail == "2":
        print("{} correos borrados".format(correos_usuarios))
        correos_pendientes = 0
        correos_usuarios = 0
        print("{} correos en total en todo CORPORATE MAIL".format(correos_usuarios))
        input("Presione [ENTER] tecla para continuar...")
        menu = "CORPORATE MAIL // " + str(correos_pendientes) + " Correos no leidos"
        opcion = corporatemail()

    elif opcion_mail == "3":
        global out_of_office
        print("Buenos días:\n"
              "Gracias por su mensaje.\n"
              "Me encuentro de vacaciones sin acceso al correo electrónico.\n"
              "Provablemente usted tampoco tenga correo y con mucha suerte no tenga acceso ni al sistema, con lo que este automensaje no tienen ningún sentido.\n"
              "Le atendería con mucho gusto a partir del día 06/06/6666, pero seguramente no estemos disponibles, mucha suerte.\n"
              "También puede dirigirse a nuestra herramienta de solución de problemas online:\n"
              "https://bofh.d00t.org/\n"
              "Gracias por su comprensión.\n"
              "Saludos cordiales,\n"
              "BOFH")
        out_of_office = True
        opcion = corporatemail()
    elif opcion_mail == "4":
        opcion = corporatemenu()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion_mail = menu_print(menu, opciones_menu)
    return opcion_mail

def user_management():
    global usuarios_activos
    global mi_password
    menu = "USER MANAGEMENT // " + str(usuarios_activos) + " Usuarios activos en el system"
    opciones_menu = ["Modificar mi password", "Modificar password de otro usuario", "Borrar un usuario",
                     "borrar todos los usuarios", "salir"]
    opcion_user_management = menu_print(menu, opciones_menu)

    if opcion_user_management == "0":
        global mi_password
        mi_password_1 = mi_password
        mi_password_2 = mi_password
        actual_password = input("Hola Señor Falken, Introduzca su password actual: ")
        if actual_password == mi_password:
            mi_password_1 = getpass.getpass("Introduzca su nuevo password: ")
            mi_password_2 = getpass.getpass("Introduzca otra vez su nuevo password: ")
            if mi_password_1 == mi_password_2:
                mi_password = mi_password_1
                print("Su password ha sido modificado con éxito.")
                input("Presione [ENTER] para continuar: ")
                opcion_umanagement = user_management()
        print("Password Incorrecto, el sistema reportará su incompetencia al departamento oportuno.")
        despedido()

    elif opcion_user_management == "1":
        luser = input("Introduzca el logon name del usuario: ")
        su_password_1 = getpass.getpass("Introduzca el password para el usuario: ")
        su_password_2 = getpass.getpass("Introduzca otra vez el password para el usuario: ")
        if su_password_1 == su_password_2:
            print("El password para el usuario {} ha sido modificado con éxito.".format(luser))
            input("Presione [ENTER] para continuar: ")
            opcion_umanagement = user_management()
        print("Password Incorrecto, el sistema reportará su incompetencia al departamento oportuno.")
        despedido()
    elif opcion_user_management == "2":
        global mi_usuario
        luser = input("Introduzca el nombre de usuario a elminiar: ")
        if luser == mi_usuario:
            print ("No se puede ser más incompetente, has eliminado tu usuario!")
            despedido()
        else:
            print("El usuario {} ha sido eliminado con éxito!".format(luser))
            input("Presione [ENTER] para continuar: ")
            opcion_user_management = menu_print(menu, opciones_menu)
    elif opcion_user_management == "3":
        uopcion = input ("Esta seguro que quiere eliminar todos los usuarios del sistema a excepción del suyo? [S/N]")
        if uopcion == "S":
            print("Todos los usuarios han sido eliminados del sistema (Menos el suyo Sr {}.)".format(mi_usuario))
            usuarios_activos = 1
            input("Presione [ENTER] para continuar: ")
            menu = "USER MANAGEMENT // " + str(usuarios_activos) + " Usuarios activos en el system"
            opcion_user_management = menu_print(menu, opciones_menu)
        opcion = user_management()
    elif opcion_user_management == "4":
        opcion = corporatemenu()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion_user_management = user_management()
    return opcion_user_management
def service_management():
    print()
def office_deploy():
    print()
def run_shell():
    print()
def system_shutdown():
    print()
#############################
# MAIN
#############################

loading_system("Starting", "OK")
borrarpantalla()
banner_print()
opcion = corporatemenu()

if correos_usuarios != 0 and out_of_office != True and usuarios_activos !=1:
    despedido()



