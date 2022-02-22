





HPUX - Recuperar permisos de un chmod -R chown -R | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - Recuperar permisos de un chmod -R chown -R

 

Lun, 09/22/2014 - 09:36 — badorius

Este artículo explica como recuperar los permisos del sistema operativo HPUX con ignite tras ejecutar por accidente un chmod -R o un chown -R donde no toca, ejemplo chmod -R 400 /usr


Lo primero que hay que hacer es acojonarse y después ponerse manos a la obra.  

Básicamente lo que haremos será extraer los permisos del ignite para montarnos un script que los reconstruya, con lo que es totalmente imprescindible tener una imagen de Ignite válida en el sistema operativo.


Vamos al directorio donde tenemos la imagen del servidor a recuperar los permisos:  

 `cd /var/opt/ignite/recovery/archives/`


Seleccionamos la imagen de la que queremos restaurar los permisos:  

 `root@hpux01:/var/opt/ignite/recovery/archives/hpux02# ls -rlt  

total 19383714  

-rw------- 1 bin sys 4960805884 Sep 14 00:26 2014-09-14,00:01  

-rw------- 1 bin sys 4963572883 Sep 21 00:27 2014-09-21,00:01  

root@hpux01:/var/opt/ignite/recovery/archives/hpux02 #`


Extraemos la información de los permisos de la imagen:  

 `gzcat "00:27 2014-09-21,00:01" | pax -v > /tmp/permissions.out`


Revisamos el contenido del fichero:  

 `root@hpux01:/ # head /tmp/permissions.out  

dr-xr-xr-x 0 bin bin Aug 9 13:57 stand/  

drwxr-xr-x 0 root root Jun 11 2013 stand/lost+found/  

-rw-r--r-- 0 root sys 25852 Aug 28 14:20 stand/ioconfig  

-rw-r--r-- 0 root sys 132808 Aug 28 14:20 stand/ext_ioconfig.lkg  

-rw-r--r-- 0 root sys 133384 Aug 28 14:20 stand/ext_ioconfig  

-rw-r--r-- 0 root sys 22 Oct 3 2013 stand/bootconf  

lrwxr-xr-x 0 root root Aug 5 16:03 stand/system -> nextboot/system  

-rw-r--r-- 0 root sys 0 Jun 11 2013 stand/.kc.lock  

dr-xr-xr-x 0 bin bin Jun 11 2013 stand/boot.sys/  

dr-xr-xr-x 0 bin bin Aug 5 16:03 stand/boot.sys/stand/  

root@hpux01:/ #`


Ahora hay que traducir los permisos a valor octal para luego poder crear el script final. Para ello ejecutaremos lo siguiente en la shell tal cual está, esto nos generará el fichero /tmp/octalperm.sed con todo los parámetros de parseo necesarios para el sed.  

 `cat >> /tmp/octalperm.sed << EOF  

# Translate directory octal permission lists  

# Based on the work of David Cornish ([www.davidcornish.com](http://www.davidcornish.com "www.davidcornish.com"))  

#  

# File types (b)lock, (c)haracter, (d)irectory, (link), (p)ipe  

s/^\([-bcdlp]\)/\1 /`


# First value - normal (0), sticky (1), sgid (2), suid (4)  

s/\(^. \)/\10/  

s/\(^.\) .\(........\)t/\1 1\2x/  

s/\(^.\) 0\(..\)s/\1 4\2x/  

s/\(^.\) 1\(..\)s/\1 5\2x/  

s/\(^.\) 0\(.....\)s/\1 2\2x/  

s/\(^.\) 1\(.....\)s/\1 3\2x/  

s/\(^.\) 4\(.....\)s/\1 6\2x/  

s/\(^.\) 5\(.....\)s/\1 7\2x/


# Read (4)/write (2)/execute (1) permissions  

s/rwx/7/g  

s/rw-/6/g  

s/r-x/5/g  

