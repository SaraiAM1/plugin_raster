import os 
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .raster import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Raster")

        self.ejemplo = QAction(QIcon(""),"Raster", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemplo)
        self.ejemplo.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == 0 and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
                vLayer = layer
            if layer.type() == 1:
                rLayer = layer
                self.dialogo.ui.cmb1.addItem(rLayer.name())
                epsg= rLayer.crs().authid()
                self.dialogo.ui.label_3.setText(str(epsg))
                #extend
                ext = rLayer.extent()
                self.dialogo.ui.label_5.setText(str(ext))
                # x minima  
                xmin = ext.xMinimum() 
                self.dialogo.ui.label_6.setText(str(xmin))
                # x maxima
                xmax = ext.xMaximum()
                self.dialogo.ui.label_7.setText(str(xmax))
                #  y minima  
                ymin = ext.yMinimum()
                self.dialogo.ui.label_8.setText(str(ymin))
                # y maxima
                ymax = ext.yMaximum()
                self.dialogo.ui.label_9.setText(str(ymax))
                #Ancho  
                ancho = rLayer.width()
                self.dialogo.ui.label_10.setText(str(ancho))
                #  Alto
                alto = rLayer.height()
                self.dialogo.ui.label_11.setText(str(alto))
                #Tamaño de pixel
                pixelSizeX = rLayer.rasterUnitsPerPixelX()
                self.dialogo.ui.label_12.setText(str(pixelSizeX))
    def unload(self):
        self.IMenu.deleteLaterÇ()
    


