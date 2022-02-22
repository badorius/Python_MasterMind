





Test from shell script if remote TCP port is open - BASH | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Test from shell script if remote TCP port is open - BASH

 

Lun, 05/29/2017 - 15:52 — badorius

 `function check_net_port ()  

{  

 local ip=$1  

 local port=$2  

 exec 3> /dev/tcp/"$ip"/"$port"  

 if [ $? -eq 0 ]; then return 0; else return 1; fi  

}`





* [Linux - bash](/?q=taxonomy/term/18)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F100%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




