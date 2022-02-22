





Linux Bugzilla con Oracle | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux Bugzilla con Oracle

 

Mar, 06/15/2010 - 14:19 — badorius

En este articulo, describo paso a paso, como configurar Bugzilla en un SLES 10 (puede servir para cualquier distribución adaptando algún punto).


SLES 10 tiene una versión antigua de perl-DBI con lo que será necesario añadir el siguiente repositorio de software mediante yast:


 `[http://download.opensuse.org](http://download.opensuse.org "http://download.opensuse.org")  

/repositories/openSUSE:/infrastructure/SLE_10/`


Seguidamente actualizamos la versión de perl-DBI.


Como tendremos que ejecutar scripts de perl que tiran de wget para descargarse módulos, tal y como comenté en el articulo de wget / proxy, si tenemos que configurar el wget para que tire de proxy editaremos el fichero /etc/wgetrc con los siguientes datos:


 `vi /etc/wgetrc  

http_proxy = [http://servidor.proxy.com:puerto/](http://servidor.proxy.com:puerto/ "http://servidor.proxy.com:puerto/")  

ftp_proxy = [http://servidor.proxy.com:puerto/](http://servidor.proxy.com:puerto/ "http://servidor.proxy.com:puerto/")  

proxy_user=usuarioproxy  

proxy_password=passwordproxy`


Seguidamente instalamos apache2 mediante yast y añadimos un virtual host editando/creando el fichero /etc/apache2/vhosts.d/bugserver.conf


vi /etc/apache2/vhosts.d/bugserver.conf


 `<VirtualHost bugserver:80>  

 ServerAdmin [admin@midominio.com](mailto:admin@midominio.com)  

 ServerName bugserver.midominio.com  

 DocumentRoot /srv/www/vhosts/bugzilla/  

 ErrorLog /var/log/apache2/bugzilla.midominio.com-error_log  

 CustomLog /var/log/apache2/bugzilla.midominio.com-access_log combined  

 HostnameLookups Off  

 UseCanonicalName Off  

 ServerSignature On  

 <Directory "/srv/www/vhosts/bugzilla/">  

 AddHandler cgi-script .cgi  

 Options +Indexes +ExecCGI  

 DirectoryIndex index.cgi  

 AllowOverride Limit  

 Options Indexes FollowSymLinks  

 Order allow,deny  

 Allow from all  

 </Director>  

SetEnv ORACLE_HOME /oracle/app/oracle/product/11.2.0/client_1  

SetEnv LD_LIBRARY_PATH /oracle/app/oracle/product/11.2.0/client_1/lib  

AddHandler cgi-script .cgi  

Options +Indexes +ExecCGI  

DirectoryIndex index.cgi  

</VirtualHost>`



Instalamos El cliente de Oracle. En mi caso, solo instalo el cliente, ya que tiro de un BD externa, se podría hacer lo mismo instalando base de datos y tirando del mismo servidor.


Descargamos el cliente de:


[http://www.oracle.com/technology/software/products/database/oracle11g/11...](http://www.oracle.com/technology/software/products/database/oracle11g/112010_linx8664soft.html "http://www.oracle.com/technology/software/products/database/oracle11g/112010_linx8664soft.html")


Y realizamos la instalación. Yo he dejado como ORACLE\_HOME=/oracle/app/oracle/product/11.2.0/client\_1


Una vez instalado el cliente, creamos el directorio para descargar y descomprimir el bugzilla:


 `mkdir -p /srv/www/vhosts/  

cd /srv/www/vhosts/  

wget [http://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-3.6.tar.gz](http://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-3.6.tar.gz "http://ftp.mozilla.org/pub/mozilla.org/webtools/bugzilla-3.6.tar.gz")  

tar xvzf bugzilla-3.6.tar.gz  

mv bugzilla-3.6 bugzilla`


Una vez ya tenemos el software, procedemos a ejecutar el script ./checksetup.pl --check-modules para que nos compruebe que módulos nos faltan para el correcto funcionamiento del bugzilla:


 `cd /srv/www/vhosts/bugzilla  

./checksetup.pl --check-modules`


Lo mas facil para instalar los módulos sería ejecutar lo siguiente:  

 `/usr/bin/perl install-module.pl –all`


Para instalar el módulo de oracle:


 `/usr/bin/perl install-module.pl DBD::Oracle`


Fruto a un error que me mostraba el bugzilla, fue necesario instalar el siguiente módulo:


 `perl install-module.pl DateTime::Locale`


Tras esto comprobamos nuevamente si nos queda algún módulo por instalar:


 `./checksetup.pl --check-modules`


Una vez ya tenemos los módulos instalados, procedemos a la creación de tablespace usuario, etc... en la BD:


Nos conectamos a la BD con un cliente y ejecutamos lo siguiente:


 `Create User and datafiles on oracle:  

CREATE TABLESPACE bugs  

DATAFILE '/oracle/oradata/bugzilla.dbf' SIZE 500M  

AUTOEXTEND ON NEXT 30M MAXSIZE 1024M;`


CREATE USER bugs  

IDENTIFIED BY "bugs"  

DEFAULT TABLESPACE bugs  

TEMPORARY TABLESPACE TEMP  

PROFILE DEFAULT;  

-- GRANT/REVOKE ROLE PRIVILEGES  

GRANT CONNECT TO bugs;  

GRANT RESOURCE TO bugs;  

-- GRANT/REVOKE SYSTEM PRIVILEGES  

GRANT UNLIMITED TABLESPACE TO bugs;  

GRANT EXECUTE ON CTXSYS.CTX\_DDL TO bugs;  




Una vez ya tenemos la BD configurada, lanzamos el script checksetup.pl el cual nos generará el fichero localconfig:


 `./checksetup.pl`


En mi caso, me dio un error al no existir el grupo Apache, el mismo script te sugiere que edites el fichero localconfig, indicando el grupo utilizado por apache, en mi caso www:  

 `Vi /srv/www/vhosts/bugzilla/localconfig  

$webservergroup = 'www';`


También tendremos que modificar los siguiente parametros:


 `$use_suexec = 0;  

$db_driver = 'oracle';  

$db_host = 'bugserver';  

$db_name = 'nombreBaseDatosSID';  

$db_user = 'bugs';  

$db_pass = 'bugs';`


Una vez configurado el localconfig, ejecutamos nuevamente el script ./checksteup.pl:


 `./checksetup.pl`


Con esto ya tenemos el bugzilla disponible accediente a [http://bugerver](http://bugerver "http://bugerver") (En el caso del ejemplo).






* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F34%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




