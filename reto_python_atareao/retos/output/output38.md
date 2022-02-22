





Linux Alsa default device | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux Alsa default device

 

Dom, 07/25/2010 - 12:57 — badorius

Tras reinstalar mi Debian, me encontré que al tener varios dispositivos de audio USB, Alsa no me cogía por defecto el que yo quería. En este caso me cogía UM1, que es un controlador Midi, con el resultado: debian sin sonido.


Al hacer un alsamixer mostraba el dispositivo UM1:


![AlsaMixer](http://www.badorius.com/sites/default/files/Alsamixer.jpg)


Al hacer un cat /proc/asound/cards, veo que el primero de la lista es UM1 con la posición 0:


 `server:~# cat /proc/asound/cards  

 0 [UM1 ]: USB-Audio - UM-1  

 EDIROL UM-1 at usb-0000:00:1d.1-1.1, full speed  

 1 [Track ]: USB-Audio - Fast Track  

 M-Audio Fast Track at usb-0000:00:1d.2-2, full speed  

 2 [nanoKONTROL ]: USB-Audio - nanoKONTROL  

 KORG INC. nanoKONTROL at usb-0000:00:1d.1-1.2, full speed`


Para modificar esto, he editado(creado) el fichero /etc/asound.conf dejándolo de la siguiente forma:


 `server:~# cat /etc/asound.conf  

pcm.!default {  

 type hw  

 card Track  

}  

ctl.!default {  

 type hw  

 card Track  

}`


Tras reiniciar, alsa ya toma la M-Audio como defualt device.


Fuente de información:


[http://alsa.opensrc.org/FAQ026](http://alsa.opensrc.org/FAQ026 "http://alsa.opensrc.org/FAQ026")  

[http://wiki.debian.org/ALSA](http://wiki.debian.org/ALSA "http://wiki.debian.org/ALSA")





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F38%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




