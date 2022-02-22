





Shell - Matar todos los procesos de un usuario. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Shell - Matar todos los procesos de un usuario.

 

Lun, 11/22/2010 - 16:09 — badorius

Para matar todos los procesos relacionados con un usuario,  

simplemente:


`kill -9 `ps -aef|grep nombreusuario|awk '{ print $2 }'``


Sería elegante ponerse antes en contacto con el usuario, o no...  

También aplicaría para cualquier cadena que quisiéramos poner en el grep.





* [HPUX](/?q=taxonomy/term/6)
* [Linux](/?q=taxonomy/term/2)
* [Shell](/?q=taxonomy/term/12)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F49%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




