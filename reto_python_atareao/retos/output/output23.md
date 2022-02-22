





HPUX Problemas rlogin - DNS | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX Problemas rlogin - DNS

 

Lun, 04/19/2010 - 13:56 — badorius

Estos últimos días, hemos experimentado problemas con la resolución de DNS. Básicamente al tener varios servidores DNS definidos en el fichero /etc/resolv.conf, nos hemos encontrado, que solo fallando uno de estos, ya no podíamos lanzar remsh o rlogin contra otras máquinas.  

La solución ha sido añadir los parámetros retry y retrans al fichero /etc/resolv.conf quedando de la siguiente forma:  

 `root@hpux01:/root # cat /etc/resolv.conf  

domain badorius.com  

nameserver 172.19.193.197 # Servidor DNS 1  

nameserver 192.168.25.10 # Servidor DNS 2  

nameserver 172.19.193.112 # Servidor DNS 3  

retrans 1500  

retry 1  

root@hpux01:/root #`


De esta forma le indicamos que tras 1 intento fallido de 1500 milisegundos pruebe con otro servidor DNS.


Adicionalmente, me parecía muy raro que el rlogin o remsh, no tirase del fichero /etc/hosts. O sea, si yo realizo un relogin a hpux2, donde hpux2 está en mi /etc/hosts, una caída de servidor dns no tendría que afectar… pues si, ya que no tenía configurado la variable de IPNODES en el nsswitch. Por defecto este valor tiene configurado resolver DNS primero.


Con lo que he añadido la variable IPNODES al nsswitch quedando de la siguiente forma:  

 `root@hpblux25:/root #  

root@hpblux25:/root # cat /etc/nsswitch.conf  

hosts: files [NOTFOUND=continue UNAVAIL=continue] dns [NOTFOUND=return UNAVAIL=return]  

services: files [NOTFOUND=return UNAVAIL=continue]  

ipnodes: files [NOTFOUND=continue] dns  

root@hpblux25:/root #`  

Primero lo va a buscar al hosts y si no lo encuentra, lo buscará por DNS





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F23%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




