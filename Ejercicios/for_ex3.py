"""
| Numero elegido por el usuario | 2                                          |
|-------------------------------|--------------------------------------------|
| Output esperado               | tabla de multiplicar del 2 (2 x 1 = 2 ...) |
"""

numero_usuario = int(input("Introduzca un número: "))

for numero in range(1, 11):
    #print(str(numero_usuario) + " x " + str(numero) + " = {}".format(numero_usuario*numero))
    print("{} x {} = {}".format(numero_usuario, numero, numero_usuario*numero))

print("\nMultiples de 2: ")

for numero in range(1, 11):
    if numero % 2 == 0:
        print("{} x {} = {}".format(numero_usuario, numero, numero_usuario*numero))