#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from ToNgueLP_Parser import *
from xml.sax import SAXParseException
import xml.dom.minidom

class Corpus_Writer:
   """Corpus writer general class"""

  def __init__(self):
      # init global vars
      self.__susp_snippet = ''
      self.__src_snippet = ''
      self.__corpus_dir = ''
      self.__corpus_file = ''
      #~ kase = input('Entre el número del caso que desea revisar: ')
      #self.__case_number = -1
      # XML parser & handler
      self.__handler = CorpusHandler()
      self.__parser = make_parser()
      self.__parser.setContentHandler(self.__handler)

      # helper flag
      self.__parsed = False

      impl = xml.dom.minidom.getDOMImplementation()
      doc = impl.createDocument(None, 'document', None)
      root = doc.documentElement
      root.setAttribute('reference', susp)
      doc.createElement('feature')

      for f in features:
         feature = doc.createElement('feature')
         feature.setAttribute('name', 'detected-plagiarism')
         feature.setAttribute('this_offset', str(f[1][0]))
         feature.setAttribute('this_length', str(f[1][1] - f[1][0]))
         feature.setAttribute('source_reference', src)
         feature.setAttribute('source_offset', str(f[0][0]))
         feature.setAttribute('source_length', str(f[0][1] - f[0][0]))
         root.appendChild(feature)

      doc.writexml(open(outdir + susp.split('.')[0] + '-'
                    + src.split('.')[0] + '.xml', 'w'),
                encoding='utf-8')
