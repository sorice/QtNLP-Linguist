# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_case_wizard_general.ui'
#
# Created: Tue Apr 21 15:13:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(550, 198)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_10.addWidget(self.label_20)
        self.lb_corpus_name = QtGui.QLabel(Dialog)
        self.lb_corpus_name.setObjectName(_fromUtf8("lb_corpus_name"))
        self.horizontalLayout_10.addWidget(self.lb_corpus_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_9.addWidget(self.label_18)
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_9.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_9.addWidget(self.label_22)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.cb_problem_type = QtGui.QComboBox(Dialog)
        self.cb_problem_type.setObjectName(_fromUtf8("cb_problem_type"))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.cb_problem_type.addItem(_fromUtf8(""))
        self.verticalLayout_10.addWidget(self.cb_problem_type)
        self.le_description = QtGui.QLineEdit(Dialog)
        self.le_description.setObjectName(_fromUtf8("le_description"))
        self.verticalLayout_10.addWidget(self.le_description)
        self.le_summary = QtGui.QLineEdit(Dialog)
        self.le_summary.setObjectName(_fromUtf8("le_summary"))
        self.verticalLayout_10.addWidget(self.le_summary)
        self.le_original_corpus_id = QtGui.QLineEdit(Dialog)
        self.le_original_corpus_id.setObjectName(_fromUtf8("le_original_corpus_id"))
        self.verticalLayout_10.addWidget(self.le_original_corpus_id)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.horizontalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_11.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(Dialog)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_11.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(Dialog)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_11.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(Dialog)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_11.addWidget(self.label_26)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.cb_text_extension = QtGui.QComboBox(Dialog)
        self.cb_text_extension.setObjectName(_fromUtf8("cb_text_extension"))
        self.cb_text_extension.addItem(_fromUtf8(""))
        self.verticalLayout_12.addWidget(self.cb_text_extension)
        self.cb_plag_type = QtGui.QComboBox(Dialog)
        self.cb_plag_type.setObjectName(_fromUtf8("cb_plag_type"))
        self.verticalLayout_12.addWidget(self.cb_plag_type)
        self.le_original_corpus = QtGui.QLineEdit(Dialog)
        self.le_original_corpus.setObjectName(_fromUtf8("le_original_corpus"))
        self.verticalLayout_12.addWidget(self.le_original_corpus)
        self.le_generator_name = QtGui.QLineEdit(Dialog)
        self.le_generator_name.setObjectName(_fromUtf8("le_generator_name"))
        self.verticalLayout_12.addWidget(self.le_generator_name)
        self.horizontalLayout_11.addLayout(self.verticalLayout_12)
        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_20.setText(_translate("Dialog", "Corpus name:", None))
        self.lb_corpus_name.setText(_translate("Dialog", "name", None))
        self.label_17.setText(_translate("Dialog", "Problem type:", None))
        self.label_18.setText(_translate("Dialog", "Description:", None))
        self.label_21.setText(_translate("Dialog", "Keywords:", None))
        self.label_22.setText(_translate("Dialog", "Original corpus id:", None))
        self.cb_problem_type.setItemText(0, _translate("Dialog", "similarity", None))
        self.cb_problem_type.setItemText(1, _translate("Dialog", "translation", None))
        self.label_23.setText(_translate("Dialog", "Text extension:", None))
        self.label_24.setText(_translate("Dialog", "Plagiarism type:", None))
        self.label_25.setText(_translate("Dialog", "Original corpus:", None))
        self.label_26.setText(_translate("Dialog", "Added by:", None))
        self.cb_text_extension.setItemText(0, _translate("Dialog", "paragraph", None))

