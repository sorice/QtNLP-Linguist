#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import UI base file
from forms.ToNgueLP_MW_UI import Ui_ToNgueLP_MW

# import reader
from modules.ToNgueLP_corpus import XML_read

class ToNgueLP_MW(QMainWindow, Ui_ToNgueLP_MW):
   def __init__(self, _name, _version, parent = None):
      # init the parent
      super(ToNgueLP_MW, self).__init__(parent)

      # setup UI
      self.setupUi(self)

      # some attributes
      self.appName = _name
      self.appVersion = _version

      # readers list
      self.__corpus_list = []

      # extra config
      self.showMaximized()
      self.setWindowTitle(self.appName + ' - ' + self.appVersion)

      # signals and slots
      self.actionLoad_New_Corpus.triggered.connect(self.load_new_corpus)
      self.actionCorpus_Information.triggered.connect(self.show_corpus_info)
      self.actionClose_Corpus.triggered.connect(self.close_corpus)


   def __create_new_corpus_tab(self):
      """Create an empty new tab for corpus"""

      try:
         _fromUtf8 = QString.fromUtf8
      except AttributeError:
         def _fromUtf8(s):
            return s

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
      # slot
      casesWorkingArea.currentChanged.connect(self.__update_selected_case)
      #
      #tab_2 = QWidget()
      #casesWorkingArea.addTab(tab_2, _fromUtf8("Compare"))
      gridLayout_3.addWidget(casesWorkingArea, 0, 1, 1, 1)

      # global layout update
      self.gridLayout.addWidget(self.corpusTabs, 0, 1, 1, 1)

      return tab


   def __create_new_case_tab(self):
      """Create a new case tab for current corpus"""

      # right area
      tab_1 = QWidget()
      gridLayout_4 = QGridLayout(tab_1)
      verticalLayout_2 = QVBoxLayout()
      sourceDoc = QTextEdit(tab_1)
      sourceDoc.setReadOnly(True)
      sourceDoc.setHtml('Source')
      verticalLayout_2.addWidget(sourceDoc)
      sourceInfo = QLabel(tab_1)
      #sourceInfo.setText(QString("id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(str(278)).arg(str('src-doc45')).arg(str(570)).arg(str(70)).arg(str(5)).arg(str(329)))
      verticalLayout_2.addWidget(sourceInfo)
      line = QFrame(tab_1)
      line.setFrameShape(QFrame.HLine)
      line.setFrameShadow(QFrame.Sunken)
      verticalLayout_2.addWidget(line)
      suspDoc = QTextEdit(tab_1)
      suspDoc.setReadOnly(True)
      suspDoc.setHtml('Suspicious')
      verticalLayout_2.addWidget(suspDoc)
      suspInfo = QLabel(tab_1)
      #suspInfo.setText(QString("id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(str(367)).arg(str('susp-doc69')).arg(str(489)).arg(str(67)).arg(str(5)).arg(str(125)))
      verticalLayout_2.addWidget(suspInfo)
      gridLayout_4.addLayout(verticalLayout_2, 0, 0, 1, 1)

      return tab_1


   def load_new_corpus(self):
      """Load a new corpus"""

      # parser instance
      __reader = XML_read.Corpus_Reader()

      if __reader.parse_xml():
         # corpus already loaded?
         __corpus_names = []
         for i in self.__corpus_list:
            __corpus_names.append(i.get_corpus_name())
         if __reader.get_corpus_name() in __corpus_names:
            QMessageBox.critical(self, self.appName, 'Corpus <b>' + __reader.get_corpus_name() + ' </b>already loaded.')
            return

         # add a new tab for corpus
         tab = self.__create_new_corpus_tab()
         _cases_list = tab.children()[1].children()[2] # cases list
         _total_lb = tab.children()[1].children()[3] # total cases
         self.corpusTabs.addTab(tab, QString(__reader.get_corpus_name()))

         for i in range(__reader.get_corpus_total_cases()):
            i = i + 1
            listItem = QListWidgetItem(QString('Case: ' + str(i)))
            listItem.setData(Qt.UserRole, i)
            _cases_list.addItem(listItem)

         _total_lb.setText(QString('Total cases: <b>%1</b>').arg(__reader.get_corpus_total_cases()))
         self.__corpus_list.append(__reader)

         QMessageBox.information(self, self.appName, 'Corpus loaded.')
      else:
         QMessageBox.critical(self, self.appName, 'Error parsing corpus.')


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

      case_index = int(_current.data(Qt.UserRole).toString())
      case = self.__corpus_list[self.corpusTabs.currentIndex()].get_case(case_index)

      case_tab = self.__create_new_case_tab()
      __cases.addTab(case_tab, _current.text())
      __cases.setCurrentIndex(__cases.count() - 1)

      __items = __cases.currentWidget() # cases tab content
      __items = __items.children() # index 1, 2, 4, 5
      __src_te = __items[1] # src text
      __src_lb = __items[2] # src data
      __susp_te = __items[4] # susp text
      __susp_lb = __items[5] # susp data
      # update components
      __src_te.setHtml(case[1])
      __src_lb.setText(QString("[<b>Source</b>] id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(case[2][12]).arg(case[2][3]).arg(case[2][9]).arg(str(0)).arg(str(0)).arg(case[2][11]))
      __susp_te.setHtml(case[0])
      __susp_lb.setText(QString("[<b>Suspicious</b>] id = <b>%1</b>, susp_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(case[2][12]).arg(case[2][1]).arg(case[2][5]).arg(str(0)).arg(str(0)).arg(case[2][7]))
      # format segments
      # source
      __cursor = __src_te.textCursor()
      __cursor.setPosition(int(case[2][11]))
      __cursor.setPosition(int(case[2][11]) + int(case[2][9]), QTextCursor.KeepAnchor)
      __format = QTextCharFormat()
      #~ __format.setFontWeight(QFont.Bold)
      __format.setFontItalic(True)
      __format.setForeground(QBrush(Qt.green))
      __cursor.mergeCharFormat(__format)
      # suspiciuos
      __cursor = __susp_te.textCursor()
      __cursor.setPosition(int(case[2][11]))
      __cursor.setPosition(int(case[2][7]) + int(case[2][5]), QTextCursor.KeepAnchor)
      __format = QTextCharFormat()
      #~ __format.setFontWeight(QFont.Bold)
      __format.setFontItalic(True)
      __format.setForeground(QBrush(Qt.red))
      __cursor.mergeCharFormat(__format)


   def __update_selected_case(self, _case):
      """Update selected case in case list"""

      # locate working elements
      __corpus = self.corpusTabs.currentWidget() # corpus
      __cases = __corpus.children()[2] # cases tab
      __cases_list = __corpus.children()[1].children()[2] # cases list
      # focus case
      __cases_list.setCurrentItem(__cases_list.findItems(__cases.tabText(_case), Qt.MatchCaseSensitive)[0])


   def show_corpus_info(self):
      """Show current corpus information"""

      if not len(self.__corpus_list):
         raise QMessageBox.critical(self, self.appName, 'No corpus loaded.')
         #~ return

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
      QMessageBox.information(self, self.appName, info)


   def close_corpus(self):
      """Close current corpus"""

      if not len(self.__corpus_list):
         QMessageBox.critical(self, self.appName, 'No corpus loaded.')
         return

      del(self.__corpus_list[self.corpusTabs.currentIndex()])
      self.corpusTabs.removeTab(self.corpusTabs.currentIndex())

      QMessageBox.information(self, self.appName, 'Corpus closed.')

