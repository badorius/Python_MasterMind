import os
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANO_BARRA_DE_VIDA = 100

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

# FORMULA A% de C = C*A/100
formula_pikachu = int(vida_pikachu * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
formula_squirtle = int(vida_squirtle * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)


# FUNC BORRAR PANTALLA
def borrarpantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def barra_vida():
    global formula_pikachu, formula_squirtle, TAMANO_BARRA_DE_VIDA, vida_pikachu, vida_squirtle
    if vida_pikachu < 0:
        vida_pikachu = 0
        print("Pikachu  {} ({}/{})".format(
            "[" + "*" * formula_pikachu + " " * (TAMANO_BARRA_DE_VIDA - formula_pikachu) + "]", vida_pikachu,
            VIDA_INICIAL_PIKACHU))
        print("Squirtle {} ({}/{})".format(
            "[" + "*" * formula_squirtle + " " * (TAMANO_BARRA_DE_VIDA - formula_squirtle) + "]", vida_squirtle,
            VIDA_INICIAL_SQUIRTLE))
        print("Squirtle gana!")
        exit(0)

    if vida_squirtle < 0:
        vida_squirtle = 0
        print("Pikachu  {} ({}/{})".format(
            "[" + "*" * formula_pikachu + " " * (TAMANO_BARRA_DE_VIDA - formula_pikachu) + "]", vida_pikachu,
            VIDA_INICIAL_PIKACHU))
        print("Squirtle {} ({}/{})".format(
            "[" + "*" * formula_squirtle + " " * (TAMANO_BARRA_DE_VIDA - formula_squirtle) + "]", vida_squirtle,
            VIDA_INICIAL_SQUIRTLE))
        print("Pikachu gana!")
        exit(0)

    print("Pikachu  {} ({}/{})".format("[" + "*" * formula_pikachu + " " * (TAMANO_BARRA_DE_VIDA- formula_pikachu) + "]", vida_pikachu, VIDA_INICIAL_PIKACHU))
    print("Squirtle {} ({}/{})".format("[" + "*" * formula_squirtle + " " * (TAMANO_BARRA_DE_VIDA- formula_squirtle) + "]", vida_squirtle, VIDA_INICIAL_SQUIRTLE))

borrarpantalla()
barra_vida()

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
    formula_pikachu = int(vida_pikachu * TAMANO_BARRA_DE_VIDA/ VIDA_INICIAL_PIKACHU)
    formula_squirtle = int(vida_squirtle * TAMANO_BARRA_DE_VIDA/ VIDA_INICIAL_SQUIRTLE)

    input("Enter para continuar...")
    borrarpantalla()
    barra_vida()


    # Turno de squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ['P', 'A', 'B', 'N']:
    #while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja [N]ada: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje.")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con pistola agua.")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja.")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no ataca.")
        vida_pikachu -= 0

    # FORMULA A% de C = C*A/100
    formula_pikachu = int(vida_pikachu * TAMANO_BARRA_DE_VIDA/ VIDA_INICIAL_PIKACHU)
    formula_squirtle = int(vida_squirtle * TAMANO_BARRA_DE_VIDA/ VIDA_INICIAL_SQUIRTLE)

    input("Enter para continuar...")
    borrarpantalla()
    barra_vida()


if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")


