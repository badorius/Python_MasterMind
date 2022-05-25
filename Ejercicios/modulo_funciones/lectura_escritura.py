
SALIDA = "SALIR"

def preguntar_producto_usuario():
    return input("Introduce un producto [ {} para salir ]: ".format(SALIDA))

def main():

    lista_compra = []

    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_producto_usuario()

    a = open("compra.txt", "w")
    a.write("\n".join(lista_compra))
    a.close()

if __name__ == "__main__":
    main()