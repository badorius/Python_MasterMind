





HPUX - TCP WRAPPERS & INETD | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX - TCP WRAPPERS & INETD

 

Mar, 01/18/2011 - 14:30 — badorius

Configurar TCP WRAPPERS en HPUX 11.31 para servicios que están en el inetd.


Para ello pondremos como ejemplo limitar el acceso del servicio telenet. Dicho servicio es levantado por el metaservicio inetd con lo que primero de todo editaremos el fichero /etc/inetd.conf


`vi /etc/inetd.conf` 


Tendremos que modiricar la entrada actual de telnet que la tendríamos con algo similar a:


`telnet stream tcp6 nowait root /usr/lbin/telnetd telnetd`


Por:


`telnet stream tcp6 nowait root /usr/lbin/tcpd /usr/lbin/telnetd telnetd`


La ruta del tcpd podría ser diferente en otra versión de HPUX, en mi caso está en /usr/lbin/tcpd.


Una vez esto, es necesario que inetd relea la configuración. Una manera de hacerlo sin para el servicio, sería primero identificar el proceso de inetd:


`ps -eaf|grep inetd`  

`root 1554 1 0 Nov 15 ? 23:54 /usr/sbin/inetd -l`


Ahora lanzaremos un kill -HUP del proceso de inetd:


`kill -HUP 1554`


Este kill nos relee la configuración, pero sin parar el servicio, si miramos el fichero /var/adm/syslog/syslog.log, veremos algo parecido a lo siguiente:


`Jan 18 14:21:11 hpuxserver inetd[1554]: Rereading configuration  

Jan 18 14:21:11 hpuxserver inetd[1554]: Configuration complete`


Con esto ya solo queda añadir las entradas deseadas en /etc/hosts.allow /etc/hosts.deny.  

Esto funciona de tal manera que primero verifica el /etc/hosts.allow y si machea aplica la regla y no continua. Si no encuentra nada en el /etc/hosts.allow continua con el /etc/hosts.deny y si encuentra una coincidencia aplica la regla de denegación. Con lo que podríamos poner como ejemplo del /etc/hosts.allow:


`telnetd : 192.168.13.0/255.255.255.0`


Y en el /etc/hosts.deny:


`telnetd : ALL`


Esto aceptará conexiones telnet desde cualquier ip de la red 192.168.13.0 y el resto será denegado.


Haciendo una prueba de conexión de telnet desde miportatil.dominio.com que está en la 192.168.10.0 nos deniega la conexión y podemos ver en el fichero /var/adm/syslog/syslog.log una entrada como la siguiente:


`Jan 18 14:13:05 hpuxserver inetd[7939]: telnet/tcp: Connection from miportatil.dominio.com(192.168.11.11) at Tue Jan 18 14:13:05 2011  

Jan 18 14:13:05 hpuxserver telnetd[7939]: refused connection from miportatil.dominio.com`


Para comprobar la configuración podemos hacer un:  

`tcpdchk -v`


Para comprobar una regla en concreto podemos hacer:  

`tcpdmatch telnetd miportatil.grifols.com`


Este ejemplo se puede aplicar a cualqueir servicio o servicio incluido en el metaservicio del inetd tal y como explica el ejemplo.





* [HPUX](/?q=taxonomy/term/6)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F56%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




