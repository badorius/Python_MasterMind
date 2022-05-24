from lista_productos import productos
import os
from random import randint


# FUNC BORRAR PANTALLA
def borrarpantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


# Function to print title menu
def print_titulo():
    titulo="Programa lista de la compra"
    print(titulo)
    print("-" * len(titulo))


# Function print list of products on products list with index number
def print_products(cart):
    default_space = 25

    for producto in productos:
        index = productos.index(producto)
        print_space = len("[ {} ] {}".format (index, producto))
        res_space = default_space - print_space

        if index %2 == 1:
            if producto in cart:
                print_space = len("[ X ] {}".format(producto))
                res_space = default_space - print_space
                print("[ X ] {}".format (producto), end='')
                print(" " * res_space, end='')
            else:
                print("[ {} ] {}".format (index, producto), end='')
                print(" " * res_space, end='')

        elif index %2 == 0:
            if producto in cart:
                print_space = len("[ X ] {}".format(producto))
                res_space = default_space - print_space
                print("[ X ] {}".format (producto), end='')
                print(" " * res_space)
            else:
                print("[ {} ] {}".format (index, producto), end='')
                print(" " * res_space)


# Function ask for user product number
def input_user_product():
    usernumber = "Wrong"
    while usernumber.isdigit() == False or int(usernumber) >= len(productos):
        usernumber = input("Selecciona uno de los productos de la lista por su número [ 0 - {} ]: ".format(len(productos)-1))

    return int(usernumber)


# Add product to shopping cart list
def add_shopping_cart(cart, user_product):
    user_exit = len(productos)-1
    if productos[user_product] in cart:
        input("Ta tienes {} en la lista de la compra!, selecciona otro producto. [ENTER] para continuar.".format(productos[user_product]))
    elif user_product != user_exit:
        cart.append(productos[user_product])

    return cart

def main():
    user_product = None
    user_exit = len(productos)-1
    cart = []

    while user_product != user_exit:

        print_titulo()
        print_products(cart)
        user_product = input_user_product()
        cart = add_shopping_cart(cart, user_product)
        borrarpantalla()

    print_titulo()
    for i in cart:
        print(i)


if __name__ == "__main__":
    main()