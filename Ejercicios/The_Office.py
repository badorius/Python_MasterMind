"""
THE OFFICE GAME/// toda semejanza con la realidad es pura coincidencia
"""
import sys, time
import random
banner = """▄▄▄█████▓ ██░ ██ ▓█████     ▒█████    █████▒ █████▒██▓ ▄████▄  ▓█████    
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▒  ██▒▓██   ▒▓██   ▒▓██▒▒██▀ ▀█  ▓█   ▀    
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░  ██▒▒████ ░▒████ ░▒██▒▒▓█    ▄ ▒███      
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██   ██░░▓█▒  ░░▓█▒  ░░██░▒▓▓▄ ▄██▒▒▓█  ▄    
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░ ████▓▒░░▒█░   ░▒█░   ░██░▒ ▓███▀ ░░▒████▒   
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▒░▒░  ▒ ░    ▒ ░   ░▓  ░ ░▒ ▒  ░░░ ▒░ ░   
    ░     ▒ ░▒░ ░ ░ ░  ░     ░ ▒ ▒░  ░      ░      ▒ ░  ░  ▒    ░ ░  ░   
  ░       ░  ░░ ░   ░      ░ ░ ░ ▒   ░ ░    ░ ░    ▒ ░░           ░      
          ░  ░  ░   ░  ░       ░ ░                 ░  ░ ░         ░  ░   
                                                      ░    """
empleado_id = random.randint(1, 1000000)
#Printing starting services
def loading_system():
    print("Starting services:")
    servicios = ["NETWORK", "BIND", "SQUID", "MYSQL", "HTTPD", "SSHD", "NFSD", "CUPSD", "DOCKER", "THE OFFICE SOFTWARE"]
    for n in range(10):
        mensaje="Starting {} service.".format(servicios[n])
        print(mensaje, end="")

        #GET STRING LEN TO KEEP OK MESSAGE ON THE SAME POSITION IN THE SCREEN.
        largomax = 50
        largo = len(mensaje)
        largorest = largomax - largo

        #PRINT POINTS SERVICE STARTING OK
        for n in range(10+largorest):
            print(".", end="")
            time.sleep(0.01)
        print (" [OK]")

    print("Software has been loaded")
    print()

opcion=input("Hola, esstas seguro que quiere jugar a THE OFFICE? [S/N]: ")
if opcion != "S":
    print("Estas de suerte, hasta la próxima.")
    exit()

loading_system()
print(banner)
print("█████████████████████████████████████████████████████████████████████")
print()
print("Hola empleado " + str(empleado_id))