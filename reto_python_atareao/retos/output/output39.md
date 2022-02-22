





Linux mount Windows Share + directorio con acento = codifiación no valida | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux mount Windows Share + directorio con acento = codifiación no valida

 

Jue, 08/19/2010 - 11:32 — badorius

Un pequeño detalle a la hora de montar un share windows.  

En primer lugar, configuré el share en el fstab de la siguiente forma:


 `//servidor/share /mnt/shareWindows smbfs username=badorius 0 0`


Al navegar por el sistema de ficheros compartido, me encontraba con que los directorios o ficheros con acentos se mostraban mal (tanto por consola como por dolphin/konqueror/nautilus) algo pareceido a:


 `/mnt/shareWindows/Tecnolog?a/Informaci?n/Administraci?n.txt`


Tras verificar que tanto las locales como el KDE estaban bien configurados a nivel de carácter, y que este problema solo aparecía en este sistema de ficheros, di con la solución añadiendo "iocharset=utf8" en el fstab, quedando de la siguiente forma:


 `//servidor/share /mnt/shareWindows smbfs iocharset=utf8,username=badorius 0 0`


Resultado:


 `/mnt/shareWindows/Tecnología/Información/Administración.txt`





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F39%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




