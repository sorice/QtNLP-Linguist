#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

'''
BEGIN PRUEBA
'''
import os
# adicionar al path de python la raiz del proyecto ToNgueLP para los imports de modulos
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))
#print sys.path
'''
END PRUEBA
'''

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# importar la ventana principal, es necesario el import aqui despues de
# creada la QApplicarion
from ui.ToNgueLP_MW import ToNgueLP_MW

# global app information
appName = "ToNgueLP"
appVersion = "0.1"

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
