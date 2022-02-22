





AIX - Me falta una lun - Dispositivos LUNZ | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - Me falta una lun - Dispositivos LUNZ

 

Jue, 11/18/2010 - 17:14 — badorius

Presentamos 8 luns a un nuevo servidor AIX y solo ve 7, la primera lun no la ve por mucho que la eliminemos y la volvamos a crear, ya que al crear la zona el servidor AIX ha creado una LUNZ, la cual bloquea la creación del hdisk HLU 0.


Primero hemos verificado que teníamos LUNZ:


`lsdev -Cc disk | grep LUNZ`


Una vez identificadas las lunsZ, las eliminamos:


`rmdev -dl hdiskN`


Donde N será cada LUNZ.


Ahora el sistema ya podrá crear el hpdisk powerhdisk con el hlu 0:


`cfgmgr`


Con esto la lun con el hlu 0 ya no quedará solapada con la LUNZ.





* [AIX](/?q=taxonomy/term/8)
* [SAN](/?q=taxonomy/term/3)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F48%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




