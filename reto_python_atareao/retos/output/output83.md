





Linux - Eliminar scsi device | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - Eliminar scsi device

 

Mar, 09/10/2013 - 07:57 — badorius

Para eliminar un scsi device directamente, primero buscamos el scsi device a eliminar. Tenemos dos posibles maneras para buscarlo:


Si tenemos lsscsi instalado, tomaríamos como referencia la referencia scsi que muestra al principio ejemplo 1:0:0:0:  

 `[root@servidor01 ~]# lsscsi  

[1:0:0:0] disk DGC LUNZ 0430 /dev/sda  

[1:0:1:0] disk DGC LUNZ 0430 /dev/sdb  

[1:0:2:0] disk DGC LUNZ 0430 /dev/sdc  

[1:0:3:0] disk DGC LUNZ 0430 /dev/sdd  

[1:0:4:0] disk DGC VRAID 0532 /dev/sddb  

[1:0:4:1] disk DGC VRAID 0532 /dev/sddc  

[1:0:4:2] disk DGC VRAID 0532 /dev/sdde  

[1:0:4:3] disk DGC VRAID 0532 /dev/sddf  

...`


O directamente con el fichero /proc/scsi/scs, tomaríamos como referencia el scsi, el channel el id y la lun, ejemplo 1:00:04:00:  

 `[root@gdsdevapp01 ~]# cat /proc/scsi/scsi  

Host: scsi1 Channel: 00 Id: 00 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi1 Channel: 00 Id: 01 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi1 Channel: 00 Id: 02 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi1 Channel: 00 Id: 03 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi2 Channel: 00 Id: 00 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi2 Channel: 00 Id: 01 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi2 Channel: 00 Id: 02 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04  

Host: scsi2 Channel: 00 Id: 03 Lun: 00  

 Vendor: DGC Model: LUNZ Rev: 0430  

 Type: Direct-Access ANSI SCSI revision: 04`


Una vez tenemos la referencia del device a eliminar (siempre hay que tener presente las capas superiores, como multipath, lvm, etc...) eliminaríamos el device con el siguiente comando:


 `echo 1 > /sys/class/scsi_device/1:0:4:0/device/delete`





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F83%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




