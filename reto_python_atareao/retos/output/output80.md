





Adding RedHat DVD as Repository | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Adding RedHat DVD as Repository

 

Mié, 02/13/2013 - 16:27 — badorius

Create file:  

/etc/yum.repos.d/rhel-dvd.repo


With the follow content:


 `[dvd]  

name=Red Hat Enterprise Linux Installation DVD  

baseurl=file:///mnt/dvd/Server  

enabled=1  

gpgcheck=1  

gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release`


Create directory /mnt/dvd if not exist:  

 `mkdir /mnt/dvd`


Mount dvd :  

 `mount /dev/dvd /mnt/dvd/`


Thats all! now You're be able to install packages from dvd with yum command.





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F80%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




