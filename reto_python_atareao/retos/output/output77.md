





AIX - Consultar WWN en AIX | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - Consultar WWN en AIX

 

Dom, 01/20/2013 - 12:09 — badorius

Para consultar los WWN (World Wide Name) en un AIX:


server01:/#lsdev -C|grep fcs | awk '{print "lscfg -vpl "$1"|grep Net"}' | ksh  

 Network Address.............2300001B318E3471  

 Network Address.............2301001B31AE3471  

 Network Address.............2300001B3391B4B1  

 Network Address.............2301001B33B1B4B1


server02:/#lsdev -C|grep fcs | awk '{print "lscfg -vpl "$1"|grep Net"}' | ksh  

 Network Address.............2300001B31943421  

 Network Address.............2301001B33B43421  

 Network Address.............2300001B318844D1  

 Network Address.............2301001B33A844D1





* [AIX](/?q=taxonomy/term/8)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F77%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




