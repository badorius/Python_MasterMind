





Weblogic Configurar NodeManager para arrancar el enviroment correcto | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic Configurar NodeManager para arrancar el enviroment correcto

 

Vie, 05/28/2010 - 11:00 — badorius

Si arrancamos un Managed Server sin nodemanager, este arranca con el entorno especificado en el script setDomain.env, pero si arrancamos un Managed Server desde el NodeManager, este por defecto no tendrá el mismo enviroment, con lo que puede que nuestra CLASSPATH sea diferente.


Hay varias maneras para que NodeManager arranque con el enviroment correcto, una de ellas y la documentada por Oracle sería ejecutando el script:


 `ORACLE_HOME/common/bin/setNMProps.sh`


Que esto añadirá:


 `StartScriptEnabled=true`


a nuestro nodemanager.properties.


Seguidamente lo arrancaríamos nuestro NodeManager con:


 `MW_HOME/wl_server_n/server/bin/startNodeManager.sh`


Con esto nuestro server tendría que arrancar con el mismo enviroment.





* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F28%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