s/r--/4/g  

s/-wx/3/g  

s/-w-/2/g  

s/--x/1/g  

s/---/0/g  

EOF  




Tras esto ya podemos ejecutar el sed que nos generará el fichero /tmp/permissions.octal:  

 `root@hpux01:/ # sed -f /tmp/octalperm.sed /tmp/permissions.out > /tmp/permissions.octal`


Verificamos el fichero:  

 `root@hpux01:/ # head /tmp/permissions.octal  

d 0555 0 bin bin Aug 9 13:57 stand/  

d 0755 0 root root Jun 11 2013 stand/lost+found/  

- 0644 0 root sys 25852 Aug 28 14:20 stand/ioconfig  

- 0644 0 root sys 132808 Aug 28 14:20 stand/ext_ioconfig.lkg  

- 0644 0 root sys 133384 Aug 28 14:20 stand/ext_ioconfig  

- 0644 0 root sys 22 Oct 3 2013 stand/bootconf  

l 0755 0 root root Aug 5 16:03 stand/system -> nextboot/system  

- 0644 0 root sys 0 Jun 11 2013 stand/.kc.lock  

d 0555 0 bin bin Jun 11 2013 stand/boot.sys/  

d 0555 0 bin bin Aug 5 16:03 stand/boot.sys/stand/`


Ahora generamos el job que nos construirá el script final, ejecutamos lo siguiente en la shell tal y como está y nos creará el fichero /var/tmp/setpermissions.sh:  

 `cat /tmp/permissions.octal | awk '{  

if($1 == "d") filename=$9  

if($1 == "l") filename=$9  

if($1 == "p") filename=$9  

if($1 == "c") filename=$11  

if($1 == "b") filename=$11  

if($1 == "-") filename=$10  

printf "chown %s:%s %s\nchmod %s %s\n", $4, $5, filename, $2, filename  

}' > /var/tmp/setpermissions.sh`


Verificamos el fichero:  

 `root@hpux01:/ # head /var/tmp/setpermissions.sh`


chown bin:bin stand/  

chmod 0555 stand/  

chown root:root stand/lost+found/  

chmod 0755 stand/lost+found/  

chown root:sys stand/ioconfig  

chmod 0644 stand/ioconfig  

chown root:sys stand/ext\_ioconfig.lkg  

chmod 0644 stand/ext\_ioconfig.lkg  

chown root:sys stand/ext\_ioconfig  

chmod 0644 stand/ext\_ioconfig  




Ya podemos copiar el fichero /var/tmp/setpermissions.sh a la máquina en la que queremos recuperar los permisos y ejectuar el script.  

 `root@hpux02:/ # sh /var/tmp/setpermissions.sh`


Quizás se necesite realizar un swverify para verificar los permisos de los ficheros, esta información se puede consultar con un:  

 `# swlist -l file -a mode -a owner -a group`


Referencias:  

[http://h10025.www1.hp.com/ewfrf/wc/document?cc=es&lc=es&dlc=es&docname=c...](http://h10025.www1.hp.com/ewfrf/wc/document?cc=es&lc=es&dlc=es&docname=c01905572 "http://h10025.www1.hp.com/ewfrf/wc/document?cc=es&lc=es&dlc=es&docname=c01905572")  

[http://wiki-ux.info/wiki/How\_to\_recover\_file\_owner\_and\_permissions\_using...](http://wiki-ux.info/wiki/How_to_recover_file_owner_and_permissions_using_a_recovery_archive "http://wiki-ux.info/wiki/How_to_recover_file_owner_and_permissions_using_a_recovery_archive")  

[https://www.google.es/?gws\_rd=ssl#q=mierda+de+chmod+-R](https://www.google.es/?gws_rd=ssl#q=mierda+de+chmod+-R "https://www.google.es/?gws_rd=ssl#q=mierda+de+chmod+-R")





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F92%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




