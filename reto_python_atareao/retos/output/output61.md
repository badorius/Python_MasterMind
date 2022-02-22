





AIX - Packet Filtering with IPSec | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - Packet Filtering with IPSec

 

Mié, 04/06/2011 - 15:25 — badorius

Mini howto IPSEC en AIX.


Para ver si tenes el software instalado:  

`root@aixserver:/> lslpp -L '*ipsec*'  

 Fileset Level State Type Description (Uninstaller)  

 ----------------------------------------------------------------------------  

 bos.msg.en_US.net.ipsec 6.1.4.0 C F IP Security Messages - U.S.  

 English  

 bos.net.ipsec.keymgt 6.1.4.1 C F IP Security Key Management  

 bos.net.ipsec.rte 6.1.4.0 C F IP Security`


Para listar las reglas activas:  

`lsfilt -a -v4 -O`


Para eliminar una regla:  

`rmfilt -v4 -n3`


Para activar las reglas configuradas:  

`mkfilt -v4 -u`


Por defecto tenemos una regla deny a todo:  

`lsfilt -a -v4 -O  

1|*** Dynamic filter placement rule for IKE tunnels ***|no  

2|deny|0.0.0.0|0.0.0.0|0.0.0.0|0.0.0.0|yes|all|any|0|any|0|both|both|no|all packets|0|all|0|||`


Con lo que al activar IPSEC tendremos un deny a todo, no tendremos acceso al servidor via TCP IP.


Aplicaremos una regla de ejemplo en la que permitiremos el acceso des de mi pc al servidor y viceversa. Siendo 192.168.10.1 mi pc y 192.168.9.1 el servidor:


`genfilt -v 4 -a P -s 192.168.10.1 -m 255.255.255.255 -d 192.168.9.1 -M 255.255.255.255 \  

 -g Y -c all -o any -p 0 -O any -P 0 -r B -w B -l N -f Y -i all`


genfilt -v 4 -a P -s 192.168.9.1 -m 255.255.255.255 -d 192.168.10.1 -M 255.255.255.255 \  

 -g Y -c all -o any -p 0 -O any -P 0 -r B -w B -l N -f Y -i all


Aplicamos la regla:  

`mkfilt -v4 -u`


Y verificamos:  

`lsfilt -a -v4 -O  

1|*** Dynamic filter placement rule for IKE tunnels ***|no  

2|permit|192.168.10.1|255.255.255.255|192.168.9.1|255.255.255.255|yes|all|any|0|any|0|both|both|no|all packets|0|all|0|||  

3|permit|192.168.9.1|255.255.255.255|192.168.10.1|255.255.255.255|yes|all|any|0|any|0|both|both|no|all packets|0|all|0|||  

4|deny|0.0.0.0|0.0.0.0|0.0.0.0|0.0.0.0|yes|all|any|0|any|0|both|both|no|all packets|0|all|0|||`


Fuentes:  

[http://www.blacksheepnetworks.com/security/resources/aix-ipsec-filtering...](http://www.blacksheepnetworks.com/security/resources/aix-ipsec-filtering.html "http://www.blacksheepnetworks.com/security/resources/aix-ipsec-filtering.html")





* [AIX](/?q=taxonomy/term/8)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




