"""def saludo_secreto():
    print("Hola Mundo")

    a = input("Cómo estás?")
    b = input("Dos más dos?")

    if b == "2":
        print("Tu si que sabes...")

saludo_secreto()"""

"""def saludo_sectario(nombre):
    print("Hola {}".format(nombre[::-1]))

saludo_sectario("nataS")
saludo_sectario("reficuL")
saludo_sectario("htiliL")
saludo_sectario("ratS gninroM")"""

def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo

largo_de_la_string = largo_string("Hola mundo")
print(largo_de_la_string)
print(len("Hola mundo"))