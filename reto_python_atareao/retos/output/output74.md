





Linux - Ups! he eliminado una LUN! | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - Ups! he eliminado una LUN!

 

Jue, 03/08/2012 - 14:06 — badorius

"Las prisas no son buenas"


Hemos creado un VolumeGroup de la siguiente forma:  

 `export LDISK1=/dev/mapper/TEST_DATA01  

export LDISK2=/dev/mapper/TEST_RESTO01  

export LDISK3=/dev/mapper/TEST_REDO01`


export VGNAME=VgTEST01  

export LVSICE1=9G  

export LVSICE2=10G  

export LVSICE3=4000M  

export LVSICE4=1G  

export LVSICE5=23G


export LVNAME1=lvdata  

export LVNAME2=lvdbexec  

export LVNAME3=lvredo  

export LVNAME4=lvdump  

export LVNAME5=lvarch


pvcreate $LDISK1 $LDISK2 $LDISK3  

read a  

vgcreate $VGNAME $LDISK1 $LDISK2 $LDISK3  

read a  

echo "Vgcreados: " ; vgdisplay -v $VGNAME  

read a


lvcreate -L$LVSICE1 -n $LVNAME1 $VGNAME $LDISK1  

lvcreate -L$LVSICE2 -n $LVNAME2 $VGNAME $LDISK2  

lvcreate -L$LVSICE3 -n $LVNAME3 $VGNAME $LDISK3  

lvcreate -L$LVSICE4 -n $LVNAME4 $VGNAME $LDISK2  

lvcreate -L$LVSICE5 -n $LVNAME5 $VGNAME $LDISK2


read a  

echo "LvCreados: " ; lvdisplay  

read a  

mkfs.ext3 /dev/$VGNAME/$LVNAME1  

mkfs.ext3 /dev/$VGNAME/$LVNAME2  

mkfs.ext3 /dev/$VGNAME/$LVNAME3  

mkfs.ext3 /dev/$VGNAME/$LVNAME4  

mkfs.ext3 /dev/$VGNAME/$LVNAME5  

read a



Ver que a cada logicalvolume asignamos una lun en concreto.


Cuando queremos eliminar una lun que tiene accesible un linux y pertenece a un VolumeGroup y a la vez funcionando con multipath, el orden correcto sería:


Eliminar el logicalvolume al que pertenece la lun.  

Eliminar el dispositivo multipath.  

Eliminar los dispositivos físicos.


Si por aquellas cosas, lo primero que hacemos es eliminar la lun de la cabina, nos encontraremos con el siguiente problema al hacer un vgdisplay:  

 `LinuxServer01:/ # vgdisplay  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-17: read failed after 0 of 4096 at 10737352704: Error d'Entrada/Sortida  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 9663610880: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 Couldn't find device with uuid '3jKDPg-JjWf-ohqS-cZHp-gsnS-A4Zd-ZdcKV3'.  

 Couldn't find all physical volumes for volume group VgGDSTEST01.  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 Couldn't find device with uuid '3jKDPg-JjWf-ohqS-cZHp-gsnS-A4Zd-ZdcKV3'.  

 Couldn't find all physical volumes for volume group VgGDSTEST01.  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 Couldn't find device with uuid '3jKDPg-JjWf-ohqS-cZHp-gsnS-A4Zd-ZdcKV3'.  

 Couldn't find all physical volumes for volume group VgGDSTEST01.  

 /dev/dm-17: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 /dev/dm-19: read failed after 0 of 4096 at 0: Error d'Entrada/Sortida  

 Couldn't find device with uuid '3jKDPg-JjWf-ohqS-cZHp-gsnS-A4Zd-ZdcKV3'.  

 Couldn't find all physical volumes for volume group VgGDSTEST01.  

 Volume group "VgTest01" not found`


Miedo, sudor frio! vgdisplay no nos muestra nuestro vg! pero no pasa nada.


Importante: Dicho Volume Group contiene mas luns, solo le hemos quitado una lun que pertenecía a LogicalVolume que queríamos eliminar. Si hemos quitado una lun del VolumGroup que no sabemos a lvol pertenecía el procedimiento ya no aplica.


Por la parte del VolumGroup lo solucionamos haciendo lo siguiente:  

 `vgreduce --removemissing VgTEST01`


Esto no en ningún caso nos recuperará datos perdidos en el VG de la lun que hemos eliminado.


El siguiente paso sería el multipah, si hacemos un multipath -ll vemos el dispositivo en failed:  

 `multipath -ll` 


TEST\_DATA01 (36006016036302700fa924d9ecd3ae111) dm-17 DGC,RAID 5  

[size=10G][features=0][hwhandler=1 emc]  

\\_ round-robin 0 [prio=0][enabled]  

 \\_ 2:0:0:7 sdw 65:96 [failed][faulty]  

 \\_ 3:0:0:7 sdac 65:192 [failed][faulty]  

\\_ round-robin 0 [prio=0][enabled]  

 \\_ 2:0:1:7 sdz 65:144 [failed][faulty]  

 \\_ 3:0:1:7 sdaf 65:240 [failed][faulty]  




 `Procedmos a eliminarlo:  

multipath -f TEST_DATA01`


Ahora eliminaremos los dispositivos físicos:  

 `echo 1 > /sys/block/sdw/device/delete  

echo 1 > /sys/block/sdac/device/delete  

echo 1 > /sys/block/sdz/device/delete  

echo 1 > /sys/block/sdaf/device/delete`


Con esto dejamos el sistema limpio.





* [Linux](/?q=taxonomy/term/2)
* [SAN](/?q=taxonomy/term/3)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F74%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




