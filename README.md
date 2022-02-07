
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
>Ejercicios/[primerprograma.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/primerprograma.py)

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
```python
>>> "asdf {} {}".format(1, 5)
'asdf 1 5'
>>>
```
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

```python
#Asignamos el valor fahrenheit a la variable fahren mediante input, devolviendo un float.
fahren=float(input("Introduce el valor en fahrenheit para ser convertido a Celsius: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
celsi=float((fahren-32)*5/9)
#Imprimimos el resultado utilizando format.
print("{} ℉ son {} ℃".format(fahren, celsi))
```
>Ejercicios/[FahrenheitToCelsius.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/FahrenheitToCelsius.py)

```python
#Libra £ a Euro €
#Asignamos el valor Libra a la variable libra mediante input, devolviendo un float.
libra=float(input("Introduce el valor en Libras para ser convertido a Euros: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
euro=float(libra*1.19)
#Imprimimos el resultado utilizando format.
print("{} Libras son {} Euros".format(libra, euro))
```
>Ejercicios/[LibraToEuro.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/LibraToEuro.py)

---
# ESTRUCTURAS DE CONTROL

Ejemplos estructuras de control con if or == !=

```python
print("Me voy a la cocina")
print("Abro la nevera")

hay_leche = input("Hay leche en la nevera (s/n): ")
hay_colacao = input("Hay colacao en la nevera (s/n): ")

if hay_leche != "s" or hay_colacao != "s":
    print("Voy al super a comprar.")
    if hay_leche != "s":
        print ("Compro leche")
    if hay_colacao != "s":
        print ("Compro colacao")

print("Ponemos la leche en el vaso")
print("Ponemos la colacao en el vaso")
print("Mezclamos")

# https://www.youtube.com/watch?v=SsoOG6ZeyUI&ab_channel=ChristianNyffenegger
```
>Ejercicios/[Preparacion_Colacao.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/Preparacion_Colacao.py)

Ejercico práctico. Programa donde partiendo de un número definido en una variable del programa, el usuario deberá introducir un número para adivinar el que hay en la variable, si el usuario acierta el número, le damos la enhorabuena, si no salimos.

```python
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
```
>Ejercicios/[adivina_el_numero.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/adivina_el_numero.py)

___
# La lógica boolean 
Ejemplos de lógica booleana con ejercicio de descuento zoo, según edad y carnet
```python
edad = int(input("Introduzca su edad: "))
tipo_de_carnet = input("Introduzca su tipo de carnet (E Estudiante / F Familia Numerosa / P Pensionista / N Nada: ")
descuento = 25
if (25 <= edad <=35 and tipo_de_carnet == "E") or edad <= 10 or (edad >= 65 and tipo_de_carnet == "P") or tipo_de_carnet == "F":
    print("Enhorabuena, se le aplica un {}% de descuento".format(descuento))
else:
    print("No cumple los requerimientos para obtener el descuento")
```
>Ejercicios/[descuento_zoo.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/descuento_zoo.py)
---
# Tipos de datos y otras aclaraciones
Con la función **type()** podemos preguntar al intérprete de python que tipo de dato es el que pasamos por parámetro:
```python
>>> type(14)
<class 'int'>
>>> type(4.2)
<class 'float'>
>>> type("hola")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> type(None)
<class 'NoneType'>
>>>
>>> 4/3
1.3333333333333333
>>> 4%3
1
>>>
```
>Cuando algo no devuelve valor es de tipo None.

>4 Dividido entre 3 (4/3) es i gual a 1.3 y me sobra una.

> 4%3 -> Me sobra una.

