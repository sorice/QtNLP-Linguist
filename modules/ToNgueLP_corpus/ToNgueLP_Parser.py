#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class CorpusHandler(ContentHandler):
   """Clase que permite manejar el ToNgueLPYYYY-plag-cases-corpus."""
   def __init__(self, *args, **kw):
      ContentHandler.__init__(self, *args, **kw)
      self.indent = 0
      self._factor = 4
      self.elements = 0
      self.corpus_name = ''
      self.version = 0
      self.lang = 'es'
      self.total_cases = 0
      self.true_cases = 0
      self.license = ''
      self.copyright = ''
      self.owners = ''
      self.authors = ''
      self.country = ''
      self.creation_date = ''
      self.last_modification_date = ''
      self.xmln = ''
      self.snippets = []
      self.snippet_pair = {}
      self.snippet_pair_id = 0

   def startElement(self, name, attrs):
      """
      Called when an element is encountered.
      """
      #~ if self.indent:
         #~ print '-' * (self.indent * self._factor),

      #~ print name, " (depth %d)" % self.indent
      atributos = attrs.getNames()
      #print atributos, "(atributos)"

      if 'corpus' in name:
         self.corpus_name = attrs.getValue('name')

      if 'snippet_pair' in name:
         self.snippet_pair_id = int(attrs.getValue('id'))
         string = str(attrs.getValue('snippet_pair_description'))
         array = []
         for tuple in string.split(';'):
            for value in tuple.split(':'):
               array.append(value)
         #print 'arreglo: ', array

         self.snippet_pair[self.snippet_pair_id] = array
         #~ print 'esto es de tipo: ', type(self.snippet_pair[self.snippet_pair_id])

      self.elements += 1
      self.indent += 1

   def endElement(self, name):
      self.indent -= 1

   def getCase(self, value):
      return self.snippet_pair[value]
