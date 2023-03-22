from PySide2.QtGui import QColor
from PySide2.QtCore import Signal, QObject

class ToolHandler(QObject):
    ToolChanged = Signal(int)
    OutlineColorChanged = Signal(QColor)
    FillColorChanged = Signal(QColor)

    def __init__(self) -> None:
        super().__init__()
        self.toolList = ['brush', 'eraser', 'line', 'fill', 'circle', 'rect', 'select']
        self.fillColor = QColor(0,0,0,0)
        self.outlineColor = QColor(0,0,0,0)
        self.currentTool = self.toolList[0]
        self.size = 1
    def set_fill_color(self, color: QColor):
        self.fillColor = color
        self.FillColorChanged.emit(self.fillColor)
    def set_outline_color(self, color: QColor):
        self.outlineColor = color
        self.OutlineColorChanged.emit(self.outlineColor)
    def set_size(self, size: int):
        self.size = size
    def set_tool(self, index):
        # brush, eraser, line, circle, rect, fill, select
        self.currentTool = self.toolList[index]
        print(f"Current Tool: {self.currentTool}")
        self.ToolChanged.emit(index)
