





Comandos Navisphere Cli. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Comandos Navisphere Cli.

 

Mié, 02/03/2010 - 12:48 — badorius

Physical Container-Front End Ports Speeds


 `naviseccli –h 10.124.23.128 port –list -sfpstate  

naviseccli –h 10.124.23.128 –set sp a –portid 0 2  

naviseccli –h 10.124.23.128 backendbus –get –speeds 0`


SP Reboot and Shutdown GUI


 `naviseccli –h 10.124.23.128 rebootsp  

naviseccli –h 10.124.23.128 resetandhold`


Disk Summary


 `naviseccli –h 10.124.23.128 getdisk  

naviseccli –h 10.124.23.128 getdisk 0_0_9 (Bus_Enclosure_Disk - specific disk)`


Storage System Properties- Cache Tab


 `naviseccli –h 10.124.23.128 getcache  

naviseccli –h 10.124.23.128 setcache –wc 0 –rca 0 –rcb 0 (to disable Write and Read Cache)  

naviseccli –h 10.124.23.128 setcache –p 4 –l 50 –h 70 (Set Page Size to 4 KB, Low WaterMark to 50%, and High WaterMark to 70%)  

naviseccli –h 10.124.23.128 setcache –wc 1 –rca 1 –rcb 1 (to enable Write and Read Cache)` 


Storage System Properties- Memory Tab


 `naviseccli –h 10.124.23.128 setcache –wsz 2500 –rsza 100 –rszb 100  

naviseccli –h 10.124.23.128 setcache –wsz 3072 –rsza 3656 –rszb 3656 (maximum amount of cache for CX3-80)`


Creating a RAID Group


 `naviseccli –h 10.124.23.128 createrg 0 1_0_0 1_0_ 1 1_0_2 1_0_3 1_0_4 –rm no –pri med (same Enclosure)  

-rm (remove/destroy Raid Group after the last LUN is unbound for the Raid Group) -pri (priority/rate of expansion/defragmentation of the Raid Group)  

naviseccli –h 10.124.23.128 createrg 1 2_0_0 3_0_0 2_0_1 3_0_1 2_0_2 3_0_2 -raidtype r1_0 (for RAID 1_0 across enclosures)`


RAID Group Properties - General


 `naviseccli –h 10.124.23.128 getrg 0`


RAID Group Properties - Disks


 `naviseccli –h 10.124.23.128 getrg 0 –disks`


Binding a LUN


 `naviseccli –h 10.124.23.128 bind r5 0 –rg 0 –rc 1 –wc 1 –sp a –sq gb –cap 10  

bind raid type (r0, r1, r1_0, r3, r5, r6) -rg (raid group) -rc / -wc (read and write cache) -sp (storage processor) -sq (size qualifier - mb, gb, tb, bc (block count) -cap (size of the LUN)`


LUN Properties


 `naviseccli –h 10.124.23.128 getlun 0  

naviseccli –h 10.124.23.128 chglun –l 0 –name Exchange_Log_Lun_0`


RAID Group Properties - Partitions


 `naviseccli –h 10.124.23.128 getrg 0 –lunlist`


Destroying a RAID Group


 `naviseccli –h 10.124.23.128 removerg 0`


Creating a Storage Group


 `navicli –h 10.127.24.128 storagegroup –create –gname ProductionHost`


Storage Group Properties - LUNs with Host ID


 `navicli –h 10.127.24.128 storagegroup –addhlu –gname ProductionHost –alu 6 –hlu 6  

navicli –h 10.127.24.128 storagegroup –addhlu –gname ProductionHost –alu 23 –hlu 23`


Storage Group Properties - Hosts


 `navicli –h 10.127.24.128 storagegroup –connecthost –host ProductionHost –gname ProductionHost`


Destroying Storage Groups


 `navicli –h 10.127.24.128 storagegroup –destroy –gname ProductionHost`





* [SAN](/?q=taxonomy/term/3)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F14%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




