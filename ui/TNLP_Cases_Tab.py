#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#TODO refactorize to get a better aproach of this class

class TNLP_CaseTab(QTabWidget):
   def __init__(self, parent = None):
      # init parent
      super(TNLP_CaseTab, self).__init__(parent)

      # case data
      self.__case = None
      self.__annotations = []
      self.__annotation_index = -1


   def set_case_data(self, _case, _annotations, _index = -1):
      '''Update case data'''

      self.__case = _case
      self.__annotations = _annotations
      self.__annotation_index = _index


   def get_case_data(self):
      '''Returns case data'''

      return (self.__case, self.__annotations, self.__annotation_index)


   def add_annotation(self, _annotation):
      '''Add new annotation to list'''

      self.__annotations.append(_annotation)
      if self.__annotation_index == -1:
         self.__annotation_index += 1
