





Export - Import repositorio SVN | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Export - Import repositorio SVN

 

Lun, 03/29/2010 - 15:01 — badorius

Tras la necesidad de cambiar de servidor de SVN, de una manera "transparente" para los usuarios, he tenido que exportar todo un repositorio con su info e importarlo en otro.


La forma fué la siguiente:


En el servidor SVN donde tenía que hacer el export, lancé el siguiente comando:


 `svnadmin dump /usr/local/svn/repositories/mirepositorio> /tmp/dump_svn_mirepositorio`


Copiamos el fichero "/tmp/dump\_svn\_mirepositorio" al otro servidor y lo importamos. En el servidor donde realizaremos el import:


 `svnadmin --force-uuid load /usr/local/svn/repositories/mirepositorio< /tmp/dump_svn_mirepositorio`


De esta forma ya tenemos todo el repo "clonado" en el nuevo servidor.


De manera adicional, se puede añadir al crontab algo paraceido a esto:


 `#BACKUP SVN mirepositorio REPO  

15 01 * * * /usr/local/svn/repositories/backups/backup_SVN.sh`


El script contendrá algo parecido a:


 `#!/bin/bash`


svnadmin dump /usr/local/svn/repositories/mirepositorio > /usr/local/svn/repositories/backups/dmp\_svn\_mirepositorio\_`date +%d`.dump  

gzip -f /usr/local/svn/repositories/backups/dmp\_svn\_mirepositorio\_`date +%d`.dump  




De esta forma guardaremos backups diarios con una ventana de un mes.





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F18%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




