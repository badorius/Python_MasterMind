





Linux - tar extraer un solo fichero. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - tar extraer un solo fichero.

 

Lun, 10/18/2010 - 10:27 — badorius

Pare extraer un único fichero de un tar, poniendo como ejemplo el fichero etc/default/sysstat de confit.tar.gz


 `$ tar -ztvf config.tar.gz  

$ tar -zxvf config.tar.gz etc/default/sysstat  

$ tar -xvf {tarball.tar} {path/to/file}`


También podríamos hacer:


 `tar --extract --file={tarball.tar} {file}  

Extract a directory called css from cbz.tar:  

$ tar --extract --file=cbz.tar css`





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F46%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




