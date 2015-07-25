# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_case_wizard_src.ui'
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
        Dialog.resize(650, 425)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.te_susp_text = QtGui.QTextEdit(Dialog)
        self.te_susp_text.setReadOnly(True)
        self.te_susp_text.setObjectName(_fromUtf8("te_susp_text"))
        self.gridLayout.addWidget(self.te_susp_text, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout.addWidget(self.label_10)
        self.lb_src_offset = QtGui.QLabel(Dialog)
        self.lb_src_offset.setObjectName(_fromUtf8("lb_src_offset"))
        self.horizontalLayout.addWidget(self.lb_src_offset)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.lb_src_length = QtGui.QLabel(Dialog)
        self.lb_src_length.setObjectName(_fromUtf8("lb_src_length"))
        self.horizontalLayout.addWidget(self.lb_src_length)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.lb_src_sentences_count = QtGui.QLabel(Dialog)
        self.lb_src_sentences_count.setObjectName(_fromUtf8("lb_src_sentences_count"))
        self.horizontalLayout.addWidget(self.lb_src_sentences_count)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_select_src_doc = QtGui.QPushButton(Dialog)
        self.btn_select_src_doc.setObjectName(_fromUtf8("btn_select_src_doc"))
        self.horizontalLayout_2.addWidget(self.btn_select_src_doc)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lb_src_doc_name = QtGui.QLabel(Dialog)
        self.lb_src_doc_name.setObjectName(_fromUtf8("lb_src_doc_name"))
        self.horizontalLayout_3.addWidget(self.lb_src_doc_name)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_10.setText(_translate("Dialog", "Offset:", None))
        self.lb_src_offset.setText(_translate("Dialog", "0", None))
        self.label_11.setText(_translate("Dialog", "Length:", None))
        self.lb_src_length.setText(_translate("Dialog", "0", None))
        self.label_12.setText(_translate("Dialog", "Sentences:", None))
        self.lb_src_sentences_count.setText(_translate("Dialog", "0", None))
        self.btn_select_src_doc.setText(_translate("Dialog", "Select document", None))
        self.label_9.setText(_translate("Dialog", "Doc name:", None))
        self.lb_src_doc_name.setText(_translate("Dialog", "src/", None))

