





Linux - AIRVIDEO en Linux Debian Ubuntu - Streaming Iphone Ipod Touch Ipad | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux - AIRVIDEO en Linux Debian Ubuntu - Streaming Iphone Ipod Touch Ipad

 

Sáb, 01/29/2011 - 23:47 — badorius

Hace tiempo que vengo buscando un software para poder ver las películas que tengo en mi media center por streaming des de mi iphone.


Esto se puede conseguir con el fantástico software AIRPLAY.


El cliente para iphone se puede encontrar en AppStore y el servidor se puede descargar tanto para windows como para MacOsX.


Este artículo describe como instalar-lo en un linux basado en debian/ubuntu de una manera muy simple.


Primero crearemos un directorio de trabajo con el usuario:


`cd  

mkdir airvideo  

cd airvideo`


Nos descargamos el script y lo ejecutamos, 


`wget [http://www.badorius.com/airvideo.txt](http://www.badorius.com/airvideo.txt "http://www.badorius.com/airvideo.txt")  

mv airvideo.txt airvideo.sh  

chmod 700 airvideo.sh`


Antes de ejecutarlo, editaremos la cabezera del script para modificar las variables que tiene al principio, adaptándolo a nuestro entorno:


`vi airvideo.sh  

INSTALL_DIR="/home/badorius/airvideo"  

FFMPEG_DIR="$INSTALL_DIR/ffmpeg"  

PROPERTIE_FILE="$INSTALL_DIR/test.properties"  

MEDIA="Movies:/home/badorius/Videos"  

AIR_VIDEO_LINK="http://inmethod.com/airvideo/download/linux/alpha4/AirVideoServerLinux.jar"`


Tras esto ya podemos ejecutar el script:


`./airvideo.sh`


Una vez finalizado el script, editaremos el fichero test.properties dejándolo algo parecido a:


`path.ffmpeg = /usr/local/bin/ffmpeg  

path.mp4creator = /usr/local/bin/mp4creator  

path.faac = /usr/local/bin/faac  

password =  

subtitles.encoding = windows-1250  

subtitles.font = Verdana  

folders = Movies:/Volumes/Data/Movies,Series:/Volumes/Data/Series`


Tras esto ya lo tenemos todo preparado para arrancar el servicio.  

Podemos crear un servicio de sistema o arrancarlo a mano:


`java -jar AirVideoServerLinux.jar /home/badorius/airvideo/test.properties`


Ya podemos disfrutar de todas nuestras películas y series en nuestro Iphone, Ipod touch o Ipad.


Fuentes de información:


[http://wiki.birth-online.de/know-how/hardware/apple-iphone/airvideo-serv...](http://wiki.birth-online.de/know-how/hardware/apple-iphone/airvideo-server-linux "http://wiki.birth-online.de/know-how/hardware/apple-iphone/airvideo-server-linux")  

[http://mischneider.net/?p=350](http://mischneider.net/?p=350 "http://mischneider.net/?p=350")





* [Debian](/?q=taxonomy/term/13)
* [Linux](/?q=taxonomy/term/2)
* [Ubuntu](/?q=taxonomy/term/14)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F58%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




