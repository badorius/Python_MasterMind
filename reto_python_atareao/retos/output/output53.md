





Linux - Instalar Debian por red con PXE. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - Instalar Debian por red con PXE.

 

Lun, 12/20/2010 - 19:51 — badorius

Tras mi última adquisición "asus eee pc 1005PE", lo primero como siempre: formatear e instalar Debian.  

Ya no compro CD's desde hace mucho y los netbooks no tienen lector, con lo que utilizo PXE para instalar el sistema operativo desde red.


Para linux (Debian, Ubuntu) existe una forma muy fácil y rapida de configurar un servidor TFTP / PXE para instalar debian desde la red. Los pasos que he seguido han sido:


Creamos el directorio donde tendremos los ficheros:  

`mkdir /var/ftpd  

cd /var/ftpd/`  

Descargamos la version netinstaller, en mi caso selecciono la SID (Inestable Forever), en caso de querer otra modificaríamos la URL:  

`wget -erobots=off -np -r -l 0 -nH --cut-dirs=8 -R 'index.html*' [http://http.us.debian.org/debian/dists/sid/main/installer-i386/current/i...](http://http.us.debian.org/debian/dists/sid/main/installer-i386/current/images/netboot/ "http://http.us.debian.org/debian/dists/sid/main/installer-i386/current/images/netboot/")`  

Ojo en la URL que no se ve completa mostrandola al final con ...  

Instalamos el paquete dnsmasq el cual ya nos trae todo lo nocesario para nuestro objetivo. (Dhcp, Tftp, Dns)  

`aptitude install dnsmasq`  

Ahora solo queda modificar el fichero de configuración de dnsmasq  

`vi /etc/dnsmasq.conf`  

Quedando este parecido a:  

`listen-address=192.168.1.1  

bind-interfaces  

dhcp-range=192.168.1.100,192.168.1.154,12h  

dhcp-option=option:router,192.168.1.2  

dhcp-option=option:dns-server,8.8.8.8  

dhcp-boot=pxelinux.0  

enable-tftp  

tftp-root=/var/ftpd`


Modificaremos los parametros adaptandose a nuestra red.


Con esto ya solo nos queda configurar el equipo para que arranque desde la interfaz de red.  

Con esto queda pendiente un howto del Asus eeepc 1005pe.


Referencias


[http://crysol.org/node/1080](http://crysol.org/node/1080 "http://crysol.org/node/1080")





* [Debian](/?q=taxonomy/term/13)
* [Linux](/?q=taxonomy/term/2)
* [Ubuntu](/?q=taxonomy/term/14)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F53%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




