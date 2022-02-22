





Elimnar ^M(aldito) salto de línea. | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Elimnar ^M(aldito) salto de línea.

 

Lun, 12/21/2009 - 15:19 — badorius

A raíz de estar arto de encontrarme con el maldito carácter ^M de salto de línea en ficheros que algún usuario ha subido por ftp al servidor, encontré esta solución:


`cat fichero1|col –b > fichero2`


Donde fichero1 es el fichero con el maldito salto de línea del DOS y fichero2 es donde obtendremos el fichero ya tratado, eliminando a este el salto de línea gracias al col –b 


col –b alabado seas.


Badorius.





* [Unix](/?q=taxonomy/term/1)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




