# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cases_view.ui'
#
# Created: Thu Sep 17 01:08:25 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(805, 545)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.lb_note_id = QtGui.QLabel(Form)
        self.lb_note_id.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_id.setObjectName(_fromUtf8("lb_note_id"))
        self.verticalLayout_2.addWidget(self.lb_note_id)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_7 = QtGui.QFrame(Form)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout.addWidget(self.line_7)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.lb_note_type = QtGui.QLabel(Form)
        self.lb_note_type.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_type.setObjectName(_fromUtf8("lb_note_type"))
        self.verticalLayout_3.addWidget(self.lb_note_type)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line_8 = QtGui.QFrame(Form)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout.addWidget(self.line_8)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_6 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.lb_note_projection = QtGui.QLabel(Form)
        self.lb_note_projection.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_projection.setObjectName(_fromUtf8("lb_note_projection"))
        self.verticalLayout_4.addWidget(self.lb_note_projection)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line_9 = QtGui.QFrame(Form)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.horizontalLayout.addWidget(self.line_9)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_7 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)
        self.lb_note_susp = QtGui.QLabel(Form)
        self.lb_note_susp.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_susp.setObjectName(_fromUtf8("lb_note_susp"))
        self.verticalLayout_5.addWidget(self.lb_note_susp)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.line_10 = QtGui.QFrame(Form)
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.horizontalLayout.addWidget(self.line_10)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_8 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_6.addWidget(self.label_8)
        self.lb_note_src = QtGui.QLabel(Form)
        self.lb_note_src.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_src.setObjectName(_fromUtf8("lb_note_src"))
        self.verticalLayout_6.addWidget(self.lb_note_src)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.line_11 = QtGui.QFrame(Form)
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.horizontalLayout.addWidget(self.line_11)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.lb_note_author = QtGui.QLabel(Form)
        self.lb_note_author.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_author.setObjectName(_fromUtf8("lb_note_author"))
        self.verticalLayout_7.addWidget(self.lb_note_author)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.line_12 = QtGui.QFrame(Form)
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.horizontalLayout.addWidget(self.line_12)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_10 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.lb_note_date = QtGui.QLabel(Form)
        self.lb_note_date.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_date.setObjectName(_fromUtf8("lb_note_date"))
        self.verticalLayout_8.addWidget(self.lb_note_date)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.line_13 = QtGui.QFrame(Form)
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.horizontalLayout.addWidget(self.line_13)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_11 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_9.addWidget(self.label_11)
        self.lb_note_human_val = QtGui.QLabel(Form)
        self.lb_note_human_val.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_human_val.setObjectName(_fromUtf8("lb_note_human_val"))
        self.verticalLayout_9.addWidget(self.lb_note_human_val)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.line_14 = QtGui.QFrame(Form)
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.horizontalLayout.addWidget(self.line_14)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_12 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_10.addWidget(self.label_12)
        self.lb_note_machine_recog = QtGui.QLabel(Form)
        self.lb_note_machine_recog.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_note_machine_recog.setObjectName(_fromUtf8("lb_note_machine_recog"))
        self.verticalLayout_10.addWidget(self.lb_note_machine_recog)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.lb_src_info = QtGui.QLabel(Form)
        self.lb_src_info.setObjectName(_fromUtf8("lb_src_info"))
        self.verticalLayout_13.addWidget(self.lb_src_info)
        self.text_src = QtGui.QTextEdit(Form)
        self.text_src.setObjectName(_fromUtf8("text_src"))
        self.verticalLayout_13.addWidget(self.text_src)
        self.gridLayout.addLayout(self.verticalLayout_13, 10, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_prev_note = QtGui.QPushButton(Form)
        self.btn_prev_note.setObjectName(_fromUtf8("btn_prev_note"))
        self.horizontalLayout_2.addWidget(self.btn_prev_note)
        self.lb_note_current = QtGui.QLabel(Form)
        self.lb_note_current.setObjectName(_fromUtf8("lb_note_current"))
        self.horizontalLayout_2.addWidget(self.lb_note_current)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lb_note_count = QtGui.QLabel(Form)
        self.lb_note_count.setObjectName(_fromUtf8("lb_note_count"))
        self.horizontalLayout_2.addWidget(self.lb_note_count)
        self.btn_next_note = QtGui.QPushButton(Form)
        self.btn_next_note.setObjectName(_fromUtf8("btn_next_note"))
        self.horizontalLayout_2.addWidget(self.btn_next_note)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.case_details = QtGui.QLabel(Form)
        self.case_details.setObjectName(_fromUtf8("case_details"))
        self.verticalLayout_12.addWidget(self.case_details)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_12.addWidget(self.line_5)
        self.lb_susp_info = QtGui.QLabel(Form)
        self.lb_susp_info.setObjectName(_fromUtf8("lb_susp_info"))
        self.verticalLayout_12.addWidget(self.lb_susp_info)
        self.text_susp = QtGui.QTextEdit(Form)
        self.text_susp.setObjectName(_fromUtf8("text_susp"))
        self.verticalLayout_12.addWidget(self.text_susp)
        self.gridLayout.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 9, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lb_susp_sentence = QtGui.QLabel(Form)
        self.lb_susp_sentence.setObjectName(_fromUtf8("lb_susp_sentence"))
        self.verticalLayout.addWidget(self.lb_susp_sentence)
        self.lb_src_sentence = QtGui.QLabel(Form)
        self.lb_src_sentence.setObjectName(_fromUtf8("lb_src_sentence"))
        self.verticalLayout.addWidget(self.lb_src_sentence)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "ID", None))
        self.lb_note_id.setText(_translate("Form", "1", None))
        self.label_5.setText(_translate("Form", "Type", None))
        self.lb_note_type.setText(_translate("Form", "Same Polarity", None))
        self.label_6.setText(_translate("Form", "Projection", None))
        self.lb_note_projection.setText(_translate("Form", "Local", None))
        self.label_7.setText(_translate("Form", "Susp\n"
"Offset / Len", None))
        self.lb_note_susp.setText(_translate("Form", "10", None))
        self.label_8.setText(_translate("Form", "Src\n"
"Offset / Len", None))
        self.lb_note_src.setText(_translate("Form", "50", None))
        self.label_9.setText(_translate("Form", "Author", None))
        self.lb_note_author.setText(_translate("Form", "Leonel", None))
        self.label_10.setText(_translate("Form", "Date", None))
        self.lb_note_date.setText(_translate("Form", "07-04-2015", None))
        self.label_11.setText(_translate("Form", "Validated \n"
"by Humans", None))
        self.lb_note_human_val.setText(_translate("Form", "True", None))
        self.label_12.setText(_translate("Form", "Artificially\n"
"Recognized", None))
        self.lb_note_machine_recog.setText(_translate("Form", "False", None))
        self.lb_src_info.setText(_translate("Form", "<html><head/><body><p>[<span style=\" font-weight:600;\">Source</span>]     doc-name = <span style=\" font-weight:600;\">src-1111</span>, length = <span style=\" font-weight:600;\">555</span> char(s), <span style=\" font-weight:600;\">1</span> word(s), <span style=\" font-weight:600;\">1</span> sentence(s), offset = <span style=\" font-weight:600;\">10</span></p></body></html>", None))
        self.text_src.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto fuente</p></body></html>", None))
        self.btn_prev_note.setText(_translate("Form", "Prev", None))
        self.lb_note_current.setText(_translate("Form", "#", None))
        self.label_3.setText(_translate("Form", "/", None))
        self.lb_note_count.setText(_translate("Form", "total", None))
        self.btn_next_note.setText(_translate("Form", "Next", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Annotation Details</span></p></body></html>", None))
        self.case_details.setText(_translate("Form", "Case details", None))
        self.lb_susp_info.setText(_translate("Form", "<html><head/><body><p>[<span style=\" font-weight:600;\">Suspicious</span>]    doc-name = <span style=\" font-weight:600;\">susp-1111</span>, length = <span style=\" font-weight:600;\">555</span> char(s), <span style=\" font-weight:600;\">1</span> word(s), <span style=\" font-weight:600;\">1</span> sentence(s), offset = <span style=\" font-weight:600;\">10</span></p></body></html>", None))
        self.text_susp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto sospechoso</p></body></html>", None))
        self.lb_susp_sentence.setText(_translate("Form", "Susp Sentence", None))
        self.lb_src_sentence.setText(_translate("Form", "Src Sentence", None))

