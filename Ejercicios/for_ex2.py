"""
| texto usuario    | "Hola, me llamo Nate. Tu como te llamas?  |
|------------------|-------------------------------------------|
| Output esperado  | mayusculas = 3                            |
"""
import string
letras_mayusculas = 0
texto_usuario = input("Introduzca un texto: ")

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("Mayusculas: {}".format(letras_mayusculas))
