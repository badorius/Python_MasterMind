
SALIDA = "SALIR"

items_del_supermercado = ["pollo", "maiz", "lechuga", "pan"]


def preguntar_producto_usuario():
    item_elegido = input("Introduce un producto [ {} para salir ]: ".format(SALIDA))
    while item_elegido.lower() not in items_del_supermercado and item_elegido != SALIDA:
        print("El item que has escrito no esta en la lista")
        item_elegido = input("Introduce un producto [ {} para salir ]: ".format(SALIDA))
    return item_elegido


def guardar_lista_a_disco(lista_compra):
    nombre_fichero = input("Como quieres que se llame el archivo? ")
    # En python podemos abreviar el abrir y cerrar ficheros de la siguiente forma:
    with open(nombre_fichero + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))
    # Con esto abrimos, escribimos y cerramos el fichero.


def main():
    lista_compra = []
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_producto_usuario()

    guardar_lista_a_disco(lista_compra)


if __name__ == "__main__":
    main()