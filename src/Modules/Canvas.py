from PySide2.QtWidgets import QGraphicsItemGroup, QGraphicsPixmapItem
from PySide2.QtGui import QPixmap
from Modules.Surface import Surface
from Modules import Global

class Canvas(QGraphicsItemGroup):
    def __init__(self, surface: Surface) -> None:
        super().__init__()
        self.PrimaryCanvas = surface
        self.Overlay = Surface(self.PrimaryCanvas.getWidth(),self.PrimaryCanvas.getHeight(),Global.Image_Format)
        self.BackgroundImage = QPixmap(self.PrimaryCanvas.getWidth(),self.PrimaryCanvas.getHeight())
        self.BackgroundImage.fill(Global.Tool_Box.fillColor)
        self.Background = QGraphicsPixmapItem(self.BackgroundImage)
        self.addToGroup(self.Background)
        self.addToGroup(self.PrimaryCanvas)
        self.addToGroup(self.Overlay)
        