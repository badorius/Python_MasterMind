





HPUX Restricted Sam | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX Restricted Sam

 

Jue, 09/09/2010 - 15:23 — badorius

Para poder dar acceso a la sam o smh a un usuario pero de una manera restrictiva, se podría hacer con:


`sam -r`


Nos mostrará un menú donde podremos seleccionar que puede o no puede administrar el usuario desde la sam.


Si hemos configurado un usuario y queremos replicar esta configuración a otros usuario y/o servidores, en el directorio:


`/etc/sam/rsam/usr/`


Y en este un fichero por cada usuario con la configuración de la sam, con un simple copiar ya tendríamos la configuración copiada a otro usuario y/o servidor


`cp /etc/sam/rsam/usr/fulanito /etc/sam/rsam/usr/menganito`


o


`scp /etc/sam/rsam/usr/fulanito srvhpux:/etc/sam/rsam/usr/fulanito`





* [HPUX](/?q=taxonomy/term/6)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F41%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




