
def lista_compra():
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

def main():
    lista_compra()

if __name__ == "__main__":
    main()