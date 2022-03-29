def main(numero):
    potencia = numero * numero
    return potencia

if __name__ == "__main__":
    user_numero = int(input("Introduzca un número: "))
    user_potencia = main(user_numero)
    print("La potencia de {} es {}.".format(user_numero, user_potencia))
