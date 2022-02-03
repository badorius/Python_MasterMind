#Libra £ a Euro €
#Asignamos el valor Libra a la variable libra mediante input, devolviendo un float.
libra=float(input("Introduce el valor en Libras para ser convertido a Euros: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
euro=float(libra*1.19)
#Imprimimos el resultado utilizando format.
print("{} Libras son {} Euros".format(libra, euro))