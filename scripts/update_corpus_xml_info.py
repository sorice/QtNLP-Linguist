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
   
   def __init__(self):
      self.__number = 0
      self.__corpus_file = ''
      self.__corpus_dir = ''
      self.__text = ''
   
   def snippet_pair_count(self, corpus_file = 'ToNgueLP-plag-cases-corpus.xml', corpus_dir = 'data/'):
      """Update **total_cases** tag = real documented **snippet_pairs** on ToNgueLP corpus. 
      
      :param corpus_file: The name of the XML file to modify.
      :type name: str.
      :param corpus_dir: Current path of the XML file *corpus_file*.
      :type state: str = valid path.
      :returns:  Number of tags *'<snippet_pair'* counted.
      :rtype: int.
      :exception: IOError
      
      .. Note:: Puede ser que no se haya actualizado el **total_cases** dentro del `/data/ToNgueLP-plag-cases-corpus.xml <../_static/01_Ingenieria/1.2_Arquitectura_y_Design/EScorpusYYY-plag-cases-corpus.html>`_ al add o delete cases manualmente.
      """
      
      # XML location
      self.__corpus_dir = corpus_dir
      self.__corpus_file = self.__corpus_dir + corpus_file
      self.__text = open(self.__corpus_file,'r').read()
      
      # Aquí hay que poner una excepción por si no está el fichero o si no existe la ruta dada.
      
      # Contar el número real de snippet_pair
      self.__number = self.__text.count('<snippet_pair')
            
      # Write the value in XML file
      init = re.search('total_cases',self.__text)
      end = re.search('total_true_cases',self.__text)
      texto_modificado = self.__text[:init.start()]+'total_cases="'+str(self.__number)+'" '+self.__text[end.start():]

      self.__text = open(self.__corpus_file,'w')
      self.__text.write(texto_modificado)
      self.__text.close()
      
      return self.__number

