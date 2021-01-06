# -*- coding: utf-8 -*-
from PySide2 import QtWidgets,QtCore,QtGui
import sys
from database.user import UserTable



# 按钮拉伸宽度
btn_expand_width = 24
# 按钮收缩宽度
btn_shrik_width = 6
class ImageViewLabel(QtWidgets.QLabel):
    # 初始化
    def __init__(self):
        super(ImageViewLabel, self).__init__()
        # 初始化数值
        self.offset = 0
        self.curIndex = 0
        self.preIndex = 0
        self.imageList = []
        self.leftToRight = True

        # 设置Label大小
        self.setMinimumSize(120,240)
        # 进行按钮分组
        self.btn_Grounp = QtWidgets.QButtonGroup(self)
        # connnect 选择传递信号button id
        self.btn_Grounp.buttonClicked[int].connect(self.onButtonClicked)

        # 动画容器，并行完成所有动画
        self.btnParalGroup = QtCore.QParallelAnimationGroup(self)
        # 定义图片切换属性动画
        self.imageAnimation = QtCore.QPropertyAnimation(self.btnParalGroup)
        # 设置动画曲线
        self.imageAnimation.setEasingCurve(QtCore.QEasingCurve.OutCirc)
        # 设置动画时间
        self.imageAnimation.setDuration(800)
        # connect
        self.imageAnimation.valueChanged.connect(self.onImagevalueChanged)

        # 动画容器，串行完成所有动画，即按顺序执行动画
        self.sequentialGroup = QtCore.QSequentialAnimationGroup(self.btnParalGroup)
        # 定义按钮拉伸属性动画
        self.btnExp_Animation = QtCore.QPropertyAnimation(self.sequentialGroup)
        # 设置动画曲线
        self.btnExp_Animation.setEasingCurve(QtCore.QEasingCurve.OutCubic)
        # 设置动画时间
        self.btnExp_Animation.setDuration(400)
        # connect
        self.btnExp_Animation.valueChanged.connect(self.onBtnExpvalueChange)


        # 定义按钮收缩属性动画
        self.btnShrik_Animation = QtCore.QPropertyAnimation(self.sequentialGroup)
        # 设置动画曲线
        self.btnShrik_Animation.setEasingCurve(QtCore.QEasingCurve.OutCubic)
        # 设置动画时间
        self.btnShrik_Animation.setDuration(400)
        # connect
        self.btnShrik_Animation.valueChanged.connect(self.onBtnShrikvalueChange)

        # 按钮切换串行执行
        self.sequentialGroup.addAnimation(self.btnExp_Animation)
        self.sequentialGroup.addAnimation(self.btnShrik_Animation)

        # 图片切换和按钮切换并行执行
        self.btnParalGroup.addAnimation(self.imageAnimation)
        self.btnParalGroup.addAnimation(self.sequentialGroup)

        # 初始化
        self.initControl()

    def initControl(self):
        # 创建一个总Widget
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        # 设置名称，这样findChild可以查询到对象
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.switchBtnLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        # 设置属性
        self.switchBtnLayout.setSpacing(12)
        self.switchBtnLayout.setContentsMargins(0,0,0,0)
        #self.

        # 开启计时器用于图片滑动
        self.imageTimer = QtCore.QTimer(self)
        self.imageTimer.setInterval(2000)
        self.imageTimer.timeout.connect(self.onImageShowTimeout)
        self.imageTimer.start()


    def onButtonClicked(self,index):
        # 判断点击是否是同一个按钮
        if self.curIndex == index:
            return;

        # 判断index达到左尽头
        if index < 0:
            index = len(self.imageList) - 1
        # 判断index到达右尽头
        if index >= len(self.imageList):
            index = 0

        self.preIndex = self.curIndex
        self.curIndex = index


        # 进行图片切换
        if (self.preIndex < self.curIndex):
            # 向左滑
            self.imageAnimation.setStartValue(0)
            self.imageAnimation.setEndValue(0-self.width())

        else:
            # 向右滑
            self.imageAnimation.setStartValue(0)
            self.imageAnimation.setEndValue(self.width())

        # 设置按钮动画
        self.btnShrik_Animation.setStartValue(btn_expand_width)
        self.btnShrik_Animation.setEndValue(btn_shrik_width)

        self.btnExp_Animation.setStartValue(btn_shrik_width)
        self.btnExp_Animation.setEndValue(btn_expand_width)

        # 重启计时器
        self.imageTimer.start(2000)
        # 开启动画
        self.btnParalGroup.start()

        #self.update()


    def onImagevalueChanged(self,variant):
        print(int(variant))
        offset = int(variant)
        self.update()

    def onBtnExpvalueChange(self,variant):
        self.btn_Grounp.button(self.curIndex).setFixedWidth(int(variant))

    def onBtnShrikvalueChange(self,variant):
        for index in range(len(self.imageList)):
            if (self.curIndex != index and self.btn_Grounp.button(index).width() > btn_shrik_width):
                self.btn_Grounp.button(index).setFixedWidth(int(variant))

    # 用于计时器自动图片切换
    def onImageShowTimeout(self):
        self.onButtonClicked(self.curIndex + 1)

    # 绘制函数
    def paintEvent(self,event):
        #self.paintEvent(event)
        # 绘制工具
        painter = QtGui.QPainter(self)
        # 防止图片走样
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)

        # 进行image绘制
        painter.drawPixmap(self.offset, 0,QtGui.QPixmap(self.imageList[self.curIndex]).scaled(self.width(),self.height()
                                                                            ,QtGui.Qt.KeepAspectRatioByExpanding,
                                                                            QtGui.Qt.SmoothTransformation))
        painter.drawPixmap(self.offset - self.width(), 0, QtGui.QPixmap(self.imageList[self.preIndex]).scaled(self.width(), self.height(),
                                                                             QtGui.Qt.KeepAspectRatioByExpanding,
                                                                             QtGui.Qt.SmoothTransformation))

    # 添加图片
    def addImage(self,imageListParam):
        self.imageList = imageListParam
        for index in range(len(self.imageList)):
            # 根据图片数量创建Button
            button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            button.setCursor(QtCore.Qt.PointingHandCursor)
            button.setFixedSize(btn_shrik_width, btn_shrik_width)

            # 添加到buttonGroup
            self.btn_Grounp.addButton(button,index)
            # 添加到switchBtnLayout
            self.switchBtnLayout.addWidget(button)

        # button等比例大小
        self.switchBtnLayout.addStretch()

