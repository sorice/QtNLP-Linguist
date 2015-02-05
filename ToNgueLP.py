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
from ui.ToNgueLP_MW import TNLP_MW

# global app information
appName = "ToNgueLP"
<<<<<<< TREE
appVersion = "0.2.1"
=======
appVersion = "0.2.1 (Sassure)"
>>>>>>> MERGE-SOURCE

if __name__ == '__main__':
   # create application
   app = QApplication(sys.argv)
   app.setApplicationName(appName)

   # create widget
   w = TNLP_MW(appName, appVersion)
   w.show()

   # connection
   QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

   # execute application
   sys.exit(app.exec_())
