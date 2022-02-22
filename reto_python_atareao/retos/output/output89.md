





AIX - Extender LV + Filsystem en HA | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - Extender LV + Filsystem en HA

 

Mié, 03/19/2014 - 11:06 — badorius

Para extender un filesystem que pertenece a un recurso del cluster, primero extenderemos el lv con comando de cluster:  

 `/usr/es/sbin/cluster/sbin/cl_extendlv -R'node' LVName LPs HDISK`  

Seguidamente, podemos ampliar el filesystem de la forma habitual.  

 `chfs -a size=512G /mountpoint (en el nodo montado)`  

No está de mas sincronizar cluster tras la acción.





* [AIX](/?q=taxonomy/term/8)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F89%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




