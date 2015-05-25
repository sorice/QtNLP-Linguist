# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_corpus.ui'
#
# Created: Tue Apr 21 15:13:08 2015
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

class Ui_NewCopus(object):
    def setupUi(self, NewCopus):
        NewCopus.setObjectName(_fromUtf8("NewCopus"))
        NewCopus.setWindowModality(QtCore.Qt.WindowModal)
        NewCopus.resize(433, 193)
        self.gridLayout = QtGui.QGridLayout(NewCopus)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(NewCopus)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(NewCopus)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(NewCopus)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(NewCopus)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.le_name = QtGui.QLineEdit(NewCopus)
        self.le_name.setObjectName(_fromUtf8("le_name"))
        self.verticalLayout_2.addWidget(self.le_name)
        self.le_lang = QtGui.QLineEdit(NewCopus)
        self.le_lang.setObjectName(_fromUtf8("le_lang"))
        self.verticalLayout_2.addWidget(self.le_lang)
        self.le_copyright = QtGui.QLineEdit(NewCopus)
        self.le_copyright.setObjectName(_fromUtf8("le_copyright"))
        self.verticalLayout_2.addWidget(self.le_copyright)
        self.le_authors = QtGui.QLineEdit(NewCopus)
        self.le_authors.setObjectName(_fromUtf8("le_authors"))
        self.verticalLayout_2.addWidget(self.le_authors)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(NewCopus)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(NewCopus)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_8 = QtGui.QLabel(NewCopus)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_6 = QtGui.QLabel(NewCopus)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.sb_version = QtGui.QSpinBox(NewCopus)
        self.sb_version.setMinimum(1)
        self.sb_version.setObjectName(_fromUtf8("sb_version"))
        self.verticalLayout_4.addWidget(self.sb_version)
        self.le_license = QtGui.QLineEdit(NewCopus)
        self.le_license.setObjectName(_fromUtf8("le_license"))
        self.verticalLayout_4.addWidget(self.le_license)
        self.le_country = QtGui.QLineEdit(NewCopus)
        self.le_country.setObjectName(_fromUtf8("le_country"))
        self.verticalLayout_4.addWidget(self.le_country)
        self.le_owners = QtGui.QLineEdit(NewCopus)
        self.le_owners.setObjectName(_fromUtf8("le_owners"))
        self.verticalLayout_4.addWidget(self.le_owners)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_save = QtGui.QPushButton(NewCopus)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.pushButton_2 = QtGui.QPushButton(NewCopus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.retranslateUi(NewCopus)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), NewCopus.close)
        QtCore.QMetaObject.connectSlotsByName(NewCopus)
        NewCopus.setTabOrder(self.le_name, self.sb_version)
        NewCopus.setTabOrder(self.sb_version, self.le_lang)
        NewCopus.setTabOrder(self.le_lang, self.le_license)
        NewCopus.setTabOrder(self.le_license, self.le_copyright)
        NewCopus.setTabOrder(self.le_copyright, self.le_country)
        NewCopus.setTabOrder(self.le_country, self.le_authors)
        NewCopus.setTabOrder(self.le_authors, self.le_owners)
        NewCopus.setTabOrder(self.le_owners, self.btn_save)
        NewCopus.setTabOrder(self.btn_save, self.pushButton_2)

    def retranslateUi(self, NewCopus):
        NewCopus.setWindowTitle(_translate("NewCopus", "New Corpus", None))
        self.label.setText(_translate("NewCopus", "Name:", None))
        self.label_3.setText(_translate("NewCopus", "Language:", None))
        self.label_5.setText(_translate("NewCopus", "Copyright:", None))
        self.label_7.setText(_translate("NewCopus", "Author(s):", None))
        self.le_name.setToolTip(_translate("NewCopus", "Corpus name", None))
        self.le_lang.setToolTip(_translate("NewCopus", "Language: es, us, fr, ...", None))
        self.le_copyright.setToolTip(_translate("NewCopus", "Copyright: copyleft, ...", None))
        self.le_authors.setToolTip(_translate("NewCopus", "Authors, comma separated", None))
        self.label_2.setText(_translate("NewCopus", "Version:", None))
        self.label_4.setText(_translate("NewCopus", "License:", None))
        self.label_8.setText(_translate("NewCopus", "Country:", None))
        self.label_6.setText(_translate("NewCopus", "Owner(s):", None))
        self.sb_version.setToolTip(_translate("NewCopus", "Corpus version", None))
        self.le_license.setToolTip(_translate("NewCopus", "License: CC, GPL, ...", None))
        self.le_country.setToolTip(_translate("NewCopus", "Country, comma separated", None))
        self.le_owners.setToolTip(_translate("NewCopus", "Owners, comma separated", None))
        self.btn_save.setText(_translate("NewCopus", "Save", None))
        self.pushButton_2.setText(_translate("NewCopus", "Cancel", None))

