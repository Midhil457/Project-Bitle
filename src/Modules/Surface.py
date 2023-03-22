from PySide2.QtWidgets import QGraphicsPixmapItem
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtGui import QPainter, QPainterPath, QPen, QBrush, QColor
from PySide2.QtCore import Qt, QRect


class Surface(QGraphicsPixmapItem):
    def __init__(self, w: int, h: int, format, Image=0, *args):
        super().__init__(*args)
        #Init Image
        self.Image = Image or QImage(w, h, format)
        self.Image.fill(Qt.transparent)
        self.Painter = QPainter(self.Image)
        self.Brush = QBrush(QColor(0,0,0,255))
        self.Pen = QPen(QColor(0,0,0,255))
        self.setPixmap(QPixmap().fromImage(self.Image))
    
    def getWidth(self):
        return self.Image.width()
    def getHeight(self):
        return self.Image.height()
    def getPainter(self):
        return self.Painter

    def getImage(self):
        return self.Image
    def getPixel(self,x,y):
        return self.Image.pixel(x,y)
    
    def erase(self, x: int, y: int, r: int):
        #Todo: Erase an region
        self.Image.setPixelColor(x,y, QColor(0,0,0,0))
        self.setPixmap(QPixmap().fromImage(self.Image))
    
    def drawRect(self, x: int, y: int, w: int, h: int):
        """
        Draw a Rect on the surface
        """
        self.Painter.drawRect(x, y, w, h)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def drawEllipse(self, rect: QRect):
        """
        Draw an Ellipse on the surface
        """
        self.Painter.drawEllipse(rect)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def drawLine(self, x1: int, y1: int, x2: int, y2: int):
        """
        Draw a line on the surface
        """
        self.Painter.drawLine(x1, y1, x2, y2)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def drawText(self, x: int, y: int, w: int, h: int, text: str):
        """
        Draw a Text on the surface
        """
        self.Painter.drawText(x, y, w, h, text=text)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def drawPoint(self, x: int, y: int):
        """
        Draw a Point on the surface
        """
        self.Painter.drawPoint(x, y)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def drawPath(self, path: QPainterPath):
        """
        Draw a QPainterPath on the surface"""
        self.Painter.drawPath(path)
        self.setPixmap(QPixmap().fromImage(self.Image))
    
    def drawImage(self,Image):
        self.Painter.drawImage(0,0,Image)
        self.setPixmap(QPixmap().fromImage(self.Image))
    
    def fill(self, brush: QBrush):
        print(self.Image.rect())
        self.Painter.fillRect(self.Image.rect(),brush)
        self.setPixmap(QPixmap().fromImage(self.Image))
    
    def floodfill(self, startX, startY):
        if self.validateCord(startX, startY):
            SearchColor = self.Image.pixelColor(startX, startY)
            queue = [(startX, startY)]
            if SearchColor != self.Brush.color():
                while queue != []:
                    queue = self.searchNeighbor(queue, SearchColor)
            
                
    def validateCord(self,x,y):

        if x in range(self.Image.width()) and y in range(self.Image.height()):
            return True
        else:
            return False
        
    
    def getNeighbors(self, x, y, validate):
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] 
        if validate:
            for index,neighbor in enumerate(neighbors):
                if self.validateCord(neighbor[0], neighbor[1]) == False:
                    neighbors.pop(index)
             
        return neighbors
        


    
    def clear(self):
        self.Image.fill(Qt.transparent)
        self.setPixmap(QPixmap().fromImage(self.Image))

    def setPen(self, pen: QPen):
        self.Pen = pen
        self.Painter.setPen(self.Pen)
        
    def setBrush(self, brush: QBrush):
        self.Brush = brush
        self.Painter.setBrush(brush)
    
    def setBrushColor(self, color: QColor):
        self.Brush.setColor(color)
    
    def setPenColor(self, color: QColor):
        self.Pen.setColor(color)
        self.Painter.setPen(self.Pen)
        
        

    def searchNeighbor(self,pixels,TargetColor):
        Neighbors = []
        for pixel in pixels:
            if self.validateCord(pixel[0],pixel[1]):
                for neighbor in self.getNeighbors(pixel[0],pixel[1],True):
                    if self.Image.pixelColor(neighbor[0],neighbor[1]) == TargetColor:
                        Neighbors.append((neighbor[0],neighbor[1]))
                        self.drawPoint(neighbor[0],neighbor[1])
        return Neighbors