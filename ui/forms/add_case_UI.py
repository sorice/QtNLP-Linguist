# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_case.ui'
#
# Created: Sat Apr 18 01:29:28 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Add_Case(object):
    def setupUi(self, Add_Case):
        Add_Case.setObjectName(_fromUtf8("Add_Case"))
        Add_Case.setWindowModality(QtCore.Qt.WindowModal)
        Add_Case.resize(814, 561)
        self.layoutWidget = QtGui.QWidget(Add_Case)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 10, 721, 521))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_9.addWidget(self.label_19)
        self.lb_corpus_name = QtGui.QLabel(self.layoutWidget)
        self.lb_corpus_name.setObjectName(_fromUtf8("lb_corpus_name"))
        self.horizontalLayout_9.addWidget(self.lb_corpus_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cb_problem_type = QtGui.QComboBox(self.layoutWidget)
        self.cb_problem_type.setObjectName(_fromUtf8("cb_problem_type"))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.cb_problem_type.setToolTip('Tipo de problema NLP o grupo de casos en el XML.')
        
        self.verticalLayout_2.addWidget(self.cb_problem_type)
        self.le_description = QtGui.QLineEdit(self.layoutWidget)
        self.le_description.setObjectName(_fromUtf8("le_description"))
        self.le_description.setToolTip(unicode('Descripci\363n opcional del caso para usar como hint.','iso8859-15'))
        
        self.verticalLayout_2.addWidget(self.le_description)
        self.le_summary = QtGui.QLineEdit(self.layoutWidget)
        self.le_summary.setObjectName(_fromUtf8("le_summary"))
        self.le_summary.setToolTip('Escriba 3 palabras de longitud menor a 21 caracteres que podr\341 utilizar en la barra de search.')
        
        self.verticalLayout_2.addWidget(self.le_summary)
        self.le_original_corpus_id = QtGui.QLineEdit(self.layoutWidget)
        self.le_original_corpus_id.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.le_original_corpus_id.setObjectName(_fromUtf8("le_original_corpus_id"))
        self.le_original_corpus_id.setToolTip(unicode('Escriba solo d\355gitos.','iso8859-15'))
        
        self.verticalLayout_2.addWidget(self.le_original_corpus_id)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cb_text_extension = QtGui.QComboBox(self.layoutWidget)
        self.cb_text_extension.setObjectName(_fromUtf8("cb_text_extension"))
        self.cb_text_extension.addItem(_fromUtf8(""))
        self.cb_text_extension.setToolTip('Longitud de los textos del caso: fragmentos, oraciones u otros.')
        
        self.verticalLayout_4.addWidget(self.cb_text_extension)
        self.cb_plag_type = QtGui.QComboBox(self.layoutWidget)
        self.cb_plag_type.setObjectName(_fromUtf8("cb_plag_type"))
        self.cb_plag_type.setToolTip(unicode('Tipolog\355as de par\341frasis propuestas por Barr\363n-Cede\361o2013','iso8859-15'))
        
        self.verticalLayout_4.addWidget(self.cb_plag_type)
        self.le_original_corpus = QtGui.QLineEdit(self.layoutWidget)
        self.le_original_corpus.setObjectName(_fromUtf8("le_original_corpus"))
        self.le_original_corpus.setToolTip('Corpus original del que fue extra\355do el caso.')
        
        self.verticalLayout_4.addWidget(self.le_original_corpus)
        self.le_generator_name = QtGui.QLineEdit(self.layoutWidget)
        self.le_generator_name.setObjectName(_fromUtf8("le_generator_name"))
        self.le_generator_name.setToolTip(unicode('Nombre de la persona o algoritmo que cre\363 el caso.','iso8859-15'))
        
        self.verticalLayout_4.addWidget(self.le_generator_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_6.addWidget(self.label_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.te_susp_text = QtGui.QTextEdit(self.layoutWidget)
        self.te_susp_text.setObjectName(_fromUtf8("te_susp_text"))
        self.te_susp_text.setToolTip('Texto completo del documento sospechoso.')
        
        self.horizontalLayout_12.addWidget(self.te_susp_text)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        self.le_susp_doc_name = QtGui.QLineEdit(self.layoutWidget)
        self.le_susp_doc_name.setObjectName(_fromUtf8("le_susp_doc_name"))
        self.le_susp_doc_name.setToolTip(unicode('Nombre del documento sospechoso sin la extensi\363n.','iso8859-15'))
        
        self.horizontalLayout_11.addWidget(self.le_susp_doc_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lb_susp_offset = QtGui.QLabel(self.layoutWidget)
        self.lb_susp_offset.setObjectName(_fromUtf8("lb_susp_offset"))
        self.horizontalLayout_10.addWidget(self.lb_susp_offset)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.lb_susp_length = QtGui.QLabel(self.layoutWidget)
        self.lb_susp_length.setObjectName(_fromUtf8("lb_susp_length"))
        self.horizontalLayout_5.addWidget(self.lb_susp_length)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.lb_susp_sentences_count = QtGui.QLabel(self.layoutWidget)
        self.lb_susp_sentences_count.setObjectName(_fromUtf8("lb_susp_sentences_count"))
        self.horizontalLayout_4.addWidget(self.lb_susp_sentences_count)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_8.addWidget(self.label_18)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.te_src_text = QtGui.QTextEdit(self.layoutWidget)
        self.te_src_text.setObjectName(_fromUtf8("te_src_text"))
        self.te_src_text.setToolTip('Texto completo del documento fuente.')
        self.horizontalLayout_15.addWidget(self.te_src_text)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_14.addWidget(self.label_17)
        self.le_src_doc_name = QtGui.QLineEdit(self.layoutWidget)
        self.le_src_doc_name.setObjectName(_fromUtf8("le_src_doc_name"))
        self.le_src_doc_name.setToolTip(unicode('Nombre del documento fuente sin la extensi\363n.','iso8859-15'))
        
        self.horizontalLayout_14.addWidget(self.le_src_doc_name)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.lb_src_offset = QtGui.QLabel(self.layoutWidget)
        self.lb_src_offset.setObjectName(_fromUtf8("lb_src_offset"))
        self.horizontalLayout_13.addWidget(self.lb_src_offset)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lb_src_length = QtGui.QLabel(self.layoutWidget)
        self.lb_src_length.setObjectName(_fromUtf8("lb_src_length"))
        self.horizontalLayout_7.addWidget(self.lb_src_length)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.lb_src_sentences_count = QtGui.QLabel(self.layoutWidget)
        self.lb_src_sentences_count.setObjectName(_fromUtf8("lb_src_sentences_count"))
        self.horizontalLayout_6.addWidget(self.lb_src_sentences_count)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.btn_add_case = QtGui.QPushButton(self.layoutWidget)
        self.btn_add_case.setObjectName(_fromUtf8("btn_add_case"))
        self.horizontalLayout_8.addWidget(self.btn_add_case)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Add_Case)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Add_Case.close)
        QtCore.QMetaObject.connectSlotsByName(Add_Case)
        Add_Case.setTabOrder(self.cb_problem_type, self.cb_text_extension)
        Add_Case.setTabOrder(self.cb_text_extension, self.le_description)
        Add_Case.setTabOrder(self.le_description, self.cb_plag_type)
        Add_Case.setTabOrder(self.cb_plag_type, self.le_summary)
        Add_Case.setTabOrder(self.le_summary, self.le_original_corpus)
        Add_Case.setTabOrder(self.le_original_corpus, self.le_original_corpus_id)
        Add_Case.setTabOrder(self.le_original_corpus_id, self.le_generator_name)
        Add_Case.setTabOrder(self.le_generator_name, self.te_susp_text)
        Add_Case.setTabOrder(self.te_susp_text, self.le_susp_doc_name)
        Add_Case.setTabOrder(self.le_susp_doc_name, self.te_src_text)
        Add_Case.setTabOrder(self.te_src_text, self.le_src_doc_name)
        Add_Case.setTabOrder(self.le_src_doc_name, self.btn_add_case)
        Add_Case.setTabOrder(self.btn_add_case, self.pushButton_2)

    def retranslateUi(self, Add_Case):
        Add_Case.setWindowTitle(QtGui.QApplication.translate("Add_Case", "Add Case", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Add_Case", "Corpus name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_corpus_name.setText(QtGui.QApplication.translate("Add_Case", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Add_Case", "Problem type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Add_Case", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Add_Case", "Keywords:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Add_Case", "Original corpus id:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_problem_type.setItemText(0, QtGui.QApplication.translate("Add_Case", "similarity", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_problem_type.setItemText(1, QtGui.QApplication.translate("Add_Case", "translation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Add_Case", "Text extension:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Add_Case", "Plagiarism type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Add_Case", "Original corpus:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Add_Case", "Added by:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_text_extension.setItemText(0, QtGui.QApplication.translate("Add_Case", "paragraph", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Add_Case", "Suspicious text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Add_Case", "Doc name:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_susp_doc_name.setText(QtGui.QApplication.translate("Add_Case", "susp/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Add_Case", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_offset.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Add_Case", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_length.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Add_Case", "Sentences:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_sentences_count.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Add_Case", "Source text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Add_Case", "Doc name:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_src_doc_name.setText(QtGui.QApplication.translate("Add_Case", "src/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Add_Case", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_offset.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Add_Case", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_length.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Add_Case", "Sentences:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_sentences_count.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_case.setText(QtGui.QApplication.translate("Add_Case", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Add_Case", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

