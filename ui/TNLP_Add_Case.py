#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.add_case_UI import Ui_Add_Case

# import constant types
from TNLP_Enums_Helper import plag_types

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
      self.te_susp_text.connect(self.te_susp_text, SIGNAL("selectionChanged()"), self.susp_snippet_stats)
      self.te_src_text.connect(self.te_src_text, SIGNAL("selectionChanged()"), self.src_snippet_stats)
      self.le_original_corpus_id.connect(self.le_original_corpus_id, SIGNAL("textChanged(QString)"), self.validate_original_corpus_id)
      self.le_summary.connect(self.le_summary, SIGNAL("textChanged(QString)"), self.validate_le_summary)

      # extra data
      self.__xml = _xml_manager
      self.__lineEdit_prev_Text = ''
      self.__prevCursorPos = 0
      self.__human_change = True    #Para el control de cambios del le_original_corpus_id
      self.__keys_le_summary_prev_Text = ''
      self.__keys_prevCursorPos = 0
      self.__le_human_change = True #Para el control de cambios del le_anotator_summary

      # load default data
      for k in plag_types.keys():
         self.cb_plag_type.addItem(k)

      self.lb_corpus_name.setText('<b>' + self.__xml.get_corpus_name() + '</b>')

      #TODO: cargar los valores de los combos problem_type y text_extension despues de
      # definir los diccionarios correspondientes en TNLP_Enums_Helper
      # en el visual ELIMINAR esos valores por defecto
      
   def validate_le_summary(self):
      """Validate keywords field. Less than 3 words, and less than 21 chars."""
      keys = str(self.le_summary.text())
      words = keys.count(' ')+1
      if self.__le_human_change and words <= 3 and len(keys) <= 21:
         self.__keys_le_summary_prev_Text = keys
         self.__keys_prevCursorPos = self.le_summary.cursorPosition()
         return
      elif self.__le_human_change == False and words <= 3 and len(keys) <= 21:
         self.__le_human_change = True
         return
      elif self.__le_human_change == True and words > 3 or len(keys) > 21:
         self.__le_human_change = False
         self.le_summary.setText(self.__keys_le_summary_prev_Text)
         return
      else:
         self.le_summary.setCursorPosition(self.__keys_prevCursorPos)
         self.__le_human_change = True
         return

      
   def validate_original_corpus_id(self):
      """Validate original corpus id as a number."""
      
      id_text = str(self.le_original_corpus_id.text())
      if self.__human_change and len(id_text)>0:
        try:
           int(id_text)
           self.__lineEdit_prev_Text = id_text
           self.__prevCursorPos = self.le_original_corpus_id.cursorPosition()
           return
        except:
           self.__human_change = False
           self.le_original_corpus_id.setText(self.__lineEdit_prev_Text)
           return
      self.le_original_corpus_id.setCursorPosition(self.__prevCursorPos)
      self.__human_change = True
      return

   def susp_snippet_stats(self):
      """Extraer datos automáticamente del snippet susp seleccionado."""
      susp_cursor = self.te_susp_text.textCursor()
      _susp_selected_text = str(susp_cursor.selectedText())
      #Offset
      self.lb_susp_offset.setText(str(susp_cursor.selectionStart()))
      #Length
      self.lb_susp_length.setText(str(len(_susp_selected_text)))
      #Sentence count
      if _susp_selected_text.endswith('.'):
         self.lb_susp_sentences_count.setText(str(_susp_selected_text.count('.')))
      else:
         self.lb_susp_sentences_count.setText(str(_susp_selected_text.count('.')+1))
      return
      
   
   def src_snippet_stats(self):
      """Extraer datos automáticamente del snippet susp seleccionado."""
      src_cursor = self.te_src_text.textCursor()
      _src_selected_text = str(src_cursor.selectedText())
      #Offset
      self.lb_src_offset.setText(str(src_cursor.selectionStart()))
      #Length
      self.lb_src_length.setText(str(len(_src_selected_text)))
      #Sentence count
      if _src_selected_text.endswith('.'):
         self.lb_src_sentences_count.setText(str(_src_selected_text.count('.')))
      else:
         self.lb_src_sentences_count.setText(str(_src_selected_text.count('.')+1))


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
      case_data['susp_offset'] = str(self.lb_susp_offset.text())
      case_data['susp_length'] = str(self.lb_susp_length.text())
      case_data['susp_sentences_count'] = str(self.lb_susp_sentences_count.text())
      case_data['src_doc'] = str(self.le_src_doc_name.text())
      case_data['src_offset'] = str(self.lb_src_offset.text())
      case_data['src_length'] = str(self.lb_src_length.text())
      case_data['src_sentences_count'] = str(self.lb_src_sentences_count.text())

      new_case_id = self.__xml.add_case(case_data['problem_type'], case_data['text_extension'], case_data['description'],
         case_data['plag_type'], case_data['annotator_summary'], case_data['automatic_summary'],
         case_data['original_corpus'], case_data['original_corpus_id'], case_data['generated_by'],
         case_data['generator_name'], case_data['susp_doc'], case_data['susp_offset'], case_data['susp_length'],
         case_data['susp_sentences_count'], case_data['src_doc'], case_data['src_offset'], case_data['src_length'],
         case_data['src_sentences_count'])

      self.__xml.write_xml()

      self.parent().update_case_list(new_case_id)

      QMessageBox.information(self, self.parent().get_app_name(), u'Case added.')
