#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from connect import Connect


class UserTable(Connect):
    def __init__(self):
        super().__init__()

    # 登陆 成功返回ID 失败返回0
    def user_login(self, user_id, user_pwd):

        conn = self.conn
        cursor = self.cursor

        sql = "select mem_name from MEMBERS where mem_id = '%s' and mem_password = '%s'" % (user_id, user_pwd)
        cursor.execute(sql)

        result = cursor.fetchone()

        if cursor.execute(sql):
            user_name = str(result[0])
            # print('welcome!' + user_name)
            return user_id
        else:
            return 0

    # 注册成功返回1 失败0 用户已经存在-1
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
