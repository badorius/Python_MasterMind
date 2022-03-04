import os
import random

import readchar


POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11
obstacle_definition = """\
############################
                        ####
##############          ####
##############          ####
##################      ####
#####                   ####
#####     ##########    ####
######                  ####
############     #####  ####
#############   ####### ####
#############   ####### ####
##############          ####
########            ########
##############          ####
############################\
"""

my_position = [3, 1]
tail = []
tail_lenght = 0
map_objects = []

end_game = False
died = False

# Create obstacle map with list comprehsion (compresion de lista)
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while not end_game:
    #my_position[POS_X]
    #my_position[POS_Y]
    #borramos pantalla
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    #DRAW MAP
    print("+" + '-' * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print ("|", end='')
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            #Unset object_in_cell var for each redraw.
            #There not objects where we are
            object_in_cell = None
            #There no tail where we are
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    #We are on object possition, so we set object_in_cell var with coordenate value do delete object from list
                    object_in_cell = map_object

            # We draw all tail lenght with for
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                # If var object_in_cell is not None, we have to remove coordenate value from list:
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + '-' * MAP_WIDTH * 3 + "+")
    print("Tamaño de la cola {}".format(tail))

    #direction = input("Dónde te quieres mover? [WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    if direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    if direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    if direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    if direction == "q":
        end_game = True



    if died:
         print("Has muerto!")