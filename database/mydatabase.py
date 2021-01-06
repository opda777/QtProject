#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from connnect import Connect


class DB():
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    user="root",
                                    password="Lcy7814",
                                    database="learningplatform")

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.conn.cursor()

    # 关闭数据库连接
    def close_conn(self):
        self.conn.close()

    # 登陆 成功返回ID 失败返回0
    def userLogin(self, user_id, user_pwd):

        conn = self.conn
        cursor = self.cursor

        sql = "select * from MEMBERS where mem_id = '%s' and mem_password = '%s'" % (user_id, user_pwd)
        cursor.execute(sql)

        result = cursor.execute(sql)
        if result:
            return user_id
        else:
            return 0

    # 注册 成功返回1 失败0 用户已经存在-1
    def userReg(self, user_id, user_pwd, user_name):

        conn = self.conn
        cursor = self.cursor

        sql = "select * from MEMBERS where mem_id = '%s'" % user_id
        result = cursor.execute(sql)

        # 判断用户是否存在
        if result:
            print('user exists!')
            return -1

        else:
            sql_1 = "INSERT INTO MEMBERS(mem_id,mem_password,mem_name) VALUES ('%s', '%s','%s');" % (
            user_id, user_pwd, user_name)

            try:
                result_1 = cursor.execute(sql_1)
                conn.commit()
            except:
                # 如果发生错误则回滚
                conn.rollback()
                return 0

        return 1

    def loadCourseList(self, tags):
        conn = self.conn
        cursor = self.cursor
        sql = "select * from courses where tags = '%s'" % tags
