





HPUX - Convert VG from Legacy to Agile/persistent DSF | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Convert VG from Legacy to Agile/persistent DSF

 

Jue, 09/01/2016 - 13:22 — badorius

Create lvmtab backup file:


 `cp -p /etc/lvmtab /etc/lvmtab.`date +%y%m%d_%s``


Convert vg from legacy to Agile:


 `vgdsf -c /dev/`


Check VG and lvmtab file:


 `vgdisplay -v /dev/  

strings /etc/lvmtab`





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F99%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




