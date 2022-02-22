





Weblogic Extender dominio para ADF a todos los servidores Managed | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic Extender dominio para ADF a todos los servidores Managed

 

Lun, 05/31/2010 - 11:40 — badorius

Para exenteder un dominio con las librerías ADF a todos los servidores Managed, tras la instalación ejecutaremos:


 `/oracle/Middleware/oracle_common/common/bin/wlst.sh`


Y ejecutamos el script applyJRF:


 `wls:/offline>applyJRF(target='*', domainDir='/oracle/Middleware/user_projects/domains/MIDOMINIO')`


Información encontrada en la web de oracle:


[http://download.oracle.com/docs/cd/E12839\_01/core.1111/e10105/scaling.htm](http://download.oracle.com/docs/cd/E12839_01/core.1111/e10105/scaling.htm "http://download.oracle.com/docs/cd/E12839_01/core.1111/e10105/scaling.htm")





* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F29%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




