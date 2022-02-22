





Linux Unix Copiar contendio con redirected tar | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux Unix Copiar contendio con redirected tar

 

Vie, 06/06/2014 - 10:52 — badorius

Como copiar todo el contenido de un directorio a otro con tar como si fuera un backup restore, conservando todos los permisos y owners:  

 `tar cvf - . | (cd /root/; tar xvf -)`  

Un ejemplo de copiar contenido con tar + remsh o ssh :  

 `tar cvf - /oracle/client/11x_64/instantclient_11204 | remsh $SERVERNAME tar xvf - /oracle/client/11x_64/instantclient_11204  

tar cvf - /oracle/client/11x_64/instantclient_11204 | ssh $SERVERNAME tar xvf - /oracle/client/11x_64/instantclient_11204`





* [AIX](/?q=taxonomy/term/8)
* [HPUX](/?q=taxonomy/term/6)
* [Linux](/?q=taxonomy/term/2)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F90%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




