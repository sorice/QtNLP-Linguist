#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.TNLP_MW_UI import Ui_ToNgueLP_MW

# import reader
#from modules.TNLP_corpus import XML_read
from modules.TNLP_corpus.TNLP_XML_Manager import TNLP_XML_Manager

# import constant types
from TNLP_Enums_Helper import plag_types

# import Case Tab helper
from TNLP_Cases_Tab import TNLP_CaseTab

# import Add Case helper
from TNLP_Add_Case import TNLP_AddCase

# import Add Annotation helper
from TNLP_Add_Annotation import TNLP_AddAnnotation

# import New Corpus helper
from TNLP_New_Corpus import TNLP_NewCorpus

try:
   _fromUtf8 = QString.fromUtf8
except AttributeError:
   def _fromUtf8(s):
      return s

class TNLP_MW(QMainWindow, Ui_ToNgueLP_MW):
   def __init__(self, _name, _version, parent = None):
      # init the parent
      super(TNLP_MW, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # remove in the future
      self.toolBar_Cases.setDisabled(True)

      # some attributes
      self.__appName = _name
      self.__appVersion = _version

      # readers list
      self.__corpus_list = []

      self.__reader = None

      # extra config
      self.showMaximized()
      self.setWindowTitle(self.__appName + ' - ' + self.__appVersion)

      # signals and slots
      self.actionLoad_New_Corpus.triggered.connect(self.load_new_corpus)
      self.actionCorpus_Information.triggered.connect(self.show_corpus_info)
      self.actionClose_Corpus.triggered.connect(self.close_corpus)
      self.actionExit.triggered.connect(self.close)
      self.actionAdd_New_Case.triggered.connect(self.__add_case)
      self.actionAdd_annotation.triggered.connect(self.__add_annotation)
      self.actionCreate_Corpus.triggered.connect(self.__create_corpus)


   def get_app_name(self):
      '''Return AppName'''

      return self.__appName


   def __create_new_corpus_tab(self):
      """Create an empty new tab for corpus"""

      tab = QWidget()
      # left area
      gridLayout_3 = QGridLayout(tab)
      frame = QFrame(tab)
      frame.setMinimumSize(QSize(216, 0))
      frame.setMaximumSize(QSize(216, 16777215))
      gridLayout_2 = QGridLayout(frame)
      # search case
      verticalLayout = QVBoxLayout()
      verticalLayout.setSpacing(0)
      searchCase = QLineEdit(frame)
      searchCase.setMinimumSize(QSize(200, 0))
      searchCase.setMaximumSize(QSize(200, 16777215))
      searchCase.setPlaceholderText("Search case?")
      verticalLayout.addWidget(searchCase)
      # slot
      searchCase.returnPressed.connect(self.__searchCase)
      #
      # cases list
      casesList = QListWidget(frame)
      casesList.setMinimumSize(QSize(200, 0))
      casesList.setMaximumSize(QSize(200, 16777215))
      casesList.setEditTriggers(QAbstractItemView.NoEditTriggers)
      verticalLayout.addWidget(casesList)
      # slot
      casesList.currentItemChanged.connect(self.__get_case)
      casesList.itemClicked.connect(self.__get_case)
      #
      # total cases
      horizontalLayout = QHBoxLayout()
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout.addItem(spacerItem)
      casesCount = QLabel(frame)
      horizontalLayout.addWidget(casesCount)
      spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout.addItem(spacerItem1)
      verticalLayout.addLayout(horizontalLayout)
      gridLayout_2.addLayout(verticalLayout, 0, 0, 1, 1)
      gridLayout_3.addWidget(frame, 0, 0, 1, 1)
      casesWorkingArea = QTabWidget(tab)
      casesWorkingArea.setMovable(True)
      # slot
      casesWorkingArea.currentChanged.connect(self.__update_selected_case)
      #
      #tab_2 = QWidget()
      #casesWorkingArea.addTab(tab_2, _fromUtf8("Compare"))
      gridLayout_3.addWidget(casesWorkingArea, 0, 1, 1, 1)

      # global layout update
      self.gridLayout.addWidget(self.corpusTabs, 0, 1, 1, 1)

      casesWorkingArea.setTabsClosable(True)
      casesWorkingArea.tabCloseRequested.connect(self.__closeCaseTab)

      return tab


   def __create_new_case_tab(self):
      """Create a new case tab for current corpus"""

      # right area
      #tab_1 = QWidget()
      tab_1 = TNLP_CaseTab()

      gridLayout = QGridLayout(tab_1)
      gridLayout.setObjectName(_fromUtf8("gridLayout"))
      horizontalLayout = QHBoxLayout()
      horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
      verticalLayout_2 = QVBoxLayout()
      verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
      label_4 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_4.setFont(font)
      label_4.setAlignment(Qt.AlignCenter)
      label_4.setObjectName(_fromUtf8("label_4"))
      verticalLayout_2.addWidget(label_4)
      lb_note_id = QLabel(tab_1)
      lb_note_id.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_id.setObjectName(_fromUtf8("lb_note_id"))
      verticalLayout_2.addWidget(lb_note_id)
      horizontalLayout.addLayout(verticalLayout_2)
      line_7 = QFrame(tab_1)
      line_7.setFrameShape(QFrame.VLine)
      line_7.setFrameShadow(QFrame.Sunken)
      line_7.setObjectName(_fromUtf8("line_7"))
      horizontalLayout.addWidget(line_7)
      verticalLayout_3 = QVBoxLayout()
      verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
      label_5 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_5.setFont(font)
      label_5.setAlignment(Qt.AlignCenter)
      label_5.setObjectName(_fromUtf8("label_5"))
      verticalLayout_3.addWidget(label_5)
      lb_note_type = QLabel(tab_1)
      lb_note_type.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_type.setObjectName(_fromUtf8("lb_note_type"))
      verticalLayout_3.addWidget(lb_note_type)
      horizontalLayout.addLayout(verticalLayout_3)
      line_8 = QFrame(tab_1)
      line_8.setFrameShape(QFrame.VLine)
      line_8.setFrameShadow(QFrame.Sunken)
      line_8.setObjectName(_fromUtf8("line_8"))
      horizontalLayout.addWidget(line_8)
      verticalLayout_4 = QVBoxLayout()
      verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
      label_6 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_6.setFont(font)
      label_6.setAlignment(Qt.AlignCenter)
      label_6.setObjectName(_fromUtf8("label_6"))
      verticalLayout_4.addWidget(label_6)
      lb_note_projection = QLabel(tab_1)
      lb_note_projection.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_projection.setObjectName(_fromUtf8("lb_note_projection"))
      verticalLayout_4.addWidget(lb_note_projection)
      horizontalLayout.addLayout(verticalLayout_4)
      line_9 = QFrame(tab_1)
      line_9.setFrameShape(QFrame.VLine)
      line_9.setFrameShadow(QFrame.Sunken)
      line_9.setObjectName(_fromUtf8("line_9"))
      horizontalLayout.addWidget(line_9)
      verticalLayout_5 = QVBoxLayout()
      verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
      label_7 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_7.setFont(font)
      label_7.setAlignment(Qt.AlignCenter)
      label_7.setObjectName(_fromUtf8("label_7"))
      verticalLayout_5.addWidget(label_7)
      lb_note_susp = QLabel(tab_1)
      lb_note_susp.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_susp.setObjectName(_fromUtf8("lb_note_susp"))
      verticalLayout_5.addWidget(lb_note_susp)
      horizontalLayout.addLayout(verticalLayout_5)
      line_10 = QFrame(tab_1)
      line_10.setFrameShape(QFrame.VLine)
      line_10.setFrameShadow(QFrame.Sunken)
      line_10.setObjectName(_fromUtf8("line_10"))
      horizontalLayout.addWidget(line_10)
      verticalLayout_6 = QVBoxLayout()
      verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
      label_8 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_8.setFont(font)
      label_8.setAlignment(Qt.AlignCenter)
      label_8.setObjectName(_fromUtf8("label_8"))
      verticalLayout_6.addWidget(label_8)
      lb_note_src = QLabel(tab_1)
      lb_note_src.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_src.setObjectName(_fromUtf8("lb_note_src"))
      verticalLayout_6.addWidget(lb_note_src)
      horizontalLayout.addLayout(verticalLayout_6)
      line_11 = QFrame(tab_1)
      line_11.setFrameShape(QFrame.VLine)
      line_11.setFrameShadow(QFrame.Sunken)
      line_11.setObjectName(_fromUtf8("line_11"))
      horizontalLayout.addWidget(line_11)
      verticalLayout_7 = QVBoxLayout()
      verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
      label_9 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_9.setFont(font)
      label_9.setAlignment(Qt.AlignCenter)
      label_9.setObjectName(_fromUtf8("label_9"))
      verticalLayout_7.addWidget(label_9)
      lb_note_author = QLabel(tab_1)
      lb_note_author.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_author.setObjectName(_fromUtf8("lb_note_author"))
      verticalLayout_7.addWidget(lb_note_author)
      horizontalLayout.addLayout(verticalLayout_7)
      line_12 = QFrame(tab_1)
      line_12.setFrameShape(QFrame.VLine)
      line_12.setFrameShadow(QFrame.Sunken)
      line_12.setObjectName(_fromUtf8("line_12"))
      horizontalLayout.addWidget(line_12)
      verticalLayout_8 = QVBoxLayout()
      verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
      label_10 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_10.setFont(font)
      label_10.setAlignment(Qt.AlignCenter)
      label_10.setObjectName(_fromUtf8("label_10"))
      verticalLayout_8.addWidget(label_10)
      lb_note_date = QLabel(tab_1)
      lb_note_date.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_date.setObjectName(_fromUtf8("lb_note_date"))
      verticalLayout_8.addWidget(lb_note_date)
      horizontalLayout.addLayout(verticalLayout_8)
      line_13 = QFrame(tab_1)
      line_13.setFrameShape(QFrame.VLine)
      line_13.setFrameShadow(QFrame.Sunken)
      line_13.setObjectName(_fromUtf8("line_13"))
      horizontalLayout.addWidget(line_13)
      verticalLayout_9 = QVBoxLayout()
      verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
      label_11 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_11.setFont(font)
      label_11.setAlignment(Qt.AlignCenter)
      label_11.setObjectName(_fromUtf8("label_11"))
      verticalLayout_9.addWidget(label_11)
      lb_note_human_val = QLabel(tab_1)
      lb_note_human_val.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_human_val.setObjectName(_fromUtf8("lb_note_human_val"))
      verticalLayout_9.addWidget(lb_note_human_val)
      horizontalLayout.addLayout(verticalLayout_9)
      line_14 = QFrame(tab_1)
      line_14.setFrameShape(QFrame.VLine)
      line_14.setFrameShadow(QFrame.Sunken)
      line_14.setObjectName(_fromUtf8("line_14"))
      horizontalLayout.addWidget(line_14)
      verticalLayout_10 = QVBoxLayout()
      verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
      label_12 = QLabel(tab_1)
      font = QFont()
      font.setBold(True)
      font.setWeight(75)
      label_12.setFont(font)
      label_12.setAlignment(Qt.AlignCenter)
      label_12.setObjectName(_fromUtf8("label_12"))
      verticalLayout_10.addWidget(label_12)
      lb_note_machine_recog = QLabel(tab_1)
      lb_note_machine_recog.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_note_machine_recog.setObjectName(_fromUtf8("lb_note_machine_recog"))
      verticalLayout_10.addWidget(lb_note_machine_recog)
      horizontalLayout.addLayout(verticalLayout_10)
      gridLayout.addLayout(horizontalLayout, 6, 0, 1, 1)
      verticalLayout_13 = QVBoxLayout()
      verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
      lb_src_info = QLabel(tab_1)
      lb_src_info.setObjectName(_fromUtf8("lb_src_info"))
      verticalLayout_13.addWidget(lb_src_info)
      text_src = QTextEdit(tab_1)
      text_src.setReadOnly(True)
      text_src.setObjectName(_fromUtf8("text_src"))
      verticalLayout_13.addWidget(text_src)
      gridLayout.addLayout(verticalLayout_13, 10, 0, 1, 1)
      horizontalLayout_2 = QHBoxLayout()
      horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_2.addItem(spacerItem)
      btn_prev_note = QPushButton(tab_1)
      btn_prev_note.setObjectName(_fromUtf8("btn_prev_note"))
      horizontalLayout_2.addWidget(btn_prev_note)
      lb_note_current = QLabel(tab_1)
      lb_note_current.setObjectName(_fromUtf8("lb_note_current"))
      horizontalLayout_2.addWidget(lb_note_current)
      label_3 = QLabel(tab_1)
      label_3.setObjectName(_fromUtf8("label_3"))
      horizontalLayout_2.addWidget(label_3)
      lb_note_count = QLabel(tab_1)
      lb_note_count.setObjectName(_fromUtf8("lb_note_count"))
      horizontalLayout_2.addWidget(lb_note_count)
      btn_next_note = QPushButton(tab_1)
      btn_next_note.setObjectName(_fromUtf8("btn_next_note"))
      horizontalLayout_2.addWidget(btn_next_note)
      spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_2.addItem(spacerItem1)
      gridLayout.addLayout(horizontalLayout_2, 8, 0, 1, 1)
      ###line_2 = QFrame(tab_1)
      ###line_2.setFrameShape(QFrame.HLine)
      ###line_2.setFrameShadow(QFrame.Sunken)
      ###line_2.setObjectName(_fromUtf8("line_2"))
      ###gridLayout.addWidget(line_2, 5, 0, 1, 1)
      horizontalLayout_3 = QHBoxLayout()
      horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
      spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_3.addItem(spacerItem2)
      label_2 = QLabel(tab_1)
      label_2.setObjectName(_fromUtf8("label_2"))
      horizontalLayout_3.addWidget(label_2)
      spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_3.addItem(spacerItem3)
      gridLayout.addLayout(horizontalLayout_3, 2, 0, 1, 1)
      verticalLayout_12 = QVBoxLayout()
      verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
      case_details = QLabel(tab_1)
      case_details.setObjectName(_fromUtf8("case_details"))
      verticalLayout_12.addWidget(case_details)
      line_5 = QFrame(tab_1)
      line_5.setFrameShape(QFrame.HLine)
      line_5.setFrameShadow(QFrame.Sunken)
      line_5.setObjectName(_fromUtf8("line_5"))
      verticalLayout_12.addWidget(line_5)
      lb_susp_info = QLabel(tab_1)
      lb_susp_info.setObjectName(_fromUtf8("lb_susp_info"))
      verticalLayout_12.addWidget(lb_susp_info)
      text_susp = QTextEdit(tab_1)
      text_susp.setObjectName(_fromUtf8("text_susp"))
      text_susp.setReadOnly(True)
      verticalLayout_12.addWidget(text_susp)
      gridLayout.addLayout(verticalLayout_12, 0, 0, 1, 1)
      line_4 = QFrame(tab_1)
      line_4.setFrameShape(QFrame.HLine)
      line_4.setFrameShadow(QFrame.Sunken)
      line_4.setObjectName(_fromUtf8("line_4"))
      gridLayout.addWidget(line_4, 9, 0, 1, 1)
      verticalLayout = QVBoxLayout()
      verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
      ###lb_susp_sentence = QLabel(tab_1)
      ###lb_susp_sentence.setObjectName(_fromUtf8("lb_susp_sentence"))
      ###verticalLayout.addWidget(lb_susp_sentence)
      ###lb_src_sentence = QLabel(tab_1)
      ###lb_src_sentence.setObjectName(_fromUtf8("lb_src_sentence"))
      ###verticalLayout.addWidget(lb_src_sentence)
      gridLayout.addLayout(verticalLayout, 4, 0, 1, 1)
      ###line_3 = QFrame(tab_1)
      ###line_3.setFrameShape(QFrame.HLine)
      ###line_3.setFrameShadow(QFrame.Sunken)
      ###line_3.setObjectName(_fromUtf8("line_3"))
      ###gridLayout.addWidget(line_3, 1, 0, 1, 1)
      ###line = QFrame(tab_1)
      ###line.setFrameShape(QFrame.HLine)
      ###line.setFrameShadow(QFrame.Sunken)
      ###line.setObjectName(_fromUtf8("line"))
      ###gridLayout.addWidget(line, 3, 0, 1, 1)
      ###line_6 = QFrame(tab_1)
      ###line_6.setFrameShape(QFrame.HLine)
      ###line_6.setFrameShadow(QFrame.Sunken)
      ###line_6.setObjectName(_fromUtf8("line_6"))
      ###gridLayout.addWidget(line_6, 7, 0, 1, 1)

      # set default values
      lb_susp_info.setText("<b>Suspicious</b>]&nbsp;&nbsp;&nbsp;id = <b>000</b>, doc-name = <b>susp-1111</b>, length = <b>555</b> char(s), offset = <b>10</b>")
      text_susp.setText("Texto sospechoso")
      #label_2.setText("<b>Annotations</b>")
      ###lb_susp_sentence.setText("Susp Sentence")
      ###lb_src_sentence.setText("Src Sentence")
      label_4.setText("ID")
      lb_note_id.setText("1")
      label_5.setText("Type")
      lb_note_type.setText("Same Polarity")
      label_6.setText("Projection")
      lb_note_projection.setText("Local")
      label_7.setText("Susp\nOffset / Len")
      lb_note_susp.setText("10")
      label_8.setText("Src\nOffset / Len")
      lb_note_src.setText("50")
      label_9.setText("Author")
      lb_note_author.setText("Leonel")
      label_10.setText("Date")
      lb_note_date.setText("07-04-2015")
      label_11.setText("Validated\nby Humans")
      lb_note_human_val.setText("True")
      label_12.setText("Artificially\nRecognized")
      lb_note_machine_recog.setText("False")
      btn_prev_note.setText("Prev")
      btn_next_note.setText("Next")
      lb_src_info.setText("<b>Source</b>]&nbsp;&nbsp;&nbsp;id = <b>000</b>, doc-name = <b>src-1111</b>, length = <b>555</b> char(s), offset = <b>10</b>")
      text_src.setText("Texto fuente")
      lb_note_current.setText("#")
      label_3.setText("/")
      lb_note_count.setText("Total")

      # shortcut
      QShortcut(Qt.CTRL + Qt.Key_W, tab_1, self.__ctrl_w)

      return tab_1


   def __ctrl_w(self):
      """Close current tab when CTRL+W is pressed"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab
      # close current tab
      self.__closeCaseTab(__cases.currentIndex())


   def load_new_corpus(self):
      """Load a new corpus"""

      # select corpus file
      xml_file = QFileDialog.getOpenFileName(self, u"Select corpus file", "", u"Corpus XML file (*.xml)")

      if not xml_file:
         QMessageBox.critical(self, self.__appName, 'Operation canceled.')
         return

      if not QFile.exists(xml_file):
         QMessageBox.critical(self, self.__appName, 'Invalid file.')
         return

      xml_file = str(xml_file)

      # parser instance
      __reader = TNLP_XML_Manager()

      if __reader.parse_xml(xml_file):
         # corpus already loaded?
         __corpus_names = []
         for i in self.__corpus_list:
            __corpus_names.append(i.get_corpus_name())
         if __reader.get_corpus_name() in __corpus_names:
            QMessageBox.critical(self, self.__appName, 'Corpus <b>' + __reader.get_corpus_name() + ' </b>already loaded.')
            return

         # add a new tab for corpus
         tab = self.__create_new_corpus_tab()
         _cases_list = tab.children()[1].children()[2] # cases list
         _total_lb = tab.children()[1].children()[3] # total cases
         self.corpusTabs.addTab(tab, QString(__reader.get_corpus_name()))

         # create cases list
         for case in __reader.get_cases():
            listItem = QListWidgetItem(QIcon(plag_types[case['plag_type']][0]), QString("[" + case['id'] + "]: " + case['annotator_summary']))
            # data: list(index, plag_type_rgb_color)
            listItem.setData(Qt.UserRole, [case['id'], plag_types[case['plag_type']][1]])
            _cases_list.addItem(listItem)

         _total_lb.setText(QString('Total cases: <b>%1</b>').arg(__reader.get_corpus_total_cases()))
         self.__corpus_list.append(__reader)

         QMessageBox.information(self, self.__appName, 'Corpus loaded.')
      else:
         QMessageBox.critical(self, self.__appName, 'Error parsing corpus.')


   def __get_case(self, _current, _old = None):
      """Return case"""

      # TODO: refactorize
      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab

      # case already loaded? activate case tab
      tmp_cases = []
      for i in range(__cases.count()):
         tmp_cases.append(__cases.tabText(i))
      if _current.text() in tmp_cases:
         __cases.setCurrentIndex(tmp_cases.index(_current.text()))
         return

      case_data = _current.data(Qt.UserRole).toList()
      case_id = int(case_data[0].toString())
      case = self.__corpus_list[self.corpusTabs.currentIndex()].get_case_by_id(case_id)
      annotations = self.__corpus_list[self.corpusTabs.currentIndex()].get_annotations_of_case(case_id)

      case_tab = self.__create_new_case_tab()
      # save extra data
      index = -1
      if len(annotations) > 0: index = 0
      case_tab.set_case_data(case, annotations, index)

      __cases.addTab(case_tab, _current.text())
      __cases.setCurrentIndex(__cases.count() - 1)

      # locate working elements
      __case_details = case_tab.findChild(QLabel, "case_details")
      __lb_susp_info = case_tab.findChild(QLabel, "lb_susp_info")
      __text_susp = case_tab.findChild(QTextEdit, "text_susp")
      __lb_src_info = case_tab.findChild(QLabel, "lb_src_info")
      __text_src = case_tab.findChild(QTextEdit, "text_src")

      # connect navigation buttons
      __btn_prev_note = case_tab.findChild(QPushButton, "btn_prev_note")
      __btn_next_note = case_tab.findChild(QPushButton, "btn_next_note")
      __btn_prev_note.clicked.connect(self.__show_prev_annotation)
      __btn_next_note.clicked.connect(self.__show_next_annotation)

      # update components
      __case_details.setText(QString("Plagiarism type: <b>%1</b>, Original corpus: <b>%2</b>, \
         Original corpus id: <b>%3</b>, Generated by: <b>%4</b>, Generator name: <b>%5</b>")
         .arg(case['plag_type'])
         .arg(case['original_corpus'])
         .arg(case['original_corpus_id'])
         .arg(case['generated_by'])
         .arg(case['generator_name']))
      __lb_susp_info.setText(QString("[<b>Suspicious</b>]&nbsp;&nbsp;&nbsp;doc-name = <b>%1</b>, \
         length = <b>%2</b> char(s), offset = <b>%3</b>")
         .arg(case['susp_snippet_doc'])
         .arg(case['susp_snippet_length'])
         .arg(case['susp_snippet_offset'])
         .arg(str(0))
         .arg(case['susp_snippet_sentences_count']))
         
      # Inyectando texto unicode dentro del QTextEdit
      __text_susp.setHtml(case['susp_text'])
      print 'TNLP_MW: ', case['susp_text'], type(case['susp_text'])
      
      __lb_src_info.setText(QString("[<b>Source</b>]&nbsp;&nbsp;&nbsp;doc-name = <b>%1</b>, \
         length = <b>%2</b> char(s), offset = <b>%3</b>")
         .arg(case['src_snippet_doc'])
         .arg(case['src_snippet_length'])
         .arg(case['src_snippet_offset'])
         .arg(str(0))
         .arg(case['src_snippet_sentences_count']))
      
      # Inyectando texto unicode dentro del QTextEdit
      __text_src.setHtml(case['src_text'])
      print 'case[src_text]:', case['src_text'], '++++++++++', type(case['src_text'])

      return

      '''
      # format segments
      # source
      __cursor = __src_te.textCursor()
      __cursor.setPosition(int(case[2][11]))
      __cursor.setPosition(int(case[2][11]) + int(case[2][9]), QTextCursor.KeepAnchor)
      __format = QTextCharFormat()
      #~ __format.setFontWeight(QFont.Bold)
      __format.setFontItalic(True)
      ##__format.setForeground(QBrush(Qt.green))
      __cursor.mergeCharFormat(__format)
      # suspiciuos
      __cursor = __susp_te.textCursor()
      __cursor.setPosition(int(case[2][11]))
      __cursor.setPosition(int(case[2][7]) + int(case[2][5]), QTextCursor.KeepAnchor)
      __format = QTextCharFormat()
      #~ __format.setFontWeight(QFont.Bold)
      __format.setFontItalic(True)
      #__format.setForeground(QBrush(Qt.red))
      __format.setFontUnderline(True)
      __format.setUnderlineStyle(QTextCharFormat.WaveUnderline)
      __format.setUnderlineColor(QColor(case_data[1].toString()))
      __cursor.mergeCharFormat(__format)'''


   def __update_selected_case(self, _tab_index):
      """Update selected case in case list"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab
      __cases_list = __corpus.children()[1].children()[2] # cases list

      # focus case
      if __cases.count() > 0:
         __cases_list.setCurrentItem(__cases_list.findItems(__cases.tabText(_tab_index), Qt.MatchCaseSensitive)[0])

         # get case data
         (case, annotations, index) = __cases.widget(_tab_index).get_case_data()

         if index < 0:
            self.__show_no_annotations()
         else:
            self.__show_annotation(index, annotations, case)
      else:
         __cases_list.setCurrentRow(__cases_list.currentRow(), QItemSelectionModel.Clear)


   def show_corpus_info(self):
      """Show current corpus information"""

      if not len(self.__corpus_list):
         QMessageBox.critical(self, self.__appName, 'No corpus loaded.')
         return

      corpus_info = self.__corpus_list[self.corpusTabs.currentIndex()].get_corpus_info()

      #TODO Arreglar la forma en que se lee el diccionario aqui
      info = 'Corpus Information<br/><br/>'
      info += 'Name: ' + corpus_info['name'] + '<br/>'
      info += 'Version: ' + corpus_info['version'] + '<br/>'
      info += 'Language: ' + corpus_info['lang'] + '<br/>'
      info += 'Owners: ' + corpus_info['owners'] + '<br/>'
      info += 'Authors: ' + corpus_info['authors'] + '<br/>'
      info += 'Country: ' + corpus_info['country'] + '<br/>'
      info += 'Created: ' + corpus_info['creation_date'] + '<br/>'
      info += 'Changed: ' + corpus_info['last_modification_date'] + '<br/>'
      info += 'Total Cases:' + corpus_info['total_cases'] + '<br/>'
      info += 'Total True Cases:' + corpus_info['total_true_cases'] + '<br/>'
      info += 'Total Annotations:' + corpus_info['total_annotations'] + '<br/>'
      info += 'Total True Annotations:' + corpus_info['total_true_annotations'] + '<br/>'


      QMessageBox.information(self, self.__appName, info)


   def close_corpus(self):
      """Close current corpus"""

      if not len(self.__corpus_list):
         QMessageBox.critical(self, self.__appName, 'No corpus loaded.')
         return

      resp = QMessageBox.question(self, self.__appName, u'Close corpus <b>' + self.corpusTabs.tabText(self.corpusTabs.currentIndex()) + '</b>?', QMessageBox.Yes | QMessageBox.No)
      if resp == QMessageBox.No:
         return

      del(self.__corpus_list[self.corpusTabs.currentIndex()])
      self.corpusTabs.removeTab(self.corpusTabs.currentIndex())

      QMessageBox.information(self, self.__appName, 'Corpus closed.')


   def closeEvent(self, event):
      """Handle the window close event"""

      resp = QMessageBox.question(self, self.__appName, u'Exit <b>' + self.__appName + '</b>?', QMessageBox.Yes | QMessageBox.No)
      if resp == QMessageBox.Yes:
         event.accept()
      else:
         event.ignore()


   def __closeCaseTab(self, tab_index):
      """Close selected tab"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab

      resp = QMessageBox.question(self, self.__appName, u'Close case <b>' + __cases.tabText(tab_index) + '</b>?', QMessageBox.Yes | QMessageBox.No)
      if resp == QMessageBox.Yes:
         # close case
         __cases.removeTab(tab_index)


   def __searchCase(self):
      """Search cases"""

      # clear the search criteria
      search_criteria = self.sender().text().trimmed()
      # if valid then search
      if search_criteria.length():
         # locate working elements
         __corpus = self.corpusTabs.currentWidget() # corpus
         __cases_list = __corpus.children()[1].children()[2] # cases list
         # focus first case matching the search criteria
         __result = __cases_list.findItems(search_criteria, Qt.MatchContains)
         if len(__result) > 0:
            __cases_list.setCurrentItem(__result[0])
      else:
         QMessageBox.critical(self, self.__appName, u'Please enter a valid search criteria.')


   def __show_prev_annotation(self):
      """Display the previous annotation if there is any"""

     # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      case_tab = case_tab.currentWidget()

      (case, annotations, index) = case_tab.get_case_data()

      if index > 0:
         index -= 1
         case_tab.set_case_data(case, annotations, index)
         self.__show_annotation(index, annotations, case)


   def __show_next_annotation(self):
      """Display the next annotation if there is any"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      case_tab = case_tab.currentWidget()

      (case, annotations, index) = case_tab.get_case_data()

      if index < len(annotations) - 1:
         index += 1
         case_tab.set_case_data(case, annotations, index)
         self.__show_annotation(index, annotations, case)


   def __show_annotation(self, _index, _annotations, _case):
      """Display annotation"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      case_tab = case_tab.currentWidget()

      ######__lb_susp_sentence = case_tab.findChild(QLabel, "lb_susp_sentence")
      ###__lb_src_sentence = case_tab.findChild(QLabel, "lb_src_sentence")
      __lb_note_id = case_tab.findChild(QLabel, "lb_note_id")
      __lb_note_type = case_tab.findChild(QLabel, "lb_note_type")
      __lb_note_projection = case_tab.findChild(QLabel, "lb_note_projection")
      __lb_note_susp = case_tab.findChild(QLabel, "lb_note_susp")
      __lb_note_src = case_tab.findChild(QLabel, "lb_note_src")
      __lb_note_author = case_tab.findChild(QLabel, "lb_note_author")
      __lb_note_date = case_tab.findChild(QLabel, "lb_note_date")
      __lb_note_human_val = case_tab.findChild(QLabel, "lb_note_human_val")
      __lb_note_machine_recog = case_tab.findChild(QLabel, "lb_note_machine_recog")
      __lb_note_current = case_tab.findChild(QLabel, "lb_note_current")
      __lb_note_count = case_tab.findChild(QLabel, "lb_note_count")
      
      # Encontrando los QTextEdit
      __text_susp = case_tab.findChild(QTextEdit, "text_susp")
      __text_src = case_tab.findChild(QTextEdit, "text_src")

      _info = _annotations[_index]

      # update components
      ###__lb_susp_sentence.setText('<b>Suspicious sentence:</b> ' + _info['susp_sentence'])
      ###__lb_src_sentence.setText('<b>Source sentence:</b> ' + _info['src_sentence'])
      __lb_note_id.setText(_info['id'])
      __lb_note_type.setText(_info['phenomenon_type'])
      __lb_note_projection.setText(_info['projection'])
      __lb_note_susp.setText(_info['susp_chunk_offset'] + ' / ' +
      _info['susp_chunk_length'])
      __lb_note_src.setText(_info['src_chunk_offset'] + ' / ' +
      _info['src_chunk_length'])
      __lb_note_author.setText(_info['author'])
      __lb_note_date.setText(_info['annotation_date'])
      __lb_note_human_val.setText(_info['validated_by_human_beings'])
      __lb_note_machine_recog.setText(_info['recognized_by_algorithms'])
      __lb_note_current.setText(str(_index + 1))
      __lb_note_count.setText(str(len(_annotations)))


      # show annotation info
      # suspicious text
      cursor = QTextCursor(__text_susp.document())
      # clear highlighted annotation
      cursor.setPosition(0, QTextCursor.MoveAnchor)
      cursor.setPosition(len(unicode(__text_susp.toPlainText(),'iso8859-1')), QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      font = QFont()
      format.setFont(font)
      cursor.setCharFormat(format)

      # highlight annotation
      cursor.setPosition(int(_info['susp_chunk_offset']))
      cursor.setPosition(int(_info['susp_chunk_offset']) + int(_info['susp_chunk_length']), QTextCursor.KeepAnchor)
      print 'len __text_susp:', unicode(__text_susp.toPlainText(),'iso8859-1'), ', ', len(unicode(__text_susp.toPlainText(),'iso8859-1'))
      format = QTextCharFormat()
      font = QFont()
      font.setItalic(True)
      font.setBold(True)
      format.setFont(font)
      format.setBackground(QBrush(Qt.green))
      cursor.mergeCharFormat(format)

      # source text
      cursor = QTextCursor(__text_src.document())
      # clear highlighted annotation
      cursor.setPosition(0, QTextCursor.MoveAnchor)
      cursor.setPosition(len(unicode(__text_src.toPlainText(),'iso8859-1')), QTextCursor.KeepAnchor)
      print 'len __text_src:', unicode(__text_src.toPlainText(),'iso8859-1'), ', ', len(unicode(__text_src.toPlainText(),'iso8859-1'))
      format = QTextCharFormat()
      font = QFont()
      format.setFont(font)
      cursor.setCharFormat(format)

      # highlight annotation
      cursor.setPosition(int(_info['src_chunk_offset']))
      cursor.setPosition(int(_info['src_chunk_offset']) + int(_info['src_chunk_length']), QTextCursor.KeepAnchor)
      format = QTextCharFormat()
      font = QFont()
      font.setItalic(True)
      font.setBold(True)
      format.setFont(font)
      format.setBackground(QBrush(Qt.green))
      cursor.mergeCharFormat(format)


   def __show_no_annotations(self):
      """Display empty data when there are no annotations"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      case_tab = case_tab.currentWidget()

      ###__lb_susp_sentence = case_tab.findChild(QLabel, "lb_susp_sentence")
      ###__lb_src_sentence = case_tab.findChild(QLabel, "lb_src_sentence")
      __lb_note_id = case_tab.findChild(QLabel, "lb_note_id")
      __lb_note_type = case_tab.findChild(QLabel, "lb_note_type")
      __lb_note_projection = case_tab.findChild(QLabel, "lb_note_projection")
      __lb_note_susp = case_tab.findChild(QLabel, "lb_note_susp")
      __lb_note_src = case_tab.findChild(QLabel, "lb_note_src")
      __lb_note_author = case_tab.findChild(QLabel, "lb_note_author")
      __lb_note_date = case_tab.findChild(QLabel, "lb_note_date")
      __lb_note_human_val = case_tab.findChild(QLabel, "lb_note_human_val")
      __lb_note_machine_recog = case_tab.findChild(QLabel, "lb_note_machine_recog")
      __lb_note_current = case_tab.findChild(QLabel, "lb_note_current")
      __lb_note_count = case_tab.findChild(QLabel, "lb_note_count")

      # update elements
      ###__lb_susp_sentence.setText('-')
      ###__lb_src_sentence.setText('-')
      __lb_note_id.setText('-')
      __lb_note_type.setText('-')
      __lb_note_projection.setText('-')
      __lb_note_susp.setText('-')
      __lb_note_src.setText('-')
      __lb_note_author.setText('-')
      __lb_note_date.setText('-')
      __lb_note_human_val.setText('-')
      __lb_note_machine_recog.setText('-')
      __lb_note_current.setText('-')
      __lb_note_count.setText('-')


   def __add_case(self):
      '''Show Add Case Window'''

      if len(self.__corpus_list) == 0:
         QMessageBox.critical(self, self.__appName, u'No corpus loaded.')
         return

      # select correct corpus reader
      __reader = self.__corpus_list[self.corpusTabs.currentIndex()]

      add = TNLP_AddCase(__reader, self)
      add.show()


   def __add_annotation(self):
      '''Show Add Annotation Window'''

      if (len(self.__corpus_list) == 0):
         QMessageBox.critical(self, self.__appName, u'No corpus loaded.')
         return
      else:
         # locate working elements
         __corpus = self.corpusTabs.currentWidget() # corpus
         case_tab = __corpus.children()[2] # cases tab
         if case_tab.count() == 0:
            QMessageBox.critical(self, self.__appName, u'No case opened.')
            return

      # select correct corpus reader
      __reader = self.__corpus_list[self.corpusTabs.currentIndex()]

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      case_tab = case_tab.currentWidget()

      # get case data
      (case, annotations, index) = case_tab.get_case_data()

      add = TNLP_AddAnnotation(__reader, case, self)
      add.show()


   def update_case_list(self, _new_case_id):
      '''Update cases list'''

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases_list = __corpus.children()[1].children()[2] # cases list
      _total_lb = __corpus.children()[1].children()[3] # total cases

      # update cases list
      __reader = self.__corpus_list[self.corpusTabs.currentIndex()]
      case = __reader.get_case_by_id(_new_case_id)
      listItem = QListWidgetItem(QIcon(plag_types[case['plag_type']][0]), QString("[" + case['id'] + "]: " + case['annotator_summary']))
      listItem.setData(Qt.UserRole, [case['id'], plag_types[case['plag_type']][1]])
      __cases_list.addItem(listItem)

      _total_lb.setText(QString('Total cases: <b>%1</b>').arg(__reader.get_corpus_total_cases()))


   def update_annotations_list(self, _new_annotation):
      '''Update annotations list'''

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      current_tab = case_tab.currentIndex()
      case_tab = case_tab.currentWidget()

      # update annotations list
      case_tab.add_annotation(_new_annotation)

      self.__update_selected_case(current_tab)


   def __create_corpus(self):
      '''Show Create Corpus Window'''

      manager = TNLP_XML_Manager()

      corpus = TNLP_NewCorpus(manager, self)
      corpus.show()
