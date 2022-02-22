





Shell script - Cómo añadir algo al final de una línea determinada del texto. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Shell script - Cómo añadir algo al final de una línea determinada del texto.

 

Mié, 04/04/2012 - 15:23 — badorius

Si queremos añadir algo al final de una determinada línea (la que tiene un cierto carácter determinado). Por ejemplo:  

 `cat file.txt  

CONVERT DATAFILE '/databasegmtmp/data_large107.dbf'  

FROM PLATFORM 'AIX-Based Systems (64-bit)'  

FORMAT '/oradata/databasegm/data_large107.dbf'`


CONVERT DATAFILE '/databasegmtmp/data\_large106.dbf'  

FROM PLATFORM 'AIX-Based Systems (64-bit)'  

FORMAT '/oradata/databasegm/data\_large106.dbf'


CONVERT DATAFILE '/databasegmtmp/audit\_small101.dbf'  

FROM PLATFORM 'AIX-Based Systems (64-bit)'  

FORMAT '/oradata/databasegm/tt\_small101.dbf'


CONVERT DATAFILE '/databasegmtmp/sgp\_data01.dbf'  

FROM PLATFORM 'AIX-Based Systems (64-bit)'  

FORMAT '/oradata/databasegm/xxx\_data01.dbf'  




Queremos añadir un punto y coma ";" al final de la línea FORMAT ...... dbf'  

Tenemos dos formas de hacerlo, awk y sed. AWK:  

 `cat file.txt| awk '/^FORMAT/{$0=$0";"}{print}'`


Con sed:  

 `cat file.txt| sed '/^FORMAT/s/$/;/'`


Para entender un poco el funcionamiento del awk:


Si la línea coincide con la expresión regular ^FORMAT (significa que cualquier línea que empiece con"FORMAT"), está se cambiará por $0 y a la vez añade la cadena deseada, en nuestro caso ";" ($0 es toda la línea que machea con el ^FORMAT). Sería igual que cuando hacemos export PATH=$PATH:/opt/bin/tool.sh


Si la línea coincide con la condición (todas las líneas coincidirán), realizará el print.





* [Shell](/?q=taxonomy/term/12)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F76%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




