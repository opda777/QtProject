#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import Connect
from connect import to_str_format



# Course对象
class Course:

    def __init__(self, row):
        # 接受传进来的元组 从元组各项中获取属性
        # course_id,employee_id,course_name,tags,info,totaltime,pic_path,price,member_num=range(9)
        self.course_id = row[0]
        self.employee_id = row[1]
        self.name = row[2]
        self.tags = row[3]
        self.info = row[4]
        self.totaltime = row[5]
        self.pic_path = row[6].replace("\\", "/")
        self.price = row[7]
        self.member_num = row[8]

        # print (self.course_name)


# 连接课程表
class CoursesTable(Connect):

    def __init__(self):
        super().__init__()

    def loadCourseListByTags(self, tags):
        conn = self.conn
        cursor = self.cursor
        sql = "select * from courses where tags = '%s'" % tags
        if cursor.execute(sql):
            # 这里返回的是元组类型的结果

            course_tuple = cursor.fetchall()
            results_list = self.make_course_list(course_tuple)
            # print (results_list)
            return results_list

    def loadCourseListById(self, course_id):
        # 根据ID获取课程
        conn = self.conn
        cursor = self.cursor
        sql = "select * from courses where course_id = '%s'" % course_id
        cursor.execute(sql)
        results = cursor.fetchone()
        print(results)
        results_course = Course(results)
        return results_course

    def loadCourseListByName(self, course_name):
        # 根据名字模糊搜索课程
        conn = self.conn
        cursor = self.cursor
        sql = "select * from courses where course_name like '%s'" % ('%' + course_name + '%')

        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

    # def loadPic(self,course_id):
    #     #由ID获取课程封面图片
    #     conn = self.conn
    #     cursor = self.cursor
    #     sql = "select pic_path from courses where course_id = '%s'"%course_id
    #     cursor.execute(sql)
    #     results = cursor.fetchone()[0]
    #     print (results)

    def make_course_list(self, c_tuple):
        course_list = self.make_result_list(Course, c_tuple)
        return course_list

    def get_data(self, args):
        conn = self.conn
        cursor = self.cursor

        if len(args):
            sql = "select * from courses LIMIT %s;" % args[0]
            results = cursor.fetchall()
            data_list = self.make_course_list(results)

        else:
            sql = "select * from courses "
            if cursor.execute(sql):
                results = cursor.fetchall()
            if cursor.execute(sql):
                data_list = self.make_course_list(results)

        return data_list

    def add_course(self, employee_id, course_name, tags, info: str = "", totaltime: int = 0, path: str = "",
                   price: int = 0):

        # 添加引号
        employee_id = to_str_format(employee_id)
        course_name = to_str_format(course_name)
        tags = to_str_format(tags)
        info = to_str_format(info)
        path = to_str_format(path)

        # 插入数据
        self.insert("courses", {"employee_id": employee_id, "course_name": course_name, "tags": tags, "info": info,
                                "totaltime": totaltime, "path": path, "price": price})

    def delete_course(self, limit_dict: dict):
        self.delete("courses", limit_dict)

    def get_courses_info(self,  kwargs: dict = {},  limit: int = 0):
        res = self.select("courses", kwargs, '*', limit)
        res_list = self.make_course_list(res)
        return res_list

    def get_resources(self, course_id):
        # 获取与课程相关的资源
        course_video_path = self.select('resources', {'course_id': course_id, "resource_type": 1}, "localPath", 1)[0][0]
        course_pic_path = self.select('resources', {'course_id': course_id, "resource_type": 2}, "localPath", 1)[0][0]
        # course_video_path = course_video_path.replace("\\", "/")
        course_pic_path = course_pic_path.replace("\\", "/")
        return course_video_path, course_pic_path
        # 获取资源路径



