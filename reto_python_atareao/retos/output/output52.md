





HPUX - lvextend: "LogicalExtentsNumber" is not bigger than current setting. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - lvextend: "LogicalExtentsNumber" is not bigger than current setting.

 

Lun, 12/20/2010 - 11:41 — badorius

Hoy nos hemos encontrado con un error al realizar una tarea rutinaria de amplicación de vg / lvol / filesystem.


Después de realizar un pvcreate, añadir un disco y sus alternates al vg vgSAP, nos encontramos con el siguiente error al hacer el lvextend:


`hpuxServer01:/root # lvextend -L 1149200 /dev/vgSAP/lvdata /dev/dsk/c13t14d7  

lvextend: "LogicalExtentsNumber" is bigger than the maximum value allowed.`


A primera instancia, no encontré donde estaba la limitación ni a nivel de vg ni de lvols:


root@hpuxServer01:/root # vgdisplay /dev/vgSAP  

--- Volume groups ---  

VG Name /dev/vgSAP  

VG Write Access read/write  

VG Status available, exclusive  

Max LV 255  

Cur LV 10  

Open LV 10  

Max PV 32  

Cur PV 8  

Act PV 8  

Max PE per PV 48000  

VGDA 16  

PE Size (Mbytes) 16  

Total PE 83192  

Alloc PE 68671  

Free PE 14521  

Total PVG 0  

Total Spare PVs 0  

Total Spare PVs in use 0  

VG Version 1.0  

VG Max Size 24000g  

VG Max Extents 1536000  




Buscando por los foros de ITRC, encontramos que comentan lo siguiente:


`There is a limit of 65535 LE's. With your 4MB LE's, that is about 260000 and you're asking for 275000. You could use the -l option and specify 65535.`


Existe una limitación de 65535 LE's con lo que la limitación del VG está en el tamaño de PE. En nuestro caso si el tamaño del PE es de 16Mb: 65535 * 16 = 1048560 Mb. Nuestra limitación en este VG es de 1048560 Mb, si el PE fuera de 32, tendríamos el doble (2097120Mb).


Tengo pendiente un próximo articulo con el detalle de una ampliación de VG / lvol / filesystem.


Referencias:


[http://forums13.itrc.hp.com/service/forums/questionanswer.do?admit=10944...](http://forums13.itrc.hp.com/service/forums/questionanswer.do?admit=109447627+1292837221320+28353475&threadId=981210 "http://forums13.itrc.hp.com/service/forums/questionanswer.do?admit=109447627+1292837221320+28353475&threadId=981210")  

[http://asgaur.com/asgaur.php/2010/04/20/logicalextentsnumber-is-bigger-t...](http://asgaur.com/asgaur.php/2010/04/20/logicalextentsnumber-is-bigger-than-the-maximum-value-allowed-in-hp-ux "http://asgaur.com/asgaur.php/2010/04/20/logicalextentsnumber-is-bigger-than-the-maximum-value-allowed-in-hp-ux")





* [HPUX](/?q=taxonomy/term/6)
* [Linux](/?q=taxonomy/term/2)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F52%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




