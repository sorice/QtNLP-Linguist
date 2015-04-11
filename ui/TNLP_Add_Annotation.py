#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.add_annotation_UI import Ui_Add_Annotation

# import constant types
from TNLP_Enums_Helper import phenomenom_types

try:
   _fromUtf8 = QString.fromUtf8
except AttributeError:
   def _fromUtf8(s):
      return s

class TNLP_AddAnnotation(QDialog, Ui_Add_Annotation):
   def __init__(self, _xml_manager, _case_data, parent = None):
      # init the parent
      super(TNLP_AddAnnotation, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # signals and slots
      self.btn_add_annotation.clicked.connect(self.__add_annotation)

      # extra data
      self.__xml = _xml_manager
      self._case = _case_data

      print self._case

      # load default data
      for i in phenomenom_types:
         self.cb_type.addItem(i)

      self.te_susp_snippet.setText(self._case['susp_text'])
      self.te_src_snippet.setText(self._case['src_text'])

      self.lb_case_name.setText('<b>[' + self._case['id'] + ']: ' + self._case['annotator_summary'] + '</b>')

      #TODO: cargar los valores de los combos problem_type y text_extension despues de
      # definir los diccionarios correspondientes en TNLP_Enums_Helper
      # en el visual ELIMINAR esos valores por defecto


   def __add_annotation(self):
      """Add a new annotation"""

      case_data = {}

      #TODO: add input validation

      # get UI data
      case_data['case_id'] = self._case['id']
      case_data['author'] = str(self.le_author.text())
      case_data['is_paraphrase'] = str('true')
      case_data['validated_by_human_beings'] = str('true')
      case_data['recognized_by_algorithms'] = str('false')
      case_data['algorithms_names'] = str('')
      case_data['annotation_date'] = str(QDate.currentDate().toString('d-M-yyyy'))
      case_data['type'] = str(self.cb_type.currentText())
      case_data['projection'] = str(self.cb_projection.currentText())
      case_data['susp_offset'] = str(self.le_susp_offset.text())
      case_data['susp_length'] = str(self.lb_susp_length.text())
      case_data['src_offset'] = str(self.le_src_offset.text())
      case_data['src_length'] = str(self.lb_src_length.text())

      self.__xml.add_annotation(case_data['case_id'], case_data['author'],
         case_data['is_paraphrase'], case_data['validated_by_human_beings'],
         case_data['recognized_by_algorithms'], case_data['algorithms_names'],
         case_data['annotation_date'], case_data['type'], case_data['projection'],
         case_data['susp_offset'], case_data['susp_length'], case_data['src_offset'],
         case_data['src_length'])

      self.__xml.write_xml()
