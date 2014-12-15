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
   Verify real values on XML corpus
   We use this as a public class example class.

   You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

   .. note:: An example of intersphinx is this: you **cannot** use this class.

   """
   
   def __init__(self):
      self.__number = 0
      self.__corpus_file = ''
      self.__corpus_dir = ''
      self.__text = ''
   
   def snippet_pair_count(self, corpus_file = 'ToNgueLP-plag-cases-corpus.xml', corpus_dir = 'data/'):
      """Update total_cases = real snippet_pairs on corpus. Puede ser que no se haya actualizado el número total al add o delete cases."""
      
      
      # XML location
      self.__corpus_dir = corpus_dir
      self.__corpus_file = self.__corpus_dir + corpus_file
      self.__text = open(self.__corpus_file,'r').read()
      
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

