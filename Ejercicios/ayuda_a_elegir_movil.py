"""
iPhone Ultra Pro Max
iPhone segunda mano
Android xino 100€
Google Pixel supercamara
Android calidad-precio

- IOS o Android?
  - Andriod
      - No tines dinero?
        - No tienes dinero: Android chino de 100€
      - Tienes dinero?
        - Te importa la camara del móvil?
          - Si: Google Pixel supercamara
          - No: Android calidad-precio
          -
  - IOS
      - Tienes dinero?
        - Si: Iphone Ultra Pro Max
        - No: Iphone segunda mando
"""

opcion = input("[I]IOS o [A]Android")
movil_ideal = "Ninguno"

if opcion == "A": # Ha seleccionado Android
    opcion = input("Tienes dinero? [S/N]")
    if opcion == "S":  # Tiene dinero
        opcion = input("Te importa la camara del móvil? [S/N]")
        if opcion == "S":  #Si le importa la camara
            movil_ideal = "Google Pixel supercamara"
        else:
            movil_ideal = "Android calidad-precio"
    else:
        movil_ideal = "Android xino 100€"

elif opcion == "I": # Ha seleccionado IOS
    opcion = input("Tienes dinero? [S/N]")
    if opcion == "S":  # Tiene dinero
        movil_ideal = "Iphone Ultra Pro Max"
    else:
        movil_ideal = "iPhone segunda mano"

print("Te móvil ideal es: " + movil_ideal)