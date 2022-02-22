





SVN Como forzar un comentario al realizar un Commit en Subversion | Badorius


















# [BadoriusBadorius](/ "Badorius")

 
 

[Inicio](/) ## SVN Como forzar un comentario al realizar un Commit en Subversion

 

Vie, 05/21/2010 - 10:06 — badorius

Ira al directorio llamado  `hooks`  dentro del repositorio:


 `cd /svn/projectname/hooks`


Crear un fichero llamado pre-commit.


 `vi pre-commit`


Pegar el siguiente código en dicho fichero, este forzará un comentario de como mínimo 10 o mas carácteres al realizar un commit.


Podéis pillar el txt en formato plano en:


[http://www.powertrip.co.za/blog/archives/pre-commit](http://www.powertrip.co.za/blog/archives/pre-commit "http://www.powertrip.co.za/blog/archives/pre-commit")


Quizás será necesario adaptar líneas como /usr/local/bin/python o /usr/local/bin/svnlook


 `#!/usr/local/bin/python  

“”"  

Subversion pre-commit hook which currently checks that the commit contains  

a commit message to avoid commiting empty changesets which tortoisesvn seems  

to have a habbit of committing.`


Based on [http://svn.collab.net/repos/svn/branches/1.2.x/contrib/hook-scripts/comm...](http://svn.collab.net/repos/svn/branches/1.2.x/contrib/hook-scripts/commit-block-joke.py "http://svn.collab.net/repos/svn/branches/1.2.x/contrib/hook-scripts/commit-block-joke.py")  

and hooks/pre-commit.tmpl


Hacked together by Jacques Marneweck 


$Id$  

“”"


import sys, os, string


SVNLOOK=’/usr/local/bin/svnlook’


def main(repos, txn):  

log\_cmd = ‘%s log -t “%s” “%s”‘ % (SVNLOOK, txn, repos)  

log\_msg = os.popen(log\_cmd, ‘r’).readline().rstrip(‘n’)


if len(log\_msg) < 10:  

sys.stderr.write (“Please enter a commit message which details what has changed during this commit.n”)  

sys.exit(1)  

else:  

sys.exit(0)


if \_\_name\_\_ == ‘\_\_main\_\_’:  

if len(sys.argv) < 3:  

sys.stderr.write(“Usage: %s REPOS TXNn” % (sys.argv[0]))  

else:  

main(sys.argv[1], sys.argv[2])  







* [Apache](/?q=taxonomy/term/9)
* [Linux](/?q=taxonomy/term/2)


* [Inicie sesión](/?q=user/login&destination=comment%2Freply%2F25%23comment-form) para enviar comentarios





 


## Inicio de sesión




Usuario: *



Contraseña: *



* [Solicitar una nueva contraseña](/?q=user/password "Solicita una contraseña nueva por correo electrónico.")






## Buscar





Search this site: 










 




