





Oracle - Lanzar AWR | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Oracle - Lanzar AWR

 

Mar, 04/19/2011 - 09:54 — badorius

AWR (Automatic Workload Repository) es una herramienta desarrollada por Oracle he incluida en Oracle 10g que nos permite extraer informes del estado de nuestra base de datos para poder relizar tareas de Tuning, esta herramienta es una evolución de Oracle StatsPack que estaba incluida en Oracle 9i.


Por defecto Oracle AWR realiza la recolección de datos cada hora con una retención de 7 días, si desaamos variar esta configuración podemos cambiarla usando:


Cada 10 minutos (el mínimo):


`begin DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(11520,10); end;  

/`


Lanzar un Snapshot:  

`BEGIN DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT('TYPICAL'); END;  

/`


Si queremos volver a ponerlo cada 60 mintuos:


`begin DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(11520,60); end;  

/`


Los informes lo podemos generar de la siguiente manera:  

`$ORACLE_HOME/rdbms/admin/awrrpt.sql  

$ORACLE_HOME/rdbms/admin/awrrpti.sql`


Una vez ejecutéis el script os pedirá el tipo de informe, texto o HTML, aparecerá un lista de los shapshop disponibles, seleccionas los que os interese y se generará el informe AWR con el nombre de fichero que hayáis definido.





* [Oracle](/?q=taxonomy/term/7)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F63%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




