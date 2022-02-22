





Weblogic - Consultar version ADF Instalada. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic - Consultar version ADF Instalada.

 

Vie, 09/10/2010 - 15:25 — badorius

Para ver exactamente que versión de ADF tenemos instalada en nuestro weblogic, iremos al directorio:


 `cd $ORACLE_HOME/oracle_common/modules/oracle.adf.model_11.1.1`


Una vez en este directorio:


 `/oracle/Middleware/oracle_common/modules/oracle.adf.model_11.1.1> java -cp adfm.jar oracle.jbo.common.PrintVersion  

BC4J Version is: 11.1.1.56.60`


Eso nos muestra la Internal Version, para relacionarla con la External Version, consultando la nota 401694.1 - Oracle JDeveloper Releases en la web de oracle, podemos relacionar:


Buscando la Nota Oracle JDeveloper Releases [ID 401694.1] en metalink veemos la siguiente relación:



JDeveloper 11g 11.1.1.3.0 (5660) OTN APR 2010 tbd This is a maintanance release, which does not include new features.  

JDeveloper 11g 11.1.1.2.0 (5536) OTN NOV 2009 tbd This is a maintanance release, which does not include new features.  

JDeveloper 11g 11.1.1.1.0 (5407) OTN JUL 2009 tbd First release to be part of the Fusion Middleware Platform 11g.  

JDeveloper 11g 11.1.1.0.2 (5156) OTN ARP 2009 tbd This is a maintanance release, which does not include new features.  

JDeveloper 11g 11.1.1.0.1 (5188) OTN DEC 2008 tbd This is a maintanance release, which does not include new features.  

JDeveloper 11g 11.1.1.0.0 (5156) OTN OCT 2008 tbd First release in the new JDeveloper 11g Branch. First release to use Oracle WebLogic Server instead of OC4J.



Para realizar cambio de versión ADF intentaré colgar otro post.


Documenación upgrade punto 5 de:


[http://download.oracle.com/docs/cd/E12839\_01/upgrade.1111/e10127/toc.htm](http://download.oracle.com/docs/cd/E12839_01/upgrade.1111/e10127/toc.htm "http://download.oracle.com/docs/cd/E12839_01/upgrade.1111/e10127/toc.htm")





* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F42%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




