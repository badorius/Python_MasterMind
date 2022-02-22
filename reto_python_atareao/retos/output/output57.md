





Weblogic - Modulo Weblogic con Apache SSL | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## Weblogic - Modulo Weblogic con Apache SSL

 

Mar, 01/25/2011 - 13:00 — badorius

Una manera de Mapear Apache SSL -> Weblogic SSL.


Primero configuramos nuestro servidor Weblogic para generar un certificado autofirmado SSL:


[http://www.badorius.com/?q=node/35](http://www.badorius.com/?q=node/35 "http://www.badorius.com/?q=node/35")


Una vez tenemos el weblogic con el certificado creado, ponemos como ejemplo que nuestro puerto SSL es el 7016


Consultamos la inforamción del certificado con el comando openssl:


`openssl s_client -connect miservidor.com:7016  

CONNECTED(00000003)  

depth=0 /C=ES/O=SR/OU=Empresa/CN=miservidor.com  

verify error:num=18:self signed certificate  

verify return:1  

depth=0 /C=ES/O=Empresa/OU=Empresa/CN=miservidor.com  

verify return:1  

---  

Certificate chain  

 0 s:/C=ES/O=SR/OU=Empresa/CN=miservidor.com  

 i:/C=ES/O=SR/OU=Empresa/CN=miservidor.com  

---  

Server certificate  

-----BEGIN CERTIFICATE-----  

MIICxDCCAi0CBECcV/wwDQYJKoZIhvcNAQEEBQAwgagxCzAJBgNVBAYTAlVTMQ4wDAYDVQQIEwVU  

ZXhhczEPMA0GA1UEBxMGQXVzdGluMSowKAYDVQQKEyFUaGUgVW5pdmVyc2l0eSBvZiBUZXhhcyBh  

dCBBdXN0aW4xKDAmBgNVBAsTH0luZm9ybWF0aW9uIFRlY2hub2xvZ3kgU2VydmljZXMxIjAgBgNV  

BAMTGXhtbGdhdGV3YXkuaXRzLnV0ZXhhcy5lZHUwHhcNMDQwNTA4MDM0NjA0WhcNMDQwODA2MDM0  

NjA0WjCBqDELMAkGA1UEBhMCVVMxDjAMBgNVBAgTBVRleGFzMQ8wDQYDVQQHEwZBdXN0aW4xKjAo  

BgNVBAoTIVRoZSBVbml2ZXJzaXR5IG9mIFRleGFzIGF0IEF1c3RpbjEoMCYGA1UECxMfSW5mb3Jt  

YXRpb24gVGVjaG5vbG9neSBTZXJ2aWNlczEiMCAGA1UEAxMZeG1sZ2F0ZXdheS5pdHMudXRleGFz  

LmVkdTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAsmc+6+NjLmanvh+FvBziYdBwTiz+d/DZ  

Uy2jyvij6f8Xly6zkhHLSsuBzw08wPzr2K+F359bf9T3uiZMuao//FBGtDrTYpvQwkn4PFZwSeY2  

Ynw4edxp1JEWT2zfOY+QJDfNgpsYQ9hrHDwqnpbMVVqjdBq5RgTKGhFBj9kxEq0CAwEAATANBgkq  

hkiG9w0BAQQFAAOBgQCPYGXF6oRbnjti3CPtjfwORoO7ab1QzNS9Z2rLMuPnt6POlm1A3UPEwCS8  

6flTlAqg19Sh47H7+Iq/LuzotKvUE5ugK52QRNMa4c0OSaO5UEM5EfVox1pT9tZV1Z3whYYMhThg  

oC4y/On0NUVMN5xfF/GpSACga/bVjoNvd8HWEg==  

-----END CERTIFICATE-----  

subject=/C=ES/O=SR/OU=Empresa/CN=miservidor.com  

issuer=/C=ES/O=SR/OU=Empresa/CN=miservidor.com  

---  

No client certificate CA names sent  

---  

SSL handshake has read 530 bytes and written 260 bytes  

---  

New, TLSv1/SSLv3, Cipher is RC4-MD5  

Server public key is 512 bit  

Compression: NONE  

Expansion: NONE  

SSL-Session:  

 Protocol : TLSv1  

 Cipher : RC4-MD5  

 Session-ID: 5A0E84746ABC09D8E15F15209377B4B6  

 Session-ID-ctx:  

 Master-Key: 1dfd123fgh1d23fg1d2gfd3fg21hd3fg1hd2f3d12fgd3g12hd3fgh1d2f3dh12d3f11h2d3f1h2d332df1g3hd1f2h3d1f2hd3 Key-Arg : None  

 Start Time: 1295948303  

 Timeout : 300 (sec)  

 Verify return code: 18 (self signed certificate)`


Copiamos la parte -----BEGIN CERTIFICATE----- hasta -----END CERTIFICATE----- incluidas y lo pegamos al nuevo fichero:


`vi /etc/apache2/ssl.crt/miservidor.com.pem` 


Tiene que quedar algo parecido a:


`cat /etc/apache2/ssl.crt/miservidor.com.pem  

-----BEGIN CERTIFICATE-----  

MIICxDCCAi0CBECcV/wwDQYJKoZIhvcNAQEEBQAwgagxCzAJBgNVBAYTAlVTMQ4wDAYDVQQIEwVU  

ZXhhczEPMA0GA1UEBxMGQXVzdGluMSowKAYDVQQKEyFUaGUgVW5pdmVyc2l0eSBvZiBUZXhhcyBh  

dCBBdXN0aW4xKDAmBgNVBAsTH0luZm9ybWF0aW9uIFRlY2hub2xvZ3kgU2VydmljZXMxIjAgBgNV  

BAMTGXhtbGdhdGV3YXkuaXRzLnV0ZXhhcy5lZHUwHhcNMDQwNTA4MDM0NjA0WhcNMDQwODA2MDM0  

NjA0WjCBqDELMAkGA1UEBhMCVVMxDjAMBgNVBAgTBVRleGFzMQ8wDQYDVQQHEwZBdXN0aW4xKjAo  

BgNVBAoTIVRoZSBVbml2ZXJzaXR5IG9mIFRleGFzIGF0IEF1c3RpbjEoMCYGA1UECxMfSW5mb3Jt  

YXRpb24gVGVjaG5vbG9neSBTZXJ2aWNlczEiMCAGA1UEAxMZeG1sZ2F0ZXdheS5pdHMudXRleGFz  

LmVkdTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAsmc+6+NjLmanvh+FvBziYdBwTiz+d/DZ  

Uy2jyvij6f8Xly6zkhHLSsuBzw08wPzr2K+F359bf9T3uiZMuao//FBGtDrTYpvQwkn4PFZwSeY2  

Ynw4edxp1JEWT2zfOY+QJDfNgpsYQ9hrHDwqnpbMVVqjdBq5RgTKGhFBj9kxEq0CAwEAATANBgkq  

hkiG9w0BAQQFAAOBgQCPYGXF6oRbnjti3CPtjfwORoO7ab1QzNS9Z2rLMuPnt6POlm1A3UPEwCS8  

6flTlAqg19Sh47H7+Iq/LuzotKvUE5ugK52QRNMa4c0OSaO5UEM5EfVox1pT9tZV1Z3whYYMhThg  

oC4y/On0NUVMN5xfF/GpSACga/bVjoNvd8HWEg==  

-----END CERTIFICATE-----`


Ahora solo falta configurar el apache.  

Editamos el fichero del apache, en mi caso el fichero de un virtual host, pero podría aplicar también en el httpd.conf si no hay virtualhost.


Esto puede cambiar dependiendo de la distro:  

`vi /etc/apache2/vhosts.d/miservidor-ssl.conf`


Y la parte que nos intersa sería:


`<VirtualHost *:443>  

 ServerAdmin [badorius@miservidor.com](mailto:badorius@miservidor.com)  

  DocumentRoot "/srv/www/htdocs"  

  ServerName badorius.com  

  SSLEngine on  

  SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP:+eNULL  

  SSLCertificateFile /etc/apache2/ssl.crt/server.crt  

  SSLCertificateKeyFile /etc/apache2/ssl.key/server.key  

  ErrorLog /var/log/apache2/miservidor-ssl-error.log  

  CustomLog /var/log/apache2/miservidor-ssl-access.log common  

  <Location />  

   <IfModule mod_weblogic.c>  

   SetHandler weblogic-handler  

   WLProxySSL ON  

   RequireSSLHostMatch false  

   EnforceBasicConstraints false  

   WebLogicHost 192.168.1.1  

   WebLogicPort 7016  

   SecureProxy ON  

   TrustedCAFile /etc/apache2/ssl.crt/miservidor.com.pem  

   SSLHostMatchOID 30  

   Debug ALL  

   DebugConfigInfo ON  

   WLLogFile "/var/log/apache2/miservidor-wl_proxy.log"¡  

  </IfModule>  

 </Location>  

</VirtualHost>`





* [Apache](/?q=taxonomy/term/9)
* [Weblogic](/?q=taxonomy/term/10)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F57%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




