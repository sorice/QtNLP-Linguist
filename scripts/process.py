#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: Developmente_Process
   :platform: Linux/Windows
   :synopsis: Script para automatizar tareas de desarrollo de TNLP.

.. moduleauthor:: Abel Meneses Abad <abelma1980@gmail.com>

   ** Resumen de procesos que automatiza**
   
   * Generación automática del entregable del date_TNLP_corpus.tar.gz
""" 

import os
import re
from datetime import date
 
# Geneerar carpeta HTML de la Documentación de TNLP
 
 #start in the root of the project with index.rst
TNLP_doc_path_start = os.path.abspath(os.path.join(os.getcwd(), '../'))

os.system('sphinx-build -b html '+TNLP_doc_path_start+' '+TNLP_doc_path_start+'/html')


# copiar dentro del ./html/data/corpuses/TNLP/README.html el código que está en ./resources/htmls/codigo_html_del_formato_TNLP.XML.html

TNLP_HTML = open(TNLP_doc_path_start+'/html/data/corpuses/TNLP/README.html','r').read()
fragmento = open(TNLP_doc_path_start+'/resources/htmls/codigo_html_del_formato_TNLP.XML.html','r').read()

init = TNLP_HTML.find('<div class="highlight-xml"') #inicio a recortar
end = TNLP_HTML.find('</table></div>')+14

#Construir nuevo README con fragmento de código corregido a mano
TNLP_HTML = TNLP_HTML[:init]+fragmento+TNLP_HTML[end:]

README = open(TNLP_doc_path_start+'/html/data/corpuses/TNLP/README.html','w')
README.write(TNLP_HTML)
README.close()

#Has un ./html/data/corpuses/TNLP/README.html en tag y en él cambia las expresiones '../../../_static' a './README_files/'

TNLP_HTML = re.sub('../../../_static','./README_files/',TNLP_HTML)

#copia el nuevo ./html/data/corpuses/TNLP/README.html dentro de ./tag + la carpeta ./resources/README_files + ./data/corpuses/TNLP/TNLP.xml

#~ os.system('mkdir '+TNLP_doc_path_start+'/tags/new/') #hacer carpeta para compactar luego

#copiar el README modificado en carpeta tags
README = open(TNLP_doc_path_start+'/scripts/README.html','w')
README.write(TNLP_HTML)
README.close()

#copiar ficheros de estáticos
os.system('cp -r '+TNLP_doc_path_start+'/resources/README_files/ '+TNLP_doc_path_start+'/scripts/')

#copiar XML
os.system('cp -r '+TNLP_doc_path_start+'/data/corpuses/TNLP/TNLP.xml '+TNLP_doc_path_start+'/scripts/')

#luego genera un <date>-TNLP_corpus.tar.gz
today = date.today()
today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
os.system('zip -r '+TNLP_doc_path_start+'/tags/'+today+'_TNLP_corpus.zip  README_files README.html TNLP.xml')
os.system('rm -r TNLP.xml README.html README_files')
print "Proceso terminado con éxito"
exit
