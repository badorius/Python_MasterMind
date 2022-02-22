import os
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]
while True:
    #my_position[POS_X]
    #my_position[POS_Y]

    print("+" + '-' * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print ("|",end='')
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ",end='')
            else:
                print("   ",end='')
        print("|")

    print("+" + '-' * MAP_WIDTH * 3 + "+")

    #direction = input("Dónde te quieres mover? [WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
    if direction == "s":
        my_position[POS_Y] += 1
    if direction == "a":
        my_position[POS_X] -= 1
    if direction == "d":
        my_position[POS_X] += 1
    if direction == "q":
        break

    #borramos pantalla
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
