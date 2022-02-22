





Oracle - HPUX - Crear fichero Pipe para export Oracle | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Oracle - HPUX - Crear fichero Pipe para export Oracle

 

Mar, 10/11/2011 - 15:59 — badorius

Como crear un fichero de tipo pipe para luego ser usado en un export:


`mknod /dev/BASEDATOS.pipe.dmp p`


Tras esto ya podemos realizar el export:


exp userid=system/manager file=/dev/BASEDATOS.pipe.dmp full=yes log=exportBASEDATOS.log


Si no creamos el fichero tipo pipe, al realizar el export tendremos un problema ocupación en el filesystem 8-O





* [HPUX](/?q=taxonomy/term/6)
* [Oracle](/?q=taxonomy/term/7)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F71%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




