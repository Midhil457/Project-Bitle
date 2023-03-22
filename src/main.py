from PySide2.QtWidgets import QMainWindow, QApplication, QListView, QGraphicsScene
from PySide2.QtGui import QImage, QColor, QIcon, QCursor, Qt
from PySide2.QtCore import QModelIndex
from Modules.Surface import Surface
from Modules.ToolHandler import ToolHandler
from UI import ParentEditor
from Modules import Surface, Map, ToolHandler, Global, Canvas, ColorSelector
from utils import GenerateMap

class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        Global.Tool_Box.set_fill_color(QColor(255,0,0,255))
        # Init UI
        self.ui = ParentEditor.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Project-Bitle')
        self.setWindowIcon(QIcon('/res/Icon.png'))
        # Init Glyph
        self.Map = GenerateMap.generateMap(40,40,Global.Image_Format)
        self.MapModel = Map.MapModel(Map=self.Map)

        self.ui.GlyphPalette.setViewMode(QListView.IconMode)
        self.ui.GlyphPalette.setModel(self.MapModel)
        self.ui.GlyphPalette.setCurrentIndex(self.MapModel.index(0,0))
        
        #Init Canvas
        self.Scene = Canvas.Viewport(self.Map[self.ui.GlyphPalette.currentIndex().row()][1])
        self.ui.ViewPort.setScene(self.Scene)
        self.ui.ViewPort.scale(10,10)
        self.ui.ViewPort.setMouseTracking(True)
    
        Global.Tool_Box.ToolChanged.connect(self.ui.ToolSettingsStack.setCurrentIndex)
        
        #Tools
        self.ui.BrushTool.toggled.connect(lambda state : Global.Tool_Box.set_tool(0) if state else None)
        self.ui.EraserTool.toggled.connect(lambda state :Global.Tool_Box.set_tool(1) if state else None)
        self.ui.LineTool.toggled.connect(lambda state :Global.Tool_Box.set_tool(2) if state else None)
        self.ui.FillTool.toggled.connect(lambda state :Global.Tool_Box.set_tool(3) if state else None)
        

        self.ui.PrimaryColorSelector.clicked.connect(self.openColorSelector)
        self.ui.ViewPort.setCursor(Qt.BlankCursor)
        self.ui.GlyphPalette.clicked.connect(self.setCharacter)
        
    def setCharacter(self,index: QModelIndex):
        print(self.Map[index.row()][1])
        self.Scene.setSurface(self.Map[index.row()][1])
    
    def openColorSelector(self):
        self.ColorDlg = ColorSelector.ColorSelectorDialog()
        self.ColorDlg.exec_()
        self.ui.PrimaryColorSelector.setText(self.ColorDlg.selectedColor.name())
        Global.Tool_Box.set_outline_color(self.ColorDlg.selectedColor)
        





EventCycle = QApplication([])
MainWindow = ParentWindow()
MainWindow.show()
EventCycle.exec_()