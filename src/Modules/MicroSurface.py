from PySide2.QtWidgets import QGraphicsPixmapItem
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtGui import QPainter, QPainterPath, QPen, QBrush, QColor
from PySide2.QtCore import Qt, QRect


class MicroSurface(QImage):
    def __init__(self, *args):
        super().__init__(*args)
        #Init Image
        
        self.fill(Qt.transparent)
        self.Painter = QPainter(self)
        
        
    
    def erase(self, x: int, y: int, r: int):
        #Todo: Erase an region
        self.setPixelColor(x,y, QColor(0,0,0,0))
        
    
    def drawRect(self, x: int, y: int, w: int, h: int):
        """
        Draw a Rect on the surface
        """
        self.Painter.drawRect(x, y, w, h)
        

    def drawEllipse(self, rect: QRect):
        """
        Draw an Ellipse on the surface
        """
        self.Painter.drawEllipse(rect)
        

    def drawLine(self, x1: int, y1: int, x2: int, y2: int):
        """
        Draw a line on the surface
        """
        self.Painter.drawLine(x1, y1, x2, y2)
        

    def drawText(self, x: int, y: int, w: int, h: int, text: str):
        """
        Draw a Text on the surface
        """
        self.Painter.drawText(x, y, w, h, text=text)
        

    def drawPoint(self, x: int, y: int):
        """
        Draw a Point on the surface
        """
        self.Painter.drawPoint(x, y)
        

    def drawPath(self, path: QPainterPath):
        """
        Draw a QPainterPath on the surface"""
        self.Painter.drawPath(path)
        
    
    def drawImage(self,Image):
        self.Painter.drawImage(0,0,Image)
    
    def fillRect(self, brush: QBrush):
        
        self.Painter.fillRect(self.rect(),brush)
        
    
        
    

    def floodfill(self, startX, startY):
        SearchColor = self.pixelColor(startX, startY)
        queue = [(startX, startY)]
        while queue != []:
            queue = self.searchNeighbor(queue, SearchColor)
            print(queue)
                
            
    
    def clear(self):
        self.fill(Qt.transparent)
        

    def setPen(self, pen: QPen):
        self.Painter.setPen(pen)
        print("Pen set")
    
    def setBrush(self, brush: QBrush):
        self.Painter.setBrush(brush)

    def searchNeighbor(self,pixels,TargetColor):
        neighbors = []
        for pixel in pixels:
            if pixel[0] > 0 or pixel[0] < self.getWidth() and pixel[1] > 0 or pixel[1] < self.getHeight():
                if self.pixelColor(pixel[0]+1,pixel[1]) == TargetColor:
                    neighbors.append((pixel[0]+1,pixel[1]))
                    self.drawPoint(pixel[0]+1,pixel[1])

                if self.pixelColor(pixel[0]-1,pixel[1]) == TargetColor:
                    neighbors.append((pixel[0]-1,pixel[1]))
                    self.drawPoint(pixel[0]-1,pixel[1])

                if self.pixelColor(pixel[0],pixel[1]+1) == TargetColor:
                    neighbors.append((pixel[0],pixel[1]+1))
                    self.drawPoint(pixel[0],pixel[1]+1)

                if self.pixelColor(pixel[0],pixel[1]-1) == TargetColor:
                    neighbors.append((pixel[0],pixel[1]-1))
                    self.drawPoint(pixel[0],pixel[1]-1)
        return neighbors