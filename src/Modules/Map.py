from PySide2.QtCore import QAbstractListModel
from PySide2.QtGui import Qt

class MapModel(QAbstractListModel):
    def __init__(self, *args, Map=None, **kwargs) -> None:
        super(MapModel,self).__init__(*args, **kwargs)

        self.Map = Map or []

    def data(self, index, role):
        if role == Qt.DecorationRole:
            return self.Map[index.row()][1].getImage()
        if role == Qt.DisplayRole:
            return self.Map[index.row()][0]
    
    def rowCount(self, index):
        return len(self.Map)
