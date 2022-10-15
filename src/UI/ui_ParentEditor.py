# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParentEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 820)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionToolBox = QAction(MainWindow)
        self.actionToolBox.setObjectName(u"actionToolBox")
        self.actionToolBox.setCheckable(True)
        self.actionToolBox.setChecked(True)
        self.actionColor_Palette = QAction(MainWindow)
        self.actionColor_Palette.setObjectName(u"actionColor_Palette")
        self.actionColor_Palette.setCheckable(True)
        self.actionColor_Palette.setChecked(True)
        self.actionTool_Settings = QAction(MainWindow)
        self.actionTool_Settings.setObjectName(u"actionTool_Settings")
        self.actionTool_Settings.setCheckable(True)
        self.actionTool_Settings.setChecked(True)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionGlyph_Palette = QAction(MainWindow)
        self.actionGlyph_Palette.setObjectName(u"actionGlyph_Palette")
        self.actionGlyph_Palette.setCheckable(True)
        self.actionGlyph_Palette.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ViewPort = QGraphicsView(self.centralwidget)
        self.ViewPort.setObjectName(u"ViewPort")

        self.horizontalLayout.addWidget(self.ViewPort)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1016, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ToolSettingsDock = QDockWidget(MainWindow)
        self.ToolSettingsDock.setObjectName(u"ToolSettingsDock")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_2 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.dockWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(119, 335))
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.ToolSettingsDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.ToolSettingsDock)
        self.ToolsDock = QDockWidget(MainWindow)
        self.ToolsDock.setObjectName(u"ToolsDock")
        self.ToolsDock.setMinimumSize(QSize(93, 309))
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BrushTool = QPushButton(self.dockWidgetContents_2)
        self.BrushTool.setObjectName(u"BrushTool")

        self.verticalLayout.addWidget(self.BrushTool)

        self.LineTool = QPushButton(self.dockWidgetContents_2)
        self.LineTool.setObjectName(u"LineTool")

        self.verticalLayout.addWidget(self.LineTool)

        self.BucketTool = QPushButton(self.dockWidgetContents_2)
        self.BucketTool.setObjectName(u"BucketTool")

        self.verticalLayout.addWidget(self.BucketTool)

        self.ToolDockVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.ToolDockVerticalSpacer)

        self.ToolsDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.ToolsDock)
        self.ColorPaletteDock = QDockWidget(MainWindow)
        self.ColorPaletteDock.setObjectName(u"ColorPaletteDock")
        self.ColorPaletteDock.setMinimumSize(QSize(136, 238))
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.ColorPaletteDock.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.ColorPaletteDock)
        self.GlyphPaletteDock = QDockWidget(MainWindow)
        self.GlyphPaletteDock.setObjectName(u"GlyphPaletteDock")
        self.GlyphPaletteDock.setMinimumSize(QSize(274, 388))
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GlyphPalette = QListView(self.dockWidgetContents_4)
        self.GlyphPalette.setObjectName(u"GlyphPalette")

        self.verticalLayout_2.addWidget(self.GlyphPalette)

        self.GlyphPaletteDock.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.GlyphPaletteDock)
        QWidget.setTabOrder(self.ViewPort, self.BrushTool)
        QWidget.setTabOrder(self.BrushTool, self.LineTool)
        QWidget.setTabOrder(self.LineTool, self.BucketTool)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionToolBox)
        self.menuView.addAction(self.actionColor_Palette)
        self.menuView.addAction(self.actionTool_Settings)
        self.menuView.addAction(self.actionGlyph_Palette)

        self.retranslateUi(MainWindow)
        self.actionToolBox.toggled.connect(self.ToolsDock.setVisible)
        self.actionColor_Palette.toggled.connect(self.ColorPaletteDock.setVisible)
        self.actionTool_Settings.toggled.connect(self.ToolSettingsDock.setVisible)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionGlyph_Palette.toggled.connect(self.GlyphPaletteDock.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionToolBox.setText(QCoreApplication.translate("MainWindow", u"ToolBox", None))
#if QT_CONFIG(tooltip)
        self.actionToolBox.setToolTip(QCoreApplication.translate("MainWindow", u"Show/Hide ToolBox", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionToolBox.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor_Palette.setText(QCoreApplication.translate("MainWindow", u"Color Palette", None))
#if QT_CONFIG(tooltip)
        self.actionColor_Palette.setToolTip(QCoreApplication.translate("MainWindow", u"Show/Hide Color Palette", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionColor_Palette.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionTool_Settings.setText(QCoreApplication.translate("MainWindow", u"Tool Settings", None))
#if QT_CONFIG(tooltip)
        self.actionTool_Settings.setToolTip(QCoreApplication.translate("MainWindow", u"Show/Hide Tool Settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionTool_Settings.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Close Application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionGlyph_Palette.setText(QCoreApplication.translate("MainWindow", u"Glyph Palette", None))
#if QT_CONFIG(tooltip)
        self.actionGlyph_Palette.setToolTip(QCoreApplication.translate("MainWindow", u"Show/Hide Glyph Palette", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionGlyph_Palette.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+G", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.ToolSettingsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tool Settings", None))
        self.ToolsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToolBox", None))
        self.BrushTool.setText(QCoreApplication.translate("MainWindow", u"Brush", None))
        self.LineTool.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.BucketTool.setText(QCoreApplication.translate("MainWindow", u"Bucket", None))
        self.ColorPaletteDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Color Palette", None))
        self.GlyphPaletteDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Glyph Palette", None))
    # retranslateUi

