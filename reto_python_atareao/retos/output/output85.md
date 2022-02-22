





HPUX - Servidor Clonado adaptar HostAgent | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Servidor Clonado adaptar HostAgent

 

Mar, 10/22/2013 - 10:46 — badorius

Al clonar una servidor HPUX, tenemos que realizar las siguientes tareas para adaptar el hostagent al nuevo host.


Adaptar el fichero /agentID.txt con los datos del nuevo servidor:  

 `root@hpux01:/root# cat /agentID.txt  

hpux01.grifols.com  

192.168.1.1`  

Eliminar el fichero caché HostIdFile.txt:  

 `root@hpux01:/root # rm /etc/log/HostIdFile.txt`  

Reiniciar el agente:  

 `root@hpux01:/root # /sbin/init.d/agent stop  

Shutting down Unisphere Agent  

root@hpux01:/root # /sbin/init.d/agent start  

Starting Unisphere Agent  

root@hpux01:/root #`





* [EMC](/?q=taxonomy/term/16)
* [HPUX](/?q=taxonomy/term/6)
* [SAN](/?q=taxonomy/term/3)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F85%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




