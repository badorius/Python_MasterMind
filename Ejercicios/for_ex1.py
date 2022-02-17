"""
#Ejemplo
texto_usuario = "Hola, me llamo Nate. Tu como te llamas?

espacios = 6
puntos = 1
comas = 1
"""
espacios = 0
puntos = 0
comas = 0

texto_usuario = input("Introducir texto: ")

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == "\"":
        comas += 1

print("Tenemos un total de {} espacios, {} puntos, {} comas.".format(espacios, puntos, comas))
