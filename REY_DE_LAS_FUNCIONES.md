# Esto son funciones
Programación imperativa es aquella en la que se seguiran las instrucciones línea a línea, sin poder volver atrás.
Las funciones nos servirán para guardar una secuencia de código bajo un nombre para poder ejecutarlas haciendo referencia a ese nombre en cualquier momento.

Ejemplo básico función:
```python
def saludo_secreto():
    print("Hola Mundo")

    a = input("Cómo estás?")
    b = input("Dos más dos?")

    if b == "2":
        print("Tu si que sabes...")

saludo_secreto()
```
>**NOTA:**
Entre funciones y código main, deben existir 2 líneas como mínimo.
Cuando llamamos a la función lo hacemos con saludo_secreto(), si no ponemos los paréntesis, estamos haciendo referencia al objecto, no llamando a la función, ya que en python las funciones son objetos. 

En python todo son objetos. Podríamos hacer un print del objeto/función, ejemplo y nos mostraría la dirección de memorial:
```python
print(saludo_secreto)
<function saludo_secreto at 0x7f4e2e167d90>
```

Ejemplo pasar argumentos a las funciones:
```python
def saludo_sectario(nombre):
    print("Hola {}".format(nombre[::-1]))

saludo_sectario("nataS")
saludo_sectario("reficuL")
saludo_sectario("htiliL")
saludo_sectario("ratS gninroM")
```
>**Nota: 
Para darle la vuelta a un string, hemos utilizado nombre[::-1], lo veremos con más detalle.**

Ejemplo devolver argumento función con return:
```python
def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo

largo_de_la_string = largo_string("Hola mundo")
print(largo_de_la_string)
```
>Nota:
return siempre es el fin de la función, pararía la función, si ponemos solo return la función finalizaría, si ponemos return $VARIABLE, la función finalizará devolviendo el valor de la variable.
Las variables que están dentro de la función, se eliminan automáticamente una vez finalizada la función. Podríamos decir que la función, es su un programa con sus variables y sus estados, todo lo que ocurra dentro se elimina una vez finaliza la función.

Python ya tiene built in functions, podemos dar un vistazo en:
[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

Realmente, abrir un archivo en python y empezar a escribir todo el código entero en el, no es el concepto correcto de python. A partir de ahora, la estructura que utilizaremos será como la del siguiente ejemplo:
```python
def main():
    print("Hola mundo")

if __name__ == "__main__":
    main()
```
Programaremos todo dentro de main, programación funcional.

**Ejerecicios "Esto son funciones"**

Usando la nueva estructura de programas basado en la función main() y la condición if final, crea un programa de cualquier tipo. Lo que te de la gana. Usa el debugger para ver como se produce el hilo de ejecución del código.
[Ejercicio 1](https://github.com/badorius/curso-python/blob/master/Ejercicios/modulo_funciones/Ejercicio1.py)

Crea un programa que contenga una función que calcule la potencia de un numero introducido como argumento, por ejemplo:
[Ejercicio 2](https://github.com/badorius/curso-python/blob/master/Ejercicios/modulo_funciones/Ejercicio2.py)

---
# Experimentos
Cuando definimos una funcion y no queremos que en esta se ejecute nada, lo haremos con pass:
```python
def main():
    pass
```
Ejemplo de recursividad:
Funciones que llaman a otra funcion dentro de un bucle:
```python
from time import sleep

def c():
    print("c")
    sleep(1)
    a()

def b():
    print("b")
    sleep(1)
    c()

def a():
    print("a")
    sleep(1)
    b()

def main():
    a()

if __name__ == "__main__":
    main()
```
Ejemplo recursividad 2: 
```python
from time import sleep

def sumar_uno(a):
    print (a)
    a += 1
    if a  != 100:
        sumar_uno(a)

def main():
    sumar_uno(1)

if __name__ == "__main__":
    main()
```

La recursividad tiene sus usos, como por ejemplo en la Secuencia de [fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci) en la que en una sequencia de numeros, cada numero se suma con el anterior.
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597

Ejemplo recursividad fibonacci:
```python
from time import sleep
MAX_NUM = 30000000

def sumar_uno(a, b):
    next_num = a + b
    print("{}, ".format(next_num),end ="")
    a = b
    b = next_num
    if next_num<= MAX_NUM:
        sumar_uno(a, b)

def main():
    a = 0
    b = 1
    sumar_uno(a, b)

if __name__ == "__main__":
    main()
```
[fibonaccy](https://github.com/badorius/curso-python/blob/master/Ejercicios/modulo_funciones/fibonacci.py)
