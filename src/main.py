from PySide2.QtWidgets import QMainWindow, QApplication, QListView, QGraphicsScene
from PySide2.QtGui import QImage, QColor
from Modules.Surface import Surface
from Modules.ToolHandler import ToolHandler
from UI import ParentEditor
from Modules import Surface, Map, ToolHandler, Global, Canvas
from utils import GenerateMap

class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        Global.Tool_Box.set_fill_color(QColor(255,0,0,255))
        # Init UI
        self.ui = ParentEditor.Ui_MainWindow()
        self.ui.setupUi(self)

        # Init Glyph
        self.Map = GenerateMap.generateMap(40,40,Global.Image_Format)
        self.MapModel = Map.MapModel(Map=self.Map)

        self.ui.GlyphPalette.setViewMode(QListView.IconMode)
        self.ui.GlyphPalette.setModel(self.MapModel)

        self.Canvas = Canvas.Canvas(self.Map[0][1])
        self.Scene = QGraphicsScene()
        self.Scene.addItem(self.Canvas)
        self.ui.ViewPort.setScene(self.Scene)




EventCycle = QApplication([])
MainWindow = ParentWindow()
MainWindow.show()
EventCycle.exec_()