# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 1031, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Total_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Total_Layout.setContentsMargins(0, 0, 0, 0)
        self.Total_Layout.setObjectName("Total_Layout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Total_menubar = QtWidgets.QMenuBar(MainWindow)
        self.Total_menubar.setGeometry(QtCore.QRect(0, 0, 1034, 26))
        self.Total_menubar.setObjectName("Total_menubar")
        self.menuSiki = QtWidgets.QMenu(self.Total_menubar)
        self.menuSiki.setObjectName("menuSiki")
        self.menu = QtWidgets.QMenu(self.Total_menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.Total_menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuUnity = QtWidgets.QMenu(self.Total_menubar)
        self.menuUnity.setObjectName("menuUnity")
        self.menuUE4 = QtWidgets.QMenu(self.Total_menubar)
        self.menuUE4.setObjectName("menuUE4")
        self.menuJavaEE = QtWidgets.QMenu(self.Total_menubar)
        self.menuJavaEE.setObjectName("menuJavaEE")
        self.menuPython = QtWidgets.QMenu(self.Total_menubar)
        self.menuPython.setObjectName("menuPython")
        self.menu_3 = QtWidgets.QMenu(self.Total_menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.Total_menubar)
        self.Total_menubar.addAction(self.menuSiki.menuAction())
        self.Total_menubar.addAction(self.menu.menuAction())
        self.Total_menubar.addAction(self.menu_2.menuAction())
        self.Total_menubar.addAction(self.menuUnity.menuAction())
        self.Total_menubar.addAction(self.menuUE4.menuAction())
        self.Total_menubar.addAction(self.menuJavaEE.menuAction())
        self.Total_menubar.addAction(self.menuPython.menuAction())
        self.Total_menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSiki.setTitle(_translate("MainWindow", "Siki学院"))
        self.menu.setTitle(_translate("MainWindow", "首页"))
        self.menu_2.setTitle(_translate("MainWindow", "独立游戏"))
        self.menuUnity.setTitle(_translate("MainWindow", "Unity"))
        self.menuUE4.setTitle(_translate("MainWindow", "UE4"))
        self.menuJavaEE.setTitle(_translate("MainWindow", "JavaEE"))
        self.menuPython.setTitle(_translate("MainWindow", "Python人工智能"))
        self.menu_3.setTitle(_translate("MainWindow", "微信小程序"))
