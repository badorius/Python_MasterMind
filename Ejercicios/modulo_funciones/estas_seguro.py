def estas_seguro(respuesta):
    if respuesta == "S":
        return True
    else:
        return False

def main():
    respuesta = input("Estás seguro [S/N]?: ")
    if estas_seguro(respuesta):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()