class ImageTextWidget(QtWidgets.QWidget):
    def __init__(self,title, text, imagePath):
        super(ImageTextWidget, self).__init__()
        Vlayout = QtWidgets.QVBoxLayout(self)
        title_label = QtWidgets.QLabel(title)
        title_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        text_label = QtWidgets.QLabel(text)
        text_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(QtGui.QPixmap(imagePath))
        image_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        Vlayout.addWidget(image_label)
        Vlayout.addWidget(title_label)
        Vlayout.addWidget(text_label)
        Vlayout.setSpacing(0)
        Vlayout.addStretch()

class log_Rig_Dialog(QtWidgets.QDialog):

    loginSinal = QtCore.Signal(str)

    def __init__(self):
        super(log_Rig_Dialog, self).__init__()

        # 关闭标题
        #self.setWindowTitle(QtCore.Qt.FramelessWindowHint)
        # 设置标题
        self.setWindowTitle("登录注册页面")

        # 设置大小
        self.setFixedSize(500,250)

        self.createWidgets()
        self.createLayouts()
        self.createConnects()

    def createWidgets(self):
        # 标签页
        self.tabWidgets = QtWidgets.QTabWidget()

        # 为标签页创建两个选项卡
        self.login_tab = QtWidgets.QWidget()
        self.register_tab = QtWidgets.QWidget()

        # 添加到标签页中
        self.tabWidgets.addTab(self.login_tab,"登录")
        self.tabWidgets.addTab(self.register_tab,"注册")

    def createLayouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.tabWidgets)
        self.create_login_tab()
        self.create_register_tab()

    def createConnects(self):
        self.login_button.clicked.connect(self.logFunction)
        self.register_button.clicked.connect(self.rigsterFunction)

    def create_login_tab(self):
        # 表单布局
        formLayout = QtWidgets.QFormLayout()
        self.log_account = QtWidgets.QLineEdit()
        self.log_account.setPlaceholderText("邮箱/手机/用户名")
        self.log_password = QtWidgets.QLineEdit()
        self.log_password.setPlaceholderText("密码")
        self.login_button = QtWidgets.QPushButton("登录")
        # 添加账号密码文本框
        formLayout.addRow("账号",self.log_account)
        formLayout.addRow("密码",self.log_password)
        formLayout.addWidget(self.login_button)

        # 设置布局
        self.login_tab.setLayout(formLayout)




    def create_register_tab(self):
        # 表单布局
        formLayout = QtWidgets.QFormLayout()
        self.rig_account = QtWidgets.QLineEdit()
        self.rig_account.setPlaceholderText("填写你常用的邮箱作为登录账号")
        self.rig_userName = QtWidgets.QLineEdit()
        self.rig_userName.setPlaceholderText("中、英文均可，最长18个英文或9个汉字")
        self.rig_password = QtWidgets.QLineEdit()
        self.rig_password.setPlaceholderText("5-20位英文、数字、符号，区分大小写")
        self.register_button = QtWidgets.QPushButton("同意服务协议并注册")
        # 添加到表单layout
        formLayout.addRow("邮箱",self.rig_account)
        formLayout.addRow("用户名",self.rig_userName)
        formLayout.addRow("密码",self.rig_password)
        formLayout.addWidget(self.register_button)

        # 设置布局
        self.register_tab.setLayout(formLayout)

    # 登录事件
    def logFunction(self):
        log_Name = None
        log_account = self.log_account.text()
        log_password = self.log_password.text()

        # 进行登录判断
        # TODO
        ut = UserTable()
        log_user = ut.user_login(log_account, log_password)


        if (log_user):
            # 弹出登录成功窗口
            messageBox = QtWidgets.QMessageBox.information(self,"提示","登录成功！",QtWidgets.QMessageBox.Ok)
            user_name = log_user.name
            self.loginSinal.emit(user_name)
            self.close()


    # 注册事件
    def rigsterFunction(self):
        rigster_name = self.rig_userName.text()
        rigster_account = self.rig_account.text()
        rigster_password = self.rig_password.text()

        # 进行数据库判断，如果没有相同账号就存入数据库
        # TODO
        ut = UserTable()
        reg_user = ut.user_reg(rigster_account, rigster_password, rigster_name)
        if (reg_user):
            # 弹出注册成功窗口
            messageBox = QtWidgets.QMessageBox.information(self,"提示","注册成功！",QtWidgets.QMessageBox.Ok)
            self.loginSinal.emit(reg_user)
        else:
            # 弹出注册失败窗口
            messageBox = QtWidgets.QMessageBox.information(self, "提示", "注册失败！", QtWidgets.QMessageBox.Ok)






