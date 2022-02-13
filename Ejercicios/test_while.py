#Tipo de variable none
respuesta = None

while respuesta !="A" and respuesta !="B" and respuesta !="C":
    respuesta = input("Que opción prefieres [A, B, C]")

if respuesta == "A":
    print ("Has elegido ok")
elif respuesta == "B":
    print ("Podrias haber elegido mejor")
elif respuesta == "C":
    print ("Has respuesto mal")


numero = 12
while numero > 1:
    print("Mi numero {} es mayor que 1".format(numero))
    numero -= 1

print("Mi numero es {}".format(numero))
