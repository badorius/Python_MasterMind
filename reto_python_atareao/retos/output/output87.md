





HPUX - Eliminar dispositivos NO\_HW y/o STALE | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Eliminar dispositivos NO\_HW y/o STALE

 

Lun, 12/30/2013 - 11:32 — badorius

Muchas veces quitamos luns y posteriormente añadimos luns al sistema operativo, ya sea por tareas de migración, backup, clone, etc..  

Tener muchos dispositivos en NO\_HW nos puede generar problemas en el servidor de diferentes colores.


El procedimiento para hacer limpieza de dispositivos NO\_HW y de ficheros lo podríamos hacer de la siguiente manera:  

 `echo "Rescaneando... ioscan..."  

ioscan  

echo "Dispositivos no hardware"  

ioscan -fnNk|grep NO_HW|sort -r|wc -l  

echo "Empezamos a eliminar"  

for i in `ioscan -fnNk|grep NO_HW|sort -r|awk '{print $3}'` ; do echo rmsf -H $i && rmsf -H $i ; done`


Después de eliminar los dispositivos NO\_HW, podemos eliminar los ficheros de dispositivo en estado STALE y volver a recrearlos, adicionalmente lanzamos un replace\_wwid para aquellos dispositivos que tenemos un lunpath solapado con uno anterior:  

 `/sbin/rmsf -x ; /sbin/ioscan ; /sbin/insf -e  

for i in `/sbin/dmesg|grep "class : lunpath"|awk '{print $5}'|sort|uniq`  

do  

echo /usr/sbin/scsimgr replace_wwid -C lunpath -I $i  

echo y | /usr/sbin/scsimgr replace_wwid -C lunpath -I $i  

done`





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F87%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




