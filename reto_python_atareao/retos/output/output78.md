





AIX - Configure Storage and assign LUNs to AIX server Example. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## AIX - Configure Storage and assign LUNs to AIX server Example.

 

Dom, 01/20/2013 - 12:18 — badorius

Configure Storage and assign LUNs to AIX server (example).


Descover LUNs on server:  

 `cfgmgr`  

To show new disks:  

 `lspv`


To show powerpath configuration:  

 `powermt display dev=all`


VG + LV + FILESYSTEM CREATION:


VG creation:  

 `aix01:/#/usr/sbin/mkvg -S -y app01_vg -s256 hdiskpower1  

0516-1254 /usr/sbin/mkvg: Changing the PVID in the ODM.  

app01_vg  

aix01:/#/usr/sbin/mkvg -S -y data_vg -s256 hdiskpower0  

0516-1254 /usr/sbin/mkvg: Changing the PVID in the ODM.  

data_vg  

aix01:/#extendvg app01_vg hdiskpower2  

0516-1254 extendvg: Changing the PVID in the ODM.`


LV Creation:  

 `aix01:/# /usr/sbin/mklv -y'data_lv' -t'jfs2' data_vg 2039  

data_lv  

aix01:/# /usr/sbin/mklv -y'app01_lv' -t'jfs2' app01_vg 299 hdiskpower1  

app01_lv  

aix01:/#lsvg -p app01_vg  

app01_vg:  

PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION  

hdiskpower1 active 299 0 00..00..00..00..00  

hdiskpower2 active 39 39 08..08..07..08..08  

aix01:/# /usr/sbin/mklv -y'oracle_lv' -t'jfs2' app01_vg 39 hdiskpower2  

oracle_lv`


Filesystem creation  

 `/usr/sbin/crfs -v jfs2 "-ddata_lv" "-m/DATA" "-Ayes" "-prw" "-a" "agblksize=4096" "-a" "logname=INLINE"  

aix01:/#/usr/sbin/crfs -v jfs2 "-dapp01_lv" "-m/app01" "-Ayes" "-prw" "-a" "agblksize=4096" "-a" "logname=INLINE"  

File system created successfully.  

78072292 kilobytes total disk space.  

New File System size is 156762112  

aix01:/#/usr/sbin/crfs -v jfs2 "-doracle_lv" "-m/ORACLE" "-Ayes" "-prw" "-a" "agblksize=4096" "-a" "logname=INLINE"  

File system created successfully.  

10183164 kilobytes total disk space.  

New File System size is 20447232  

aix01:/#mount /DATA  

aix01:/#mount /ORACLE  

aix01:/#mount /app01  

aix01:/#df -k  

Filesystem 1024-blocks Free %Used Iused %Iused Mounted on  

/dev/hd4 1572864 1275336 19% 6068 3% /  

/dev/hd2 4194304 1556820 63% 69698 17% /usr  

/dev/hd9var 1572864 1329920 16% 4504 2% /var  

/dev/hd3 5767168 5553080 4% 227735 16% /tmp  

/dev/hd1 1572864 1534532 3% 317 1% /home  

/proc - - - - - /proc  

/dev/hd10opt 1572864 1342176 15% 2022 1% /opt  

/dev/usr_local_lv 10485760 10479764 1% 35 1% /usr/local  

/dev/data_lv 534511616 533905460 1% 4 1% /DATA  

/dev/oracle_lv 10223616 10181796 1% 4 1% /ORACLE  

/dev/app01_lv 78381056 78062628 1% 4 1% /app01`


 `aix01:/#lspv  

hdisk0 0008759adeb96e33 rootvg active  

aix01:/#lsvg -l rootvg  

rootvg:  

LV NAME TYPE LPs PPs PVs LV STATE MOUNT POINT  

hd5 boot 1 2 2 closed/stale N/A  

hd6 paging 21 42 2 open/syncd N/A  

hd8 jfs2log 1 2 2 open/stale N/A  

hd4 jfs2 3 6 2 open/stale /  

hd2 jfs2 8 16 2 open/stale /usr  

hd9var jfs2 3 6 2 open/stale /var  

hd3 jfs2 11 22 2 open/stale /tmp  

hd1 jfs2 3 6 2 open/stale /home  

hd10opt jfs2 3 6 2 open/stale /opt  

lg_dumplv sysdump 6 6 1 open/syncd N/A  

usr_local_lv jfs2 20 40 2 open/stale /usr/local`


 `aix01:/#lsvg -p rootvg  

rootvg:  

PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION  

hdisk0 active 558 474 111..61..79..111..112  

hdisk1 missing 149 71 09..02..00..30..30  

aix01:/#lsdev -C|grep hdisk  

hdisk0 Available 00-08-00 SAS Disk Drive  

hdisk1 Defined 04-00-01 XP MPIO Disk XP24000 (Fibre)`





* [AIX](/?q=taxonomy/term/8)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F78%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




