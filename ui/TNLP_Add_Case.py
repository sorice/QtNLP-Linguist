#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import constant types
from TNLP_Enums_Helper import *
# convert dict to list to simplify access to values
plag_types = list(plag_types)

# import text normalization functions
from modules.TNLP_textNormalization.textMode_Functions import convertWin_Into_UnixText

# import LETTERS to calculate especial chars.
import string
LETTERS = unicode(''.join([string.letters, string.digits,'Ññ']),'iso8859-1')

try:
   _fromUtf8 = QString.fromUtf8
except AttributeError:
   def _fromUtf8(s):
      return s

class TNLP_AddCase(QWizard):
   def __init__(self, _xml_manager, parent = None):
      # init the parent
      super(TNLP_AddCase, self).__init__(parent)

      # extra data
      self.__xml = _xml_manager
      self.__working_dir = QFileInfo(self.__xml.get_xml_url()).absolutePath()

      self.setWindowTitle('Add Case')

      # setup wizard pages
      self.__setupPages()

      # optimized for 800x600
      self.resize(752, 526)

      self.setWindowModality(Qt.WindowModal)


   def __setupPages(self):
      """Configures wizard pages"""

      self.addPage(self.__create_general_page())
      self.addPage(self.__create_docs_page())


   def __create_general_page(self):
      """Creates de first page of the wizard, or the general data of a case."""

      page = QWizardPage()
      page.setSubTitle("General case data")

      gridLayout = QGridLayout()
      gridLayout.setObjectName(_fromUtf8("gridLayout"))
      horizontalLayout_10 = QHBoxLayout()
      horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
      label_20 = QLabel()
      label_20.setObjectName(_fromUtf8("label_20"))
      horizontalLayout_10.addWidget(label_20)
      lb_corpus_name = QLabel()
      lb_corpus_name.setObjectName(_fromUtf8("lb_corpus_name"))
      horizontalLayout_10.addWidget(lb_corpus_name)
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_10.addItem(spacerItem)
      gridLayout.addLayout(horizontalLayout_10, 0, 0, 1, 1)
      horizontalLayout = QHBoxLayout()
      horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
      horizontalLayout_8 = QHBoxLayout()
      horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
      verticalLayout_9 = QVBoxLayout()
      verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
      label_17 = QLabel()
      label_17.setObjectName(_fromUtf8("label_17"))
      verticalLayout_9.addWidget(label_17)
      label_18 = QLabel()
      label_18.setObjectName(_fromUtf8("label_18"))
      verticalLayout_9.addWidget(label_18)
      label_21 = QLabel()
      label_21.setObjectName(_fromUtf8("label_21"))
      verticalLayout_9.addWidget(label_21)
      label_22 = QLabel()
      label_22.setObjectName(_fromUtf8("label_22"))
      verticalLayout_9.addWidget(label_22)
      horizontalLayout_8.addLayout(verticalLayout_9)
      verticalLayout_10 = QVBoxLayout()
      verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
      cb_problem_type = QComboBox()
      cb_problem_type.setObjectName(_fromUtf8("cb_problem_type"))
      cb_problem_type.setToolTip('Tipo de problema NLP o grupo de casos en el XML.')
      verticalLayout_10.addWidget(cb_problem_type)
      le_description = QLineEdit()
      le_description.setObjectName(_fromUtf8("le_description"))
      le_description.setToolTip(unicode('Descripci\363n opcional del caso para usar como hint.','iso8859-15'))
      verticalLayout_10.addWidget(le_description)
      le_summary = QLineEdit()
      le_summary.setObjectName(_fromUtf8("le_summary"))
      le_summary.setToolTip('Escriba 3 palabras de longitud menor a 21 caracteres que podr\341 utilizar en la barra de search.')
      verticalLayout_10.addWidget(le_summary)
      le_original_corpus_id = QLineEdit()
      le_original_corpus_id.setObjectName(_fromUtf8("le_original_corpus_id"))
      le_original_corpus_id.setToolTip(unicode('Escriba solo d\355gitos.','iso8859-15'))
      verticalLayout_10.addWidget(le_original_corpus_id)
      horizontalLayout_8.addLayout(verticalLayout_10)
      horizontalLayout.addLayout(horizontalLayout_8)
      horizontalLayout_11 = QHBoxLayout()
      horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
      verticalLayout_11 = QVBoxLayout()
      verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
      label_23 = QLabel()
      label_23.setObjectName(_fromUtf8("label_23"))
      verticalLayout_11.addWidget(label_23)
      label_24 = QLabel()
      label_24.setObjectName(_fromUtf8("label_24"))
      verticalLayout_11.addWidget(label_24)
      label_25 = QLabel()
      label_25.setObjectName(_fromUtf8("label_25"))
      verticalLayout_11.addWidget(label_25)
      label_26 = QLabel()
      label_26.setObjectName(_fromUtf8("label_26"))
      verticalLayout_11.addWidget(label_26)
      horizontalLayout_11.addLayout(verticalLayout_11)
      verticalLayout_12 = QVBoxLayout()
      verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
      cb_text_extension = QComboBox()
      cb_text_extension.setObjectName(_fromUtf8("cb_text_extension"))
      cb_text_extension.setToolTip('Longitud de los textos del caso: fragmentos, oraciones u otros.')
      verticalLayout_12.addWidget(cb_text_extension)
      cb_plag_type = QComboBox()
      cb_plag_type.setObjectName(_fromUtf8("cb_plag_type"))
      cb_plag_type.setToolTip(unicode('Tipolog\355as de par\341frasis propuestas por Barr\363n-Cede\361o2013','iso8859-15'))
      verticalLayout_12.addWidget(cb_plag_type)
      le_original_corpus = QLineEdit()
      le_original_corpus.setObjectName(_fromUtf8("le_original_corpus"))
      le_original_corpus.setToolTip('Corpus original del que fue extra\355do el caso.')
      verticalLayout_12.addWidget(le_original_corpus)
      le_generator_name = QLineEdit()
      le_generator_name.setObjectName(_fromUtf8("le_generator_name"))
      le_generator_name.setToolTip(unicode('Nombre de la persona o algoritmo que cre\363 el caso.','iso8859-15'))
      verticalLayout_12.addWidget(le_generator_name)
      horizontalLayout_11.addLayout(verticalLayout_12)
      horizontalLayout.addLayout(horizontalLayout_11)
      gridLayout.addLayout(horizontalLayout, 1, 0, 1, 1)

      page.setLayout(gridLayout)

      # default labels & data
      label_20.setText("Corpus name:")
      lb_corpus_name.setText('<b>' + self.__xml.get_corpus_name() + '</b>')
      label_17.setText("Problem type:")
      label_18.setText("Description:")
      label_21.setText("Keywords:")
      label_22.setText("Original corpus id:")
      #~ cb_problem_type.setItemText(0, "similarity")
      #~ cb_problem_type.setItemText(1, "translation")
      label_23.setText("Text extension:")
      label_24.setText("Plagiarism type:")
      label_25.setText("Original corpus:")
      label_26.setText("Added by:")
      #~ cb_text_extension.setItemText(0, "paragraph")

      for i in plag_types:
         cb_plag_type.addItem(i)

      for i in text_extension:
         cb_text_extension.addItem(i)

      for i in phenomenom_types:
         cb_problem_type.addItem(i)

      # register fields, mandatory (*)
      page.registerField("problem_type", cb_problem_type)
      page.registerField("description*", le_description)
      page.registerField("summary*", le_summary)
      page.registerField("original_corpus_id*", le_original_corpus_id)
      page.registerField("text_extension", cb_text_extension)
      page.registerField("plag_type", cb_plag_type)
      page.registerField("original_corpus*", le_original_corpus)
      page.registerField("generator_name*", le_generator_name)

      return page


   def __create_docs_page(self):
      """Creates de second page of the wizard, or the data of the susp and src docs."""

      page = QWizardPage()
      page.setSubTitle("Select suspicious and source documents")

      gridLayout = QGridLayout()
      gridLayout.setObjectName(_fromUtf8("gridLayout"))
      horizontalLayout = QHBoxLayout()
      horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
      btn_select_susp_doc = QPushButton()
      btn_select_susp_doc.setObjectName(_fromUtf8("btn_select_susp_doc"))
      horizontalLayout.addWidget(btn_select_susp_doc)
      label_9 = QLabel()
      label_9.setObjectName(_fromUtf8("label_9"))
      horizontalLayout.addWidget(label_9)
      lb_susp_doc_name = QLabel()
      lb_susp_doc_name.setObjectName(_fromUtf8("lb_susp_doc_name"))
      horizontalLayout.addWidget(lb_susp_doc_name)
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout.addItem(spacerItem)
      gridLayout.addLayout(horizontalLayout, 0, 0, 1, 1)
      horizontalLayout_2 = QHBoxLayout()
      horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
      label_10 = QLabel()
      label_10.setObjectName(_fromUtf8("label_10"))
      horizontalLayout_2.addWidget(label_10)
      lb_susp_offset = QLabel()
      lb_susp_offset.setObjectName(_fromUtf8("lb_susp_offset"))
      horizontalLayout_2.addWidget(lb_susp_offset)
      label_11 = QLabel()
      label_11.setObjectName(_fromUtf8("label_11"))
      horizontalLayout_2.addWidget(label_11)
      lb_susp_length = QLabel()
      lb_susp_length.setObjectName(_fromUtf8("lb_susp_length"))
      horizontalLayout_2.addWidget(lb_susp_length)
      label_12 = QLabel()
      label_12.setObjectName(_fromUtf8("label_12"))
      horizontalLayout_2.addWidget(label_12)
      lb_susp_sentences_count = QLabel()
      lb_susp_sentences_count.setObjectName(_fromUtf8("lb_susp_sentences_count"))
      horizontalLayout_2.addWidget(lb_susp_sentences_count)
      spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_2.addItem(spacerItem1)
      gridLayout.addLayout(horizontalLayout_2, 1, 0, 1, 1)
      te_susp_text = QTextEdit()
      te_susp_text.setReadOnly(True)
      te_susp_text.setObjectName(_fromUtf8("te_susp_text"))
      gridLayout.addWidget(te_susp_text, 2, 0, 1, 1)
      horizontalLayout_4 = QHBoxLayout()
      horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
      btn_select_src_doc = QPushButton()
      btn_select_src_doc.setObjectName(_fromUtf8("btn_select_src_doc"))
      horizontalLayout_4.addWidget(btn_select_src_doc)
      label_16 = QLabel()
      label_16.setObjectName(_fromUtf8("label_16"))
      horizontalLayout_4.addWidget(label_16)
      lb_src_doc_name = QLabel()
      lb_src_doc_name.setObjectName(_fromUtf8("lb_src_doc_name"))
      horizontalLayout_4.addWidget(lb_src_doc_name)
      spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_4.addItem(spacerItem2)
      gridLayout.addLayout(horizontalLayout_4, 3, 0, 1, 1)
      horizontalLayout_3 = QHBoxLayout()
      horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
      label_13 = QLabel()
      label_13.setObjectName(_fromUtf8("label_13"))
      horizontalLayout_3.addWidget(label_13)
      lb_src_offset = QLabel()
      lb_src_offset.setObjectName(_fromUtf8("lb_src_offset"))
      horizontalLayout_3.addWidget(lb_src_offset)
      label_14 = QLabel()
      label_14.setObjectName(_fromUtf8("label_14"))
      horizontalLayout_3.addWidget(label_14)
      lb_src_length = QLabel()
      lb_src_length.setObjectName(_fromUtf8("lb_src_length"))
      horizontalLayout_3.addWidget(lb_src_length)
      label_15 = QLabel()
      label_15.setObjectName(_fromUtf8("label_15"))
      horizontalLayout_3.addWidget(label_15)
      lb_src_sentences_count = QLabel()
      lb_src_sentences_count.setObjectName(_fromUtf8("lb_src_sentences_count"))
      horizontalLayout_3.addWidget(lb_src_sentences_count)
      spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_3.addItem(spacerItem3)
      gridLayout.addLayout(horizontalLayout_3, 4, 0, 1, 1)
      te_src_text = QTextEdit()
      te_src_text.setReadOnly(True)
      te_src_text.setObjectName(_fromUtf8("te_src_text"))
      gridLayout.addWidget(te_src_text, 5, 0, 1, 1)

      page.setLayout(gridLayout)

      # default labels & data
      btn_select_susp_doc.setText("Select susp doc")
      label_9.setText("Doc name:")
      lb_susp_doc_name.setText("susp/")
      label_10.setText("Offset:")
      lb_susp_offset.setText("0")
      label_11.setText("Length:")
      lb_susp_length.setText("0")
      label_12.setText("Sentences:")
      lb_susp_sentences_count.setText("0")
      btn_select_src_doc.setText("Select src doc")
      label_16.setText("Doc name:")
      lb_src_doc_name.setText("src/")
      label_13.setText("Offset:")
      lb_src_offset.setText("0")
      label_14.setText("Length:")
      lb_src_length.setText("0")
      label_15.setText("Sentences:")
      lb_src_sentences_count.setText("0")

      # register fields, mandatory (*)
      page.registerField("susp_doc_name", lb_susp_doc_name)
      page.registerField("lb_susp_doc_name", lb_susp_doc_name)
      page.registerField("susp_offset", lb_susp_offset)
      page.registerField("susp_length", lb_susp_length)
      page.registerField("susp_sentences_count", lb_susp_sentences_count)
      page.registerField("susp_text", te_susp_text)
      page.registerField("src_doc_name", lb_src_doc_name)
      page.registerField("src_offset", lb_src_offset)
      page.registerField("src_length", lb_src_length)
      page.registerField("src_sentences_count", lb_src_sentences_count)
      page.registerField("src_text", te_src_text)

      # connect signals & slots
      btn_select_susp_doc.clicked.connect(self.__select_susp_doc)
      btn_select_src_doc.clicked.connect(self.__select_src_doc)
      te_susp_text.textChanged.connect(self.__susp_text_changed)
      te_src_text.textChanged.connect(self.__src_text_changed)
      te_susp_text.selectionChanged.connect(self.__susp_selection_changed)
      te_src_text.selectionChanged.connect(self.__src_selection_changed)

      return page


   def accept(self):
      """Process the wizard data and adds the case to corpus"""

      # get wizard data
      '''problem_type = phenomenom_types[self.field("problem_type").toInt()[0]]
      description = str(self.field("description").toString())
      summary = str(self.field("summary").toString())
      original_corpus_id = str(self.field("original_corpus_id").toString())
      txt_extension = text_extension[self.field("text_extension").toInt()[0]]
      plag_type = plag_types[self.field("plag_type").toInt()[0]]
      original_corpus = str(self.field("original_corpus").toString())
      generator_name = str(self.field("generator_name").toString())
      susp_doc_name = str(self.field("susp_doc_name").toString())
      susp_offset = str(self.field("susp_offset").toInt()[0])
      susp_length = str(self.field("susp_length").toInt()[0])
      susp_sentences_count = str(self.field("susp_sentences_count").toInt()[0])
      susp_text = str(self.field("susp_text").toString())
      src_doc_name = str(self.field("src_doc_name").toString())
      src_offset = str(self.field("src_offset").toInt()[0])
      src_length = str(self.field("src_length").toInt()[0])
      src_sentences_count = str(self.field("src_sentences_count").toInt()[0])
      src_text = str(self.field("src_text").toString())'''

      # some widgets report empty strings, so obtain values using QObjetc.findChild instead
      problem_type = str(self.page(0).findChild(QComboBox, 'cb_problem_type').currentText())
      description = str(self.page(0).findChild(QLineEdit, 'le_description').text()).strip()
      annotator_summary = str(self.page(0).findChild(QLineEdit, 'le_summary').text()).strip()
      original_corpus_id = str(self.page(0).findChild(QLineEdit, 'le_original_corpus_id').text()).strip()
      text_extension = str(self.page(0).findChild(QComboBox, 'cb_text_extension').currentText())
      plag_type = str(self.page(0).findChild(QComboBox, 'cb_plag_type').currentText())
      original_corpus = str(self.page(0).findChild(QLineEdit, 'le_original_corpus').text()).strip()
      generator_name = str(self.page(0).findChild(QLineEdit, 'le_generator_name').text()).strip()
      susp_doc = str(self.page(1).findChild(QLabel, 'lb_susp_doc_name').text()).strip()
      susp_offset = str(self.page(1).findChild(QLabel, 'lb_susp_offset').text()).strip()
      susp_length = str(self.page(1).findChild(QLabel, 'lb_susp_length').text()).strip()
      susp_sentences_count = str(self.page(1).findChild(QLabel, 'lb_susp_sentences_count').text()).strip()
      susp_text = unicode(self.page(1).findChild(QTextEdit, 'te_susp_text').toPlainText(), 'iso8859-1')
      src_doc = str(self.page(1).findChild(QLabel, 'lb_src_doc_name').text()).strip()
      src_offset = str(self.page(1).findChild(QLabel, 'lb_src_offset').text()).strip()
      src_length = str(self.page(1).findChild(QLabel, 'lb_src_length').text()).strip()
      src_sentences_count = str(self.page(1).findChild(QLabel, 'lb_src_sentences_count').text()).strip()
      src_text = unicode(self.page(1).findChild(QTextEdit, 'te_src_text').toPlainText(), 'iso8859-1')
      automatic_summary = ""
      generated_by = "human"

      #~ print problem_type, description, annotator_summary, original_corpus_id, text_extension, plag_type, original_corpus, generator_name, susp_doc_name, susp_offset, susp_length, susp_sentences_count, susp_text, src_doc_name, src_offset, src_length, src_sentences_count, src_text
      # validate data
      if susp_text == '' or susp_length == '0' or susp_sentences_count == '0':
         QMessageBox.critical(self, self.parent().get_app_name(), 'Incorrect suspicious data. Please select a suspicious file and snippet.')
         return
      else:
         if src_text == '' or src_length == '0' or src_sentences_count == '0':
            QMessageBox.critical(self, self.parent().get_app_name(), 'Incorrect source data. Please select a source file and snippet.')
            return

      new_case_id = self.__xml.add_case(problem_type, text_extension, description, plag_type, annotator_summary,
         automatic_summary, original_corpus, original_corpus_id, generated_by, generator_name, susp_doc, susp_offset,
         susp_length, susp_sentences_count, src_doc, src_offset, src_length, src_sentences_count)

      self.__xml.write_xml()

      self.parent().update_case_list(new_case_id)

      QMessageBox.information(self, self.parent().get_app_name(), u'Case added.')

      self.close()


   def __select_susp_doc(self):
      """Helper function"""

      susp_doc_name = self.page(1).findChild(QLabel, 'lb_susp_doc_name')
      susp_text = self.page(1).findChild(QTextEdit, 'te_susp_text')

      _file = QFileDialog.getOpenFileName(self, u"Select suspicious file", self.__working_dir, u"Text files (*.txt)")

      if not _file:
         QMessageBox.critical(self, self.parent().get_app_name(), 'Operation canceled.')
         return

      if not _file.startsWith(self.__working_dir):
         QMessageBox.critical(self, self.parent().get_app_name(), 'Suspicious files must be relative to case file, located in:\n' + self.__working_dir)
         return

      f = QFile(_file)
      if not f.exists():
         QMessageBox.critical(self, self.parent().get_app_name(), 'Invalid file.')
         return
      
      convertWin_Into_UnixText(self, _file)
      
      f = QFile(_file)
      if f.open(QFile.ReadOnly):
         _txt = open(_file).read()
         _text = unicode(_txt,'utf8')
         susp_text.setText(_text)

         _dir = _file.right(_file.length() - QString(self.__working_dir).length())
         _dir = _dir.remove(0, 1)
         _dir.chop(4)

         susp_doc_name.setText(_dir)
      else:
         QMessageBox.critical(self, self.parent().get_app_name(), 'Error opening file.')


   def __select_src_doc(self):
      """Helper function"""

      src_doc_name = self.page(1).findChild(QLabel, 'lb_src_doc_name')
      src_text = self.page(1).findChild(QTextEdit, 'te_src_text')

      _file = QFileDialog.getOpenFileName(self, u"Select source file", self.__working_dir, u"Text files (*.txt)")

      if not _file:
         QMessageBox.critical(self, self.parent().get_app_name(), 'Operation canceled.')
         return

      if not _file.startsWith(self.__working_dir):
         QMessageBox.critical(self, self.parent().get_app_name(), 'Source files must be relative to case file, located in:\n' + self.__working_dir)
         return

      f = QFile(_file)
      if not f.exists():
         QMessageBox.critical(self, self.parent().get_app_name(), 'Invalid file.')
         return
      
      convertWin_Into_UnixText(self, _file)
      
      f = QFile(_file)
      if f.open(QFile.ReadOnly):
         _txt = open(_file).read()
         _text = unicode(_txt,'utf8')
         src_text.setText(_text)

         _dir = _file.right(_file.length() - QString(self.__working_dir).length())
         _dir = _dir.remove(0, 1)
         _dir.chop(4)

         src_doc_name.setText(_dir)
      else:
         QMessageBox.critical(self, self.parent().get_app_name(), 'Error opening file.')


   def __susp_text_changed(self):
      """Handle susp text changed"""

      # locate working elements
      _text = self.page(1).findChild(QTextEdit, 'te_susp_text')
      _offset = self.page(1).findChild(QLabel, 'lb_susp_offset')
      _len = self.page(1).findChild(QLabel, 'lb_susp_length')
      _sentences = self.page(1).findChild(QLabel, 'lb_susp_sentences_count')

      self.__text_changed(_text, _offset, _len, _sentences)


   def __src_text_changed(self):
      """Handle src text changed"""

      # locate working elements
      _text = self.page(1).findChild(QTextEdit, 'te_src_text')
      _offset = self.page(1).findChild(QLabel, 'lb_src_offset')
      _len = self.page(1).findChild(QLabel, 'lb_src_length')
      _sentences = self.page(1).findChild(QLabel, 'lb_src_sentences_count')

      self.__text_changed(_text, _offset, _len, _sentences)


   def __text_changed(self, _text_cmp, _offset, _len, _sentences):
      """Updates components data"""

      _text_cmp.textCursor().clearSelection()
      _text_cmp.textCursor().movePosition(QTextCursor.Start)

      _offset.setText('0')
      _len.setText('0')
      _sentences.setText('0')


   def __susp_selection_changed(self):
      """Handle susp text changed"""

      # locate working elements
      _text = self.page(1).findChild(QTextEdit, 'te_susp_text')
      #~ print 'type _text __susp_selection_changed', type(_text)

      _offset = self.page(1).findChild(QLabel, 'lb_susp_offset')
      _len = self.page(1).findChild(QLabel, 'lb_susp_length')
      _sentences = self.page(1).findChild(QLabel, 'lb_susp_sentences_count')

      self.__selection_changed(_text, _offset, _len, _sentences)


   def __src_selection_changed(self):
      """Handle src text changed"""

      # locate working elements
      _text = self.page(1).findChild(QTextEdit, 'te_src_text')
      #~ print 'type _text __src_selection_changed', type(_text)
      _offset = self.page(1).findChild(QLabel, 'lb_src_offset')
      _len = self.page(1).findChild(QLabel, 'lb_src_length')
      _sentences = self.page(1).findChild(QLabel, 'lb_src_sentences_count')

      self.__selection_changed(_text, _offset, _len, _sentences)


   def __selection_changed(self, _text_cmp, _offset, _len, _sentences):
      """Updates components data"""

      cursor = _text_cmp.textCursor()
      
      txt = unicode(_text_cmp.toPlainText(),'iso8859-1')

      if len(txt) == 0:
         return
      p1 = cursor.selectionStart()
      p2 = cursor.selectionEnd()
      
      # set upper limit
      if p2 == len(txt): p2 -= 1

      if txt[p2] == '.':
         y = p2
      else:
         y = txt.find('.', p2, len(txt))

      # Find first letter char of the sentence. Avoid PlainText problems.
      x_temp = txt.rfind('.', 0, p1)
      while txt[x_temp] not in LETTERS:
         x = x_temp+1
         x_temp+=1

      if x == -1:
         x = 0

      if y == -1:
         y = len(txt)
      else:
         y += 1

      # clear document format
      cursor.setPosition(0)
      cursor.setPosition(_text_cmp.toPlainText().length(), QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      format.setBackground(QBrush(Qt.white))
      cursor.setCharFormat(format)

      # highlight selection
      cursor.setPosition(x)
      cursor.setPosition(y, QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      format.setBackground(QBrush(Qt.green))
      cursor.mergeCharFormat(format)

      cursor.clearSelection()
      cursor.movePosition(QTextCursor.Start)
      
      #~ print 'len txt __selection_changed:', txt[x:y], ',', len(txt[x:y])

      # update widgets
      _offset.setText(str(x))
      _len.setText(str(y - x))
      _sentences.setText(str(len(txt[x:y].split(".")) - 1))
