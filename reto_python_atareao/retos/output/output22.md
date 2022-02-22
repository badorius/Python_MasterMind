





Bonding en SLES 10 | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Bonding en SLES 10

 

Vie, 04/16/2010 - 15:01 — badorius

Hoy me ha tocado configurar Bonding en SLES10. Los pasos que he seguido:


El fichero modprobe.conf.local, lo he dejado de la siguiente forma:


 `sles10:~/scripts # more /etc/modprobe.conf.local  

#  

# please add local extensions to this file  

#  

alias bond0 bonding  

options bonding miimon=100 mode=0 use_carrier=0`


He creado un fichero ifcfg-bond0 como el siguiente:


 `sles10:/etc/sysconfig/network # more ifcfg-bond0  

BOOTPROTO='static'  

BROADCAST=''  

ETHTOOL_OPTIONS=''  

IPADDR='192.168.9.81'  

MTU=''  

NAME='Bound Ingerface'  

NETMASK='255.255.255.224'  

NETWORK=''  

REMOTE_IPADDR=''  

STARTMODE='auto'  

UNIQUE=''  

USERCONTROL='no'  

BONDING_MASTER='yes'  

_nm_name='bus-pci-0000:02:00.0'  

BONDING_SLAVE_0='bus-pci-0000:02:00.0'  

BONDING_SLAVE_1='bus-pci-0000:02:00.1'  

BONDING_MODULE_OPTS='miimon=100 mode=0 use_carrier=0'`


Para saber el bus-pci que tenemos que poner en el BONDING\_SLAVE, lo podemos mirar en los ficheros ifcfg-eth-id-*** de las tarjetas.


 `sles10:/etc/sysconfig/network # grep bus-pci ifcfg-eth-id-00\:26\:55\:7d\:d0\:7*  

ifcfg-eth-id-00:26:55:7d:d0:74:_nm_name='bus-pci-0000:02:00.0'  

ifcfg-eth-id-00:26:55:7d:d0:76:_nm_name='bus-pci-0000:02:00.1'`


Los ficheros ifcfg-eth**** de las tarjetas físicas los he movido a una carpeta llamada backup, para que estos ficheros no sean utilizados.


 `sles10:/etc/sysconfig/network # ls -lrt ifcfg-*  

-rw-r--r-- 1 root root 251 Apr 13 12:06 ifcfg-eth-id-00:26:55:7d:d0:76  

-rw-r--r-- 1 root root 251 Apr 13 12:06 ifcfg-eth-id-00:26:55:7d:d0:74  

-rw-r--r-- 1 root root 412 Apr 13 12:56 ifcfg-bond0`


 `sles10:/etc/sysconfig/network # mv ifcfg-eth-id-00\:26\:55\:7d\:d0\:7* backup/`


He creado el default gw con el siguiente fichero:


 `sles10:/etc/sysconfig/network # more routes  

default 192.168.9.91 - -`


He cargado el módulo de bonding:


 `sles10:/etc/sysconfig/network # modprobe bonding`


Ahora ya podemos reinicar la red:


 `sles10:/etc/sysconfig/network # rcnetwork restart`


Podemos reiniciar el servidor para probar que todo arranca con normalidad.





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F22%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




