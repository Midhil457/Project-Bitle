# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColorPicker.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        if not ColorPicker.objectName():
            ColorPicker.setObjectName(u"ColorPicker")
        ColorPicker.resize(504, 355)
        self.gridLayout = QGridLayout(ColorPicker)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Color_Alpha_Layout = QHBoxLayout()
        self.Color_Alpha_Layout.setObjectName(u"Color_Alpha_Layout")
        self.Color_Alpha_Label = QLabel(ColorPicker)
        self.Color_Alpha_Label.setObjectName(u"Color_Alpha_Label")
        self.Color_Alpha_Label.setMaximumSize(QSize(21, 16777215))

        self.Color_Alpha_Layout.addWidget(self.Color_Alpha_Label)

        self.Color_Alpha_SpinBox = QSpinBox(ColorPicker)
        self.Color_Alpha_SpinBox.setObjectName(u"Color_Alpha_SpinBox")
        self.Color_Alpha_SpinBox.setMaximumSize(QSize(93, 16777215))
        self.Color_Alpha_SpinBox.setMaximum(255)

        self.Color_Alpha_Layout.addWidget(self.Color_Alpha_SpinBox)


        self.gridLayout.addLayout(self.Color_Alpha_Layout, 3, 1, 1, 2)

        self.Color_Blue_Layout = QHBoxLayout()
        self.Color_Blue_Layout.setObjectName(u"Color_Blue_Layout")
        self.Color_Blue_Label = QLabel(ColorPicker)
        self.Color_Blue_Label.setObjectName(u"Color_Blue_Label")
        self.Color_Blue_Label.setMaximumSize(QSize(21, 16777215))

        self.Color_Blue_Layout.addWidget(self.Color_Blue_Label)

        self.Color_Blue_SpinBox = QSpinBox(ColorPicker)
        self.Color_Blue_SpinBox.setObjectName(u"Color_Blue_SpinBox")
        self.Color_Blue_SpinBox.setMaximumSize(QSize(93, 16777215))
        self.Color_Blue_SpinBox.setMaximum(255)

        self.Color_Blue_Layout.addWidget(self.Color_Blue_SpinBox)


        self.gridLayout.addLayout(self.Color_Blue_Layout, 2, 1, 1, 2)

        self.ColorPicker_Response = QDialogButtonBox(ColorPicker)
        self.ColorPicker_Response.setObjectName(u"ColorPicker_Response")
        self.ColorPicker_Response.setOrientation(Qt.Horizontal)
        self.ColorPicker_Response.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.ColorPicker_Response, 4, 1, 1, 2)

        self.Color_Red_Layout_2 = QHBoxLayout()
        self.Color_Red_Layout_2.setObjectName(u"Color_Red_Layout_2")
        self.Color_Red_Label = QLabel(ColorPicker)
        self.Color_Red_Label.setObjectName(u"Color_Red_Label")
        self.Color_Red_Label.setMaximumSize(QSize(21, 16777215))

        self.Color_Red_Layout_2.addWidget(self.Color_Red_Label)

        self.Color_Red_SpinBox = QSpinBox(ColorPicker)
        self.Color_Red_SpinBox.setObjectName(u"Color_Red_SpinBox")
        self.Color_Red_SpinBox.setMaximumSize(QSize(93, 16777215))
        self.Color_Red_SpinBox.setMaximum(255)

        self.Color_Red_Layout_2.addWidget(self.Color_Red_SpinBox)


        self.gridLayout.addLayout(self.Color_Red_Layout_2, 0, 1, 1, 2)

        self.Color_Alpha_Layout_2 = QHBoxLayout()
        self.Color_Alpha_Layout_2.setObjectName(u"Color_Alpha_Layout_2")
        self.Color_Hex_LineEdit = QLineEdit(ColorPicker)
        self.Color_Hex_LineEdit.setObjectName(u"Color_Hex_LineEdit")
        self.Color_Hex_LineEdit.setInputMask(u"\\#HHHHHHHH")
        self.Color_Hex_LineEdit.setCursorPosition(9)
        self.Color_Hex_LineEdit.setClearButtonEnabled(True)

        self.Color_Alpha_Layout_2.addWidget(self.Color_Hex_LineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Color_Alpha_Layout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.Color_Alpha_Layout_2, 4, 0, 1, 1)

        self.Color_Green_Layout_2 = QHBoxLayout()
        self.Color_Green_Layout_2.setObjectName(u"Color_Green_Layout_2")
        self.Color_Green_Label = QLabel(ColorPicker)
        self.Color_Green_Label.setObjectName(u"Color_Green_Label")
        self.Color_Green_Label.setMaximumSize(QSize(21, 16777215))

        self.Color_Green_Layout_2.addWidget(self.Color_Green_Label)

        self.Color_Green_SpinBox = QSpinBox(ColorPicker)
        self.Color_Green_SpinBox.setObjectName(u"Color_Green_SpinBox")
        self.Color_Green_SpinBox.setMaximumSize(QSize(93, 16777215))
        self.Color_Green_SpinBox.setMaximum(255)

        self.Color_Green_Layout_2.addWidget(self.Color_Green_SpinBox)


        self.gridLayout.addLayout(self.Color_Green_Layout_2, 1, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ColorField = QLabel(ColorPicker)
        self.ColorField.setObjectName(u"ColorField")
        self.ColorField.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.331579 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"")
        self.ColorField.setScaledContents(True)
        self.ColorField.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.ColorField)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 4, 1)


        self.retranslateUi(ColorPicker)
        self.ColorPicker_Response.accepted.connect(ColorPicker.accept)
        self.ColorPicker_Response.rejected.connect(ColorPicker.reject)

        QMetaObject.connectSlotsByName(ColorPicker)
    # setupUi

    def retranslateUi(self, ColorPicker):
        ColorPicker.setWindowTitle(QCoreApplication.translate("ColorPicker", u"Dialog", None))
        self.Color_Alpha_Label.setText(QCoreApplication.translate("ColorPicker", u"A:", None))
        self.Color_Blue_Label.setText(QCoreApplication.translate("ColorPicker", u"B:", None))
        self.Color_Red_Label.setText(QCoreApplication.translate("ColorPicker", u"R:", None))
        self.Color_Hex_LineEdit.setText(QCoreApplication.translate("ColorPicker", u"#000000", None))
        self.Color_Hex_LineEdit.setPlaceholderText("")
        self.Color_Green_Label.setText(QCoreApplication.translate("ColorPicker", u"G:", None))
        self.ColorField.setText("")
    # retranslateUi

