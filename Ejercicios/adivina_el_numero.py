
import random
random_number = random.randint(1,5)
system_password = "Joshua"
try_number=1
try_max=3

print("[WOPR] Hola serñor Falken, cuanto tiempo!!!")
print("[WOPR] Le apetece jugar a un juego?")
print("[WOPR] Adivine un número del 1 al 5 para conseguir la contraseña de acceso al sistema WOPR,"
      "usted tiene un máximo de {} intentos.".format(try_number))
user_number=int(input("[WOPR] Introduzca un número del 1 al 5: " ))

while user_number != random_number and try_number < try_max:
    print("[WOPR] ERROR!!! ERROR!!! ERROR!!!")
    print("[WOPR] El número introducido no es correcto, numero de intentos fallidos: {}".format(try_number))
    user_number = int(input("[WOPR] Introduzca un número del 1 al 5: "))
    try_number = try_number + 1
print(try_number, try_max)
if try_number < try_max:
    print("[WOPR] Enhorabuena Señor Falken, el número introducido {} coincide con el número del sistema {}".format(int(user_number), int(random_number)))
    print("[WOPR] La contraseña al sistema es: " + system_password)
    print("[WOPR]: ~ root#_")
else:
    print("[WOPR] Lo siento Señor Falken, useted ha superado el número máximo de intentos.")
