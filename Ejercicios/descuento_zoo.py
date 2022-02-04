edad = int(input("Introduzca su edad: "))
tipo_de_carnet = input("Introduzca su tipo de carnet (E Estudiante / F Familia Numerosa / P Pensionista / N Nada: ")
descuento = 25
if (25 <= edad <=35 and tipo_de_carnet == "E") or edad <= 10 or (edad >= 65 and tipo_de_carnet == "P") or tipo_de_carnet == "F":
    print("Enhorabuena, se le aplica un {}% de descuento".format(descuento))
else:
    print("No cumple los requerimientos para obtener el descuento")

