#Asignamos el valor fahrenheit a la variable fahren mediante input, devolviendo un float.
fahren=float(input("Introduce el valor en fahrenheit para ser convertido a Celsius: "))
#Aplicamos la fórmula de conversión con float y la asignamos a una nueva variable
celsi=float((fahren-32)*5/9)
#Imprimimos el resultado utilizando format.
print("{} ℉ son {} ℃".format(fahren, celsi))
