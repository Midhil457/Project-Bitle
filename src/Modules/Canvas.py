from PySide2.QtWidgets import QGraphicsItemGroup, QGraphicsPixmapItem, QGraphicsSceneMouseEvent, QGraphicsScene
from PySide2.QtGui import QPixmap, QBrush, QColor
from Modules.Surface import Surface
from PySide2.QtGui import QPainterPath, QPainter
from PySide2.QtCore import Signal, Qt
import Modules.Global, Modules.ToolHandler

class Viewport(QGraphicsScene):
    drawingFinished = Signal()
    
    def __init__(self, surface: Surface) -> None:
        super().__init__()
        print(self.items())
        self.PrimaryCanvas = surface
        self.Overlay = Surface(surface.getWidth(),surface.getHeight(),Modules.Global.Image_Format)
        self.UIOverlay = Surface(surface.getWidth(),surface.getHeight(),Modules.Global.Image_Format)
        
        self.BackgroundPattern = QBrush()
        self.BackgroundPattern.setTexture(QPixmap('/home/midhil/Documents/GitHub/Midhil457/Project-Bitle/res/BackgroundPattern.png'))
        self.BackgroundImage = Surface(surface.getWidth(),surface.getHeight(),Modules.Global.Image_Format)
        self.BackgroundImage.fill(self.BackgroundPattern)
        self.addItem(self.BackgroundImage)
        self.addItem(self.PrimaryCanvas)
        self.addItem(self.Overlay)
        self.addItem(self.UIOverlay)
        self.Overlay.setZValue(1000)
        self.UIOverlay.setZValue(2000)
        self.startPoint = 0
        Modules.Global.Tool_Box.OutlineColorChanged.connect(self.Overlay.setPenColor)
        Modules.Global.Tool_Box.OutlineColorChanged.connect(self.UIOverlay.setPenColor)
        
    def setSurface(self,surface: Surface):
        self.removeItem(self.PrimaryCanvas)
        self.PrimaryCanvas = surface
        self.addItem(self.PrimaryCanvas)
    
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(event)
        
        self.startPoint = event.scenePos()
        if  Modules.Global.Tool_Box.currentTool == 'brush':
            self.Path = QPainterPath()
            self.Path.moveTo(self.startPoint.x(),self.startPoint.y())
            self.Overlay.drawPoint(self.startPoint.x(),self.startPoint.y())
        
        if  Modules.Global.Tool_Box.currentTool == 'line':
            self.Overlay.drawPoint(self.startPoint.x(),self.startPoint.y())
        
        if  Modules.Global.Tool_Box.currentTool == 'fill':
            self.PrimaryCanvas.floodfill(round(event.scenePos().x()),round(event.scenePos().y()))

            
            
                
        
    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(event)
        self.UIOverlay.clear()
        self.UIOverlay.drawPoint(round(event.scenePos().x()),round(event.scenePos().y()))
        if self.startPoint:
            self.Overlay.clear()
            if  Modules.Global.Tool_Box.currentTool == 'brush':
                self.Path.lineTo(round(event.scenePos().x()),round(event.scenePos().y()))
                self.Overlay.drawPath(self.Path)
            
            if  Modules.Global.Tool_Box.currentTool == 'line':
                self.Overlay.drawLine(round(self.startPoint.x()),self.startPoint.y(),round(event.scenePos().x()),round(event.scenePos().y()))
        
    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print(event)
        self.startPoint = 0
        self.PrimaryCanvas.drawImage(self.Overlay.getImage())
        self.Overlay.clear()
        self.drawingFinished.emit()
        
        print(self.items())