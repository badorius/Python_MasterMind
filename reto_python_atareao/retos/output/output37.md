





SSH sin password (Intercambio de claves) | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## SSH sin password (Intercambio de claves)

 

Mar, 07/06/2010 - 10:10 — badorius

En este articulo se describe como establecer una relación de confianza entre dos nodos vía SSH, intercambiando claves.  

De esta forma podemos lanzar comandos de un nodo a otro sin introducir contraseña, muy útil para scripting.


En el ejemplo pondermos los nodos A y B.


Generamos las claves en el nodo A (sin contraseña):


 `a@A:~> ssh-keygen -t rsa  

Generating public/private rsa key pair.  

Enter file in which to save the key (/home/a/.ssh/id_rsa):  

Created directory '/home/a/.ssh'.  

Enter passphrase (empty for no passphrase):  

Enter same passphrase again:  

Your identification has been saved in /home/a/.ssh/id_rsa.  

Your public key has been saved in /home/a/.ssh/id_rsa.pub.  

The key fingerprint is:  

1a:2f:04:73:2f:1a:23:3a:2b:ab:3f:23:13:cb:12:e3 a@A`


Creamos el directorio ~/.ssh en el nodo B:


 `a@A:~> ssh b@B mkdir -p .ssh  

b@B's password:`


Seguidamente añadimos la nueva clave publica al fichero b@B:.ssh/authorized\_keys:


 `a@A:~> cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'  

b@B's password:`


Ya lo tenemos listo:  

 `a@A:~> ssh b@B hostname  

B`





* [AIX](/?q=taxonomy/term/8)
* [HPUX](/?q=taxonomy/term/6)
* [Linux](/?q=taxonomy/term/2)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F37%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




