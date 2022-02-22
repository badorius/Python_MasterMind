





Configurar Apache para Cluster weblogic | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Configurar Apache para Cluster weblogic

 

Mar, 03/30/2010 - 14:22 — badorius

Descripción breve de como configurar un apache para hacer de proxy bridge de un cluster weblogic (Debian).


Primero copiaremos el módulo de apache, que vendrá en nuestro directorio de weblogic, algo parecido a:


 `cp $HOME/Oracle/Middleware/wlserver_10.3/server/plugin/linux/i686/mod_wl_22.so /usr/lib/apache2/modules`


Seguidamente editamos o creamos si no existe el fichero /etc/apache2/mods-available/weblogic\_module.load


Añadiendo la siguiente línea:


 `LoadModule weblogic_module /usr/lib/apache2/modules/mod_wl_22.so`


Activamos el módulo en el apache:


 `a2enmod weblogic_module`


Reiniciamos el apache:


 `/etc/init.d/apache2 restart`


Editamos el fichero apache2.conf o httpd.conf dependiendo de la distro y añadimos algo parecido a:


 `<IfModule mod_weblogic.c>  

  WebLogicCluster 127.0.0.1:7002,127.0.0.1:7003  

  MatchExpression /*  

</IfModule>`


donde 127.0.0.1:7002 127.0.0.1:7003 serán los servidores de aplicación que están a la espera de peticiones.





* [Apache](/?q=taxonomy/term/9)
* [Linux](/?q=taxonomy/term/2)
* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F19%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




