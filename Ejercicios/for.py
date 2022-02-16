vocales = ["a", "e", "i", "o", "u"]
vocales_encontradas = 0

frase = input ("Introduzca una frase para contar sus vocales: ")
for letra in frase:
    if letra in vocales:
        vocales_encontradas +=1
        print("He encontrado una {}".format(letra))

print("El número de vocales en la frase introducida és de: {}".format(vocales_encontradas))