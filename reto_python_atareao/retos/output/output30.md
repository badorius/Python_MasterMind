





Linux instalar Fuentes MS truetype msttcorefonts | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Linux instalar Fuentes MS truetype msttcorefonts

 

Vie, 06/04/2010 - 10:16 — badorius

Cuando uno está tan bien acostumbrado con distribuciones como debian o derivados, hay necesidades que son realmente muy fáciles de solucionar, que quiero decir? pues que en este caso, si necesitamos las fuentes truetype de M$, con debian bastaría con un aptitude install msttcorefonts, pero cuando tenemos que pelearnos con distros como RH o SLES, lo tenemos mas complicado.


Tras darle unas cuantas vueltas, la manera mas rápida y fácil de instalar las msstt fonts, ha sido ejecutando el script adjunto en el post (por motivos del hosting lo pongo en .txt y no .sh).


Sería tan fácil como:


 `mkdir /usr/share/fonts/truetype/  

wget [http://www.badorius.com/sites/default/files/fetchmsttfonts.txt](http://www.badorius.com/sites/default/files/fetchmsttfonts.txt "http://www.badorius.com/sites/default/files/fetchmsttfonts.txt")  

chmod 700 fetchmsttfonts.txt  

sh fetchmsttfonts.sh`





* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F30%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




