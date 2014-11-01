#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.ToNgueLP_MW_UI import Ui_ToNgueLP_MW

'''
BEGIN PRUEBA
'''
from modules.ToNgueLP_corpus import XML_read as corpus_reader
'''
END PRUEBA
'''

class ToNgueLP_MW(QMainWindow, Ui_ToNgueLP_MW):
   def __init__(self, _name, _version, parent = None):
      # init the parent
      super(ToNgueLP_MW, self).__init__(parent)

      # setup the UI
      self.setupUi(self)

      # some attributes
      self.appName = _name
      self.appVersion = _version

      # aditional configuration
      self.showMaximized()
      self.setWindowTitle(self.appName + ' - ' + self.appVersion)

      # setup signals and slots
      self.actionLoad_New_Corpus.triggered.connect(self.load_new_corpus)


   def load_new_corpus(self):
      '''
      Carga un corpus
      '''
      corpus_info = corpus_reader.parse_xml()

      print corpus_info[0]
      print '\r'
      print corpus_info[1]
