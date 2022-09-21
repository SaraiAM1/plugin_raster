import os 
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .interfaz import Ui_MainWindow

class interfaz (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn4.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()

    def nombreCmb(self):
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == 0:
                nomVLayer = layer.name()
                self.ui.cmb1.addItem(nomVLayer)
            if layer.type() == 1:
                nomRLayer = layer.name()
                self.ui.lb1.setText(nomRLayer)
