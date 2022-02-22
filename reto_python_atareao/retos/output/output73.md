





AIX - LINUX : Linux NFS server - Aix NFS Client (vmount: Operation not permitted.) | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - LINUX : Linux NFS server - Aix NFS Client (vmount: Operation not permitted.)

 

Lun, 11/28/2011 - 13:00 — badorius

Por necesidades hoy he tenido que exportar un filesystem por NFS con un linux (SLES) y montar este en un AIX y me he econtrado con el error: (vmount: Operation not permitted.)


Primero edito el fichero exports del linux para indicar el filesystem a exportar y sus parámetros:  

`vi /etc/exports`


En este caso solo pongo una entrada:  

`/filesystem aix.server.com(rw,nohide,no_root_squash,sync)`


Con esto ya puedo reiniciar o arrancar el NFS en linux:


`/etc/init.d/nfsserver restart`


Seguidamente, en el servidor AIX intento montar el filesystem con el comando mount y me da el error vmount: Operation not permitted.  

`root@aix.server.com:/> mount linux.server.com:/filesystem /filesystem  

mount: 1831-008 giving up on:  

linux.server.com:/filesystem  

vmount: Operation not permitted.`


`root@aix.server.com:/> nfso -o nfs_use_reserved_ports=1  

Setting nfs_use_reserved_ports to 1  

root@aix.server.com:/> mount linux.server.com:/filesystem /filesystem`


Linux por defecto para la comunicación NFS utiliza puertos por debajo de 1024 y AIX por defecto utiliza puertos por encima de 1024.





* [AIX](/?q=taxonomy/term/8)
* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F73%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




