# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_case.ui'
#
# Created: Fri May  8 17:30:08 2015
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
        self.gridLayout = QtGui.QGridLayout(Add_Case)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_19 = QtGui.QLabel(Add_Case)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_9.addWidget(self.label_19)
        self.lb_corpus_name = QtGui.QLabel(Add_Case)
        self.lb_corpus_name.setObjectName(_fromUtf8("lb_corpus_name"))
        self.horizontalLayout_9.addWidget(self.lb_corpus_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Add_Case)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(Add_Case)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(Add_Case)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(Add_Case)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cb_problem_type = QtGui.QComboBox(Add_Case)
        self.cb_problem_type.setObjectName(_fromUtf8("cb_problem_type"))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.cb_problem_type)
        self.le_description = QtGui.QLineEdit(Add_Case)
        self.le_description.setObjectName(_fromUtf8("le_description"))
        self.verticalLayout_2.addWidget(self.le_description)
        self.le_summary = QtGui.QLineEdit(Add_Case)
        self.le_summary.setObjectName(_fromUtf8("le_summary"))
        self.verticalLayout_2.addWidget(self.le_summary)
        self.le_original_corpus_id = QtGui.QLineEdit(Add_Case)
        self.le_original_corpus_id.setObjectName(_fromUtf8("le_original_corpus_id"))
        self.verticalLayout_2.addWidget(self.le_original_corpus_id)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Add_Case)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(Add_Case)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(Add_Case)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(Add_Case)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cb_text_extension = QtGui.QComboBox(Add_Case)
        self.cb_text_extension.setObjectName(_fromUtf8("cb_text_extension"))
        self.cb_text_extension.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.cb_text_extension)
        self.cb_plag_type = QtGui.QComboBox(Add_Case)
        self.cb_plag_type.setObjectName(_fromUtf8("cb_plag_type"))
        self.verticalLayout_4.addWidget(self.cb_plag_type)
        self.le_original_corpus = QtGui.QLineEdit(Add_Case)
        self.le_original_corpus.setObjectName(_fromUtf8("le_original_corpus"))
        self.verticalLayout_4.addWidget(self.le_original_corpus)
        self.le_generator_name = QtGui.QLineEdit(Add_Case)
        self.le_generator_name.setObjectName(_fromUtf8("le_generator_name"))
        self.verticalLayout_4.addWidget(self.le_generator_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_13 = QtGui.QLabel(Add_Case)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_5.addWidget(self.label_13)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.te_susp_text = QtGui.QTextEdit(Add_Case)
        self.te_susp_text.setObjectName(_fromUtf8("te_susp_text"))
        self.horizontalLayout_5.addWidget(self.te_susp_text)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_9 = QtGui.QLabel(Add_Case)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(Add_Case)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_6.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(Add_Case)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_6.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(Add_Case)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_6.addWidget(self.label_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.le_susp_doc_name = QtGui.QLineEdit(Add_Case)
        self.le_susp_doc_name.setObjectName(_fromUtf8("le_susp_doc_name"))
        self.verticalLayout_7.addWidget(self.le_susp_doc_name)
        self.le_susp_offset = QtGui.QLineEdit(Add_Case)
        self.le_susp_offset.setObjectName(_fromUtf8("le_susp_offset"))
        self.verticalLayout_7.addWidget(self.le_susp_offset)
        self.lb_susp_length = QtGui.QLabel(Add_Case)
        self.lb_susp_length.setObjectName(_fromUtf8("lb_susp_length"))
        self.verticalLayout_7.addWidget(self.lb_susp_length)
        self.lb_susp_sentences_count = QtGui.QLabel(Add_Case)
        self.lb_susp_sentences_count.setObjectName(_fromUtf8("lb_susp_sentences_count"))
        self.verticalLayout_7.addWidget(self.lb_susp_sentences_count)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_18 = QtGui.QLabel(Add_Case)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_8.addWidget(self.label_18)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.te_src_text = QtGui.QTextEdit(Add_Case)
        self.te_src_text.setObjectName(_fromUtf8("te_src_text"))
        self.horizontalLayout_7.addWidget(self.te_src_text)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_17 = QtGui.QLabel(Add_Case)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_15 = QtGui.QLabel(Add_Case)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_9.addWidget(self.label_15)
        self.label_14 = QtGui.QLabel(Add_Case)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_9.addWidget(self.label_14)
        self.label_16 = QtGui.QLabel(Add_Case)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_9.addWidget(self.label_16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.le_src_doc_name = QtGui.QLineEdit(Add_Case)
        self.le_src_doc_name.setObjectName(_fromUtf8("le_src_doc_name"))
        self.verticalLayout_10.addWidget(self.le_src_doc_name)
        self.le_src_offset = QtGui.QLineEdit(Add_Case)
        self.le_src_offset.setObjectName(_fromUtf8("le_src_offset"))
        self.verticalLayout_10.addWidget(self.le_src_offset)
        self.lb_src_length = QtGui.QLabel(Add_Case)
        self.lb_src_length.setObjectName(_fromUtf8("lb_src_length"))
        self.verticalLayout_10.addWidget(self.lb_src_length)
        self.lb_src_sentences_count = QtGui.QLabel(Add_Case)
        self.lb_src_sentences_count.setObjectName(_fromUtf8("lb_src_sentences_count"))
        self.verticalLayout_10.addWidget(self.lb_src_sentences_count)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.btn_add_case = QtGui.QPushButton(Add_Case)
        self.btn_add_case.setObjectName(_fromUtf8("btn_add_case"))
        self.horizontalLayout_8.addWidget(self.btn_add_case)
        self.pushButton_2 = QtGui.QPushButton(Add_Case)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 0, 1, 1)

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
        Add_Case.setTabOrder(self.le_susp_doc_name, self.le_susp_offset)
        Add_Case.setTabOrder(self.le_susp_offset, self.te_src_text)
        Add_Case.setTabOrder(self.te_src_text, self.le_src_doc_name)
        Add_Case.setTabOrder(self.le_src_doc_name, self.le_src_offset)
        Add_Case.setTabOrder(self.le_src_offset, self.btn_add_case)
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
        self.label_10.setText(QtGui.QApplication.translate("Add_Case", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Add_Case", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Add_Case", "Sentences:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_susp_doc_name.setText(QtGui.QApplication.translate("Add_Case", "susp/", None, QtGui.QApplication.UnicodeUTF8))
        self.le_susp_offset.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_length.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_sentences_count.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Add_Case", "Source text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Add_Case", "Doc name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Add_Case", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Add_Case", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Add_Case", "Sentences:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_src_doc_name.setText(QtGui.QApplication.translate("Add_Case", "src/", None, QtGui.QApplication.UnicodeUTF8))
        self.le_src_offset.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_length.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_sentences_count.setText(QtGui.QApplication.translate("Add_Case", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_case.setText(QtGui.QApplication.translate("Add_Case", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Add_Case", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

