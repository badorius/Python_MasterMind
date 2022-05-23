from lista_productos import productos, shopping_cart
from random import randint


class shopping_cart:
    def __init__(self, product, items, price):
        self.product = product
        self.items = items
        self.price = price


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


# Function create empty list cart
def create_list_cart():
    product_quantity = 0
    cart = []

    for producto in productos:
        product_price = randint(1, 20)
        cart.append( shopping_cart(producto, product_quantity, product_price) )

        return cart

def add_shopping_cart(user_product):
    pass


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
    cart = create_list_cart()

    while user_product != len(productos)-1:

        print_titulo()
        print_products()
        user_product = input_user_product()
        add_shopping_cart(user_product)

    for obj in cart:
        print(obj.product, obj.items, obj.price)
    #lista_compra()

if __name__ == "__main__":
    main()