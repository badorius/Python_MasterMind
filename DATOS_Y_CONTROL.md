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
---
# El combate Pokemon

>Ejercicios/[test_while_pokemon.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/test_while_pokemon.py)
---
# La barra de vida

En python no existen las constantes, pero podemos utilizar variables en mayúsculas para hacer referencia a variables que no cambiaran de valor, de esta forma sabemos que sería como una constante, es como una nomenclatura.

>Ejercicios/[test_while_pokemon_nate.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/test_while_pokemon_nate.py)
---
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

```
>Ejercicios/[lista_de_la_compra.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/lista_de_la_compra.py)
---
**Información a comentar en la versión del curso:**
- El if con el input directamente: 
```python 
  if input("Seguro que quiere aãdir {} a la lista? [S/N]".fromat (opcion)) == "S":
```
- Cuando en una condición no queremos que se realice nada, podemos usar pass, ejemplo
```python 
  if input_usuario == "Q":
    pass
   elif input....
```
- Ejemplo de como hacer un while true y romperlo con un break tras una condición:
```python 
   while true:
    if input_de_usuario =="Q":
        break
   elif input....
```
_Importante utilizar el breakpoint/debug para ver el recorrido del if/while en caso de comportamiento diferente al esperado._
---
# Aprendiendo el for
Ejemplo for:
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "Hola, estoy aprendiendo python"
for item in a:
    print(item)

for letra in frase:
    print(letra)
```
>Ejercicios/[for.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/for.py)

Ejemplo for con función range. Range es una función muy util para el for, la que le pasamos un número y hace un iterable de todos los números:
```python
numero_de_repeticiones = int(input("Cuantas veces quires repetir el menssaje? "))
for a in range(numero_de_repeticiones):
    print("Hola")
```
Si imprimimos un range, nos muestra un iterable, 
```python
>>> print(range(4))
range(0, 4)
```
Un range se puede convertir en una lista:
```python
>>> print(list(range(4)))
[0, 1, 2, 3]
>>>
```
Si queremos hacer un for por ejemplo que no empiece en 0, podemos hacerlo con range indicando el inicio y el fin como parámetro:
```python
>>> for i in range(1,5):
...     print(i)
... 
1
2
3
4
>>>  
```
>Ejercicios/[for_in_range.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/for_in_range.py)
---
# Algunos ejercicios sencillos 

1. Ejemplo

| texto_usuario                               | "Hola, me llamo Nate. Tu como te llamas? |
|---------------------------------------------|------------------------------------------|
| Output esperado                             | espacioes 6, puntos 1, comas 1           |



>Ejercicios/[for_ex1.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/for_ex1.py)

2. Ejemplo
En este ejemplo utilizaremos la libreŕia string haciendo un import de esta y utilizando string.ascii_uppercase

| texto usuario    | "Hola, me llamo Nate. Tu como te llamas?  |
|------------------|-------------------------------------------|
| Output esperado  | mayusculas = 3                            |


>Ejercicios/[for_ex2.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/for_ex2.py)
