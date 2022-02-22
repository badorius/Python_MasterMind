





Editar un comando ksh - vi | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Editar un comando ksh - vi

 

Jue, 12/31/2009 - 21:22 — badorius

Algunas veces, estamos lanzando un comando desde la ksh un poco largo, también conocido como "churro"


`while true ; do [ -f /home/pepe/file ] && mv /home/simpson /pub/bar && rm /bin/laden ....` 


Y en medio del churro, nos equivocamos tipeando, pues una buena solución es entrar en el vi desde la shell, presionando ESC y luego la tecla v.


Una vez desde el vi, ya podemos editar todo el churro comodamente, al finalizar hacemos :wq para lanzarlo en la ksh.


Nota, en linux desde la ksh quizás necesitamos hacer:  

`set -o vi`  

Para tener vi en la ksh.


Bueno mi último post del año.





* [Linux](/?q=taxonomy/term/2)
* [Unix](/?q=taxonomy/term/1)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




