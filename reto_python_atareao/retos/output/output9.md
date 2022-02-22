





Ejemplo de EXPORT e IMPORT de Oracle. | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Ejemplo de EXPORT e IMPORT de Oracle.

 

Mié, 01/13/2010 - 16:54 — badorius

Suponiendo el caso, de que realizamos cada día un export de una Base de Datos, generando un fichero BASEDATOS.dmp, podríamos importar todo un esquema de este export siguiendo estos pasos.


Importante: lanzar el commando siempre con el usuario propietario de la BDD.


Primero realizaremos un backup / export del esquema que en cuestión:


 `exp system file=NOMBRE_ESQUEMA.dmp log=NOMBRE_ESQUEMA.log owner=USUARIO_ESQUEMA`


Tras esto, ya podemos eliminar todos los objetos de la Base de Datos.


Una vez borrados los objetos, importaremos el esquema del fichero export que se supone que ya teníamos generado de toda la Base de Datos.


 `imp system file=FICHERO_EXPORT_BD.dmp log=ESQUEMA_imp.log fromuser=USUARIO_ESQUEMA touser=USUARIO_ESQUEMA`


El `USUARIO_ESQUEMA` origen y destino, en el caso de necesidad, podrían ser diferentes.


Gracias Moi.





* [Oracle](/?q=taxonomy/term/7)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




