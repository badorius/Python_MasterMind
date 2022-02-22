





Vmware - Linux Añadir nuevo disco sin reiniciar Guest. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Vmware - Linux Añadir nuevo disco sin reiniciar Guest.

 

Mié, 06/08/2011 - 11:44 — badorius

Cuando tenemos una servidor virtualizado en producción y queremos añadir un nuevo disco, para que el Guest reconozca el disco sin necesidad de reiniciar este (lo que vendría a ser un ioscan ; insf en HPUX), podriamos montarnos con el siguiente contenido: 


`#!/bin/bash  

HOSTID=`ls /sys/class/scsi_host`  

echo $HOSTID  

for i in $HOSTID ; do  

echo "- - -" > /sys/class/scsi_host/$i/scan`  

done  

Esto se entiende que solo tiene una sola "placa SCSI" virtual, ya que si no podríamos tener mas de un HOSTID.


Después de ejecutar el script, ya podemos ver la lun, haciendo un "dmesg" o un "fdisk -l".





* [Debian](/?q=taxonomy/term/13)
* [Linux](/?q=taxonomy/term/2)
* [Ubuntu](/?q=taxonomy/term/14)
* [Wmware](/?q=taxonomy/term/15)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F64%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




