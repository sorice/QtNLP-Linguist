#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#TODO refactorize to get a better aproach of this class

class TNLP_QWizardPage(QWizardPage):
   def __init__(self, parent = None):
      # init parent
      super(TNLP_QWizardPage, self).__init__(parent)


   def isComplete(self):
      """Reimplemented for edit case only"""

      result = True

      if self.findChild(QLineEdit, 'le_description').text().trimmed() == "":
         result = False
      if self.findChild(QLineEdit, 'le_summary').text().trimmed() == "":
         result = False
      if self.findChild(QLineEdit, 'le_original_corpus_id').text().trimmed() == "":
         result = False
      if self.findChild(QLineEdit, 'le_original_corpus').text().trimmed() == "":
         result = False
      if self.findChild(QLineEdit, 'le_generator_name').text().trimmed() == "":
         result = False

      return result
