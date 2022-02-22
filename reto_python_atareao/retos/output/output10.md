





Transacciones Administración SAP I | Badorius

















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Transacciones Administración SAP I

 

Mié, 01/13/2010 - 17:03 — badorius

Rutinas de un administrador, son:


Control de usuarios activos SM04  

Control de Work Process SM50  

Control de bloqueos SM12  

Control de actualizaciones SM13  

Control de dump ST22  

Control de logs del sistema SM21  

Control de jobs procesados SM37  

Control de la base de datos DB02  

Control de los backups de base de datos DB12  

ABM de usuarios SU01  

ABM de roles PFCG  

Para monitoreo de performance tienes las ST*  

La transacción SSAA es una buena herramienta para llevar una administración ordenada.


• Verificación de status de los Work Process:  

• Transacción: SM50 (Tools  Administration  Monitor  System Monitoring  Process Overview).


• Verificación de servidores Online: (Dependiente de mandante)  

• Transacción: SM51 (Tools  Administration  Monitor  System Monitoring  Servers).


• Verificación de usuarios en el sistema:  

• Transacción: SM04 (Tools  Administration  Monitor  System Monitoring  User Overview).


• Verificación de entradas de bloqueo:  

• Transacción: SM12 (Tools  Administration  Monitor  Lock entries).


• Verificación de errores de actualización:  

• Transacción: SM13 (Tools  Administration  Monitor  Update).


• Análisis de dumps del sistema:  

• Transacción: ST22 (Tools  Administration  Monitor  Dump analysis).


• Verificación del log del sistema:  

• Transacción: SM21 (Tools  Administration  Monitor  System Log).


• Chequeo de consistencia del spool:  

• Transacción: SPAD (Tools  CCMS  Spool  Spool Administration).


• Verificación de ordenes de salida de impresión:  

• Transacción: SP01 (Tools  CCMS  Spool  Output controller).


• Verificación de jobs de fondo:  

• Transacción: SM37 (Tools  Services  Jobs  Job Overview).


• Verificación de ejecución de Batch Inputs:  

• Transacción: SM35 (System  services  Batch Input  Sessions).


• Directorios del sistema SAP:  

• Transacción: AL11 (Tools  Administration  Monitor  Performance  Exceptions/Users  SAP directories).


• Calendario planificación para gestión de la BD:  

• Transacción: DB13 (Tools  CCMS  DB Administration  DBA Planning Calendar).


• Verificación de los logs de Backup:  

• Transacción: DB12 (Tools  CCMS  DB Administration  Backup logs).  

• Database backups y Redo log backups.


• Verificación de la Base de Datos:  

• Transacción: DB02 (Tools  Administration  Monitor  Performance  Database  Table/Indexes).  

• Mirar si existen Objetos críticos, el tamaño de los tablespaces e índices desaparecidos.


• Verificación de Tiempos de Respuesta del Sistema:  

• Transacción: ST03 (Tools  Administration  Monitor  Performance  Workload  Analysis), o ST03N  

• Para ver los tiempos de los WP.


• Verificación de estadísticas de Buffers:  

• Transacción: ST02 (Tools  Administration  Monitor  Performance  Setup/Buffers  Buffers).


• Verificación del Sistema Operativo:  

• Transacción: OS06 (Tools  Administration  Monitor  Performance  Operating System  Local  Activity), o ST06  

• En detail analysis menu, tenemos opciones para analizar el SO, el rendimiento de la BD y funciones adicionales.  

• OS Collector es el sevicio saposcol.


• Verificación de rendimiento de la Base de Datos:  

• Transacción: ST04 (Tools  Administration  Monitor  Performance  Database  Activity).  

• En detail analysis menu, tenemos opciones para analizar la actividad de la BD, condiciones excepcionales y funciones adicionales.


• Reorganización del TEMSE:  

• Transacción: SP12 (Tools  CCMS  SPOOL  Temse Administration).  

• Administración de Usuarios:  

• Transacción: SU01


• Roles de Usuarios:  

• Transacción: PFCG


• Datos de Autorización de Usuarios:  

• Transacción: SU53


• Envío de Mensajes a Usuarios:  

• Transacción: SM02





* [SAP](/?q=taxonomy/term/5)






 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




