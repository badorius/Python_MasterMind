





ORACLE - Crear DBLINK | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## ORACLE - Crear DBLINK

 

Mar, 09/21/2010 - 10:34 — badorius

Un DBLINK nos permite acceder desde una base de datos Oracle a objetos de otra base de datos Oracle.


Para crear el DBLINK, con un usuario con permisos:


 `Create database link NOMBRE_LINK connect to USUARIO identified by CONTRASEÑA USING 'BASEDATOS_DESTINO';`


Consulta ejemplo utilizando DBLINK:


 `select * from TABLA@NOMBRE_LINK`


Para consultar los DBLINKS:


 `select * from dba_db_links;`





* [Oracle](/?q=taxonomy/term/7)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F43%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




