





HPUX - Cambiar el número de PVs que acepta un VG en caliente. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Cambiar el número de PVs que acepta un VG en caliente.

 

Mié, 05/13/2015 - 11:08 — badorius

Para cambiar el número de PVs que acepta un VG


1. Chequear a tabla de combinaciones de PV y max PE per PV que se pueden aplicar al VG. Esto lo conseguimos con el comando:


 `# vgmodify –v –t [VG_NAME]`


 Obtendrás una salida similar a:


 `Volume Group configuration for /dev/vgAPP_01 has been saved in /etc/lvmconf/vgAPP_01.conf`


 Current Volume Group settings:  

 Max LV 255  

 Max PV 16  

 Max PE per PV 1016  

 PE Size (Mbytes) 4  

 VGRA Size (Kbytes) 176


 VGRA space (Kbytes) on Physical Volumes with extents in use:  

 PV current -n  

 /dev/rdisk/disk830 896 4096  

 /dev/rdisk/disk831 896 4096  

 /dev/rdisk/disk832 896 4096  

 Summary 896 4096


 Volume Group optimized settings (no PEs renumbered):  

 max\_pv(-p) max\_pe(-e) Disk size (Mb)  

 3 35836 143345  

 4 26876 107505  

 5 21500 86001  

 ...  

 24 4348 17393  

 26 4092 16369  

 28 3836 15345 


2. Una vez escogida la nueva configuración, por ejemplo 19 PVcon un max PE per PV de 5628. Ejecutar el comando vgmodify en modo REVIEW para chequear que se puede realizar el cambio.  

 `# vgmodify -r -a -p 19 -e 5628 [VG_NAME]`


3. Si en el paso anterior no muestra ningún error, podemos modificar el VG con el comando anterior pero obviando el modo REVIEW:  

 `# vgmodify -a -p 19 -e 5628 [VG_NAME]`





* [HPUX](/?q=taxonomy/term/6)
* [LVM](/?q=taxonomy/term/17)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F93%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




