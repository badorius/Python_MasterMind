from lista_productos import productos
from random import randint

# Function to print title menu
def print_titulo():
    titulo="Programa lista de la compra"
    print(titulo)
    print("-" * len(titulo))


# Function print list of products on products list with index number
def print_products():
    for producto in productos:
        index = productos.index(producto)
        print("[ {} ] {}".format (index,producto))


# Function ask for user product number
def input_user_product():
    usernumber = "Wrong"
    while usernumber.isdigit() == False or int(usernumber) >= len(productos):
        usernumber = input("Selecciona uno de los productos de la lista por su número [ 0 - {} ]: ".format(len(productos)-1))

    return int(usernumber)

# Add product to shopping cart list
def add_shopping_cart(cart, user_product):
    user_exit = len(productos)-1
    if user_product != user_exit:
        cart.append(productos[user_product])

    return cart


def lista_compra():
    lista = [],[]
    opcion = None
    elemento = None

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

def main():
    user_product = None
    user_exit = len(productos)-1
    cart = []

    while user_product != user_exit:

        print_titulo()
        print_products()
        user_product = input_user_product()
        cart = add_shopping_cart(cart, user_product)

    for i in cart:
        print(i)
    #lista_compra()

if __name__ == "__main__":
    main()