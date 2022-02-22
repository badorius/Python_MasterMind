





Weblogic Generar certificado auto-firmado | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic Generar certificado auto-firmado

 

Mar, 06/15/2010 - 14:48 — badorius

Para generar un certificado auto-firmado en weblogic, podemos hacer:


 `keytool -genkey -v -alias miservidor -keyalg RSA -keysize 512 -dname "CN=miservidor.midominio.com, OU=Empresa, O=Emp, C=ES" -keypass password -validity 365 -keystore MiKeyStore.jks -storepass password`


 `keytool -certreq -v -alias miservidor -file miservidor_req.pem -keypass password -storepass password -keystore MiKeyStore.jks`


Tras esto, desde la consola de adminsitración de Weblogic, iremos al servidor que queremos configurar con el certificado y pondremos las siguientes opciones en keystore:


 `Keystores:Custom Identity and Java Standard Trust  

Custom Identity Keystore: /ruta/a/mi/keystore/MiKeyStore.jks  

Custom Identity Keystore Type: JKS  

Custom Identity Keystore Passphrase: password  

Java Standard Trust Keystore Passphrase: changeit`


Seguidamente en SSL:


 `Identity and Trust Locatinos: Keystores  

Private Key Alias: miservidor  

Private Key Passphrase: password`





* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F35%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




