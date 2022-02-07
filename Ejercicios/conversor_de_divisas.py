dolar_euro = 0.91
libra_euro = 1.18
mensaje = "Bienvenido al conversor de divisas"
print(mensaje + "\n" + "-" * len(mensaje) + "\n")

while(True):
    opcion = input("Elija una opoción de conversión: \n"
                    "A - De dolar a euro \n"
                    "B - De euro a dolar \n"
                    "C - De libra a euro \n"
                    "D - De euro a libra \n"
                    "Q - Salir \n")

    texto_usuario = "Introduzca la cantidad de {} a convertir: "


    if opcion == "A":
        cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
        print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

    elif opcion == "B":
        cantidad_de_dinero = float(input(texto_usuario.format("euros")))
        print("La cantidad en dollars es: {}".format(cantidad_de_dinero / dolar_euro))

    elif opcion == "C":
        cantidad_de_dinero = float(input(texto_usuario.format("libras")))
        print("La cantidad en euros es: {}".format(cantidad_de_dinero * libra_euro))

    elif opcion == "D":
        cantidad_de_dinero = float(input(texto_usuario.format("euros")))
        print("La cantidad en libras es: {}".format(cantidad_de_dinero / libra_euro))

    elif opcion == "Q":
        print("Saliendo del programa.")
        exit(1)
    else:
        print("No elegido ninguna opción valida")
