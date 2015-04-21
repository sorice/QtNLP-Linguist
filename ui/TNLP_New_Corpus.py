#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.new_corpus_UI import Ui_NewCopus

class TNLP_NewCorpus(QDialog, Ui_NewCopus):
   def __init__(self, _xml_manager, parent = None):
      # init the parent
      super(TNLP_NewCorpus, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # signals and slots
      self.btn_save.clicked.connect(self.__create_corpus)

      # extra data
      self.__xml = _xml_manager


   def __create_corpus(self):
      """Create a new corpus"""

      corpus_data = {}

      #TODO: add input validation

      # get UI data
      corpus_data['name'] = str(self.le_name.text())
      corpus_data['version'] = str(self.sb_version.text())
      corpus_data['lang'] = str(self.le_lang.text())
      corpus_data['total_cases'] = str('0')
      corpus_data['total_true_cases'] = str('0')
      corpus_data['total_annotations'] = str('0')
      corpus_data['total_true_annotations'] = str('0')
      corpus_data['license'] = str(self.le_license.text())
      corpus_data['copyright'] = str(self.le_copyright.text())
      corpus_data['owners'] = str(self.le_owners.text())
      corpus_data['authors'] = str(self.le_authors.text())
      corpus_data['country'] = str(self.le_country.text())
      corpus_data['creation_date'] = str(QDateTime.currentDateTime().toString('ddd MMM d yyyy hh:mm:ss '))
      corpus_data['last_modification_date'] = corpus_data['creation_date']
      corpus_data['xmlns'] = str('http://tnlp.github.com')

      xml_file = QFileDialog.getSaveFileName(self, u"Create corpus", "", u"Corpus XML file (*.xml)")

      if not xml_file:
         QMessageBox.critical(self, self.parent().get_app_name(), 'Operation canceled.')
         return

      if not xml_file.endsWith('.xml'):
         xml_file = xml_file.append('.xml')

      xml_file = str(xml_file)

      new_corpus = self.__xml.create_corpus(xml_file, corpus_data['name'], corpus_data['version'],
         corpus_data['lang'], corpus_data['total_cases'], corpus_data['total_true_cases'],
         corpus_data['total_annotations'], corpus_data['total_true_annotations'], corpus_data['license'],
         corpus_data['copyright'], corpus_data['owners'], corpus_data['authors'], corpus_data['country'],
         corpus_data['creation_date'], corpus_data['last_modification_date'], corpus_data['xmlns'])

      if new_corpus:
         QMessageBox.information(self, self.parent().get_app_name(), u'Corpus created.')
      else:
         QMessageBox.critical(self, self.parent().get_app_name(), u'Error creating corpus ' + corpus_data['name'])
