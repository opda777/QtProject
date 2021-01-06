# -*- coding: utf-8 -*-

import sys
import QT_UI
import OpdaWidgets
import mainGui
import courseGui
import courseVideo
import commentGui
import searchGui
import searchTabGui
import personalHomepageGui
from myVideoWidget import MyVideoWidget
from PySide2 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets
from database.course import CoursesTable
from functools import partial


class mainWidget(QtWidgets.QWidget, mainGui.Ui_Form):
    def __init__(self):
        super(mainWidget, self).__init__()
        self.setupUi(self)


class courseWiget(QtWidgets.QWidget, courseGui.Ui_Form):
    def __init__(self):
        super(courseWiget, self).__init__()
        self.setupUi(self)

        # 设置button背景
        self.courseViedo_button.setText("")
        self.courseViedo_button.setStyleSheet("QPushButton{border-image: url(课程1.jpg)}")

        self.courseViedo_button.clicked.connect(self.createVideoMainwindow)

    def createVideoMainwindow(self):
        self.video_mainWindow = courseVideo()
        self.video_mainWindow.show()


class courseVideo(QtWidgets.QMainWindow, courseVideo.Ui_MainWindow):
    def __init__(self):
        super(courseVideo, self).__init__()
        self.setupUi(self)

        # 判断是否在手动拖进度条

        # 判断是否需要全屏
        self.videoFullScreen = False
        # 创建全屏的Widget
        self.videoFullScreenWidget = MyVideoWidget()
        self.videoFullScreenWidget.setFullScreen(1)
        # 先隐藏
        self.videoFullScreenWidget.hide()

        # 创建播放器
        self.player = QtMultimedia.QMediaPlayer()
        # 指定视频输出的widget
        self.player.setVideoOutput(self.video_widget)
        # 设置默认的视频
        self.player.setMedia(QtMultimedia.QMediaContent("Unity.mp4"))
        # 设置音量
        self.player.setVolume(1)

        # 信号槽
        self.playVideo_button.clicked.connect(self.playVideo)
        self.pauseVideo_button.clicked.connect(self.pauseVideo)
        self.player.positionChanged.connect(self.changeSlider)

        # 双击信号槽
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)
        self.video_widget.doubleClickedItem.connect(self.videoDoubleClicked)

        # 滑动条
        self.video_slider.valueChanged[int].connect(self.SlidevideoSlider)
        self.video_slider.mousePressItem.connect(self.PressvideoSlider)

    def playVideo(self):
        self.player.play()

    def pauseVideo(self):
        self.player.pause()

    def changeSlider(self, position):
        # 滑动条不处于滑动状态才改变
        if not self.video_slider.isSliderDown():
            self.videoLength = self.player.duration() + 0.1
            self.video_slider.setValue(round((position / self.videoLength) * 100))
            self.video_label.setText(str(round((position / self.videoLength) * 100, 2)) + "%")

    # 滑动Slider
    def SlidevideoSlider(self, value):
        if self.video_slider.isSliderDown():
            print(self.videoLength)
            self.player.setPosition(int((value / self.video_slider.maximum()) * int(self.videoLength)))
            self.video_label.setText(str(round((value * 1000 / self.videoLength) * 100, 2)) + "%")

    # 按住Slider
    def PressvideoSlider(self, text):
        self.player.setPosition(int(self.videoLength * (self.video_slider.value() * 0.01)))
        self.video_label.setText(str(round((self.video_slider.value() * 1000 / self.videoLength) * 100, 2)) + "%")

    def videoDoubleClicked(self, text):
        # 开始播放后才能全屏
        if self.player.duration() > 0:
            # 当前是否全屏
            if self.videoFullScreen:
                self.player.pause()
                self.videoFullScreenWidget.hide()
                self.player.setVideoOutput(self.video_widget)
                self.player.play()
                self.videoFullScreen = False
            else:
                self.player.pause()
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.player.play()
                self.videoFullScreen = True

    def closeEvent(self, QCloseEvent):
        super(courseVideo, self).closeEvent(QCloseEvent)

        # 删除播放器
        self.player.deleteLater()


