import os
usuario = os.getlogin()
directorio_descargas = "/home/" + usuario + "/Descargas"
directorio_downloads = "/home/" + usuario + "/Downloads"

if os.path.isdir(directorio_descargas):
    directorio=directorio_descargas
    print(os.listdir(directorio_descargas))
elif os.path.isdir(directorio_downloads):
    directorio=directorio_downloads

print("Directorio: {} \n".format(directorio))
for file in os.listdir(directorio):
    print(file)
