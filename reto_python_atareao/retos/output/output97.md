





TCP/IP Access Using bash | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## TCP/IP Access Using bash

 

Lun, 04/25/2016 - 14:46 — badorius

When executing a command on a /dev/tcp/$host/$port pseudo-device file, Bash opens a TCP connection to the associated socket.


A socket is a communications node associated with a specific I/O port. (This is analogous to a hardware socket, or receptacle, for a connecting cable.) It permits data transfer between hardware devices on the same machine, between machines on the same network, between machines across different networks, and, of course, between machines at different locations on the Internet.


The following examples assume an active Internet connection.


Getting the time from nist.gov:  

 `bash$ cat` 


Generalizing the above into a script:  

 `#!/bin/bash  

# This script must run with root permissions.`


URL="time.nist.gov/13"


Time=$(cat  

Downloading a URL:  

 `bash$ exec 5<>/dev/tcp/www.net.cn/80  

bash$ echo -e "GET / HTTP/1.0\n" >&5  

bash$ cat <&5` 


Example 29-1. Using /dev/tcp for troubleshooting  

 `#!/bin/bash  

# dev-tcp.sh: /dev/tcp redirection to check Internet connection.`


# Script by Troy Engel.  

# Used with permission.


TCP\_HOST=news-15.net # A known spam-friendly ISP.  

TCP\_PORT=80 # Port 80 is http.


# Try to connect. (Somewhat similar to a 'ping' . . .)  

echo "HEAD / HTTP/1.0" >/dev/tcp/${TCP\_HOST}/${TCP\_PORT}  

MYEXIT=$?


: <From the bash reference:  

/dev/tcp/host/port  

 If host is a valid hostname or Internet address, and port is an integer  

port number or service name, Bash attempts to open a TCP connection to the  

corresponding socket.  

EXPLANATION


if [ "X$MYEXIT" = "X0" ]; then  

 echo "Connection successful. Exit code: $MYEXIT"  

else  

 echo "Connection unsuccessful. Exit code: $MYEXIT"  

fi


exit $MYEXIT  







* [Linux](/?q=taxonomy/term/2)
* [Linux - bash](/?q=taxonomy/term/18)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F97%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




