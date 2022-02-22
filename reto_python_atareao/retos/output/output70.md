





HPUX - Eliminar dispositivos que no estan en uso (STALE) + replace\_wwid | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Eliminar dispositivos que no estan en uso (STALE) + replace\_wwid

 

Mié, 09/28/2011 - 09:04 — badorius

Es una tarea rutinaria para un administrador, la de asignar y desasignar Luns a un servidor. En HPUX cada dispositivo nuevo nos creará un special file después de hacer un ioscan ; insf.  

Que pasa si después desasignamos esta lun? No pasa nada, pero los ficheros de dispositivo (special files) continúan residentes en el sistema, una manera de hacer limpieza es con el rmsf -x (Stale).


Con lo siguiente eliminaríamos los SpecialFiles que no están en uso y tras un ioscan, reinstalaríamos todos los specialfiles nuevamente:  

`rmsf -x ; ioscan ; insf -e`


Adicionalmente, nos podemos encontrar, que al desasignar una Lun y asignar una nueva, nos aparezcan los siguientes errores en el dmesg:  

`Lunpath, instance 952  

An attempt to probe existing LUN id 0x0 failed with error of 5`


Lo solucionaríamos con un replace\_wwid donde pasaríamos el número de instance con el flag -I (ejemplo 952, 953, 955...)


`scsimgr -f replace_wwid -C lunpath -I 952  

scsimgr -f replace_wwid -C lunpath -I 953  

scsimgr -f replace_wwid -C lunpath -I 955  

scsimgr -f replace_wwid -C lunpath -I 956  

scsimgr -f replace_wwid -C lunpath -I 958`


Tras esto se tendría que volver a lanzar un ioscan; insf.


La lun no será visible hasta que no realicemos dicha operación.





* [HPUX](/?q=taxonomy/term/6)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F70%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




