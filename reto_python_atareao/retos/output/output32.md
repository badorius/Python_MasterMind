





Linux configurar wget con proxy | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux configurar wget con proxy

 

Lun, 06/14/2010 - 14:56 — badorius

Si tenemos una máquina con linux detrás de un proxy el cual nos pide autenticar, la manera de configurar el wget sería editando el fichero /etc/wgetrc.


 `vi /etc/wgetrc`


La parte que tendríamos que añadir sería:


 `http_proxy = [http://servidorproxy.midominio.com:PUERTOPROXY/](http://servidorproxy.midominio.com:PUERTOPROXY/ "http://servidorproxy.midominio.com:PUERTOPROXY/")  

ftp_proxy = [http://servidorproxy.midominio.com:PUERTOPROXY/](http://servidorproxy.midominio.com:PUERTOPROXY/ "http://servidorproxy.midominio.com:PUERTOPROXY/")  

proxy_user=usuarioProxy  

proxy_password=passwordUsuario`





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F32%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




