#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.add_annotation_UI import Ui_Add_Annotation

# import constant types
from TNLP_Enums_Helper import paraphrase_types

try:
   _fromUtf8 = QString.fromUtf8
except AttributeError:
   def _fromUtf8(s):
      return s

class TNLP_AddAnnotation(QDialog, Ui_Add_Annotation):
   def __init__(self, _xml_manager, _case_data, parent = None, _edit = False, _annotation = None):
      # init the parent
      super(TNLP_AddAnnotation, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # extra data
      self.__xml = _xml_manager
      self._case = _case_data
      self.__edit_mode = _edit
      self.__annotation = _annotation
      if self.__edit_mode == True:
         self.__annotation_index = self.__annotation['id']

      self.lb_case_name.setText('<b>[' + self._case['id'] + ']: ' + self._case['annotator_summary'] + '</b>')

      # load default data
      for i in paraphrase_types:
         self.cb_type.addItem(i)

      if self.__edit_mode == True:
         self.setWindowTitle('Edit Annotation')
         self.label.setText('Editor:')
         self.btn_add_annotation.setText('Save')
         self.cb_type.setCurrentIndex(self.cb_type.findText(self.__annotation['phenomenon_type']))
         self.cb_projection.setCurrentIndex(self.cb_projection.findText(self.__annotation['projection']))

      self.te_susp_snippet.setText(self._case['susp_text'])
      self.te_src_snippet.setText(self._case['src_text'])

      self.lb_susp_sentence.setWordWrap(True)
      self.lb_src_sentence.setWordWrap(True)

      # signals and slots
      self.btn_add_annotation.clicked.connect(self.__add_annotation)
      self.te_susp_snippet.selectionChanged.connect(self.__susp_selection_changed)
      self.te_src_snippet.selectionChanged.connect(self.__src_selection_changed)

      #TODO: cargar los valores de los combos problem_type y text_extension despues de
      # definir los diccionarios correspondientes en TNLP_Enums_Helper
      # en el visual ELIMINAR esos valores por defecto


   def __add_annotation(self):
      """Add a new annotation"""

      case_data = {}

      #TODO: add input validation

      # get UI data
      case_data['case_id'] = self._case['id']
      case_data['author'] = str(self.le_author.text().trimmed())
      case_data['is_paraphrase'] = str('True')
      case_data['validated_by_human_beings'] = str('True')
      case_data['recognized_by_algorithms'] = str('False')
      case_data['algorithms_names'] = str('')
      case_data['annotation_date'] = str(QDate.currentDate().toString('yyyy-M-d'))
      case_data['type'] = str(self.cb_type.currentText())
      case_data['projection'] = str(self.cb_projection.currentText())
      case_data['susp_offset'] = str(self.lb_susp_offset.text())
      case_data['susp_length'] = str(self.lb_susp_length.text())
      case_data['src_offset'] = str(self.lb_src_offset.text())
      case_data['src_length'] = str(self.lb_src_length.text())

      if len(case_data['author']) == 0 or case_data['susp_length'] == '0' or case_data['src_length'] == '0':
         msg = 'Please write the author and select the suspicious and source chunks'
         if self.__edit_mode == True:
            msg = 'Please write the editor and select the suspicious and source chunks'

         QMessageBox.critical(self, self.parent().get_app_name(), 'Incorrect annotation data. ' + msg)
         return;

      if self.__edit_mode == False:
         annotation = self.__xml.add_annotation(case_data['case_id'], case_data['author'],
            case_data['is_paraphrase'], case_data['validated_by_human_beings'],
            case_data['recognized_by_algorithms'], case_data['algorithms_names'],
            case_data['annotation_date'], case_data['type'], case_data['projection'],
            case_data['susp_offset'], case_data['susp_length'], case_data['src_offset'],
            case_data['src_length'])
      else:
         annotation = self.__xml.edit_annotation(self.__annotation_index, case_data['case_id'], case_data['author'],
            case_data['is_paraphrase'], case_data['validated_by_human_beings'],
            case_data['recognized_by_algorithms'], case_data['algorithms_names'],
            case_data['annotation_date'], case_data['type'], case_data['projection'],
            case_data['susp_offset'], case_data['susp_length'], case_data['src_offset'],
            case_data['src_length'])

      if self.__edit_mode == False:
         self.parent().update_annotations_list(annotation)
         QMessageBox.information(self, self.parent().get_app_name(), u'Annotation added.')
      else:
         # use the same approach of edit case here to get the updated annotation
         self.parent().update_case_list(case_data['case_id'], True)
         QMessageBox.information(self, self.parent().get_app_name(), u'Annotation updated.')


   def __susp_selection_changed(self):
      """Handle susp selection changed"""

      self.__selection_changed(self.te_susp_snippet, self.lb_susp_sentence, self.lb_susp_offset, self.lb_susp_length)


   def __src_selection_changed(self):
      """Handle src selection changed"""

      self.__selection_changed(self.te_src_snippet, self.lb_src_sentence, self.lb_src_offset, self.lb_src_length)


   def __selection_changed(self, _text, _sentence, _offset, _len):
      """Updates components data"""

      cursor = _text.textCursor()

      txt = unicode(_text.toPlainText(),'iso8859-1')

      if len(txt) == 0:
         return

      p1 = cursor.selectionStart()
      p2 = cursor.selectionEnd()

      # set upper limit
      if p2 == len(txt): p2 -= 1

      if txt[p2] == '.':
         x = txt.rfind(' ', 0, p1)
         y = p2
      else:
         x = txt.rfind(' ', 0, p1)
         y = txt.find(' ', p2, len(txt))

      if x == -1:
         x = 0
      else:
         x += 1

      if y == -1:
         y = len(txt)

      # clear document format
      cursor.setPosition(0)
      cursor.setPosition(_text.toPlainText().length(), QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      format.setBackground(QBrush(Qt.white))
      cursor.setCharFormat(format)

      # highlight selection
      cursor.setPosition(x)
      cursor.setPosition(y, QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
      format.setUnderlineColor(QColor(Qt.red))
      font = QFont()
      font.setItalic(True)
      font.setBold(True)
      format.setFont(font)
      cursor.mergeCharFormat(format)

      cursor.clearSelection()
      cursor.movePosition(QTextCursor.Start)

      # update widgets
      _sentence.setText(txt[x:y])
      _offset.setText(str(x))
      _len.setText(str(y - x))
