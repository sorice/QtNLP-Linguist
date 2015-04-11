#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.add_case_UI import Ui_Add_Case

# import plag types
from TNLP_Plag_Types import plag_types

try:
   _fromUtf8 = QString.fromUtf8
except AttributeError:
   def _fromUtf8(s):
      return s

class TNLP_AddCase(QDialog, Ui_Add_Case):
   def __init__(self, _xml_manager, parent = None):
      # init the parent
      super(TNLP_AddCase, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # signals and slots
      self.btn_add_case.clicked.connect(self.__add_case)

      # extra data
      self.__xml = _xml_manager

      # load default data
      for k in plag_types.keys():
         self.cb_plag_type.addItem(k)

      #TODO: cargar los valores de los combos problem_type y text_extension despues de
      # definir los diccionarios correspondientes en TNLP_Plag_Types
      # en el visual ELIMINAR esos valores por defecto


   def __add_case(self):
      """Add a new case"""

      case_data = {}

      #TODO: add input validation

      # get UI data
      case_data['problem_type'] = str(self.cb_problem_type.currentText())
      case_data['text_extension'] = str(self.cb_text_extension.currentText())
      case_data['description'] = str(self.le_description.text())
      case_data['plag_type'] = str(self.cb_plag_type.currentText())
      case_data['annotator_summary'] = str(self.le_summary.text())
      case_data['automatic_summary'] = str('')
      case_data['original_corpus'] = str(self.le_original_corpus.text())
      case_data['original_corpus_id'] = str(self.le_original_corpus_id.text())
      case_data['generated_by'] = str('human')
      case_data['generator_name'] = str(self.le_generator_name.text())
      case_data['susp_doc'] = str(self.le_susp_doc_name.text())
      case_data['susp_offset'] = str(self.le_susp_offset.text())
      case_data['susp_length'] = str(self.lb_susp_length.text())
      case_data['susp_sentences_count'] = str(self.lb_susp_sentences_count.text())
      case_data['src_doc'] = str(self.le_src_doc_name.text())
      case_data['src_offset'] = str(self.le_src_offset.text())
      case_data['src_length'] = str(self.lb_src_length.text())
      case_data['src_sentences_count'] = str(self.lb_src_sentences_count.text())

      self.__xml.add_case(case_data['problem_type'], case_data['text_extension'], case_data['description'],
         case_data['plag_type'], case_data['annotator_summary'], case_data['automatic_summary'],
         case_data['original_corpus'], case_data['original_corpus_id'], case_data['generated_by'],
         case_data['generator_name'], case_data['susp_doc'], case_data['susp_offset'], case_data['susp_length'],
         case_data['susp_sentences_count'], case_data['src_doc'], case_data['src_offset'], case_data['src_length'],
         case_data['src_sentences_count'])

      self.__xml.write_xml('/home/lordford/test1.xml')
