# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courseVideo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from MySlider import MySlider
from myVideoWidget import MyVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pauseVideo_button = QtWidgets.QPushButton(self.centralwidget)
        self.pauseVideo_button.setGeometry(QtCore.QRect(446, 370, 90, 28))
        self.pauseVideo_button.setObjectName("pauseVideo_button")
        self.playVideo_button = QtWidgets.QPushButton(self.centralwidget)
        self.playVideo_button.setGeometry(QtCore.QRect(300, 370, 90, 28))
        self.playVideo_button.setObjectName("playVideo_button")
        self.video_slider = MySlider(self.centralwidget)
        self.video_slider.setGeometry(QtCore.QRect(240, 340, 311, 22))
        self.video_slider.setOrientation(QtCore.Qt.Horizontal)
        self.video_slider.setObjectName("video_slider")
        self.video_widget = MyVideoWidget(self.centralwidget)
        self.video_widget.setGeometry(QtCore.QRect(70, 20, 691, 301))
        self.video_widget.setObjectName("video_widget")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(QtCore.QRect(570, 340, 51, 16))
        self.video_label.setObjectName("video_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "播放器"))
        self.pauseVideo_button.setText(_translate("MainWindow", "暂停"))
        self.playVideo_button.setText(_translate("MainWindow", "播放"))
        self.video_label.setText(_translate("MainWindow", "0%"))

