





HPUX Reiniciar VPAR con Dump | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX Reiniciar VPAR con Dump

 

Mié, 01/13/2010 - 12:52 — badorius

En el caso de tener una vpar de HPUX inaccesible ya sea por ssh o consola, una manera de reiniciar la vpar creando un dump para poder analizar a posteriori, sería:


 `#vparreset –p $NOMBRE_DE_LA_VPAR –t`


Esto lo lanzaríamos desde otra vpar que forme parte de la misma npar.


La vpar tardará en reiniciar porque generará en el momento de la parada un DUMP en /var/adm/crash (A tener en cuenta espacio en /var).


Dicho dump tendrá que ser analizado con la herramienta crashinfo.bin de hp, lanzándola de la siguiente manera:


 `#./crashinfo –v /var/adm/crash/crash.4 > /tmp/ci.out`


Si se detectara un PID en el análisis que ha podido causar el problema, para extraer un proctree de los PIDs:


 `#./crashinfo -full_comm –proctree /var/adm/crash/crash.4 > /tmp/ci_proctree.out`





* [HPUX](/?q=taxonomy/term/6)
* [Unix](/?q=taxonomy/term/1)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




