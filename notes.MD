
[Mastermind](https://www.mastermind.ac/courses/take/iniciacion-python)
# Instalar pycharm necesario para el curso 
```bash
pacman -S pycharm-community-edition
```
___
# Input y Output
- Creamos primero nuevo proyecto en PyCharm, verificamos el interprete que sea el correcto en settings.
- Nombre del proyecto PrimerPrograma
- Una vez creado el proyecto, hacemos New -> Python File y creamos un fichero dentro del proyecto llamado primerprograma.py

![](IMG/PrimerPrograma.gif)

Haciendo click justo al lado de una línea, creamos un breakpoint, de esta manera al ejecutar en modo debug, podemos ir viendo toda la información saltando paso a paso.

![](IMG/Debug_BreakPoint.gif)

Ahora crearemos nuestro primero programa en el directorio PrimerPrograma donde buscaremos el número mayor y menor entre tres números entrados por el usuario con las siguientes funciones:
``` 
#Introducimos tres números con la funcion input y la asignamos a la variable convertiendo esta de tipo int
numero1=int(input("Introduce el primero número:"))
numero2=int(input("Introduce el segundo número:"))
numero3=int(input("Introduce el tercer  número:"))

#Con la función max y min búscamos el número mayor y menor

print ("El número mayor es:" + str(max(numero1, numero2, numero3)))
print ("El número menor es:" + str(min(numero1, numero2, numero3)))

"""
Con triple doble comillas creamos comentario en bloque, con # creamos comentario de línea
"""
```
>Encontraremos este programa en PrimerPrograma/primerprograma.py*
___
# Corrigiendo tu primer programa

Con python **no podemos** concatenar strings con int de la siguiente forma:
```python
>>> "Tu nomero es el"+5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>
```
Para concatenar string con int, una de las maneras sería:
```python
>>> "Tu nomero es el {}".format(5)
'Tu nomero es el 5'
>>>
```
```.format``` es lo que se conoce como método, que veremos más adelante. Vendría a ser como una función,  un comando que se ejecuta de esa string en este caso del número 5
````python
>>> "asdf {} {}".format(1, 5)
'asdf 1 5'
>>>
````
Llamamos al método format del string, asdf con el fin de concatenar int con str.
Modificamos el primerprograma.py concatenando con el format:
```python
#Introducimos tres números con la funcion input y la asignamos a la variable convertiendo esta de tipo int
numero1=int(input("Introduce el primero número: "))
numero2=int(input("Introduce el segundo número: "))
numero3=int(input("Introduce el tercer  número: "))

#Con la función max y min búscamos el número mayor y menor

"""print ("El número mayor es:" + str(max(numero1, numero2, numero3)))
   print ("El número menor es:" + str(min(numero1, numero2, numero3)))"""

#Modificamos el print con el método format:
print("El número mayor entre {} {} {} es el {} y el menor el {}".format(numero1, numero2, numero3,
                                                                         max(numero1, numero2, numero3),
                                                                         min(numero1, numero2, numero3)
                                                                        )
      )
```
Como ejercicio vamos a realizar dos programas
- F° to C°: Fahrenheit to Celsius Conversion Formula. (F-32)*5/9=C
- Libra £ a Euro €. En estos momentos 1 British Pound és igual a
1,19 EUR L*1,19=C

>Ejercicios/FahrenheitToCelsius.py
```python
#Asignamos el valor fahrenheit a la variable fahren mediante input, devolviendo un float.
fahren=float(input("Introduce el valor en fahrenheit para ser convertido a Celsius: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
celsi=float((fahren-32)*5/9)
#Imprimimos el resultado utilizando format.
print("{} ℉ son {} ℃".format(fahren, celsi))
```
>Ejercicios/LibraToEuro.py
````python
#Libra £ a Euro €
#Asignamos el valor Libra a la variable libra mediante input, devolviendo un float.
libra=float(input("Introduce el valor en Libras para ser convertido a Euros: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
euro=float(libra*1.19)
#Imprimimos el resultado utilizando format.
print("{} Libras son {} Euros".format(libra, euro))
````