class commentWidget(QtWidgets.QWidget, commentGui.Ui_Form):
    def __init__(self):
        super(commentWidget, self).__init__()
        self.setupUi(self)


class searchWidget(QtWidgets.QWidget, searchGui.Ui_Form):
    def __init__(self):
        super(searchWidget, self).__init__()
        self.setupUi(self)


class searchTabWidget(QtWidgets.QWidget, searchTabGui.Ui_Form):
    def __init__(self):
        super(searchTabWidget, self).__init__()
        self.setupUi(self)


class personalHomepageWidget(QtWidgets.QWidget, personalHomepageGui.Ui_Form):
    def __init__(self):
        super(personalHomepageWidget, self).__init__()
        self.setupUi(self)


class courseButton(QtWidgets.QPushButton):
    successCreate = QtCore.Signal(object)

    def __init__(self, course_Info):
        super(courseButton, self).__init__()

        self.courseInfo = course_Info
        self.setFixedSize(250, 125)

        # self.setStyleSheet("QPushButton{border-image: url(课程1.jpg)}")

        # TODO:设置buttonImage
        course_Img = course_Info.pic_path
        if course_Img != '':
            img_path = "QPushButton{border-image: url(" + course_Img + ")}"
            print(img_path)
            self.setStyleSheet(img_path)

        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,
                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.clicked.connect(self.createCourseWidget)

    def createCourseWidget(self):
        self.successCreate.emit(self.courseInfo)


class userWidget(QtWidgets.QWidget):
    def __init__(self, userName="无名氏"):
        super(userWidget, self).__init__()

        # 设置widget固定大小
        self.setFixedSize(175, 50)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        self.user_Name = userName
        self.user_Name_Label = QtWidgets.QLabel()
        self.user_Name_Label.setText(self.user_Name)
        self.user_Name_Label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.user_Button = QtWidgets.QPushButton()
        # 设置sizePolicy
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        # 设置buttonImage
        self.user_Button.setStyleSheet("QPushButton{border-image: url(用户头像.jpg)}")
        self.user_Button.setSizePolicy(self.sizePolicy)
        self.user_Button.setFixedSize(40, 40)

        self.H_layout = QtWidgets.QHBoxLayout()
        self.H_layout.addWidget(self.user_Button)
        self.H_layout.addWidget(self.user_Name_Label)
        self.setLayout(self.H_layout)

        # self.user_Button.clicked.connect(self.createHomePage)

    # 创建个人主页
    def createHomePage(self):
        # 个人主页
        self.homePage = personalHomepageWidget()
        self.homePage.show()

        # 首先生成8个按钮
        for i in range(5):
            for j in range(3):
                course_btn = courseButton("")
                course_btn.setParent(self.parent())
                self.homePage.gridLayout.addWidget(course_btn, j, i)
                course_btn.successCreate.connect(self.courseWiget_To_MainWidget)

    def courseWiget_To_MainWidget(self):
        self.lastWidget.setCurrentIndex(1)


class courseInfo(object):

    def __init__(self):
        super(courseInfo, self).__init__()
        self.courseName = "测试课程"
        self.courseTeacher = "测试老师"
        self.coursePrice = 100
        self.commentsList = []
        self.courseImage = "课程_1.png"


