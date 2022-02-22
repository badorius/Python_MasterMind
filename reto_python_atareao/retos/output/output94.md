





Some large files in /var/opt/psb/db/pgsql/base/<directories> (HPUX 11.31, 11/09) | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Some large files in /var/opt/psb/db/pgsql/base/<directories> (HPUX 11.31, 11/09)

 

Jue, 08/13/2015 - 10:40 — badorius

...seems like a bug in older SFM Versions.  

To resolve this problem i've done the following steps:


1.) cimprovider -ls > /tmp/cimprovider\_orig


2.) Stop psbdb


 #/sbin/init.d/psbdb stop


3.) Delete the database.


 #cd /var/opt/psb/db  

 #rm -r pgsql


4.) Reconfigure ProviderSvcsBase .


 #swconfig -x reconfigure=true -x autoselect\_dependencies=false ProviderSvcsBase


5.) Reconfigure SysFaultMgmt and all other providers that has its own database.


 #swconfig -x reconfigure=true -x autoselect\_dependencies=false SysFaultMgmt WBEMP-FCP SAS- PROVIDER RAIDSA-PROVIDER WBEMP-Storage


6.) cimprovider -ls > /tmp/cimprovider\_new


7.) Check that cimserver\_orig and cimserver\_new have the same number of providers listed


8.) Send test events


 # sfmconfig -t -a


9.) Check if the test events were logged


 # evweb eventviewer -L -x


REFERENCE:  

[http://h30499.www3.hp.com/t5/System-Administration/some-large-files-in-v...](http://h30499.www3.hp.com/t5/System-Administration/some-large-files-in-var-opt-psb-db-pgsql-base-lt-directories-gt/td-p/5668351#.VcxD5vgeFhE "http://h30499.www3.hp.com/t5/System-Administration/some-large-files-in-var-opt-psb-db-pgsql-base-lt-directories-gt/td-p/5668351#.VcxD5vgeFhE")





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F94%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




