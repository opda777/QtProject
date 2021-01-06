# -- coding: utf-8 --
from user import UserTable
from course import CoursesTable
from connect import Connect
from courseMessages import CourseMessageTable


# User:
# 用户登陆
def user_login():
    ut = UserTable()
    # user_login(用户ID(email)，密码)
    login_user = ut.user_login('1@qq.com', '1231321')
    # 成功返回用户类 失败返回0


# 用户注册
def user_reg():
    ut = UserTable()
    # user_reg(用户ID(email),密码,昵称)
    reg_user = ut.user_reg('2@qq.com', '222222', 'lcy')
    # 成功返回True 失败False


# 获取用户信息
def get_user_info():
    ut = UserTable()
    ut.get_user_info("2@qq.com")
    # 有结果返回User类 无结果返回0


# Course:
# 获取全部课程信息
def GetAllCourses():
    ct = CoursesTable()

    # 无参数 获取全部
    result_list = ct.get_courses_info()
    # 返回由Course类组成的List
    print(result_list)


# 获取部分课程信息
def GetCourseWithLimit():
    ct = CoursesTable()

    # get_courses_info(条件字典{"字段":"内容",...}, 结果条数)
    result_list = ct.get_courses_info({"tags": "'UE4'"}, 2)
    # 返回由Course类组成的List
    for result in result_list:
        print(result.name)


# 获取与课程相关的资源
def get_course_resource():
    ct = CoursesTable()

    # get_resources(课程ID)
    path = ct.get_resources(1)
    print(path)
    # 返回元组(视频路径, 封面路径)


# 发布留言
def post_message():
    cmt = CourseMessageTable()
    # post_message(课程ID, 用户ID, 评论内容)
    cmt.post_message(1, "1@qq.com", "gg")


# 回复留言
def reply_message():
    cmt = CourseMessageTable()
    # reply_message(留言ID, 职员ID, 回复内容）
    cmt.reply_message(6, "1@emp.com", "thx")


def delete_test():
    ct = Connect()
    ct.delete('administrators')


get_course_resource()
