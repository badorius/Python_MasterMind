





Linux - Instalar Jdownloader en Debian Ubuntu de repositorio. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - Instalar Jdownloader en Debian Ubuntu de repositorio.

 

Dom, 08/14/2011 - 13:56 — badorius

Lo primero instalaremos java-sun:  

`aptitude install sun-java6-bin sun-java6-jre sun-java6-fonts sun-java6-plugin`


Seguidamente, con update-alternatives, dejaremos la JVM de sun por defecto:  

`update-alternatives --config java`  

En mi ejemplo, selecciono la opción 4:  

 `------------------------------------------------------------  

 0 /usr/lib/jvm/java-6-openjdk/jre/bin/java 1061 mode automàtic  

 1 /usr/bin/gij-4.4 1044 mode manual  

 2 /usr/bin/gij-4.6 1046 mode manual  

 3 /usr/lib/jvm/java-6-openjdk/jre/bin/java 1061 mode manual  

* 4 /usr/lib/jvm/java-6-sun/jre/bin/java 63 mode manual`


Añadimos el repositorio en el fichero /etc/apt/sources.list, editando este y añadiendo lo siguiente al final del fichero:  

`#JDOWNLOADER  

deb [http://ppa.launchpad.net/jd-team/jdownloader/ubuntu](http://ppa.launchpad.net/jd-team/jdownloader/ubuntu "http://ppa.launchpad.net/jd-team/jdownloader/ubuntu") maverick main  

deb-src [http://ppa.launchpad.net/jd-team/jdownloader/ubuntu](http://ppa.launchpad.net/jd-team/jdownloader/ubuntu "http://ppa.launchpad.net/jd-team/jdownloader/ubuntu") maverick main`  

Añadimos la clave del repositorio:  

 `apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A68F637`  

Actualizamos los repos:  

`aptitude update`  

Instalamos Jdownloader:  

 `aptitude install jdownloader` 


Ya tenemos jdownloader listo para usar.





* [Debian](/?q=taxonomy/term/13)
* [Linux](/?q=taxonomy/term/2)
* [Ubuntu](/?q=taxonomy/term/14)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F68%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




