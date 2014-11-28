#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  update_corpus_xml_info.py
#  
#  Copyright 2014 Abel Meneses Abad <abelma1980@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.  

import re

class Update_Corpus_XML_Info:
   """Verify real values on XML corpus"""
   
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

