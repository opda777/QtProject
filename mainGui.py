# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1485, 800)
        Form.setMinimumSize(QtCore.QSize(1485, 800))
        Form.setMaximumSize(QtCore.QSize(1485, 800))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1461, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 50))
        self.label.setMaximumSize(QtCore.QSize(150, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(400, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_button = QtWidgets.QPushButton(self.widget_2)
        self.main_button.setObjectName("main_button")
        self.horizontalLayout_2.addWidget(self.main_button)
        self.allcourse_button = QtWidgets.QPushButton(self.widget_2)
        self.allcourse_button.setObjectName("allcourse_button")
        self.horizontalLayout_2.addWidget(self.allcourse_button)
        self.unity_button = QtWidgets.QPushButton(self.widget_2)
        self.unity_button.setObjectName("unity_button")
        self.horizontalLayout_2.addWidget(self.unity_button)
        self.ue4_button = QtWidgets.QPushButton(self.widget_2)
        self.ue4_button.setObjectName("ue4_button")
        self.horizontalLayout_2.addWidget(self.ue4_button)
        self.mystery_button = QtWidgets.QPushButton(self.widget_2)
        self.mystery_button.setObjectName("mystery_button")
        self.horizontalLayout_2.addWidget(self.mystery_button)
        self.horizontalLayout.addWidget(self.widget_2)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 50))
        self.widget.setMaximumSize(QtCore.QSize(500, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(215, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_button = QtWidgets.QPushButton(self.widget_3)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout_3.addWidget(self.login_button)
        self.register_button = QtWidgets.QPushButton(self.widget_3)
        self.register_button.setObjectName("register_button")
        self.horizontalLayout_3.addWidget(self.register_button)
        self.horizontalLayout.addWidget(self.widget_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 1471, 321))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("TestImage_1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(680, 400, 132, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 470, 1371, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.showCourse_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.showCourse_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.showCourse_gridLayout.setObjectName("showCourse_gridLayout")
        self.moreCourse_button = QtWidgets.QPushButton(Form)
        self.moreCourse_button.setGeometry(QtCore.QRect(1390, 750, 93, 28))
        self.moreCourse_button.setObjectName("moreCourse_button")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(1410, 470, 61, 271))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_button.setText(_translate("Form", "首页"))
        self.allcourse_button.setText(_translate("Form", "全部课程"))
        self.unity_button.setText(_translate("Form", "Unity"))
        self.ue4_button.setText(_translate("Form", "UE4"))
        self.mystery_button.setText(_translate("Form", "神秘"))
        self.login_button.setText(_translate("Form", "登录"))
        self.register_button.setText(_translate("Form", "注册"))
        self.label_3.setText(_translate("Form", "热门课程"))
        self.moreCourse_button.setText(_translate("Form", "更多课程"))
