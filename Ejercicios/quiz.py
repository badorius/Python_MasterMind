
titulo = "Biernvenido al Test sobre el queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: que haces cuando ves una tabla de quesos?\n"
                "A - Salgo corriendo.\n"
                "B - Pruebo una de los quesos o incluso varios.\n"
                "C - No puedo exitar devorarla\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 2: como te gusta la hamburguesa?\n"
                "A - Sin queso.\n"
                "B - Con queso.\n"
                "C - Pan y queso\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 3: Eres intolerante a la lactosa?\n"
                "A - Si.\n"
                "B - A veces.\n"
                "C - No\n"
)

if opcion == "A":
    #puntuacion = puntuacion + 0
    puntuacion += 0
elif opcion == "B":
    # puntuacion = puntuacion + 5
    puntuacion += 5
elif opcion == "C":
    # puntuacion = puntuacion + 10
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres fanático de los quesos")
elif puntuacion >=15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso")
else:
    print("Resultado: Felicidades, no te gusta el queso")
print (puntuacion)
