"""
| Numeros input usuario | [1, 2, 3, 4, 5, 6]                           |
|-----------------------|----------------------------------------------|
| Output esperado       | numero mas pequeño 1, numero más grande el 6 |
"""

"""
#Metodo 1, Atención al while para preguntar S/N
numeros_usuario = []
numero_introducidos = input("Introduzca un número para añadir en la lista: ")
numeros_usuario.append(numero_introducidos)

while input("Desea introducir otro número [S/N]?") != "N":
    numero_introducidos = input("Introduzca un número para añadir en la lista: ")
    numeros_usuario.append(numero_introducidos)

print(numeros_usuario)
"""
"""
#Metodo 2, Atención a la metodo split para romper las comas:

numero_introducidos = input("Introduzca los números separados por comas: ") #1,2,3,4,5,6
numeros_usuario = numero_introducidos.split(",")
numeros_usuario_limpio = []

for numero in numeros_usuario:
    numeros_usuario_limpio.append(int(numero))

print (numeros_usuario_limpio)
"""
# Metodo 3, Atención al for, list comprehesion (compresion de lista) Es una forma de listar.
numero_introducidos = input("Introduzca los números separados por comas: ") #1,2,3,4,5,6
numeros_usuario = [int(numero) for numero in numero_introducidos.split(",")]

#Steamos las variables de numero grande y pequeño con el primer valor de la lista
numero_pequenio = numeros_usuario[0]
numero_grande = numeros_usuario[0]

#Atención al numeros_usuario[1:]: --> Esto es un filtro de lista, le decimos que empiece por la posición 1 y no la 0, también podríamos poner [1:3] esto recorrería del 1 al 3
for numero in numeros_usuario[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero
    if numero_grande < numero:
        numero_grande = numero

print("El numero pequeño es {} y el grande {}".format(numero_pequenio, numero_grande))



