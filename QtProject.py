# -*- coding: utf-8 -*-

import sys
import QT_UI
import OpdaWidgets
from PySide2 import QtWidgets,QtCore,QtGui



class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # 窗口名称
        self.setWindowTitle("Siki学院")
        # 设置窗口大小
        self.setFixedSize(1500,800)
        # 去除问号
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connects()



    def create_widgets(self):
        # 滚动区域
        self.scroll = QtWidgets.QScrollArea()
        # 主widget
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setFixedSize(1485, 1500)

        # 设置滚动区域相关属性
        self.scroll.setWidget(self.main_widget)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.setCentralWidget(self.scroll)

        # 创建菜单栏
        self.Total_MenuBar = QtWidgets.QMenuBar()
        self.Total_MenuBar.addMenu("首页")
        self.Total_MenuBar.addMenu("全部课程")
        self.Total_MenuBar.addMenu("独立游戏")
        self.Total_MenuBar.addMenu("Unity")
        self.Total_MenuBar.addMenu("UE4")
        self.Total_MenuBar.addMenu("JavaEE")
        self.Total_MenuBar.addMenu("Python人工智能")
        self.Total_MenuBar.addMenu("微信小程序")
        self.Total_MenuBar.addMenu("神秘")
        # 搜索栏
        self.search = QtWidgets.QLineEdit()
        self.search.setPlaceholderText("Search...")
        # 登录注册按钮
        self.login_button = QtWidgets.QPushButton("登录")
        self.register_button = QtWidgets.QPushButton("注册")
        # 图片轮播
        self.imagePlay = OpdaWidgets.ImageViewLabel()
        self.imagePlay.addImage(["TestImage_1.png","TestImage_2.jpg","TestImage_3.png"])

        # 文本
        self.label_1 = QtWidgets.QLabel("网课课程")
        self.label_2 = QtWidgets.QLabel("精选网校课程，满足你的学习兴趣。")
        self.label_3 = QtWidgets.QLabel("A计划")
        self.label_4 = QtWidgets.QLabel("完整学习路线，零基础入门到就业学习教程")
        # 设置位置
        self.label_1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        # 网课按钮
        self.all_button = QtWidgets.QPushButton("全部课程")
        self.unity_button = QtWidgets.QPushButton("Unity")
        self.ue4_button = QtWidgets.QPushButton("Unreal Engine")
        self.java_button = QtWidgets.QPushButton("JavaEE")

        # 其他按钮
        self.lastUpdate_button = QtWidgets.QPushButton("最新")
        self.hot_button = QtWidgets.QPushButton("最热")
        self.recommend_button = QtWidgets.QPushButton("推荐")
        self.moreCourse_button = QtWidgets.QPushButton("更多课程")
        self.moreclass_button = QtWidgets.QPushButton("更多班级")

        # showQlabel
        #self.unity_showlabel = QtWidgets.QLabel("学习Unity3D游戏开发，成为独立游戏开发者！")
        #self.unity_showlabel.setPixmap(QtGui.QPixmap("TestImage_4.png"))
        self.unity_showlabel = OpdaWidgets.ImageTextWidget("Unity","学习Unity3D游戏开发，成为独立游戏开发者！","TestImage_4.png")





    def create_layouts(self):
        # 主layout
        main_layout = QtWidgets.QVBoxLayout()
        #main_layout.setGeometry(QtCore.QRect(600,100,1000,900))
        #for i in range(10):
        #    main_layout.addWidget(QtWidgets.QPushButton("Test"))
        # 设置layout
        self.main_widget.setLayout(main_layout)


        # 头部layout
        top_layout = QtWidgets.QVBoxLayout()
        # 导航栏
        menu_layout = QtWidgets.QHBoxLayout()
        menu_layout.addWidget(self.Total_MenuBar)
        menu_layout.addWidget(self.search)
        menu_layout.addWidget(self.login_button)
        menu_layout.addWidget(self.register_button)


        top_layout.addLayout(menu_layout)
        top_layout.addWidget(self.imagePlay)

        # 中部layout
        center_layout = QtWidgets.QVBoxLayout()


        # 课程
        course_layout = QtWidgets.QVBoxLayout()
        # 中部课程文本栏
        course_text_layout = QtWidgets.QVBoxLayout()
        course_text_layout.addWidget(self.label_1)
        course_text_layout.addWidget(self.label_2)


        # 中部课程导航栏
        course_menu_layout = QtWidgets.QHBoxLayout()
        # 中部课程左边导航栏
        course_menu_Leftlayout = QtWidgets.QHBoxLayout()
        course_menu_Leftlayout.addWidget(self.all_button)
        course_menu_Leftlayout.addWidget(self.unity_button)
        course_menu_Leftlayout.addWidget(self.ue4_button)
        course_menu_Leftlayout.addWidget(self.java_button)
        # 中部课程右边导航栏
        course_menu_Rightlayout = QtWidgets.QHBoxLayout()
        course_menu_Rightlayout.addWidget(self.lastUpdate_button)
        course_menu_Rightlayout.addWidget(self.hot_button)
        course_menu_Rightlayout.addWidget(self.recommend_button)

        course_menu_layout.addLayout(course_menu_Leftlayout)
        course_menu_layout.addLayout(course_menu_Rightlayout)
        # 设置大小比例
        course_menu_layout.setStretchFactor(course_menu_Leftlayout, 4)
        course_menu_layout.setStretchFactor(course_menu_Rightlayout, 1)
        # 设置间隔
        course_menu_Leftlayout.setContentsMargins(0, 0, 100, 0)
        course_menu_Rightlayout.setContentsMargins(50, 0, 0, 0)

        # 网课Grid
        course_Gridlayout = QtWidgets.QGridLayout()
        # 设置行列
        for i in range(3):
            for j in range(4):
                label = QtWidgets.QLabel("测试")
                image = QtGui.QPixmap("TestImage_1.png")
                label.setPixmap(image)
                course_Gridlayout.addWidget(label,i,j)

        course_layout.addLayout(course_text_layout)
        course_layout.addLayout(course_menu_layout)
        course_layout.addLayout(course_Gridlayout)
        course_layout.addWidget(self.moreCourse_button)

        # A计划
        aProject_layout = QtWidgets.QVBoxLayout()
        aProject_layout.addWidget(self.label_3)
        aProject_layout.addWidget(self.label_4)
        # 课程计划
        aProject_Gridlayout = QtWidgets.QGridLayout()
        # 设置行列
        for i in range(2):
            for j in range(4):
                label = QtWidgets.QLabel("测试")
                image = QtGui.QPixmap("TestImage_2.jpg")
                label.setPixmap(image)
                aProject_Gridlayout.addWidget(label, i, j)

        aProject_layout.addLayout(aProject_Gridlayout)
        aProject_layout.addWidget(self.moreclass_button)

        center_layout.addLayout(course_layout)
        center_layout.addLayout(aProject_layout)

        # 底部layout
        bottom_layout = QtWidgets.QVBoxLayout()
        botton_show_layout = QtWidgets.QHBoxLayout()
        botton_show_layout.addWidget(self.unity_showlabel)


        bottom_layout.addLayout(botton_show_layout)


        main_layout.addLayout(top_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(bottom_layout)



    def create_connects(self):
        pass
        


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QtWidgets.QApplication(sys.argv)
    # 初始化
    myWin = MyMainWindow()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())



