# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_annotation.ui'
#
# Created: Wed Sep 16 16:09:45 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Add_Annotation(object):
    def setupUi(self, Add_Annotation):
        Add_Annotation.setObjectName(_fromUtf8("Add_Annotation"))
        Add_Annotation.setWindowModality(QtCore.Qt.WindowModal)
        Add_Annotation.resize(788, 546)
        self.gridLayout = QtGui.QGridLayout(Add_Annotation)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(Add_Annotation)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lb_case_name = QtGui.QLabel(Add_Annotation)
        self.lb_case_name.setObjectName(_fromUtf8("lb_case_name"))
        self.horizontalLayout_7.addWidget(self.lb_case_name)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Add_Annotation)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_author = QtGui.QLineEdit(Add_Annotation)
        self.le_author.setObjectName(_fromUtf8("le_author"))
        self.horizontalLayout.addWidget(self.le_author)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Add_Annotation)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cb_type = QtGui.QComboBox(Add_Annotation)
        self.cb_type.setObjectName(_fromUtf8("cb_type"))
        self.horizontalLayout_2.addWidget(self.cb_type)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Add_Annotation)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cb_projection = QtGui.QComboBox(Add_Annotation)
        self.cb_projection.setObjectName(_fromUtf8("cb_projection"))
        self.cb_projection.addItem(_fromUtf8(""))
        self.cb_projection.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cb_projection)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.line = QtGui.QFrame(Add_Annotation)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_12 = QtGui.QLabel(Add_Annotation)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.te_susp_snippet = QtGui.QTextEdit(Add_Annotation)
        self.te_susp_snippet.setReadOnly(True)
        self.te_susp_snippet.setObjectName(_fromUtf8("te_susp_snippet"))
        self.verticalLayout.addWidget(self.te_susp_snippet)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_10 = QtGui.QLabel(Add_Annotation)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.lb_susp_sentence = QtGui.QLabel(Add_Annotation)
        self.lb_susp_sentence.setText(_fromUtf8(""))
        self.lb_susp_sentence.setObjectName(_fromUtf8("lb_susp_sentence"))
        self.verticalLayout_2.addWidget(self.lb_susp_sentence)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(Add_Annotation)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lb_susp_offset = QtGui.QLabel(Add_Annotation)
        self.lb_susp_offset.setObjectName(_fromUtf8("lb_susp_offset"))
        self.horizontalLayout_5.addWidget(self.lb_susp_offset)
        self.label_5 = QtGui.QLabel(Add_Annotation)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lb_susp_length = QtGui.QLabel(Add_Annotation)
        self.lb_susp_length.setObjectName(_fromUtf8("lb_susp_length"))
        self.horizontalLayout_5.addWidget(self.lb_susp_length)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_13 = QtGui.QLabel(Add_Annotation)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.te_src_snippet = QtGui.QTextEdit(Add_Annotation)
        self.te_src_snippet.setReadOnly(True)
        self.te_src_snippet.setObjectName(_fromUtf8("te_src_snippet"))
        self.verticalLayout_3.addWidget(self.te_src_snippet)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.label_11 = QtGui.QLabel(Add_Annotation)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.lb_src_sentence = QtGui.QLabel(Add_Annotation)
        self.lb_src_sentence.setText(_fromUtf8(""))
        self.lb_src_sentence.setObjectName(_fromUtf8("lb_src_sentence"))
        self.verticalLayout_4.addWidget(self.lb_src_sentence)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(Add_Annotation)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lb_src_offset = QtGui.QLabel(Add_Annotation)
        self.lb_src_offset.setObjectName(_fromUtf8("lb_src_offset"))
        self.horizontalLayout_6.addWidget(self.lb_src_offset)
        self.label_7 = QtGui.QLabel(Add_Annotation)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lb_src_length = QtGui.QLabel(Add_Annotation)
        self.lb_src_length.setObjectName(_fromUtf8("lb_src_length"))
        self.horizontalLayout_6.addWidget(self.lb_src_length)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.btn_add_annotation = QtGui.QPushButton(Add_Annotation)
        self.btn_add_annotation.setObjectName(_fromUtf8("btn_add_annotation"))
        self.horizontalLayout_11.addWidget(self.btn_add_annotation)
        self.pushButton_2 = QtGui.QPushButton(Add_Annotation)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Add_Annotation)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)

        self.retranslateUi(Add_Annotation)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Add_Annotation.close)
        QtCore.QMetaObject.connectSlotsByName(Add_Annotation)
        Add_Annotation.setTabOrder(self.le_author, self.cb_type)
        Add_Annotation.setTabOrder(self.cb_type, self.cb_projection)
        Add_Annotation.setTabOrder(self.cb_projection, self.te_susp_snippet)
        Add_Annotation.setTabOrder(self.te_susp_snippet, self.te_src_snippet)
        Add_Annotation.setTabOrder(self.te_src_snippet, self.btn_add_annotation)
        Add_Annotation.setTabOrder(self.btn_add_annotation, self.pushButton_2)

    def retranslateUi(self, Add_Annotation):
        Add_Annotation.setWindowTitle(QtGui.QApplication.translate("Add_Annotation", "Add annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Add_Annotation", "Annotation for case", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_case_name.setText(QtGui.QApplication.translate("Add_Annotation", "case name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Add_Annotation", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Add_Annotation", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Add_Annotation", "Projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_projection.setItemText(0, QtGui.QApplication.translate("Add_Annotation", "local", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_projection.setItemText(1, QtGui.QApplication.translate("Add_Annotation", "global", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Add_Annotation", "Suspicious snippet:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Add_Annotation", "Suspicious chunk:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Add_Annotation", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_offset.setText(QtGui.QApplication.translate("Add_Annotation", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Add_Annotation", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_susp_length.setText(QtGui.QApplication.translate("Add_Annotation", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Add_Annotation", "Source snippet:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Add_Annotation", "Source chunk:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Add_Annotation", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_offset.setText(QtGui.QApplication.translate("Add_Annotation", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Add_Annotation", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_src_length.setText(QtGui.QApplication.translate("Add_Annotation", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_annotation.setText(QtGui.QApplication.translate("Add_Annotation", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Add_Annotation", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

