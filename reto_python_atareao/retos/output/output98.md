





Linux - Howto recreate/restore PV/VG | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - Howto recreate/restore PV/VG

 

Lun, 07/04/2016 - 09:16 — badorius

Ohhhh.. I have lost the LVM metadata information on all my discs ... I lost all VG information .... vgscan , vgdisplay, pvscan, pvs, doesn't show any VG information! All disks are aviable on server and I can see It with multipath, but when I run pvscan/pvs, there's no LVM information on It.


May still have a hope of retrieving information from the PV / VG.


Run the procedure under their responsibility, the procedure described below could remove the entire contents of your VG.


Go to /etc/lvm/archiver/


cat from last copy from your vg file:


 `cat vgDB01_00010-111064439.vg`


pv0 {  

id = "2RP6OX-w6uo-smtQ-Vp05-avud-2uwE-Db5duT"  

device = "/dev/mapper/LX\_DB01\_DATOS\_1"


pv1 {  

id = "u5f5kk-S2Sf-QhrY-WTCR-Xnzz-he9G-N0M5Nc"  

device = "/dev/mapper/LX\_DB01\_REDOS\_1"


pv2 {  

id = "m9Ji4x-9RWW-rdWV-GBJ0-e62y-9Ipu-pdacLy"  

device = "/dev/mapper/LX\_DB01\_REDOS\_2"


pv3 {  

id = "0iiGPY-zfBT-cV3u-PnQV-e2Z4-Y1hp-dmUtSY"  

device = "/dev/mapper/LX\_DB01\_RESTO"  

}  

]  




Recreate pv metada on disk header:


 `pvcreate --uuid "2RP6OX-w6uo-smtQ-Vp05-avud-2uwE-Db5duT" --restorefile /etc/lvm/archive/vgDB01_00010-111064439.vg /dev/mapper/LX_DB01_DATOS_1`


pvcreate --uuid "u5f5kk-S2Sf-QhrY-WTCR-Xnzz-he9G-N0M5Nc" --restorefile /etc/lvm/archive/vgDB01\_00010-111064439.vg /dev/mapper/LX\_DB01\_REDOS\_1 


pvcreate --uuid "m9Ji4x-9RWW-rdWV-GBJ0-e62y-9Ipu-pdacLy" --restorefile /etc/lvm/archive/vgDB01\_00010-111064439.vg /dev/mapper/LX\_DB01\_REDOS\_2


pvcreate --uuid "0iiGPY-zfBT-cV3u-PnQV-e2Z4-Y1hp-dmUtSY" --restorefile /etc/lvm/archive/vgDB01\_00010-111064439.vg /dev/mapper/LX\_DB01\_RESTO  




Restore vg:  

 `vgcfgrestore vgDB01`





* [Linux](/?q=taxonomy/term/2)
* [LVM](/?q=taxonomy/term/17)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F98%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




