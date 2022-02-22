





Apache + SSL + SVN + LDAP | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Apache + SSL + SVN + LDAP

 

Mar, 03/23/2010 - 16:16 — badorius

Voy a explicar brevemente como configurar un servidor Apache + SVN con LDAP.


En mi caso me he visto obligado a realizarlo con SLE 10, lo que me ha traido alguna pelea ya que estoy muy bien acostumbrado con debian y su aptitude.


Me ha sorprendido mucho, que una distro com SLE 10 no tenga algunos paquetes en su repostirio, con lo que he tenido que añadir fuentes de repositorio al sistema. No voy a entrar con detalle pero indico donde se pueden encontrar repositorios para nuestra distro SLE o OpenSuse:


 `[http://en.opensuse.org/Additional\_package\_repositories](http://en.opensuse.org/Additional_package_repositories "http://en.opensuse.org/Additional_package_repositories")`


En mi caso, añadi las siguientes fuentes:


 `[http://download.opensuse.org/repositories/Apache/SLE\_10/](http://download.opensuse.org/repositories/Apache/SLE_10/ "http://download.opensuse.org/repositories/Apache/SLE_10/")  

[http://download.opensuse.org/repositories/Apache:/Modules/Apache\_SLE\_10/](http://download.opensuse.org/repositories/Apache:/Modules/Apache_SLE_10/ "http://download.opensuse.org/repositories/Apache:/Modules/Apache_SLE_10/")  

[http://download.opensuse.org/repositories/Apache:/Modules/SLE\_10/](http://download.opensuse.org/repositories/Apache:/Modules/SLE_10/ "http://download.opensuse.org/repositories/Apache:/Modules/SLE_10/")  

[http://download.opensuse.org/repositories/server:/php/server\_apache\_SLE\_10/](http://download.opensuse.org/repositories/server:/php/server_apache_SLE_10/ "http://download.opensuse.org/repositories/server:/php/server_apache_SLE_10/")`


Realicé la instalación del siguiente software:


● apache2  

● apache2-doc  

● apache2-prefork  

● libapr1  

● libapr-util1  

● neon  

● subversion  

● subversion-server  

● apache2-mod-apparmor  

● apache2-example-pages  

● apache2-mod\_php  

● apache2-devel  

● apache2-prefork  

● apache2-doc  

● apache2-mod\_perl  

● apache2-utils  

● apache2-mod\_python  

● openssl


Seguidamente hay que comprobar que modulos de apache tenemos activados:


 `# httpd2 -t -D DUMP_MODULES`


Los modulos mas importantes, que nos interesan para este caso serían:


 `auth_basic_module (shared)  

 authz_groupfile_module (shared)  

 authn_file_module (shared)  

 authz_user_module (shared)  

 ldap_module (shared)  

 authnz_ldap_module (shared)  

 ssl_module (shared)  

 authz_default_module (shared)  

 authn_alias_module (shared)  

 dav_module (shared)  

 dav_svn_module (shared)  

 authz_svn_module (shared)`


Importante que los últimos tres módulos esten cargados en este orden:  

dav\_module dav\_svn\_module auth\_svn\_module


En caso contrario, editariamos el fichero /etc/sysconfig/apache2 y corregiríamos el orden en la variable APACHE\_MODULES, quedando algo parecido a lo siguiente:


 `APACHE_MODULES="authz_host actions alias auth_basic authz_groupfile authn_file authz_user autoindex cgi dir include log_config mime negotiation setenvif status userdir asis imagemap ldap authnz_ldap ssl php5 authz_default authn_alias mod_dav mod_dav_svn mod_authz_svn"`


Ahora creamos un repositorio SVN:


 `mkdir /usr/local/svn  

mkdir /usr/local/svn/repositories  

svnadmin create /usr/local/svn/repositories/mirepositorio  

chown –R wwwrun /usr/local/svn/`


Configuramos el apache para que realice la autentificación por LDAP. Editamos el fichero /etc/apache2/httpd.conf y añadimos al final del documento la siguiente entrada:


 ``<Location "/mirepositorio" >  

  DAV svn  

  SVNPath  /usr/local/svn/repositories/mirepositorio  

  AuthType Basic  

  AuthBasicProvider ldap  

  AuthName "Subversion repository"  

  AuthLDAPURL ldap://DC.EMPRESA.COM/OU=EUR,DC=empresa,DC=com?sAMAccountName?base  

  AuthLDAPBindDN  "CN=usuariosvn,OU=Users,DC=empresa,DC=com"  

  AuthLDAPBindPassword passwordusuariosvn  

  AuthzLDAPAuthoritative off  

  Require ldap-attribute memberOf="CN=SVNUsers,OU=Informatica,OU=ES,OU=EUR,DC=empresa,DC=com"  

  Require ldap-attribute memberOf="CN=Admins,OU=Informatica,OU=ES,OU=EUR,DC=empresa,DC=com"  

</Location>``



Puntos a tener en cuenta en estas directivas de apache:  

El módulo funcionará con un usuario creado en el Ldap con el que realizaremos las consultas.


AuthLDAPURL: Indicaremos el servidor Ldap y a partir de que CN del path buscaremos el usuario del servicio. (Recomiendo la herramienta adexplorer, para poder ver el PATH de un CN en concreto).


AuthLDAPBindDN : Usuario que utilizaremos para realizar las consultas en el Ldap.


AuthLDAPBindPassword : Password del usuario que realizará las consultas.


Require ldap-attribute : Indicamos que para poder acceder al repositorio, necesita cumplir un atributo. Aquí tenemos muchas opciones, en mi caso el que me ha resultado más práctico, ha sido filtrar por Grupo, de esta manera, solo será necesario añadir un usuario al grupo que se ha configurado para darle permisos.


Continuará.....





* [Apache](/?q=taxonomy/term/9)
* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F16%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




