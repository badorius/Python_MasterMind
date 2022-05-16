def es_impar(numero):
    if numero % 2 == 0:
        print("El número {} es par.".format(numero))
    else:
        print("El número {} es impar.".format(numero))

def main():
    numero=int(input("Introducir número: "))
    es_impar(numero)

if __name__ == "__main__":
    main()