from PySide2.QtGui import QColor
class ToolHandler:
    def __init__(self) -> None:
        self.toolList = ['brush', 'eraser', 'line', 'circle', 'rect', 'fill', 'select']
        self.fillColor = QColor(0,0,0,0)
        self.outlineColor = QColor(0,0,0,0)
        self.currentTool = self.toolList[0]

    def set_fill_color(self, color: QColor):
        self.fillColor = color
    
    def set_outline_color(self, color: QColor):
        self.outlineColor = color