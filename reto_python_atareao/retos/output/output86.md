





HPUX - Montar Share de windows con CIFS | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Montar Share de windows con CIFS

 

Lun, 12/30/2013 - 11:15 — badorius

Montar un share de windows en HPUX con CIFS, 


Creamos el directorio donde montaremos el share:  

 `mkdir /share`


Configuramos el CIFS para que arranque automáticamente en el boot (opcional) editando el siguiente fichero:  

 `vi /etc/rc.config.d/cifsclient`


Modificamos el siguiente valor a 1:  

 `RUN_CIFSCLIENT=1.`


Arrancamos el servicio de CIFS:  

 `/opt/cifsclient/bin/cifsclient start`


Si el share necesita credenciales, primero será necesario autenticarse contra la máquina/dominio:  

 `cifslogin [SERVIDORWINDOWS] -U [USUARIO] -D [DOMINIO] -s`  

Esto nos pedirá las credenciales.


Una vez autenticado contra la máquina podemos montar el share remoto:  

 `cifsmount //MSSERVER/$SHARE /share -s`


Validamos con cifslist si el recurso está montado.  

 `root@hpuxserver01:/root # cifslist  

Mounted Object Mountpoint State  

-------------------------------------------------------------------------------  

\\MSSERVER.DOMINIO.COM \SHARE$ /share MS  

===============================================================================  

Server Local User Remote User Domain State  

-------------------------------------------------------------------------------  

MSSERVER.DOMINIO.COM root USUARIO DOMINIO LS  

root@hpuxserver01:/root #`





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F86%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