class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()

        # 设置固定大小
        self.setFixedSize(1500, 800)

        # 初始化widget
        self.inifMainWidget()
        self.inifCourseWidget()
        self.searchWidget = searchWidget()
        self.homePage = personalHomepageWidget()
        # 创建登录注册窗口
        self.log_rig_dialog = OpdaWidgets.log_Rig_Dialog()
        self.log_rig_dialog.loginSinal.connect(self.loginChange)

        # 页面切换Widget
        self.stackWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stackWidget)
        self.stackWidget.addWidget(self.mainWidget)
        self.stackWidget.addWidget(self.courseWidget)
        self.stackWidget.addWidget(self.searchWidget)
        self.stackWidget.addWidget(self.homePage)

        self.mainWidget.ue4_button.clicked.connect(lambda: self.stackWidget.setCurrentIndex(2))
        self.searchWidget.pushButton.clicked.connect(lambda: self.stackWidget.setCurrentIndex(0))
        self.courseWidget.back_Button.clicked.connect(lambda: self.stackWidget.setCurrentIndex(0))

    # 初始化首页
    def inifMainWidget(self):
        self.mainWidget = mainWidget()
        self.setMainCourseImage()
        self.mainWidget.login_button.clicked.connect(self.loginFunction)
        self.mainWidget.register_button.clicked.connect(self.registerFunction)

    # 初始化课程页
    def inifCourseWidget(self):
        self.courseWidget = courseWiget()
        # self.courseWidget.listWidget.setSpacing(10)
        self.courseWidget.back_Button.clicked.connect(self.to_CourseWidget)

    # 登陆注册
    def loginFunction(self):
        self.log_rig_dialog.tabWidgets.setCurrentIndex(0)
        self.log_rig_dialog.show()

    def registerFunction(self):
        self.log_rig_dialog.tabWidgets.setCurrentIndex(1)
        self.log_rig_dialog.show()

    # 读取数据库课程图片
    def setMainCourseImage(self):
        # 首先生成8个按钮     self.button_list =[]
        ct = CoursesTable()
        course_list = ct.get_courses_info()
        print(course_list)
        k = 0
        for i in range(4):
            for j in range(2):
                course = course_list[k]
                course_btn = courseButton(course)
                course_btn.setFixedSize(300, 150)
                self.mainWidget.showCourse_gridLayout.addWidget(course_btn, j, i)
                # 传递课程参数到按钮事件
                course_btn.successCreate.connect(lambda arg=course: self.to_CourseWidget(arg))
                k += 1


    def to_CourseWidget(self, course_Info = ''):
        # 点击返回按钮的时候course_Info会传递一个False回来 造成读取错误
        # TODO:加载课程信息至页面

        if course_Info:
            course_img = course_Info.pic_path
            img_path = "QPushButton{border-image: url(" + course_img + ")}"
            self.courseWidget.courseViedo_button.setStyleSheet(img_path)
            self.courseWidget.courseName_label.setText(course_Info.name)
            self.courseWidget.label_10.setText(course_Info.info)
            self.courseWidget.coursePrice_label.setText(str(course_Info.price) + u"元")
        self.stackWidget.setCurrentIndex(1)

    # 进行登录替换
    def loginChange(self, log_Name):
        # 创建userWidget
        self.userWidget = userWidget(log_Name)
        # 去除导航栏的登录注册widget
        self.mainWidget.horizontalLayout.removeWidget(self.mainWidget.widget_3)
        # 隐藏
        self.mainWidget.widget_3.hide()
        # 添加
        self.mainWidget.horizontalLayout.addWidget(self.userWidget)
        # 设置连接
        self.userWidget.user_Button.clicked.connect(self.to_HomePage)

    # 创建个人主页
    def to_HomePage(self):
        # 个人主页
        self.stackWidget.setCurrentIndex(3)
        self.homePage.backToMain_button.clicked.connect(lambda: self.stackWidget.setCurrentIndex(0))
        # 首先生成8个按钮
        for i in range(3):
            for j in range(5):
                course_btn = courseButton("")
                self.homePage.gridLayout.addWidget(course_btn, j, i)
                course_btn.successCreate.connect(self.to_CourseWidget)


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QtWidgets.QApplication(sys.argv)
    # 初始化
    myWin = MyMainWindow()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
