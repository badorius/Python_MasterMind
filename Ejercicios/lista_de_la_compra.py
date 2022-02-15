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
