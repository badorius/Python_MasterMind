





Minimal package install for X11 forwarding in Linux | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Minimal package install for X11 forwarding in Linux

 

Mié, 02/13/2013 - 16:23 — badorius

Minimal package install for X11 forwarding in Linux


urw-fonts For X forwarding  

xorg-x11-xauth For X forwarding


And X11Forwarding yes on file /etc/ssh/sshd\_config 


[root@server01 ~]# grep -i x11for /etc/ssh/sshd\_config  

X11Forwarding yes





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F79%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




