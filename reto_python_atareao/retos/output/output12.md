





Ampliación filesystem AIX | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Ampliación filesystem AIX

 

Mié, 01/13/2010 - 17:24 — badorius

Esto es un ejemplo de como ampliar un filesystem llamado /filesystem1 en un AIX, añadiendo una lun nueva al VG.


Miramos a que volumgroup pertenece /filesystem1 con el comando lsvg –o | lsvg –i –l:


 `aixserver01:root:/>lsvg -o | lsvg -i –l  

....  

....  

....  

Data1vg:  

LV NAME TYPE LPs PPs PVs LV STATE MOUNT POINT  

fil01_lv jfs 220 220 3 open/syncd /filesystem1  

fil02_lv jfs 200 200 2 open/syncd /fil02  

fil03_lv jfs 256 256 2 open/syncd /fil03  

....  

....  

....`


Miramos a que vg pertence cada disco:


 `aixserver01:root:/>lspv | grep hdiskpower  

hdiskpower0 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower1 0X0X0X0X0X0X0X0X datavg active  

hdiskpower2 0X0X0X0X0X0X0X0X datavg active  

hdiskpower3 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower4 0X0X0X0X0X0X0X0X data3vg active  

hdiskpower11 0X0X0X0X0X0X0X0X vgtemp active  

hdiskpower13 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower14 0X0X0X0X0X0X0X0X datavg active  

hdiskpower15 0X0X0X0X0X0X0X0X data3vg active`


Un lsvg data1vg nos muestra la información del espacio libre en este vg:


 `aixserver01:root:/filesystem1>lsvg data1vg  

VOLUME GROUP: data1vg VG IDENTIFIER: 00dc042x00004c0000000131544fa49d  

VG STATE: active PP SIZE: 256 megabyte(s)  

VG PERMISSION: read/write TOTAL PPs: 1852 (474112 megabytes)  

MAX LVs: 256 FREE PPs: 11 (1932 megabytes)  

LVs: 9 USED PPs: 1758 (450048 megabytes)  

OPEN LVs: 9 QUORUM: 3  

TOTAL PVs: 4 VG DESCRIPTORS: 4  

STALE PVs: 0 STALE PPs: 0  

ACTIVE PVs: 4 AUTO ON: yes  

MAX PPs per PV: 2032 MAX PVs: 16  

LTG size: 128 kilobyte(s) AUTO SYNC: no  

HOT SPARE: no BB POLICY: relocatable`


Con un lsvg –p data1vg podemos ver los PPs Totales y libres de cada disco del volumgroup data1vg:


 `aixserver01:root:/filesystem1>lsvg -p data1vg  

data1vg:  

PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION  

hdiskpower3 active 1399 0 00..00..00..00..00  

hdiskpower13 active 15 0 00..00..00..00..00  

hdiskpower0 active 319 11 00..00..00..00..11`


Lanzamos un cfgmgr para reconozca el nuevo disco y un powermt config, powermt save:


 `aixserver01:root:/>cfgmgr  

aixserver01:root:/>powermt config  

aixserver01:root:/>powermt save`


Un lspv|grep hdiskpower ahora ya nos mostrará el nuevo disco:


 `aixserver01:root:/>lspv | grep hdiskpower  

hdiskpower0 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower1 0X0X0X0X0X0X0X0X datavg active  

hdiskpower2 0X0X0X0X0X0X0X0X datavg active  

hdiskpower3 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower4 0X0X0X0X0X0X0X0X data3vg active  

hdiskpower12 none None  

hdiskpower13 0X0X0X0X0X0X0X0X data1vg active  

hdiskpower14 0X0X0X0X0X0X0X0X datavg active  

hdiskpower15 0X0X0X0X0X0X0X0X data3vg active`


Añadimos hdiskpower12 al volumgroup data1vg:


 `aixserver01:root:/>extendvg data1vg hdiskpower12`


Ahora un lsvg –p data1vg ya nos muestra el disco hdiskpower12 en el vg data1vg:


 `aixserver01:root:/filesystem1>lsvg -p data1vg  

data1vg:  

PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION  

hdiskpower3 active 1399 0 00..00..00..00..00  

hdiskpower13 active 15 0 00..00..00..00..00  

hdiskpower0 active 319 0 00..00..00..00..00  

hdiskpower12 active 119 119 24..24..24..24..24`


Ampliar el filesystem desde la smit:


 `aixserver01:root:/>smit chfs`


Resumen, Para saber a qué VG pertenece un sistema de fitchero podemos hacer también: 


`df /filesystem1` --> en la primera columna obtenemos el Logical Volumen que lo contiene (fil01\_lv)  

`lslv -l fil01_lv` --> miramos la distribución del LV en discos (hdiskpowerX)  

`lspv |grep hdiskpowerX` --> y obtenemos el VG que tenemos que ampliar





* [AIX](/?q=taxonomy/term/8)
* [Unix](/?q=taxonomy/term/1)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F12%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




