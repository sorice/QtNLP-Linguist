#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: Update_Corpus_XML_Infomation
   :platform: Linux
   :synopsis: Actualizar informaciones del XML del corpus.

.. moduleauthor:: Abel Meneses Abad <abelma1980@gmail.com>

"""

import re

class Update_Corpus_XML_Info:
   """
   Verify real values on XML corpus.
   """
   
   def __init__(self, number, corpus_file, corpus_dir, text):
      """Inicializar el script"""
      self.number = number
      self.corpus_file = corpus_file
      self.corpus_dir = corpus_dir
      self.text = text
   
   def snippet_pair_count(self):
      """Return the number of tags == **snippet_pairs** on a XML file. 
      
      :param corpus_file: The name of the XML file to modify.
      :type name: str.
      :param corpus_dir: Current path of the XML file *corpus_file*.
      :type state: str = valid path.
      :returns:  Number of expression *'<snippet_pair'* counted.
      :rtype: int.
      :exception: IOError
      
      .. Note:: Puede ser que no se haya actualizado el **total_cases** dentro del `/data/ToNgueLP-plag-cases-corpus.xml <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/EScorpusYYY-plag-cases-corpus.html>`_ al add o delete cases manualmente.
      """

      # Comprobar si existe el fichero XML.
      try:
         self.text = open(self.corpus_file,'r').read()
      except IOError:
          print 'The file does not exist'
          return None
      
      # Contar el número de veces que aparece la expresión '<snippet_pair'
      self.number = self.text.count('<snippet_pair')
            
      # Write the value in XML file
      init = re.search('total_cases',self.text)
      end = re.search('total_true_cases',self.text)
      texto_modificado = self.text[:init.start()]+'total_cases="'+str(self.number)+'" '+self.text[end.start():]

      self.text = open(self.corpus_file,'w')
      self.text.write(texto_modificado)
      self.text.close()
      
      return self.number
