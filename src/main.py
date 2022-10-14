from PySide2.QtWidgets import QMainWindow, QApplication
from UI import ParentEditor

class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ##Init UI
        self.ui = ParentEditor.Ui_MainWindow()
        self.ui.setupUi(self)



EventCycle = QApplication([])
MainWindow = ParentWindow()
MainWindow.show()
EventCycle.exec_()