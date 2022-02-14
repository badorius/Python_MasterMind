from random import randint
vida_inicial_pikachu = 80
vida_inicial_squirtle = 90

vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle

# FORMULA A% de C = C*A/100
formula_pikachu = int(vida_pikachu * 100 / vida_inicial_pikachu)
formula_squirtle = int(vida_pikachu * 100 / vida_inicial_squirtle)

print(formula_squirtle, formula_pikachu)

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate.

    # Turno de pikachu
    print("Turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Vola voltio")
        vida_squirtle -= 10

    else:
        # Onda Trueno
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    # FORMULA A% de C = C*A/100
    formula_pikachu = int(vida_pikachu * 100 / vida_inicial_pikachu)
    formula_squirtle = int(vida_pikachu * 100 / vida_inicial_squirtle)

    print("La vida de pikachu es  {}\nLa vida de squirtle es {}".format("[" + "#" * formula_pikachu + " " * (100 - formula_pikachu) + "]", "[" + "#" * formula_squirtle + " " * (100 - formula_squirtle) + "]"))
    input("Enter para continuar...")

    # Turno de squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje.")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con pistola agua.")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja.")
        vida_pikachu -= 9

    print("La vida de pikachu es  {}\nLa vida de squirtle es {}".format("[" + "#" * formula_pikachu + " " * (100 - formula_pikachu) + "]", "[" + "#" * formula_squirtle + " " * (100 - formula_squirtle) + "]"))
    input("Enter para continuar...")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")


