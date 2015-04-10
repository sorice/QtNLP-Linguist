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

# import plag types
from TNLP_Plag_Types import plag_types

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

      # extra config
      self.showMaximized()
      self.setWindowTitle(self.__appName + ' - ' + self.__appVersion)

      # signals and slots
      self.actionLoad_New_Corpus.triggered.connect(self.load_new_corpus)
      self.actionCorpus_Information.triggered.connect(self.show_corpus_info)
      self.actionClose_Corpus.triggered.connect(self.close_corpus)
      self.actionExit.triggered.connect(self.close)


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
      tab_1 = QWidget()

      gridLayout = QGridLayout(tab_1)
      gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
      text_susp.setReadOnly(True)
      text_susp.setObjectName(_fromUtf8("text_susp"))
      verticalLayout_12.addWidget(text_susp)
      gridLayout.addLayout(verticalLayout_12, 0, 0, 1, 1)
      line_3 = QFrame(tab_1)
      line_3.setFrameShape(QFrame.HLine)
      line_3.setFrameShadow(QFrame.Sunken)
      line_3.setObjectName(_fromUtf8("line_3"))
      gridLayout.addWidget(line_3, 1, 0, 1, 1)
      horizontalLayout_3 = QHBoxLayout()
      horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_3.addItem(spacerItem)
      label_2 = QLabel(tab_1)
      label_2.setObjectName(_fromUtf8("label_2"))
      horizontalLayout_3.addWidget(label_2)
      spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_3.addItem(spacerItem1)
      gridLayout.addLayout(horizontalLayout_3, 2, 0, 1, 1)
      line = QFrame(tab_1)
      line.setFrameShape(QFrame.HLine)
      line.setFrameShadow(QFrame.Sunken)
      line.setObjectName(_fromUtf8("line"))
      gridLayout.addWidget(line, 3, 0, 1, 1)
      verticalLayout = QVBoxLayout()
      verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
      lb_susp_sentenc = QLabel(tab_1)
      lb_susp_sentenc.setObjectName(_fromUtf8("lb_note_susp_sentence"))
      verticalLayout.addWidget(lb_susp_sentenc)
      lb_src_sentence = QLabel(tab_1)
      lb_src_sentence.setObjectName(_fromUtf8("lb_note_src_sentence"))
      verticalLayout.addWidget(lb_src_sentence)
      gridLayout.addLayout(verticalLayout, 4, 0, 1, 1)
      line_2 = QFrame(tab_1)
      line_2.setFrameShape(QFrame.HLine)
      line_2.setFrameShadow(QFrame.Sunken)
      line_2.setObjectName(_fromUtf8("line_2"))
      gridLayout.addWidget(line_2, 5, 0, 1, 1)
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
      lb_susp_offset = QLabel(tab_1)
      lb_susp_offset.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_susp_offset.setObjectName(_fromUtf8("lb_susp_offset"))
      verticalLayout_5.addWidget(lb_susp_offset)
      horizontalLayout.addLayout(verticalLayout_5)
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
      lb_susp_length = QLabel(tab_1)
      lb_susp_length.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
      lb_susp_length.setObjectName(_fromUtf8("lb_susp_length"))
      verticalLayout_6.addWidget(lb_susp_length)
      horizontalLayout.addLayout(verticalLayout_6)
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
      horizontalLayout_2 = QHBoxLayout()
      horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
      spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_2.addItem(spacerItem2)
      btn_prev_note = QPushButton(tab_1)
      btn_prev_note.setObjectName(_fromUtf8("btn_prev_note"))
      horizontalLayout_2.addWidget(btn_prev_note)
      btn_next_note = QPushButton(tab_1)
      btn_next_note.setObjectName(_fromUtf8("btn_next_note"))
      horizontalLayout_2.addWidget(btn_next_note)
      spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout_2.addItem(spacerItem3)
      gridLayout.addLayout(horizontalLayout_2, 7, 0, 1, 1)
      line_4 = QFrame(tab_1)
      line_4.setFrameShape(QFrame.HLine)
      line_4.setFrameShadow(QFrame.Sunken)
      line_4.setObjectName(_fromUtf8("line_4"))
      gridLayout.addWidget(line_4, 8, 0, 1, 1)
      verticalLayout_13 = QVBoxLayout()
      verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
      lb_src_info = QLabel(tab_1)
      lb_src_info.setObjectName(_fromUtf8("lb_src_info"))
      verticalLayout_13.addWidget(lb_src_info)
      text_src = QTextEdit(tab_1)
      text_src.setReadOnly(True)
      text_src.setObjectName(_fromUtf8("text_src"))
      verticalLayout_13.addWidget(text_src)
      gridLayout.addLayout(verticalLayout_13, 9, 0, 1, 1)

      # extra child used for setData
      action = QAction(tab_1)
      action.setObjectName(_fromUtf8("case_extra_data"))
      #

      # set default values
      lb_susp_info.setText("<html><head/><body><p>[<span style=\" font-weight:600;\">Suspicious</span>] &nbsp;&nbsp;&nbsp; id = <span style=\" font-weight:600;\">000</span>, susp_name = <span style=\" font-weight:600;\">susp-1111</span>, length = <span style=\" font-weight:600;\">555</span> char(s), <span style=\" font-weight:600;\">1</span> word(s), <span style=\" font-weight:600;\">1</span> sentence(s), origin_offset = <span style=\" font-weight:600;\">10</span></p></body></html>")
      text_susp.setText("Texto sospechoso")
      label_2.setText("<html><head/><body><p><span style=\" font-weight:600;\">Annotation Details</span></p></body></html>")
      lb_susp_sentenc.setText("Susp Sentence")
      lb_src_sentence.setText("Src Sentence")
      label_4.setText("ID")
      lb_note_id.setText("1")
      label_5.setText("Type")
      lb_note_type.setText("Same Polarity")
      label_6.setText("Projection")
      lb_note_projection.setText("Local")
      label_7.setText("Susp\nOffset / Len")
      lb_susp_offset.setText("10")
      label_8.setText("Src\nOffset / Len")
      lb_susp_length.setText("50")
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
      lb_src_info.setText("<html><head/><body><p>[<span style=\" font-weight:600;\">Source</span>]     id = <span style=\" font-weight:600;\">000</span>, src_name = <span style=\" font-weight:600;\">src-1111</span>, length = <span style=\" font-weight:600;\">555</span> char(s), <span style=\" font-weight:600;\">1</span> word(s), <span style=\" font-weight:600;\">1</span> sentence(s), origin_offset = <span style=\" font-weight:600;\">10</span></p></body></html>")
      text_src.setText("Texto fuente")

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

      # parser instance
      __reader = TNLP_XML_Manager()

      if __reader.parse_xml('test/corpuses/TNLP/TNLP-test.xml'):
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
         for i in range(__reader.get_corpus_total_cases()):
            i = i + 1
            _tmp_case = __reader.get_case_summary(i)
            listItem = QListWidgetItem(QIcon(plag_types[_tmp_case[0]][0]), QString("[" + _tmp_case[1] + "]: " + _tmp_case[2]))
            # data: list(index, plag_type_rgb_color)
            listItem.setData(Qt.UserRole, [_tmp_case[1], plag_types[_tmp_case[0]][1]])
            _cases_list.addItem(listItem)

         _total_lb.setText(QString('Total cases: <b>%1</b>').arg(__reader.get_corpus_total_cases()))
         self.__corpus_list.append(__reader)

         QMessageBox.information(self, self.__appName, 'Corpus loaded.')
      else:
         QMessageBox.critical(self, self.__appName, 'Error parsing corpus.')


   def __get_case(self, _current, _old):
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

      case_tab = self.__create_new_case_tab()
      __cases.addTab(case_tab, _current.text())
      __cases.setCurrentIndex(__cases.count() - 1)

      # locate working elements
      __case_details = case_tab.findChild(QLabel, "case_details")
      __lb_susp_info = case_tab.findChild(QLabel, "lb_susp_info")
      __text_susp = case_tab.findChild(QTextEdit, "text_susp")
      __lb_note_susp_sentence = case_tab.findChild(QLabel, "lb_note_susp_sentence")
      __lb_note_src_sentence = case_tab.findChild(QLabel, "lb_note_src_sentence")
      __lb_note_id = case_tab.findChild(QLabel, "lb_note_id")
      __lb_note_type = case_tab.findChild(QLabel, "lb_note_type")
      __lb_note_projection = case_tab.findChild(QLabel, "lb_note_projection")
      __lb_note_susp = case_tab.findChild(QLabel, "lb_susp_offset")
      __lb_note_src = case_tab.findChild(QLabel, "lb_susp_length")
      __lb_note_author = case_tab.findChild(QLabel, "lb_note_author")
      __lb_note_date = case_tab.findChild(QLabel, "lb_note_date")
      __lb_note_human_val = case_tab.findChild(QLabel, "lb_note_human_val")
      __lb_note_machine_recog = case_tab.findChild(QLabel, "lb_note_machine_recog")
      __btn_prev_note = case_tab.findChild(QPushButton, "btn_prev_note")
      __btn_next_note = case_tab.findChild(QPushButton, "btn_next_note")
      __lb_src_info = case_tab.findChild(QLabel, "lb_src_info")
      __text_src = case_tab.findChild(QTextEdit, "text_src")
      __case_extra_data = case_tab.findChild(QAction, "case_extra_data")
      #__case_extra_data = __case_extra_data.data().toList()

      __annotations = self.__corpus_list[self.corpusTabs.currentIndex()].get_annotations_of_case(case_id)
      __selected_annotation = -1
      if len(__annotations) > 0:
         __selected_annotation = 0;

         # display first annotation
         self.__show_annotation(__annotations[0])
         '''__lb_note_susp_sentence.setText('<b>Suspicious sentence:</b> ' + 'Suspicious sentence extracted from susp snippet')
         __lb_note_src_sentence.setText('<b>Source sentence:</b> ' + 'Source sentence extracted from src snippet')
         __lb_note_id.setText(__annotations[__selected_annotation]['id'])
         __lb_note_type.setText(__annotations[__selected_annotation]['phenomenon_type'])
         __lb_note_projection.setText(__annotations[__selected_annotation]['projection'])
         __lb_note_susp.setText(__annotations[__selected_annotation]['susp_chunk_offset'] + ' / ' +
            __annotations[__selected_annotation]['susp_chunk_length'])
         __lb_note_src.setText(__annotations[__selected_annotation]['src_chunk_offset'] + ' / ' +
            __annotations[__selected_annotation]['src_chunk_length'])
         __lb_note_author.setText(__annotations[__selected_annotation]['author'])
         __lb_note_date.setText(__annotations[__selected_annotation]['annotation_date'])
         __lb_note_human_val.setText(__annotations[__selected_annotation]['validated_by_human_beings'])
         __lb_note_machine_recog.setText(__annotations[__selected_annotation]['recognized_by_algorithms'])'''
      else:
         __lb_note_susp_sentence.setText('-')
         __lb_note_src_sentence.setText('-')
         __lb_note_id.setText('-')
         __lb_note_type.setText('-')
         __lb_note_projection.setText('-')
         __lb_note_susp.setText('-')
         __lb_note_src.setText('-')
         __lb_note_author.setText('-')
         __lb_note_date.setText('-')
         __lb_note_human_val.setText('-')
         __lb_note_machine_recog.setText('-')

      # save data for navigation system
      __case_extra_data.setData([__annotations, __selected_annotation])

      # connect navigation buttons
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
         length = <b>%2</b> char(s), <b>%3</b> words, <b>%4</b> sentence(s), offset = <b>%5</b>")
         .arg(case['susp_snippet_doc'])
         .arg(case['susp_snippet_length'])
         .arg(str(0))
         .arg(case['susp_snippet_sentences_count'])
         .arg(case['susp_snippet_offset']))
      __text_susp.setHtml('TODO: leer el fichero y poner el contenido aqui o hacerlo en el parser...')
      __lb_src_info.setText(QString("[<b>Source</b>]&nbsp;&nbsp;&nbsp;doc-name = <b>%1</b>, \
         length = <b>%2</b> char(s), <b>%3</b> words, <b>%4</b> sentence(s), offset = <b>%5</b>")
         .arg(case['src_snippet_doc'])
         .arg(case['src_snippet_length'])
         .arg(str(0))
         .arg(case['src_snippet_sentences_count'])
         .arg(case['src_snippet_offset']))
      __text_src.setHtml('TODO: leer el fichero y poner el contenido aqui o hacerlo en el parser...')

      # show the first annotation if there is any
      #

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


   def __update_selected_case(self, _case):
      """Update selected case in case list"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab
      __cases_list = __corpus.children()[1].children()[2] # cases list
      # focus case
      if __cases.count() > 0:
         __cases_list.setCurrentItem(__cases_list.findItems(__cases.tabText(_case), Qt.MatchCaseSensitive)[0])


   def show_corpus_info(self):
      """Show current corpus information"""

      if not len(self.__corpus_list):
         QMessageBox.critical(self, self.__appName, 'No corpus loaded.')
         return

      corpus_info = self.__corpus_list[self.corpusTabs.currentIndex()].get_corpus_info()

      info = 'Corpus Information<br/><br/>'
      info += 'Name: ' + corpus_info[0] + '<br/>'
      info += 'Version: ' + corpus_info[1] + '<br/>'
      info += 'Language: ' + corpus_info[2] + '<br/>'
      info += 'Owners: ' + corpus_info[3] + '<br/>'
      info += 'Authors: ' + corpus_info[4] + '<br/>'
      info += 'Country: ' + corpus_info[5] + '<br/>'
      info += 'Created: ' + corpus_info[6] + '<br/>'
      info += 'Changed: ' + corpus_info[7] + '<br/>'
      info += 'Total Cases:' + str(corpus_info[8]) + '<br/>'

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
         resp = QMessageBox.critical(self, self.__appName, u'Please enter a valid search criteria.')


   def __show_prev_annotation(self):
      """Display the previous annotation if there is any"""

     # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab

      _navigation_data = __cases.currentWidget().findChild(QAction, "case_extra_data")
      _annotations = _navigation_data.data().toList()
      _index = _annotations[1].toInt()[0]
      _annotations = _annotations[0].toList()
      _result = []

      if _index > 0:
         # morph QVariant data to QString
         for i in range(len(_annotations)):
            _annotations[i] = _annotations[i].toMap()
            _tmp = {}
            keys = _annotations[i].keys()
            for j in range(len(keys)):
               keys[j] = str(keys[j])

            values = _annotations[i].values()
            for j in range(len(values)):
               values[j] = str(values[j].toString())

            for j in range(len(_annotations[i])):
               _tmp[keys[j]] = values[j]

            _annotations[i] = _tmp

         _index -= 1
         # update navigation data
         _navigation_data.setData([_annotations, _index])
         # show annotation info
         self.__show_annotation(_annotations[_index])

      return


   def __show_next_annotation(self):
      """Display the next annotation if there is any"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab

      _navigation_data = __cases.currentWidget().findChild(QAction, "case_extra_data")
      _annotations = _navigation_data.data().toList()
      _index = _annotations[1].toInt()[0]
      _annotations = _annotations[0].toList()
      _result = []

      if _index < len(_annotations) - 1:
         # morph QVariant data to QString
         for i in range(len(_annotations)):
            _annotations[i] = _annotations[i].toMap()
            _tmp = {}
            keys = _annotations[i].keys()
            for j in range(len(keys)):
               keys[j] = str(keys[j])

            values = _annotations[i].values()
            for j in range(len(values)):
               values[j] = str(values[j].toString())

            for j in range(len(_annotations[i])):
               _tmp[keys[j]] = values[j]

            _annotations[i] = _tmp

         _index += 1
         # update navigation data
         _navigation_data.setData([_annotations, _index])
         # show annotation info
         self.__show_annotation(_annotations[_index])

      return


   def __show_annotation(self, _info):
      """Display annotation"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      case_tab = __corpus.children()[2] # cases tab
      __lb_note_susp_sentence = case_tab.findChild(QLabel, "lb_note_susp_sentence")
      __lb_note_src_sentence = case_tab.findChild(QLabel, "lb_note_src_sentence")
      __lb_note_id = case_tab.findChild(QLabel, "lb_note_id")
      __lb_note_type = case_tab.findChild(QLabel, "lb_note_type")
      __lb_note_projection = case_tab.findChild(QLabel, "lb_note_projection")
      __lb_note_susp = case_tab.findChild(QLabel, "lb_susp_offset")
      __lb_note_src = case_tab.findChild(QLabel, "lb_susp_length")
      __lb_note_author = case_tab.findChild(QLabel, "lb_note_author")
      __lb_note_date = case_tab.findChild(QLabel, "lb_note_date")
      __lb_note_human_val = case_tab.findChild(QLabel, "lb_note_human_val")
      __lb_note_machine_recog = case_tab.findChild(QLabel, "lb_note_machine_recog")

      # update components
      __lb_note_susp_sentence.setText('<b>Suspicious sentence:</b> ' + 'Suspicious sentence extracted from susp snippet')
      __lb_note_src_sentence.setText('<b>Source sentence:</b> ' + 'Source sentence extracted from src snippet')
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
