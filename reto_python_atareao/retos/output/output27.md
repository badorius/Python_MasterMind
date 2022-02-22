





Linux enjaular/chroot a un usuario con Jailkit | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux enjaular/chroot a un usuario con Jailkit

 

Lun, 05/24/2010 - 14:57 — badorius

Tras la necesidad de crear un usuario que solo tenga acceso a los logs del sistema, me planteé la idea de enjaular a un usuario. 


Para versiones nuevas de ssh, parece que permite hacer chroot de un usuario de una manera fácil y nativa del demonio, como la versión del servidor con la que estoy trabajando, no tiene la última versión de SSH y tampoco es una debian (:\_\_\_\_\_\_O), me veo obligado a realizarlo con jailkit, creando un paquete RPM del código fuente.


Los pasos que se han seguido, son los siguientes.


Nos vamos al directorio, donde nos bajaremos el código fuente del jailkit:  

 `cd /usr/src/packages/SOURCES`


Nos descargamos el soft (si el link no funciona, mirar la última versión desde la web):  

 `wget [http://olivier.sessink.nl/jailkit/jailkit-2.11.tar.gz](http://olivier.sessink.nl/jailkit/jailkit-2.11.tar.gz "http://olivier.sessink.nl/jailkit/jailkit-2.11.tar.gz")`


En el mismo directorio, crearemos el fichero .spec para poder hacer un build del rpm:  

 `vi jailkit-2.11.spec`


El fichero tiene que quedar de la siguiente manera:  

 `Summary: GNU programa  

Name: jailkit  

Version: 2.11  

Release: 1  

Source0: %{name}-%{version}.tar.gz  

License: GPL  

Group: Development/Tools  

BuildRoot: %{_builddir}/%{name}-root  

%description  

Jail chroot software  

%prep  

%setup -q  

%build  

./configure  

make  

%install  

rm -rf $RPM_BUILD_ROOT  

make DESTDIR=$RPM_BUILD_ROOT install  

%clean  

rm -rf $RPM_BUILD_ROOT  

%files  

%defattr(-,root,root)  

/etc/jailkit/jk_check.ini  

 /etc/jailkit/jk_chrootsh.ini  

 /etc/jailkit/jk_init.ini  

 /etc/jailkit/jk_lsh.ini  

 /etc/jailkit/jk_socketd.ini  

 /etc/jailkit/jk_uchroot.ini  

 /etc/jailkit/jk_update.ini  

 /usr/bin/jk_uchroot  

 /usr/sbin/jk_addjailuser  

 /usr/sbin/jk_check  

 /usr/sbin/jk_chrootlaunch  

 /usr/sbin/jk_chrootsh  

 /usr/sbin/jk_cp  

 /usr/sbin/jk_init  

 /usr/sbin/jk_jailuser  

 /usr/sbin/jk_list  

 /usr/sbin/jk_lsh  

 /usr/sbin/jk_procmailwrapper  

 /usr/sbin/jk_socketd  

 /usr/sbin/jk_update  

 /usr/share/jailkit/jk_lib.py  

 /usr/share/jailkit/jk_lib.pyc  

 /usr/share/man/man8/jailkit.8.gz  

 /usr/share/man/man8/jk_addjailuser.8.gz  

 /usr/share/man/man8/jk_check.8.gz  

 /usr/share/man/man8/jk_chrootlaunch.8.gz  

 /usr/share/man/man8/jk_chrootsh.8.gz  

 /usr/share/man/man8/jk_cp.8.gz  

 /usr/share/man/man8/jk_init.8.gz  

 /usr/share/man/man8/jk_jailuser.8.gz  

 /usr/share/man/man8/jk_list.8.gz  

 /usr/share/man/man8/jk_lsh.8.gz  

 /usr/share/man/man8/jk_procmailwrapper.8.gz  

 /usr/share/man/man8/jk_socketd.8.gz  

 /usr/share/man/man8/jk_uchroot.8.gz  

 /usr/share/man/man8/jk_update.8.gz  

#/usr/local/bin/jailkit  

#%doc /usr/local/info/jailkit.info  

#%doc %attr(0444,root,root) /usr/local/man/man1/jailkit.1  

#%doc COPYING AUTHORS README NEWS`


Seguidamente, crearemos el fichero rpm:


 `rpmbuild -ba jailkit-2.11.spec`


Tras ello, ya disponemos del RPM, podemos realizar la instalación del paquete:  

 `rpm -i /usr/src/packages/RPMS/x86_64/jailkit-2.11-1.x86_64.rpm`


Una vez ya tenemos el jail software, procederemos a chrootear al usuario que en el ejemplo será el usuario “luser”:


 `mkdir /oracle/jail  

chown root:root /oracle/jail  

jk_init -v /oracle/jail basicshell  

jk_init -v /oracle/jail netutils  

jk_init -v /oracle/jail ssh  

jk_init -v /oracle/jail jk_lsh  

useradd -d /oracle/luser -m luser -s /bin/bash  

passwd luser  

jk_jailuser -m -j /oracle/jail luser  

jk_cp -v -f /oracle/jail /bin/bash`


Verificamos el usuario en el fichero /etc/passwd  

 `vi /etc/passwd  

luser:x:1003:1004::/home/jail/./home/luser:/usr/sbin/jk_chrootsh`


Modificamos el fichero /oracle/jail/etc/passwd dejándolo de la siguiente forma:  

 `vi /oracle/jail/etc/passwd  

luser:x:1002:100::/home/luser:/bin/bash`  

Creamos el directorio opt:  

 `mkdir /oracle/jail/opt`  

Copiamos en el Jail, los comandos adicionales que podamos necesitar, como tail en mi ejemplo:  

 `cp /usr/bin/tail /oracle/jail/bin/`


Para realizar un update del jail:  

 `jk_update -j /oracle/jail -d`


Con esto el usuario luser, ya podrá iniciar sesión de manera enjaulada en su directorio, a este punto se pueden crear hardlinks o copiar ficheros logs, o lo que sea necesario al directorio home de este usuario.





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F27%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




