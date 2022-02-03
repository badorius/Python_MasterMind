#Introducimos tres números con la funcion input y la asignamos a la variable convertiendo esta de tipo int
numero1=int(input("Introduce el primero número: "))
numero2=int(input("Introduce el segundo número: "))
numero3=int(input("Introduce el tercer  número: "))

#Con la función max y min búscamos el número mayor y menor

"""print ("El número mayor es:" + str(max(numero1, numero2, numero3)))
   print ("El número menor es:" + str(min(numero1, numero2, numero3)))"""

#Modificamos el print con el método format:
print("El número mayor entre {} {} {} es el {} y el menor el {}".format(numero1, numero2, numero3,
                                                                         max(numero1, numero2, numero3),
                                                                         min(numero1, numero2, numero3)
                                                                        )
      )


