from UI import ColorPicker
from PySide2.QtWidgets import QDialog
from PySide2.QtGui import QColor, QPixmap, QImage, QLinearGradient, QBrush, Qt
from Modules import MicroSurface
import math

class ColorSelectorDialog(QDialog):

    def __init__(self, *args):
        super().__init__(*args)
        self.ui = ColorPicker.Ui_ColorPicker()
        self.ui.setupUi(self)
        self.ColorWheel = MicroSurface.MicroSurface(300,300,QImage.Format_ARGB32_Premultiplied)
        self.values = []
        
        ColorField = QLinearGradient(0.5,1,0.5,0)
        ColorField.setCoordinateMode(QLinearGradient.ObjectBoundingMode)
        ColorField.setColorAt(0,Qt.black)
        ColorField.setColorAt(0.5,Qt.transparent)
        ColorField.setColorAt(1,Qt.white)
        
        brush = QBrush(ColorField)
        self.ColorWheel.fillRect(brush)
        self.ui.ColorField.setCursor(Qt.CrossCursor)
        
        self.ui.ColorField.setPixmap(QPixmap().fromImage(self.ColorWheel))
        self.selectedColor = QColor(0,0,0,255)
        self.ui.Color_Alpha_SpinBox.setValue(255)
        
        

        self.ui.Color_Red_SpinBox.valueChanged.connect(lambda red: self.setColor(r=red) if self.ui.Color_Red_SpinBox.hasFocus() else None)
        self.ui.Color_Green_SpinBox.valueChanged.connect(lambda green: self.setColor(g=green)if self.ui.Color_Green_SpinBox.hasFocus() else None)
        self.ui.Color_Blue_SpinBox.valueChanged.connect(lambda blue: self.setColor(b=blue)if self.ui.Color_Blue_SpinBox.hasFocus() else None)
        self.ui.Color_Alpha_SpinBox.valueChanged.connect(lambda alpha: self.setColor(a=alpha)if self.ui.Color_Alpha_SpinBox.hasFocus() else None)



        self.ui.Color_Hex_LineEdit.textChanged.connect(lambda hex: self.setColor(hex=hex) if self.ui.Color_Hex_LineEdit.hasFocus() else None)
        
    
            

        self.ui.ColorField.setPixmap(QPixmap().fromImage(self.ColorWheel))

    def setColor(self,r=None,g=None,b=None,a=None, hex=""):
        if hex:
            self.selectedColor.setNamedColor(hex)
            self.ui.Color_Red_SpinBox.setValue(self.selectedColor.red())
            self.ui.Color_Green_SpinBox.setValue(self.selectedColor.green())
            self.ui.Color_Blue_SpinBox.setValue(self.selectedColor.blue())
            self.ui.Color_Alpha_SpinBox.setValue(self.selectedColor.alpha())
        else:

            if r != None:
                self.selectedColor.setRed(r)
            if g != None:
                self.selectedColor.setGreen(g)
            if b != None:
                self.selectedColor.setBlue(b)
            if a != None:
                self.selectedColor.setAlpha(a)
                 
            if self.selectedColor.alpha() == 255:
                self.ui.Color_Hex_LineEdit.setText(self.selectedColor.name())
            else:
                self.ui.Color_Hex_LineEdit.setText(self.selectedColor.name(QColor.HexArgb))
        
"""
for x in range(300):
            
            for y in range(300):

                if math.sqrt((x-150)**2+(y-150)**2) <= 150:
                    angle =  (math.degrees( math.atan2(x - 150.0, y- 150.0) ) + 150.0) % 360.0
                    self.values.append([x,y,QColor().fromHsl(angle,math.sqrt((x-150)**2+(y-150)**2),self.ui.Lightness_Slider.value())])
                    
                    self.ColorWheel.setPixelColor(x,y,QColor().fromHsl(angle,math.sqrt((x-150)**2+(y-150)**2),0.5))
"""