





Aix - Eliminar dispositivo de Fibra. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Aix - Eliminar dispositivo de Fibra.

 

Mié, 12/29/2010 - 11:34 — badorius

Tras una migración de cabina, nos encontramos con errores de link al conectar el servidor AIX a los switches.  

Tras cambiar de cable, de puerto de switch, etc... continua con el mismo comportamiento, decidimos eliminar el dispositivo de fibra en el AIX con el siguiente comando: 


`rmdev -l fcs1 -R –d` 


Tras esto, con un cfgmgr, se recrea el dispositivo y ya funciona correctamente.





* [AIX](/?q=taxonomy/term/8)
* [SAN](/?q=taxonomy/term/3)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F54%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




