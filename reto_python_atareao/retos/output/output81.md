





AIX - CHULETA LVM | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - CHULETA LVM

 

Lun, 08/26/2013 - 09:25 — badorius

* Mirror VG  

Primero extendvg para agregar los discos de mirror  

mirrorvg # solo si tengo un disco de mirror (independientemente de la cantidad de discos origen)  

Para romper el mirror  

unmirrorvg 


* Montar VG  

varyonvg 


* Desmontar VG  

varyoffvg # previamente desmontar los LV.


* Crear LV  

mklv [-y ] ...  

 tamaño indicado en M|G|Logical Partitions


* Crear LV y FS en un solo paso  

crfs -v jfs2 -g -a size= -A yes -p rw -m 


* Crear FS sobre LV existente  

crfs -v jfs2 -d -A yes -p rw -m 


* Borrar LV  

rmlv # No elimina entrada en /etc/filesystems


* Borrar LV y FS en un solo paso  

rmfs -i # Elimina entrada en /etc/filesystems y LV


* Agregar Discos LV  

extendlv [M|G] 


* Cambios en el FS  

chfs -a size=[+|-][M|G] 


* Mirror LV  

Primero extendvg para agregar los discos de mirror  

mklvcopy 2 ... # el original siempre es m=1.  

rmlvcopy 1 ... 


Mas datos:  

[http://pic.dhe.ibm.com/infocenter/aix/v6r1/index.jsp?topic=%2Fcom.ibm.ai...](http://pic.dhe.ibm.com/infocenter/aix/v6r1/index.jsp?topic=%2Fcom.ibm.aix.cmds%2Fdoc%2Faixcmds3%2Fmkvg.htm "http://pic.dhe.ibm.com/infocenter/aix/v6r1/index.jsp?topic=%2Fcom.ibm.aix.cmds%2Fdoc%2Faixcmds3%2Fmkvg.htm")


La version se puede cambiar en v6r1 / v7r1 / v5r3





* [AIX](/?q=taxonomy/term/8)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F81%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




