# Aprendiendo el while
Ejemplo while para validar una de las posibles opciones de un input. Primero seteamos la variable a tipo de dato None, entramos en el while y preguntamos hasta que la respuesta sea una de las opciones.
```python
#Tipo de variable none
respuesta = None

while respuesta !="A" and respuesta !="B" and respuesta !="C":
    respuesta = input("Que opción prefieres [A, B, C]")

if respuesta == "A":
    print ("Has elegido ok")
elif respuesta == "B":
    print ("Podrias haber elegido mejor")
elif respuesta == "C":
    print ("Has respuesto mal")
```
Otro ejemplo de while modificando valor variable hasta salir del loop:
```python
numero = 12
while numero > 1:
    print("Mi numero {} es mayor que 1".format(numero))
    numero -= 1

print("Mi numero es {}".format(numero))
```
# El combate Pokemon

>Ejercicios/[test_while_pokemon.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/test_while_pokemon.py)

# La barra de vida

En python no existen las constantes, pero podemos utilizar variables en mayúsculas para hacer referencia a variables que no cambiaran de valor, de esta forma sabemos que sería como una constante, es como una nomenclatura.

>Ejercicios/[test_while_pokemon_nate.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/test_while_pokemon_nate.py)

# Las listas
Las listas son un tipo de variable en python, ```python list = ["naranja", "peras", "manzanas"]``` es como una array, puede contener, número, strings, etc...
En las listas, podemos poner objetos nuevos, podemos buscar valores, buscar posiciones, que hay en la posición N, podemos unir dos listas y podemos ejecutar un código por cada uno de los objetos de nuestra lista.

Ejemplos:
```python
vocales = ["a", "e", "e", "i", "o"]
vocales.append("u") # Añadimos la u a la lista
vocales.append("l") # Añadimos la l a la lista
vocales.pop() # Borramos el ultimo elemento de la lísta
len(vocales) #Nos devuelve el número de elementos de la lista.

letra = a
letra in vocales # nos devuelve un true. Busca un valor en la lista.
```
Ejemplo not in aplicado en el while de pokemons:
```python
    while ataque_squirtle not in ['P', 'A', 'B', 'N']:
    #while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja [N]ada: ")
```
Ejercicio lista de la compra.
```python
"""
Programa lista de la compra
Que deseas comprar? ([Q] para salir) > Leche
Seguro que deseas comprar "Leche"? [S/N] > S
Leche añadida a la lista de la compra.

Que deseas comprar? ([Q] para salir) > Pan
Seguro que deseas comprar "Pan"? [S/N] > N

Que deseas comprar? ([Q] para salir) > Pan
Seguro que deseas comprar "Pan"? [S/N] > S
Pan añadida a la lista de la compra.

Que deseas comprar? ([Q] para salir) > Pan
Pan ya existe en la lista de la compra.

Programa lista de la compra
Que deseas comprar? ([Q] para salir) > Q

La lista de la compra es:
["Leche", "Pan"]
"""

lista = []
opcion = None
titulo="Programa lista de la compra"
elemento = None
print(titulo)
print("-" * len(titulo))


while elemento != "Q":
    elemento = input("Que deseas comprar? ([Q] para salir) >")
    if elemento in lista:
        print("{} ya existe en la lista de la compra.".format(elemento))
    elif elemento != "Q":
        while opcion not in ["S", "N"]:
            opcion = input("Seguro que deseas comprar {} [S/N]".format(elemento))
        if opcion == "S":
            lista.append(elemento)
            print("{} ha sido añadido a la lista.".format(elemento))
            opcion = None
        else:
            opcion = None
print("La lista de la compra es: ")
print (lista)
exit()
```
>Ejercicios/[lista_de_la_compra.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/lista_de_la_compra.py)
