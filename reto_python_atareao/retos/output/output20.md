





Desabilitar SSL en NodeManager de Weblogic | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Desabilitar SSL en NodeManager de Weblogic

 

Mar, 04/06/2010 - 16:47 — badorius

Si queremos desactivar el SSL de nuestro Nodemanager, no será suficiente desactivándolo desde la consola de administración-> Machine -> NodeManager -> Type: Plain.


Adicionalmente se tendrá que editar el siguiente fichero, que contiene los parametros de arranque de NodeManager:


 `/Oracle/Middleware/wlserver_10.3/common/nodemanager/nodemanager.properties`


Donde el parámetro:


 `SecureListener=true`


Lo podremos en:


 `SecureListener=false`





* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F20%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




