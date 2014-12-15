#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
# add current ToNgueLP location to python PATH to locate modules
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import main window
from ui.ToNgueLP_MW import ToNgueLP_MW

# global app information
appName = "ToNgueLP"
appVersion = "0.2.1"

if __name__ == '__main__':
   # create application
   app = QApplication(sys.argv)
   app.setApplicationName(appName)

   # create widget
   w = ToNgueLP_MW(appName, appVersion)
   w.show()

   # connection
   QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

   # execute application
   sys.exit(app.exec_())
