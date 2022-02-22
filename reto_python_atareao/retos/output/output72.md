





Ubuntu - Upgrade de 11.04 a 11.10 Problemas: dbus Couldn't connect to system bus - networking waiting up to 60 | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Ubuntu - Upgrade de 11.04 a 11.10 Problemas: dbus Couldn't connect to system bus - networking waiting up to 60

 

Dom, 10/16/2011 - 20:35 — badorius

Al actualizar Ubuntu de 11.04 a 11.10 si nos encontramos con el problema de que arranca sin conexión de red, dando el siguiente mensaje error:  

`"waiting up to 60 more seconds for the network configuration"`  

y:  

`Couldn't connect to system bus: Failed to connect to socket /var/run/dbus/system_bus_socket: Connection refused`


Y tampoco arranca el entorno gráfico, la solución:


`sudo mv /var/run/* /run/  

sudo mv /var/lock/* /run/lock/  

sudo rm -r /var/run  

sudo rm -r /var/lock  

sudo ln -s /run /var/run  

sudo ln -s /run/lock /var/lock  

sudo rm /run/dbus/*`





* [Ubuntu](/?q=taxonomy/term/14)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F72%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




