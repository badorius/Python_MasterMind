





Conceptronic CLLRCMCE Linux - Lirc | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Conceptronic CLLRCMCE Linux - Lirc

 

Vie, 04/30/2010 - 22:38 — badorius

Despues de adquirir un mando Conceptronic CLLRCMCE para mi media center, he tenido que aventurarme en configurarlo para el correcto funcionamiento en lirc / mythtv.


El mando es el siguiente:


![Conceptronic CLLRCMCE](http://www.badorius.com/sites/default/files/CLLRCMCECW.jpg)


El mando funciona por radio frecuencia, no por Infrarojos, con lo que a primeras pensé que no podría funcionar con lirc.


La configuración ha sido tan sencillo como...


Primero he identificado el dispositivo:


 `root@server:~# ls -lrt /dev/input/by-id/usb-*  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-Device_USB_Device-event-if02 -> ../event7  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-TopSeed_Technology_Corp._USB_RF_Combo_Device-event-mouse -> ../event4  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-TopSeed_Technology_Corp._USB_RF_Combo_Device-mouse -> ../mouse1  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-TopSeed_Technology_Corp._USB_RF_Combo_Device-event-kbd -> ../event3  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-Device_USB_Device-event-mouse -> ../event6  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-Device_USB_Device-event-kbd -> ../event5  

lrwxrwxrwx 1 root root 9 2010-04-30 19:12 /dev/input/by-id/usb-Device_USB_Device-mouse -> ../mouse2`


Se entiende que ya se ha instalado lirc:


 `root@server:~# aptitude install lirc lirc-modules-source`


Tras, he editado los siguientes ficheros de lirc, dejandolos de la siguiente forma:


 `root@server:~# cat /etc/lirc/hardware.conf  

# /etc/lirc/hardware.conf  

#  

#Chosen Remote Control  

REMOTE="gyration"  

REMOTE_MODULES=""  

REMOTE_DRIVER="devinput"  

REMOTE_DEVICE="/dev/input/by-id/usb-TopSeed_Technology_Corp._USB_RF_Combo_Device-event-kbd"  

REMOTE_SOCKET=""  

REMOTE_LIRCD_CONF=""  

REMOTE_LIRCD_ARGS=""`


#Chosen IR Transmitter  

TRANSMITTER=""  

TRANSMITTER\_MODULES=""  

TRANSMITTER\_DRIVER=""  

TRANSMITTER\_DEVICE=""  

TRANSMITTER\_SOCKET=""  

TRANSMITTER\_LIRCD\_CONF=""  

TRANSMITTER\_LIRCD\_ARGS=""


#Enable lircd  

START\_LIRCD="true"


#Don't start lircmd even if there seems to be a good config file  

#START\_LIRCMD="false"


#Try to load appropriate kernel modules  

LOAD\_MODULES="true"


# Default configuration files for your hardware if any  

LIRCMD\_CONF=""


#Forcing noninteractive reconfiguration  

#If lirc is to be reconfigured by an external application  

#that doesn't have a debconf frontend available, the noninteractive  

#frontend can be invoked and set to parse REMOTE and TRANSMITTER  

#It will then populate all other variables without any user input  

#If you would like to configure lirc via standard methods, be sure  

#to leave this set to "false"  

FORCE\_NONINTERACTIVE\_RECONFIGURATION="false"  

START\_LIRCMD=""  

root@server:~#  




Como remote, le he indicado "Gyration" ya que este mando está basado en este modelo.


Ahora el lircd.conf:


 `root@server:~# cat /etc/lirc/lircd.conf  

#  

# lircd.conf  

# for Gyration MCE remote(s). Could almost certainly be expanded to work for their keyboard as well.  

#  

# Composed by Marc Randolph based upon  

# initial lircd.conf by Modulok ([https://bugs.launchpad.net/mythbuntu/+bug/156494/comments/6](https://bugs.launchpad.net/mythbuntu/+bug/156494/comments/6 "https://bugs.launchpad.net/mythbuntu/+bug/156494/comments/6"))  

# with help from the Linux MCE wiki ([http://wiki.linuxmce.org/index.php/Gyration-GYR3101US-codes](http://wiki.linuxmce.org/index.php/Gyration-GYR3101US-codes "http://wiki.linuxmce.org/index.php/Gyration-GYR3101US-codes"))  

#  

# Notes:  

# Star and Hash keys produce two key sequences: 0x002A followed by either 8 for star, or 3 for hash  

#  

# Revision history  

# 2.3 - Marc Randolph - Renamed camera to pictures and video to videos. Added alternative mappings  

# 2.2 - Marc Randolph - Added untested DVDMenu entry  

# 2.1 - Marc Randolph - StarHash comment was wrong  

# 2.0 - Marc Randolph - Special codes should be correct, or at least, very close to correct  

# 1.0 - Marc Randolph - added missing codes and changed names to match up the mceusb remote  

# - Some of the more special codes have not been verified (Pictures, LiveTV, etc)  

# 0.1 - Modulok - Initial revision  

#  

#  

begin remote`


 name gyration  

 bits 16  

 eps 30  

 aeps 100


 one 0 0  

 zero 0 0  

 pre\_data\_bits 16  

 pre\_data 0x8001  

 gap 135997  

 toggle\_bit\_mask 0x0


 begin codes  

 Home 0x0066 # AKA "Windows button"  

 Up 0x0067  

 Left 0x0069  

 Right 0x006A  

 Down 0x006C  

 Mute 0x0071  

 VolDown 0x0072  

 VolUp 0x0073  

 Power 0x0074  

 Pause 0x0077  

 More 0x0082 # AKA "Info" or Help  

 Back 0x009E  

 Skip 0x00A3  

 Replay 0x00A5  

 Stop 0x00A6  

 RecTV 0x00A7 #Not "recorded TV", but "record current show on TV"  

 Rewind 0x00A8  

 Play 0x00CF  

 Forward 0x00D0  

 Pictures 0x00D4 # not on Dell remote  

 RecordedTV 0x00E2 # aka KEY\_MEDIA  

 Guide 0x016A  

 LiveTV 0x016E # aka KEY\_PVR  

 DVD 0x0185  

 Music 0x0187 # not on Dell remote # aka KEY\_MP3  

 Videos 0x0189 # not on Dell remote  

 ChanUp 0x0192  

 ChanDown 0x0193  

 DVDMenu 0x019A # untested. not on Dell remote  

 Clear 0x0001  

 One 0x0002  

 Two 0x0003  

 Three 0x0004  

 Four 0x0005  

 Five 0x0006  

 Six 0x0007  

 Seven 0x0008  

 Eight 0x0009  

 Nine 0x000A  

 Zero 0x000B  

 Enter 0x001C  

 StarHash 0x002A # Star=0x2a and 0x08; Hash = 0x2a and 0x03  

# StarHash 0x002A # Air-music; Star=0x2a and 0x09; Hash = 0x2a and 0x04  

# Camera unknown # Air-music  

# Email 0x009E # Air-music  

# Browser 0x00AC # Air-music  

# Radio unknown # Air-music  

# Favorites 0x009C # Air-music  

 end codes


end remote  

# Alternative mappings to try if some of the above don't work  

# (please report any findings back to [http://www.mythtv.org/wiki/Gyration-based\_MCE\_Remotes](http://www.mythtv.org/wiki/Gyration-based_MCE_Remotes "http://www.mythtv.org/wiki/Gyration-based_MCE_Remotes"))  

# Up 0x0062  

# Left 0x0064  

# Right 0x0066  

# Down 0x0068  

# Pause 0x0075  

# Power 0x008E  

# Halt 0x019C  

# Lights 0x0111  

# Clear 0x0016  

# Enter 0x0024  

# DVDMenu 0x0029  




Con esto ya podemos reiniciar el demonio lircd:


 `root@paquito:~# /etc/init.d/lirc restart`


Podemos verificar que el demonio está en marcha con el dispositivo que toca:  

 `root@server:~# ps -eaf|grep -i lirc  

root 6199 1 0 22:40 ? 00:00:00 /usr/sbin/lircd --output=/var/run/lirc/lircd --driver=devinput --device=/dev/input/by-id/usb-TopSeed_Technology_Corp._USB_RF_Combo_Device-event-kbd  

root 7373 32449 0 23:35 pts/0 00:00:00 grep --color=auto -i lirc`


Adicionalmente he creado el fichero .Xmodmap en el home del usuario con el siguiente contenido:


 `root@server:~# cat /home/usuario/.Xmodmap  

keysym XF86AudioPrev = Prior  

keysym XF86AudioNext = Next  

keysym XF86AudioRewind = Left  

keysym XF86Forward = Right  

keysym XF86AudioRecord = R  

keysym XF86AudioStop = Escape  

keysym XF86AudioPlay = P  

keysym XF86Back = Escape  

keysym Pause = P  

keysym SunProps = I`


El pc que utilizo para media center, es un Giada N10 con procesador Intel Atom N330 chipset ION Nvidia:


![Giada N10](http://www.badorius.com/sites/default/files/POGIADAION330BLUE.jpg)





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F24%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




