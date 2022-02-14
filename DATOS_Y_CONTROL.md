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
