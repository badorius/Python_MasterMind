"""
THE OFFICE GAME/// toda semejanza con la realidad es pura coincidencia by BADORIUS
"""
#############################
# IMPORT LIB
#############################

import sys, time, random, os, getpass
from datetime import date

#############################
# CLASS
#############################
class Servicio:
    nombre = "service"
    estado = "Enabled"
    def enable(self):
        self.estado = "Enabled"
    def disable(self):
        self.estado = "Disabled"
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
lista_servicios = ["NETWORK", "BIND", "SQUID", "MYSQL", "HTTPD", "SSHD", "NFSD", "CUPSD", "DOCKER", "THE OFFICE SOFTWARE"]
services_status = "enabled"
mi_usuario = "falken"
mi_password = "joshua"
active_services=len(lista_servicios)
office_version="Prod 2.0.0"

#Instanciamos los objectos antes definidos en la clase
servicio = [ Servicio() for i in range(len(lista_servicios))]
#Creamos una lista de objetos servicios con atributo nombre y metodos enable/disable que modifican el atributo estado.
for count in range(len(lista_servicios)):
    servicio[count].nombre = lista_servicios[count]
    #print(servicio[count].nombre, servicio[count].estado)
   # lista_servicios.append(servicio)

#############################
# FUNCTIONS
#############################

#Printing starting services funct
def loading_system(statusa, statusb):
    global lista_servicios
    """opcion = input("Hola, estas seguro que quiere jugar a THE OFFICE? [S/N]: ")
    if opcion != "S":
        print("Estas de suerte, hasta la próxima.")
        exit()"""

    print(statusa + "services:")
    for n in range(len(lista_servicios)):
        #mensaje=statusa + " {} service.".format(lista_servicios[n])
        mensaje=statusa + " {} service.".format(servicio[n].nombre)
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
    global services_status
    global lista_servicios
    global servicio
    global active_services
    menu = "SERVICE MANAGEMENT // " + str(active_services) + " servicios activos en el sistema"
    opciones_menu = ["Parar/Desactivar un servicio", "Parar/Desactivar todos los servicios", "salir"]
    opcion_service_management = menu_print(menu, opciones_menu)

    if opcion_service_management == "0":
        opcion_servicio=input ("Introduzca el nombre del servicio a parar y desactivar [{}]: ".format (lista_servicios))
        if opcion_servicio not in lista_servicios:
            print("Servicio no existe! muy muy mal! DESPEDIDO!")
            despedido()
        else:
            active_services = active_services - 1
            #indice = servicio.nombre(opcion_servicio)
            #servicio[indice].disable
            time.sleep(1)
            print("Parando servicio {} ....".format(opcion_servicio))
            print ("El Servicio {} ha sido parado y desactivado.".format(opcion_servicio))
            input("Presione [ENTER] para continuar: ")
            menu = "SERVICE MANAGEMENT // " + str(active_services) + " servicios activos en el sistema"
            opcion_service_management = service_management()

    elif opcion_service_management == "1":
        uopcion = input("Esta seguro que quiere parar y desactivar todos los servicios del systema? [S/N] ")
        if uopcion == "S":
            active_services = 0
            print("Parando todos los servicios ....")
            time.sleep(1)
            print("Todos los servicios han sido parados y desactivados.")
            input("Presione [ENTER] para continuar: ")
            menu = "SERVICE MANAGEMENT // " + str(active_services) + " servicios activos en el sistema"
            opcion_service_management = service_management()
        input("Presione [ENTER] para continuar: ")
        menu = "SERVICE MANAGEMENT // " + str(active_services) + " servicios activos en el sistema"
        opcion_service_management = service_management()
    elif opcion_service_management == "2":
        opcion = corporatemenu()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion_user_management = service_management()
    return opcion_service_management

def office_deploy():
    global office_version
    menu = "DEPLOY MANAGEMENT // Version actual: " + str(office_version)
    opciones_menu = ["Desplegar nueva version", "Eliminar software", "salir"]
    opcion_office_deploy = menu_print(menu, opciones_menu)

    if opcion_office_deploy == "0":
        aviable_versions=["Prod 1.0.0", "Dev 0.1.0", "Trojan.exe"]
        user_version = input("Selecciones la versión para subir a producción {}: ".format(aviable_versions))

        if user_version not in aviable_versions:
            print ("Opción incorrecta!")
            print("En serio??? Solo tenías que tipear correctamente una de las opciones anteriores! vaya sysadmin!")
            despedido()

        office_version = user_version
        print("Deploying version {} to production environment...".format(office_version))
        time.sleep(1)
        print("Version {} has been deployed to production environment...".format(office_version))
        input("Presione [ENTER] para continuar: ")
        menu = "DEPLOY MANAGEMENT // Version actual: " + str(office_version)
        opcion_office_deploy=office_deploy()

    elif opcion_office_deploy == "1":
        uopcion = input("Esta seguro que quiere eliminar todas las versiones del sistema, incluido GIT, backups, etc...? [S/N] ")
        if uopcion == "S":
            print("Eliminando todas las versiones ....")
            time.sleep(1)
            office_version = "NULL"
            print("Todas las versiones han sido eliminadas y usted despedido.")
            input("Presione [ENTER] para continuar: ")
            despedido()
        input("Presione [ENTER] para continuar: ")
        menu = "DEPLOY MANAGEMENT // Version actual: " + str(office_version)
        opcion_office_deploy=office_deploy()
    elif opcion_office_deploy == "2":
        opcion = corporatemenu()
    else:
        print("Opción incorrecta!")
        time.sleep(1)
        borrarpantalla()
        banner_print()
        opcion_office_deploy = office_deploy()

    return opcion_office_deploy

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

if correos_usuarios != 0 and out_of_office != True and usuarios_activos !=1 and active_services != 0 and office_version!= Trojan.exe:
    despedido()
else:
    print("You WIN!")



