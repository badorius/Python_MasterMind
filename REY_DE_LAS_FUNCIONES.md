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
Cuando llamamos a la función lo hacemos con saludo_secreto(), si no ponemos los paréntesis, estamos haciendo referencia al objecto, no llamando a la función, ya que en python las funciones son objetos. En python todo son objetos.
Podríamos hacer un print del objeto/función, ejemplo y nos mostraría la dirección de memorial:

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

Ejemplo devolver argumento función:
```python

```
