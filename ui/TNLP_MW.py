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
      gridLayout_4 = QGridLayout(tab_1)
      verticalLayout_2 = QVBoxLayout()

      suspInfo = QLabel(tab_1)
      #suspInfo.setText(QString("id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(str(367)).arg(str('susp-doc69')).arg(str(489)).arg(str(67)).arg(str(5)).arg(str(125)))
      verticalLayout_2.addWidget(suspInfo)

      suspDoc = QTextEdit(tab_1)
      suspDoc.setObjectName(_fromUtf8("suspDoc"))
      suspDoc.setReadOnly(True)
      suspDoc.setHtml('Suspicious')
      verticalLayout_2.addWidget(suspDoc)

      line = QFrame(tab_1)
      line.setFrameShape(QFrame.HLine)
      line.setFrameShadow(QFrame.Sunken)
      verticalLayout_2.addWidget(line)

      """annotationsWidget = QGroupBox(centralwidget)
      annotationsWidget.setGeometry(QRect(130, 80, 282, 319))
      annotationsWidget.setContextMenuPolicy(Qt.PreventContextMenu)
      annotationsWidget.setFlat(True)
      annotationsWidget.setObjectName(_fromUtf8("annotationsWidget"))
      gridLayout = QGridLayout(annotationsWidget)
      gridLayout.setObjectName(_fromUtf8("gridLayout"))
      verticalLayout_2 = QVBoxLayout()
      verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
      horizontalLayout = QHBoxLayout()
      horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
      addAnnotation = QPushButton(annotationsWidget)
      addAnnotation.setMinimumSize(QSize(64, 0))
      addAnnotation.setMaximumSize(QSize(64, 16777215))
      addAnnotation.setObjectName(_fromUtf8("addAnnotation"))
      horizontalLayout.addWidget(addAnnotation)
      previousAnnotation = QPushButton(annotationsWidget)
      previousAnnotation.setMinimumSize(QSize(64, 0))
      previousAnnotation.setMaximumSize(QSize(64, 16777215))
      previousAnnotation.setObjectName(_fromUtf8("previousAnnotation"))
      horizontalLayout.addWidget(previousAnnotation)
      nextAnnotation = QPushButton(annotationsWidget)
      nextAnnotation.setMinimumSize(QSize(64, 0))
      nextAnnotation.setMaximumSize(QSize(64, 16777215))
      nextAnnotation.setObjectName(_fromUtf8("nextAnnotation"))
      horizontalLayout.addWidget(nextAnnotation)
      spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      horizontalLayout.addItem(spacerItem)
      verticalLayout_2.addLayout(horizontalLayout)
      verticalLayout = QVBoxLayout()
      verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
      chunkSusp = QLabel(annotationsWidget)
      chunkSusp.setObjectName(_fromUtf8("chunkSusp"))
      verticalLayout.addWidget(chunkSusp)
      chunkSrc = QLabel(annotationsWidget)
      chunkSrc.setObjectName(_fromUtf8("chunkSrc"))
      verticalLayout.addWidget(chunkSrc)
      verticalLayout_2.addLayout(verticalLayout)
      gridLayout.addLayout(verticalLayout_2, 0, 0, 1, 1)
      annotationsList = QListView(annotationsWidget)
      annotationsList.setObjectName(_fromUtf8("annotationsList"))
      gridLayout.addWidget(annotationsList, 1, 0, 1, 1)"""

      sourceInfo = QLabel(tab_1)
      #sourceInfo.setText(QString("id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(str(278)).arg(str('src-doc45')).arg(str(570)).arg(str(70)).arg(str(5)).arg(str(329)))
      verticalLayout_2.addWidget(sourceInfo)

      sourceDoc = QTextEdit(tab_1)
      sourceDoc.setReadOnly(True)
      sourceDoc.setHtml('Source')
      verticalLayout_2.addWidget(sourceDoc)

      gridLayout_4.addLayout(verticalLayout_2, 0, 0, 1, 1)
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
      #__reader = XML_read.Corpus_Reader()
      __reader = TNLP_XML_Manager()
      print __reader

      if __reader.parse_xml('abc.xml'):
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
            listItem = QListWidgetItem(QIcon(plag_types[_tmp_case[1]][0]), QString("[" + _tmp_case[0] + "]: " + _tmp_case[2]))
            # data: list(index, plag_type_rgb_color)
            listItem.setData(Qt.UserRole, [i, plag_types[_tmp_case[1]][1]])
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
      case_index = int(case_data[0].toString())
      case = self.__corpus_list[self.corpusTabs.currentIndex()].get_case(case_index)

      case_tab = self.__create_new_case_tab()
      __cases.addTab(case_tab, _current.text())
      __cases.setCurrentIndex(__cases.count() - 1)

      __items = __cases.currentWidget() # cases tab content
      __items = __items.children() # index 1, 2, 4, 5

      __susp_lb = __items[1] # susp text
      __susp_te = __items[2] # susp data
      __src_lb = __items[4] # src text
      __src_te = __items[5] # src data

      # update components
      __src_te.setHtml(case[1])
      __src_lb.setText(QString("[<b>Source</b>]&nbsp;&nbsp;&nbsp;&nbsp;id = <b>%1</b>, src_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(case[2][12]).arg(case[2][3]).arg(case[2][9]).arg(str(0)).arg(str(0)).arg(case[2][11]))
      __susp_te.setHtml(case[0])
      __susp_lb.setText(QString("[<b>Suspicious</b>]&nbsp;&nbsp;&nbsp;&nbsp;id = <b>%1</b>, susp_name = <b>%2</b>, length = <b>%3</b> char(s), <b>%4</b> words, <b>%5</b> sentence(s), orig_offset = <b>%6</b>").arg(case[2][12]).arg(case[2][1]).arg(case[2][5]).arg(str(0)).arg(str(0)).arg(case[2][7]))
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
      __cursor.mergeCharFormat(__format)


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
         print "Searching for \"" + search_criteria + "\""
         # locate working elements
         __corpus = self.corpusTabs.currentWidget() # corpus
         __cases_list = __corpus.children()[1].children()[2] # cases list
         # focus first case matching the search criteria
         __result = __cases_list.findItems(search_criteria, Qt.MatchContains)
         if len(__result) > 0:
            __cases_list.setCurrentItem(__result[0])
      else:
         print "Please enter a valid search string"
