





Weblogic Añadir ADF al classpath. | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic Añadir ADF al classpath.

 

Vie, 05/21/2010 - 10:12 — badorius

Para añadir las librerías ADF al classpath de Weblogic, primero lo añadiremos al setDomainEnv.sh:


 `weblogic@wlsserver:/oracle/Middleware/user_projects/domains/MIDOMINIO/bin> vi setDomainEnv.sh` 


#  

if [ "${POST\_CLASSPATH}" != "" ] ; then  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/oracle.adf.share\_11.1.1/adf-share-wls.jar${CLASSPATHSEP}${POST\_CLASSPATH}"  

 export POST\_CLASSPATH  

else  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/oracle.adf.share\_11.1.1/adf-share-wls.jar"  

 export POST\_CLASSPATH  

fi


if [ "${POST\_CLASSPATH}" != "" ] ; then  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/features/adf.share\_11.1.1.jar${CLASSPATHSEP}${POST\_CLASSPATH}"  

 export POST\_CLASSPATH  

else  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/features/adf.share\_11.1.1.jar"  

 export POST\_CLASSPATH  

fi


if [ "${POST\_CLASSPATH}" != "" ] ; then  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/features/adf.model\_11.1.1.jar${CLASSPATHSEP}${POST\_CLASSPATH}"  

 export POST\_CLASSPATH  

else  

 POST\_CLASSPATH="${COMMON\_COMPONENTS\_HOME}/modules/features/adf.model\_11.1.1.jar"  

 export POST\_CLASSPATH  

fi


#



En el caso de tener Managed servers y estos son gestionados por NodeManager, será necesario modificar el fichero /server/bin/startNodeManger.sh de la siguiente forma:



ORACLE\_HOME="/opt/products/oracle/WLS103/jdeveloper"  

export ORACLE\_HOME  

ADF\_CLASSPATH="${ORACLE\_HOME}/modules/features/adf.share\_11.1.1.jar"  

export ADF\_CLASSPATH  

set -x  

CLASSPATH="${WEBLOGIC\_CLASSPATH}${CLASSPATHSEP}${CLASSPATH}${CLASSPATHSEP}${BEA\_HOME}  

${CLASSPATHSEP}${ADF\_CLASSPATH}"  

export CLASSPATH


StopScriptEnabled=true  

StartScriptEnabled=true






* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F26%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




