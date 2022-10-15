from PySide2.QtWidgets import QMainWindow, QApplication, QListView
from PySide2.QtGui import QImage, QColor
from Modules.Surface import Surface
from Modules.ToolHandler import ToolHandler
from UI import ParentEditor
from Modules import Surface, Map, ToolHandler
from utils import GenerateMap

class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Map = GenerateMap.generateMap(40,40,QImage.Format_RGBA64_Premultiplied)
        self.MapModel = Map.MapModel(Map=self.Map)
        ##Init UI
        self.ui = ParentEditor.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.GlyphPalette.setViewMode(QListView.IconMode)
        self.ui.GlyphPalette.setModel(self.MapModel)





EventCycle = QApplication([])
MainWindow = ParentWindow()
MainWindow.show()
EventCycle.exec_()