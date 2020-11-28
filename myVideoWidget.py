from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2 import QtCore,QtGui,QtWidgets

class MyVideoWidget(QVideoWidget):

    # 创建双击信号
    doubleClickedItem = QtCore.Signal(str)

    def __init__(self,parent= None):
        super(MyVideoWidget, self).__init__(parent)

    # 双击事件
    def mouseDoubleClickEvent(self, QMouseEvent):
        self.doubleClickedItem.emit("double clicked")