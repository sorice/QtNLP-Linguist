# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TNLP_MW.ui'
#
# Created: Fri Apr 10 14:57:50 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ToNgueLP_MW(object):
    def setupUi(self, ToNgueLP_MW):
        ToNgueLP_MW.setObjectName(_fromUtf8("ToNgueLP_MW"))
        ToNgueLP_MW.resize(953, 611)
        self.centralwidget = QtGui.QWidget(ToNgueLP_MW)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.corpusTabs = QtGui.QTabWidget(self.centralwidget)
        self.corpusTabs.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.corpusTabs.setTabPosition(QtGui.QTabWidget.West)
        self.corpusTabs.setMovable(True)
        self.corpusTabs.setObjectName(_fromUtf8("corpusTabs"))
        self.gridLayout.addWidget(self.corpusTabs, 0, 1, 1, 1)
        ToNgueLP_MW.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ToNgueLP_MW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCorpus = QtGui.QMenu(self.menubar)
        self.menuCorpus.setObjectName(_fromUtf8("menuCorpus"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        self.menuScripts = QtGui.QMenu(self.menubar)
        self.menuScripts.setObjectName(_fromUtf8("menuScripts"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuLogin = QtGui.QMenu(self.menubar)
        self.menuLogin.setObjectName(_fromUtf8("menuLogin"))
        self.menuCases = QtGui.QMenu(self.menubar)
        self.menuCases.setObjectName(_fromUtf8("menuCases"))
        self.menuAnnotations = QtGui.QMenu(self.menubar)
        self.menuAnnotations.setObjectName(_fromUtf8("menuAnnotations"))
        ToNgueLP_MW.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ToNgueLP_MW)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ToNgueLP_MW.setStatusBar(self.statusbar)
        self.toolBar_Main = QtGui.QToolBar(ToNgueLP_MW)
        self.toolBar_Main.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar_Main.setMovable(False)
        self.toolBar_Main.setFloatable(False)
        self.toolBar_Main.setObjectName(_fromUtf8("toolBar_Main"))
        ToNgueLP_MW.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_Main)
        self.toolBar_Fixed = QtGui.QToolBar(ToNgueLP_MW)
        self.toolBar_Fixed.setMinimumSize(QtCore.QSize(280, 0))
        self.toolBar_Fixed.setMaximumSize(QtCore.QSize(280, 16777215))
        self.toolBar_Fixed.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar_Fixed.setMovable(False)
        self.toolBar_Fixed.setFloatable(False)
        self.toolBar_Fixed.setObjectName(_fromUtf8("toolBar_Fixed"))
        ToNgueLP_MW.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_Fixed)
        self.toolBar_Cases = QtGui.QToolBar(ToNgueLP_MW)
        self.toolBar_Cases.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar_Cases.setMovable(False)
        self.toolBar_Cases.setFloatable(False)
        self.toolBar_Cases.setObjectName(_fromUtf8("toolBar_Cases"))
        ToNgueLP_MW.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_Cases)
        self.actionLoad_New_Corpus = QtGui.QAction(ToNgueLP_MW)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/menu_corpus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_New_Corpus.setIcon(icon)
        self.actionLoad_New_Corpus.setObjectName(_fromUtf8("actionLoad_New_Corpus"))
        self.actionAdd_New_Corpus_Doc = QtGui.QAction(ToNgueLP_MW)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/add_corpus_doc.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_New_Corpus_Doc.setIcon(icon1)
        self.actionAdd_New_Corpus_Doc.setObjectName(_fromUtf8("actionAdd_New_Corpus_Doc"))
        self.actionCorpus_Information = QtGui.QAction(ToNgueLP_MW)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/corpus_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCorpus_Information.setIcon(icon2)
        self.actionCorpus_Information.setObjectName(_fromUtf8("actionCorpus_Information"))
        self.actionClose_Corpus = QtGui.QAction(ToNgueLP_MW)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/close_corpus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_Corpus.setIcon(icon3)
        self.actionClose_Corpus.setObjectName(_fromUtf8("actionClose_Corpus"))
        self.actionAdd_Algorithm_Output = QtGui.QAction(ToNgueLP_MW)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/add_algorithm_output.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Algorithm_Output.setIcon(icon4)
        self.actionAdd_Algorithm_Output.setObjectName(_fromUtf8("actionAdd_Algorithm_Output"))
        self.actionAdd_New_Case = QtGui.QAction(ToNgueLP_MW)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/add_case.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_New_Case.setIcon(icon5)
        self.actionAdd_New_Case.setObjectName(_fromUtf8("actionAdd_New_Case"))
        self.actionEdit_Case = QtGui.QAction(ToNgueLP_MW)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/edit_case.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Case.setIcon(icon6)
        self.actionEdit_Case.setObjectName(_fromUtf8("actionEdit_Case"))
        self.actionValidate_Case = QtGui.QAction(ToNgueLP_MW)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/validate_case.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValidate_Case.setIcon(icon7)
        self.actionValidate_Case.setObjectName(_fromUtf8("actionValidate_Case"))
        self.action_Re_Define_Boundaries = QtGui.QAction(ToNgueLP_MW)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/redefine_boundaries.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Re_Define_Boundaries.setIcon(icon8)
        self.action_Re_Define_Boundaries.setObjectName(_fromUtf8("action_Re_Define_Boundaries"))
        self.actionView_Annotation = QtGui.QAction(ToNgueLP_MW)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/icons/view_annotation.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Annotation.setIcon(icon9)
        self.actionView_Annotation.setObjectName(_fromUtf8("actionView_Annotation"))
        self.actionSave_Corpus = QtGui.QAction(ToNgueLP_MW)
        self.actionSave_Corpus.setObjectName(_fromUtf8("actionSave_Corpus"))
        self.actionSelect_Parser = QtGui.QAction(ToNgueLP_MW)
        self.actionSelect_Parser.setObjectName(_fromUtf8("actionSelect_Parser"))
        self.actionSuggest_Parser = QtGui.QAction(ToNgueLP_MW)
        self.actionSuggest_Parser.setObjectName(_fromUtf8("actionSuggest_Parser"))
        self.actionMain_View = QtGui.QAction(ToNgueLP_MW)
        self.actionMain_View.setObjectName(_fromUtf8("actionMain_View"))
        self.actionComparison_View = QtGui.QAction(ToNgueLP_MW)
        self.actionComparison_View.setObjectName(_fromUtf8("actionComparison_View"))
        self.actionDictionary_View = QtGui.QAction(ToNgueLP_MW)
        self.actionDictionary_View.setObjectName(_fromUtf8("actionDictionary_View"))
        self.actionConvert_Documents = QtGui.QAction(ToNgueLP_MW)
        self.actionConvert_Documents.setObjectName(_fromUtf8("actionConvert_Documents"))
        self.actionVerify_Corpus_and_Parser = QtGui.QAction(ToNgueLP_MW)
        self.actionVerify_Corpus_and_Parser.setObjectName(_fromUtf8("actionVerify_Corpus_and_Parser"))
        self.actionGenerate_Output = QtGui.QAction(ToNgueLP_MW)
        self.actionGenerate_Output.setObjectName(_fromUtf8("actionGenerate_Output"))
        self.actionCompare_Parser_Output_and_XML_Output = QtGui.QAction(ToNgueLP_MW)
        self.actionCompare_Parser_Output_and_XML_Output.setObjectName(_fromUtf8("actionCompare_Parser_Output_and_XML_Output"))
        self.actionGenerate_XML_Output = QtGui.QAction(ToNgueLP_MW)
        self.actionGenerate_XML_Output.setObjectName(_fromUtf8("actionGenerate_XML_Output"))
        self.actionCompare_Parser_and_XML_Output = QtGui.QAction(ToNgueLP_MW)
        self.actionCompare_Parser_and_XML_Output.setObjectName(_fromUtf8("actionCompare_Parser_and_XML_Output"))
        self.actionCompare_XMLs = QtGui.QAction(ToNgueLP_MW)
        self.actionCompare_XMLs.setObjectName(_fromUtf8("actionCompare_XMLs"))
        self.actionUpdate_XMLs_Info = QtGui.QAction(ToNgueLP_MW)
        self.actionUpdate_XMLs_Info.setObjectName(_fromUtf8("actionUpdate_XMLs_Info"))
        self.actionAbout_ToNgueLP = QtGui.QAction(ToNgueLP_MW)
        self.actionAbout_ToNgueLP.setObjectName(_fromUtf8("actionAbout_ToNgueLP"))
        self.actionHelp = QtGui.QAction(ToNgueLP_MW)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionUser_s_Manual = QtGui.QAction(ToNgueLP_MW)
        self.actionUser_s_Manual.setObjectName(_fromUtf8("actionUser_s_Manual"))
        self.actionExit = QtGui.QAction(ToNgueLP_MW)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAdd_case = QtGui.QAction(ToNgueLP_MW)
        self.actionAdd_case.setObjectName(_fromUtf8("actionAdd_case"))
        self.actionEdit_case = QtGui.QAction(ToNgueLP_MW)
        self.actionEdit_case.setObjectName(_fromUtf8("actionEdit_case"))
        self.actionDelete_case = QtGui.QAction(ToNgueLP_MW)
        self.actionDelete_case.setObjectName(_fromUtf8("actionDelete_case"))
        self.actionAdd_annotation = QtGui.QAction(ToNgueLP_MW)
        self.actionAdd_annotation.setObjectName(_fromUtf8("actionAdd_annotation"))
        self.actionEdit_annotation = QtGui.QAction(ToNgueLP_MW)
        self.actionEdit_annotation.setObjectName(_fromUtf8("actionEdit_annotation"))
        self.actionDelete_annotation = QtGui.QAction(ToNgueLP_MW)
        self.actionDelete_annotation.setObjectName(_fromUtf8("actionDelete_annotation"))
        self.menuCorpus.addAction(self.actionLoad_New_Corpus)
        self.menuCorpus.addAction(self.actionAdd_New_Corpus_Doc)
        self.menuCorpus.addAction(self.actionSave_Corpus)
        self.menuCorpus.addAction(self.actionCorpus_Information)
        self.menuCorpus.addAction(self.actionSelect_Parser)
        self.menuCorpus.addAction(self.actionSuggest_Parser)
        self.menuCorpus.addSeparator()
        self.menuCorpus.addAction(self.actionExit)
        self.menuTools.addAction(self.actionMain_View)
        self.menuTools.addAction(self.actionComparison_View)
        self.menuTools.addAction(self.actionDictionary_View)
        self.menuScripts.addAction(self.actionConvert_Documents)
        self.menuScripts.addAction(self.actionVerify_Corpus_and_Parser)
        self.menuScripts.addAction(self.actionGenerate_XML_Output)
        self.menuScripts.addAction(self.actionCompare_XMLs)
        self.menuScripts.addAction(self.actionUpdate_XMLs_Info)
        self.menuHelp.addAction(self.actionAbout_ToNgueLP)
        self.menuHelp.addAction(self.actionUser_s_Manual)
        self.menuCases.addAction(self.actionAdd_case)
        self.menuCases.addAction(self.actionEdit_case)
        self.menuCases.addAction(self.actionDelete_case)
        self.menuAnnotations.addAction(self.actionAdd_annotation)
        self.menuAnnotations.addAction(self.actionEdit_annotation)
        self.menuAnnotations.addAction(self.actionDelete_annotation)
        self.menubar.addAction(self.menuCorpus.menuAction())
        self.menubar.addAction(self.menuCases.menuAction())
        self.menubar.addAction(self.menuAnnotations.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuScripts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLogin.menuAction())
        self.toolBar_Main.addAction(self.actionLoad_New_Corpus)
        self.toolBar_Main.addAction(self.actionAdd_New_Corpus_Doc)
        self.toolBar_Main.addAction(self.actionCorpus_Information)
        self.toolBar_Main.addAction(self.actionClose_Corpus)
        self.toolBar_Main.addAction(self.actionAdd_Algorithm_Output)
        self.toolBar_Cases.addAction(self.actionAdd_New_Case)
        self.toolBar_Cases.addAction(self.actionEdit_Case)
        self.toolBar_Cases.addAction(self.actionValidate_Case)
        self.toolBar_Cases.addAction(self.action_Re_Define_Boundaries)
        self.toolBar_Cases.addAction(self.actionView_Annotation)

        self.retranslateUi(ToNgueLP_MW)
        self.corpusTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ToNgueLP_MW)

    def retranslateUi(self, ToNgueLP_MW):
        ToNgueLP_MW.setWindowTitle(QtGui.QApplication.translate("ToNgueLP_MW", "ToNgueLP", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCorpus.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Corpus", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfig.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScripts.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Scripts", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLogin.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCases.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Cases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAnnotations.setTitle(QtGui.QApplication.translate("ToNgueLP_MW", "Annotations", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Main.setWindowTitle(QtGui.QApplication.translate("ToNgueLP_MW", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Fixed.setWindowTitle(QtGui.QApplication.translate("ToNgueLP_MW", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_Cases.setWindowTitle(QtGui.QApplication.translate("ToNgueLP_MW", "toolBar_3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_New_Corpus.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Load New Corpus", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Corpus_Doc.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Add New Corpus Doc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCorpus_Information.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Corpus Information", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Corpus.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Close Corpus", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Algorithm_Output.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Add Algorithm Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Add New Case", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Edit Case", None, QtGui.QApplication.UnicodeUTF8))
        self.actionValidate_Case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Validate Case", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Re_Define_Boundaries.setText(QtGui.QApplication.translate("ToNgueLP_MW", "(Re)Define Boundaries", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Annotation.setText(QtGui.QApplication.translate("ToNgueLP_MW", "View Annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Corpus.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Save Corpus", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Parser.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Select Parser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuggest_Parser.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Suggest Parser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMain_View.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Main View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionComparison_View.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Comparison View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDictionary_View.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Dictionary View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_Documents.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Convert Documents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerify_Corpus_and_Parser.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Verify Corpus and Parser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_Output.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Generate Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompare_Parser_Output_and_XML_Output.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Compare Parser Output and XML Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_XML_Output.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Generate XML Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompare_Parser_and_XML_Output.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Compare Parser and XML Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompare_XMLs.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Compare XMLs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_XMLs_Info.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Update XMLs Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_ToNgueLP.setText(QtGui.QApplication.translate("ToNgueLP_MW", "About ToNgueLP", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUser_s_Manual.setText(QtGui.QApplication.translate("ToNgueLP_MW", "User\'s Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("ToNgueLP_MW", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Add case", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Edit case", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_case.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Delete case", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_annotation.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Add annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_annotation.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Edit annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_annotation.setText(QtGui.QApplication.translate("ToNgueLP_MW", "Delete annotation", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
