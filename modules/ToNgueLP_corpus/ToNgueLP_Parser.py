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
      #~ atributos = attrs.getNames()
      #~ print atributos, "(atributos)"

      if 'corpus' in name:
         self.corpus_name = str(attrs.getValue('name'))
         self.version = str(attrs.getValue('version'))
         self.lang = str(attrs.getValue('lang'))
         self.total_cases = int(attrs.getValue('total_cases'))
         self.true_cases = int(attrs.getValue('total_true_cases'))
         self.license = str(attrs.getValue('license'))
         self.copyright = str(attrs.getValue('copyright'))
         self.owners = str(attrs.getValue('owners'))
         self.authors = str(attrs.getValue('authors'))
         self.country = str(attrs.getValue('country'))
         self.creation_date = str(attrs.getValue('creation_date'))
         self.last_modification_date = str(attrs.getValue('last_modification_date'))

      if 'snippet_pair' in name:
         self.snippet_pair_id = int(attrs.getValue('id'))
         string = str(attrs.getValue('snippet_pair_description'))
         array = []
         for tuple in string.split(';'):
            for value in tuple.split(':'):
               array.append(value)

         array.append(str(attrs.getValue('id')))

         self.snippet_pair[self.snippet_pair_id] = array

      self.elements += 1
      self.indent += 1

   def endElement(self, name):
      self.indent -= 1

   def getCase(self, value):
      return self.snippet_pair[value]