También tenemos tipo de datos compuestos como los de clase list:
```python
>>> a = [1, 2, 3, 4]
>>> type (a)
<class 'list'>
>>>
```
De clase diccionario:
```python
>>> type (a)
<class 'dict'>
>>>
```
De clase tuplas:
```python
>>> a = (2, 3)
>>> type (a)
<class 'tuple'>
>>>
```
Más adelante entraremos con mas detalle con las estructuras de datos.
De momento trabajaremos con datos escalares, escalares significa que solo tiene un valor, no es una lista de valores, ni una matriz de valores, ni una estructura de valores tridimensional.
Entonces por ahora tenemos integer float string boolean y tipo none.
En python podemos convertir los datos de un tipo a otro, eso se llama casteo o cast, conversión de tipo.
Se puede hacer de varias maneras:
```python
>>> 2 + 2.0
4.0
>>> float(2)
2.0
>>> int(2.0)
2
>>>
```
### Variables 
Las variables deben seguir una nomenclatura conocida como underscore 
- En python las variables siempre empiezan por minúscula.
- No pueden existir espacions en el nombre, estos deben ser substituidos por underscore _
- Se recomienda que el nombre de la variable sea descriptivo de lo que representa.

Ejemplo: ```coche_de_un_amigo```

### Comentarios
Los comentarios son muy importantes para poder entender el código. Una línea de comentario se realiza con un #
```python
#Esto es un comentario de línea en python
```
Si queremos comentar un bloque en python, lo haremos abriendo y cerrando el bloque con """
```python
"""Esto es un bloque
que contiene varias líneas
y queremos dejarlo como comentario 
"""
```
### Indentación python
A diferencia del lenguaje C donde un bloque lo abrimos y cerramos con corchetes {} en python se hace con los : y el tab. Python confía que abrimos y cerramos un bloque solo con la indentación, por este motivo es muy importante

Ejemplo C:
```shell
if (condicion) {
  Instrucción 1;
  Instrucción 2;
  Instrucción n;
}
  else {
    Instrucción A;
    Instrucción B;
  }
```
Ejemplo python:
```python
if (condicion):
    Instrucción 1
else:
    instrucción 2
```
---
# Test sobre quesos
Realizaremos una encuesta para ver con detalle el if.
Antes comentaremos un par de notas de interés en el código.
Con la función ```len()``` obtenemos el número de caracteres de un string.
Esto nos puede ser de utiidad como veremos en la quiz para hacer subrayados simple de strings. 

Ejemplo subrayado simple con len()
```python
titulo = "Biernvenido al Test sobre el queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
```
Para poder hacer un print de un bloque de texto, python necesita que esté todo en úna línea, pero si nosotros queremos mantener la estructura de tabulación dentro del código, lo podemos hacer con triple doble comilla """
Ejemplo:
```python
opcion = input("""Pregunta 1: que haces cuando ves una tabla de quesos?
A - Salgo corriendo.
B - Pruebo una de los quesos o incluso varios.
C - No puedo exitar devorarla
""")
```
O con \n y comillas de esta forma podemos poner los tabuladores dentro del código, quizás sería una buena opción para mantener visualmente la misma estructura de bloque de texto en el código, ejemplo:
```python
opcion = input("Pregunta 1: que haces cuando ves una tabla de quesos?\n"
                "A - Salgo corriendo.\n"
                "B - Pruebo una de los quesos o incluso varios.\n"
                "C - No puedo exitar devorarla\n"
)
```
En python else if, es ```elif``` como podremos ver en el ejemplo siguiente. Al igual que sumar un valor al valor actual de una variable se puede hacer con el puntucacion +=5, esto equivale a puntuacion = puntuacion + 5.
Ejemplo:
```python
if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()
```
Y para finalizar, aquí el programa completo:
```python
titulo = "Biernvenido al Test sobre el queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: que haces cuando ves una tabla de quesos?\n"
                "A - Salgo corriendo.\n"
                "B - Pruebo una de los quesos o incluso varios.\n"
                "C - No puedo exitar devorarla\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 2: como te gusta la hamburguesa?\n"
                "A - Sin queso.\n"
                "B - Con queso.\n"
                "C - Pan y queso\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 3: Eres intolerante a la lactosa?\n"
                "A - Si.\n"
                "B - A veces.\n"
                "C - No\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres fanático de los quesos")
elif puntuacion >=15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso")
else:
    print("Resultado: Felicidades, no te gusta el queso")
print (puntuacion)
```
>Ejercicios/[quiz.py](https://github.com/badorius/Python_MasterMind/blob/master/Ejercicios/quiz.py)
---
#Eligiendo tu nuevo movil
En primer lugar vamos a mejorar el conversor de divisas, para ello crearemos un nuevo programa conversor_de_divisas.py
