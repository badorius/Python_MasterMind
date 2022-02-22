





HPUX NFS - AUTOMOUNTER | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX NFS - AUTOMOUNTER

 

Jue, 04/15/2010 - 11:14 — badorius

Los clientes de NFS en hpux funcionan con el demonio automountd.


Para reiniciarlo:  

 `/sbin/init.d/autofs stop  

/sbin/init.d/autofs start`


Verificamos si está el demonio en marcha:


 `root@hpuxserver:/ # ps -eaf|grep -i automount  

 root 2126 1 0 Jan 13 ? 8:00 /usr/sbin/automountd  

 root 4019 102 0 12:06:16 pts/5 0:00 grep -i automount  

root@hpuxserver:/ #`


La configuración de lo que tiene que mantener montado por nfs está en los ficheros auto\_master y auto.direct:  

 `root@hpuxserver:/ # ls -lrt /etc/auto*  

-rw-r--r-- 1 root root 54 Jul 11 2006 /etc/auto_master  

-rw-r--r-- 1 root sys 221 Jul 28 2006 /etc/auto.direct  

-rw-r--r-- 1 root root 149 May 17 2009 /etc/auto_parms.log.old  

-rw-r--r-- 1 root root 149 Jan 13 09:38 /etc/auto_parms.log`


El contenido del auto.direct viene a ser algo parecido a:  

 `root@hpuxserver:/ # more /etc/auto.direct  

/nfs "-o vers=3,proto=udp" hpuxNFSserver:/export/nfsfilesystem  

/usr/sap/trans "-o vers=3,proto=udp" sapserver:/export/usr/sap/trans`


El auto\_master solo contiene un par de parametros, uno de ellos es el fichero auto.direct.


Si no queremos reiniciar el demonio automountd, podemos ejectuar el comando automount:


 `root@hpuxserver:/ # automount`


Si hemos desmontado manualmente un filesystem nfs desde un cliente, para montarlo a mano y no reiniciar el automound, sería tan sencillo como:  

 `mount /nfs hpuxNFSserver:/export/nfsfilesystem`





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F21%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




