#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import Connect


class CoursesTable(Connect):

    def __init__(self):
        super().__init__()

    def loadCourseListByTags(self,tags):
        conn = self.conn 
        cursor = self.cursor
        sql = "select * from courses where tags = '%s'"%tags
        if(cursor.execute(sql)):
            #这里返回的是元组类型的结果

            course_tuple = cursor.fetchall()
            results_list = self.makeCourseList(course_tuple)
            # print (results_list)
            return results_list

    def loadCourseListById(self,id):
        #根据ID获取课程
        conn = self.conn 
        cursor = self.cursor
        sql = "select * from courses where course_id = '%s'"%id
        cursor.execute(sql)
        results = cursor.fetchone()
        print (results)
        results_course = Course(results)
        return results_course
  
    def loadCourseListByName(self,course_name):
        #根据名字模糊搜索课程
        conn = self.conn 
        cursor = self.cursor
        sql = "select * from courses where course_name like '%s'"%('%'+course_name+'%')

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

    def makeCourseList(self,classname='Course',tuple):
        super().make_result_list
        # course_list = list()
        # #把数据元组转换成自定义类的列表
        # for item in tuple:
        #     myCourse = Course(item)
        #     course_list.append(myCourse)
        #     print(myCourse.course_name)

        # return course_list

    def get_data(self, sql):
        conn = self.conn 
        cursor = self.cursor
        sql = "select * from courses LiMIT '%s'"%rowlimit
        if cursor.execute(sql):
            results = cursor.fetchall()
            data_list = makeCourseList(results)

        return data_list



    def getData(self):
        conn = self.conn 
        cursor = self.cursor
        sql = "select * from courses "
        if cursor.execute(sql):
            results = cursor.fetchall()
            data_list = makeCourseList(results)

        return data_list
       

