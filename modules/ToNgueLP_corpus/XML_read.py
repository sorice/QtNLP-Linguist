#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from ToNgueLP_Parser import *
from xml.sax import SAXParseException
#from fuzzywuzzy import fuzz
from scripts import update_corpus_xml_info


class Corpus_Reader:
   """Corpus parser general class"""

   def __init__(self):
      # init global vars
      self.__susp_snippet = ''
      self.__src_snippet = ''
      self.__corpus_dir = ''
      self.__corpus_file = ''
      self.__first_run = True

      # XML parser & handler
      self.__handler = CorpusHandler()
      self.__parser = make_parser()
      self.__parser.setContentHandler(self.__handler)

      # helper flag
      self.__parsed = False


   def parse_xml(self, corpus_file = 'ToNgueLP-plag-cases-corpus.xml', corpus_dir = 'data/'):
      """Parse corpus XML and return the data to the UI"""

      # XML location
      self.__corpus_dir = corpus_dir
      self.__corpus_file = self.__corpus_dir + corpus_file

      # parse file safely
      try:
         self.__parser.parse(open(self.__corpus_file))
         self.__parsed = True
      except SAXParseException as e:
         self.__parsed = False

      if self.__parsed:
         self.__first_run = False

      return self.__parsed

      #~ print "El nombre del corpus es: ", handler.corpus_name
      #~ print "Total Elements: %d" % handler.elements

      #~ print 'Elementos del Par de fragmentos[', handler.snippet_pair_id,'] = ',handler.snippet_pair[handler.snippet_pair_id]


   def get_case(self, _case = 1):
      """Return corpus info about one particular case"""

      # return if not parsed yet
      if not self.__parsed:
         return None
      else:
         # output vars
         susp_snippet = ''
         src_snippet = ''

         # get element info
         element = self.__handler.getCase(_case)
         #~ print 'element: ', element
         if element != None:
            textoa = open(self.__corpus_dir + '/susp/' + element[1] + '.txt', 'r').read()
            susp_snippet = textoa[int(element[7]):int(element[7]) + int(element[5])]
            textob = open(self.__corpus_dir + '/src/' + element[3] + '.txt', 'r').read()
            src_snippet = textob[int(element[11]):int(element[11]) + int(element[9])]

            # return case info
            return (susp_snippet, src_snippet, tuple(element))

         # return None if errors
         return None


   def get_corpus_name(self):
      """Return corpus name"""

      if not self.__parsed:
         return None

      return self.__handler.corpus_name


   def get_corpus_total_cases(self):
      """Return corpus total cases"""
      __info = update_corpus_xml_info.Update_Corpus_XML_Info()

      if not self.__parsed: # Si no abrió el .XML ents...
         return None
      elif self.__first_run: # Sí es la primera vez que se solicita el # total de casos...
         return self.__handler.total_cases
      else: # de lo contrario, verifica el número de pares de fragmentos
         self.__handler.total_cases = __info.snippet_pair_count()

      return self.__handler.total_cases


   def get_corpus_info(self):
      """Return corpus information"""

      if not self.__parsed:
         return None

      return (self.__handler.corpus_name, self.__handler.version, self.__handler.lang,
         self.__handler.owners, self.__handler.authors, self.__handler.country,
         self.__handler.creation_date, self.__handler.last_modification_date, self.__handler.total_cases)


   def get_case_summary(self, _case = 1):
      """Return basic information about a case"""

      _case_info = self.__handler.getCase(_case)
      # return tuple(id, plag_type, brief_description)
      return (_case_info[12], _case_info[13], _case_info[14])


'''   fuzzr = fuzz.ratio(susp_snippet,src_snippet)

#  fuzz_partial = fuzz.partial_ratio(susp_snippet,src_snippet)
   init = time.time()

#  fuzz_sort = fuzz.token_sort_ratio(susp_snippet,src_snippet)

   timea = time.time() - init

print 'El fragmento sospechoso es: ', susp_snippet

print '/n ****************************** /n'

print 'El fragmento fuente es: ', src_snippet

#print 'fuzz ratio = ', fuzzr

#print 'fuzz partial ratio = ', fuzz_partial

print 'fuzz sort ratio = ', fuzz_sort

print 'La comparación de los fragmentos demora: ', timea

'''
