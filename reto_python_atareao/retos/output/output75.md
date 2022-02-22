





HPUX - Montar FS con CIO en paquetes de ServiceGuard | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Montar FS con CIO en paquetes de ServiceGuard

 

Lun, 03/26/2012 - 09:22 — badorius

Los opciones de montaje a configurar en el fichero .cntl del paquete serían las siguientes:


Lo que es data, redo y archivelog:


 `LV[3]=/dev/vgSAPsn0/lvdata; FS[3]=/oracle/SAP; FS_MOUNT_OPT[3]=" -F vxfs -e -o cio,delaylog,nodatainlog"`


LV[4]=/dev/vgSAPsn0/lvarch; FS[4]=/oracle/SAP/saparch; FS\_MOUNT\_OPT[4]=" -F vxfs -e -o cio,delaylog,nodatainlog"  

  

Resto:


 `LV[0]=/dev/vgSAPsn0/lvusrsap; FS[0]=/usr/sap/SAP; FS_MOUNT_OPT[0]=" -F vxfs -e"`





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F75%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




