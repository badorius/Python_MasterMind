import os
import random

import readchar
import pokemon




POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11
obstacle_definition = """\
############################
                        ####
                        ####
##############          ####
##################      ####
#####                   ####
#####     ##########    ####
######                  ####
###### #####     #####  ####
###### ######   ####### ####
###### ######   ####### ####
###### ######           ####
######              ########
##############          ####
############################\
"""

my_position = [0, 1]
tail = []
tail_lenght = 0
map_objects = []
score = 0

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
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

    #DRAW MAP
    print("+" + '-' * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print ("|", end='')
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            #Unset object_in_cell var for each redraw.
            #There not objects where we are
            object_in_cell = None
            #There no tail where we are
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    #We are on object possition, so we set object_in_cell var with coordenate value do delete object from list
                    object_in_cell = map_object

            # We draw all tail lenght with for
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                # If var object_in_cell is not None, we have to remove coordenate value from list:
                if object_in_cell:
                    pokemon.borrarpantalla()
                    pokemon.barra_vida()
                    pokemon.main_run_poquemon()
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1
                    score += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + '-' * MAP_WIDTH * 2 + "+")
    print("SCORE: {}".format(score))

    #direction = input("Dónde te quieres mover? [WASD]: ")
    direction = readchar.readchar()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_lenght]
            my_position = new_position


    if died:
         print("Has muerto!")