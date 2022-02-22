





HPUX Jugando con los procesos #>psrset. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## HPUX Jugando con los procesos #>psrset.

 

Jue, 01/14/2010 - 15:45 — badorius

Si queremos asignar procesos a una cpu en concreto, mover procesos de una cpu a otra, en HPUX tenemos la opción de hacerlo con psreset.


Los procesos por defecto se lanzan en el pset 0, podemos crear un pset nuevo (pset 1), asignado a una CPU y mover procesos a ese pset. De esta forma podríamos garantizar una CPU para un proceso determinado o aislar un proceso peligroso/problemático a otra CPU:


Creamos un pset:


 `# psrset -c 1  

successfully created pset 1  

successfully assigned processor 1 to pset 1`


Consultamos los psets:


 `# psrset  

PSET 0  

SPU_LIST 0  

OWNID 0  

GRPID 0  

PERM 755  

IOINTR ALLOW  

NONEMPTY DFLTPSET  

EMPTY FAIL  

LASTSPU DFLTPSET  

LDOM_LIST 0  

RTE DISALLOW`  

 `PSET 1  

SPU_LIST 1  

OWNID 0  

GRPID 3  

PERM 755  

IOINTR ALLOW  

NONEMPTY DFLTPSET  

EMPTY FAIL  

LASTSPU DFLTPSET  

LDOM_LIST 0  

RTE DISALLOW`


Una vez tenemos dos psets uno en cada cpu, miramos con el top un proces, en el ejemplo el de java: 


 `0 ? 6006 root 152 20 311M 93036K run 26:37 0.32 0.32 java`


Notar que el primer dígito (0) es la cpu donde está el proceso.


Pasamos el proceso al pset 1 con el pid:


 `# psrset -b 1 6006`


Verficiamos el proceso con un top y ya lo podemos ver en la CPU 1:


 `1 ? 6006 root 152 20 311M 93036K run 26:37 0.30 0.30 java`


Si haces psets y se reinicia la maquina, los psets, lógicamente se pierden, en caso necesario, se tendría que crear un script en el arranque.


Eliminación el pset 1 (no destruye lo procesos, volvería al pset 0):


 `# psrset -d 1`


Podemos crear tantos psets como queramos o por lógica por tantas cpus tengamos.





* [HPUX](/?q=taxonomy/term/6)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F13%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




