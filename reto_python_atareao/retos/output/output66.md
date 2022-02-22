





HPUX - Bloquer Desbloquear usuario con modprpw | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Bloquer Desbloquear usuario con modprpw

 

Jue, 07/07/2011 - 16:16 — badorius

Si queremos bloquear un usuario en HPUX sin perder la contraseña de este (sin hacer passwd -l username)


Podemos hacer los siguiente:  

`/usr/lbin/modprpw -l -m alock=YES username  

/usr/lbin/modprpw -l -m alock=NO username`





* [HPUX](/?q=taxonomy/term/6)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F66%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




