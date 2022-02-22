





Linux Multipath | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux Multipath

 

Mié, 12/23/2009 - 16:56 — badorius

Multipath, vendría a ser un sustituto de powerpath de EMC, pero nativo del operativo.


Para disponer de multipath el operativo debe tener instalado el siguiente paquete:


`[root@ linserver ~]# rpm -qa|grep -i multi  

device-mapper-multipath-0.4.7-30.el5`


Antes de arrancar el demonio de multipath, es necesario editar el fichero de configuración /etc/multipath.conf y comentar las líneas:


 `#blacklist {  

# devnode "*"  

#}`


Normalmente estas líneas vienen descomentadas por defecto, con lo que nos pone en la blacklist todos los dispositivos y el multipath no funcionaría con las nuevas luns.


Aconsejo echarle un ojo a este fichero. En mi caso ha quedado de la siguiente forma:


 `[root@linserver ~]# grep -v ^# /etc/multipath.conf  

defaults {  

 user_friendly_names yes  

}  

blacklist {  

devnode "^(ram|raw|loop|fd|md|dm-|sr|scd|st)[0-9]*"  

devnode "^hd[a-z]"  

devnode "^cciss!c[0-9]d[0-9]*"`


Podemos ver como deja los discos locales (hd[a-z]) en la blacklist del multipath.


Una vez configurado multipath, ya podemos arrancar el servicio:


 `/etc/init.d/multipathd start`


Para añadirlo al arranque del sistema:


 `# chkconfig multipathd on`


Una vez esto, ya podemos verificar que el servidor tiene el multipath activo. Si el servidor ya tiene alguna lun asignada, podremos ver el estado de los paths con:


 `[root@linserver ~]# multipath -ll  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]  

mpath3 (3600601603d6f1b005445da12b3efde11) dm-3 DGC,RAID 5  

[size=4.0G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][enabled]  

 \_ 2:0:1:0 sda 8:0 [active][ready]  

 \_ 3:0:0:0 sdf 8:80 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:0:0 sdc 8:32 [active][ready]  

 \_ 3:0:1:0 sdd 8:48 [active][ready]`


Para adaptar multipahing para lvm, es necesario editar el fichero /etc/lvm/lvm.conf y modificar la línea filter con algo parecido a lo siguiente:


 `filter = [ "r|/dev/cdrom|","r|/dev/sd.*|" ]`


En este ejemplo podemos ver 2 luns con multipath (mpath2 y mpat3) con el estado de cada camino.


Una vez multipath funcionando correctamente, ya podemos crear el vg y/o filesystem. Un pequeño ejemplo de cómo montar un vg con su volumen lógico y filesystem:


 `export LDISK=/dev/mapper/mpath2  

export VGNAME=VgDatosTest00  

export LVSICE=500M  

export LVNAME=LogVoldDatodsTest00  

pvcreate $LDISK  

vgcreate $VGNAME $LDISK  

echo "Vgcreados: " ; vgdisplay  

lvcreate –L$LVSICE -n $LVNAME $VGNAME  

echo "LvCreados: " ; lvdisplay  

mkfs.ext3 /dev/$VGNAME/$LVNAME`


Las variables, se podrían modificar para adaptarlo a las necesidades. Para ampliar un lvol y su filesystem:


 `lvextend -L 900M /dev/$VGNAME/$LVNAME  

resize2fs /dev/$VGNAME/$LVNAME 900M`


Para encogerlo (quizás es necesario desmontar el volumen):


 `resize2fs /dev/$VGNAME/$LVNAME 600M  

lvreduce -L 600M /dev/$VGNAME/$LVNAME`


Para eliminar una lun del servidor, después de quitarle la lun y exportar el vg, multipath continua viendo las luns como failed (Ejemplo lun con 4GB):


 `[root@linserver ~]# multipath -ll  

sdg: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdi: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdj: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdl: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]  

mpath3 (3600601603d6f1b005445da12b3efde11) dm-3 DGC,RAID 5  

[size=4.0G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=0][active]  

 \_ 2:0:1:2 sdf 8:80 [failed][faulty]  

 \_ 3:0:0:2 sdi 8:128 [failed][faulty]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:0:2 sdc 8:32 [failed][faulty]  

 \_ 3:0:1:2 sdl 8:176 [failed][faulty]`


Eliminamos la lun del multipath con multipath -f (nombre del multipath)


 `[root@linserver ~]# multipath -f mpath3`


El multipath ha desaparecido pero los paths no (sdg, sdi, sdj, sdl):


 `[root@linserver ~]# multipath -ll  

sdg: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdi: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdj: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

sdl: checker msg is "emc_clariion_checker: Logical Unit is unbound or LUNZ"  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]`


Para eliminar los paths, en este ejemplo sdg, sdi, sdj, sdl:


 `[root@linserver ~]# echo 1 > /sys/block/sdg/device/delete  

[root@linserver ~]# echo 1 > /sys/block/sdi/device/delete  

[root@linserver ~]# echo 1 > /sys/block/sdj/device/delete  

[root@linserver ~]# echo 1 > /sys/block/sdl/device/delete`


Una vez elimnados, ya no mostrará mas el error del multipath y los caminos han desaparecido:


 `[root@linserver emulex]# multipath -ll  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]`


Presentar una lun nueva al servidor. Despues de dar acceso a una nueva lun, es necesario forzar el redescubrimiento de dicha lun (lo que en hpux sería un ioscan):


 `[root@linserver emulex]# echo 1 > /sys/class/fc_host/host2/issue_lip`


Donde hostn es una de las tarjetas de fibras de nuestro servidor, en este caso tenemos dos. Ahora multipath tendrá acceso a dos de los cuatro caminos del mpath3:


 `[root@linserver emulex]# multipath -ll  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]  

mpath3 (3600601603d6f1b005445da12b3efde11) dm-3 DGC,RAID 5  

[size=4.0G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=1][active]  

 \_ 2:0:1:0 sda 8:0 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:0:0 sdc 8:32 [active][ready]`


Reliazamos la misma operacion en la otra tarjeta de fibra y ya disponemos de los 4 caminos:


 `[root@linserver emulex]# echo 1 > /sys/class/fc_host/host3/issue_lip  

[root@linserver emulex]# multipath -ll  

mpath2 (3600601603d6f1b003ecf7decb2efde11) dm-2 DGC,RAID 5  

[size=30G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][active]  

 \_ 2:0:0:1 sdb 8:16 [active][ready]  

 \_ 3:0:1:1 sdk 8:160 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:1:1 sde 8:64 [active][ready]  

 \_ 3:0:0:1 sdh 8:112 [active][ready]  

mpath3 (3600601603d6f1b005445da12b3efde11) dm-3 DGC,RAID 5  

[size=4.0G][features=1 queue_if_no_path][hwhandler=1 emc][rw]  

\_ round-robin 0 [prio=2][enabled]  

 \_ 2:0:1:0 sda 8:0 [active][ready]  

 \_ 3:0:0:0 sdf 8:80 [active][ready]  

\_ round-robin 0 [prio=0][enabled]  

 \_ 2:0:0:0 sdc 8:32 [active][ready]  

 \_ 3:0:1:0 sdd 8:48 [active][ready]`


Con esto finalizo mis aventuras con multipath hasta día de hoy.





* [Linux](/?q=taxonomy/term/2)
* [Multipath](/?q=taxonomy/term/4)
* [SAN](/?q=taxonomy/term/3)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




