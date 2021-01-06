#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import importlib


# 连接基类
class Connect:

    def __init__(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.conn = pymysql.connect(host="localhost",
                                    user="root",
                                    password="Lcy7814",
                                    database="learningplatform")
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 析构时关闭连接
        self.close_conn()

    def close_conn(self):
        # 关闭数据库连接
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql):
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql):
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return result

    def __edit(self, sql):
        conn = self.conn
        cursor = self.cursor
        count = 0
        try:

            count = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        return count

    @staticmethod
    def make_result_list(class_name, r_tuple):

        if len(r_tuple) == 1:
            return class_name(r_tuple[0])

        result_list = list()
        for item in r_tuple:
            new_result = class_name(item)
            result_list.append(new_result)
        return result_list

    def get_data(self, sql, *args):

        if args == ():
            self.get_all()

    def select(self, table: str, kwargs: dict, item: str = '*', limit: int = 0):
        cursor = self.cursor
        # item为要选择的列 不写默认为全部

        sql = "select %s from %s" % (item, table)
        key_len = len(kwargs)
        print(sql)

        # 如果字典参数不为空 添加where
        if kwargs != {}:
            sql += " where "
        i = 0
        for k, v in kwargs.items():
            sql_add_1 = "%s = %s" % (k, v)
            # 如果字典项不为首项或者末项 在sql语句后加"and"
            if i != 0 and i != key_len:
                sql_add_1 = " and " + sql_add_1
            i = i + 1

            sql = sql + sql_add_1
        # 如果limit参数不为0 在SQL语句中添加limit语句
        if limit != 0:
            sql_add_2 = " LIMIT %s" % limit
            sql = sql + sql_add_2
        print(sql)
        cursor.execute(sql)

        # if limit == 1:
        #     result = cursor.fetchone()
        # else:
        #     result = cursor.fetchall()
        result = cursor.fetchall()
        return result

    def update(self, table: str, key: str, value: any, kwargs: dict):
        sql_1 = "UPDATE %s SET " % table
        sql_2 = " WHERE %s = %s " % (key, value)
        key_len = len(kwargs)
        i = 0
        sql_1_add = ""
        for k, v in kwargs.items():
            # 如果字典项不为首项或者末项 在sql语句后加"and"

            sql_1_add = "%s = %s " % (k, v)
            if i != 0 and i != key_len:
                sql_1_add = " , " + sql_1_add
                # sql_add_1 = " , " + sql_add_1

            sql_1 += sql_1_add
            i = i + 1
            print(sql_1_add)
        sql = sql_1 + sql_2

        print(sql)
        self.__edit(sql)

    def insert(self, table: str, data_dict: dict):

        # key_list = []
        # value_list = []

        # for k in data_dict:
        #     key_list.append(k)
        #     value_list.append(data_dict[k])

        key_tuple = tuple(data_dict)
        value_tuple = tuple(data_dict.values())
        sql1 = ",".join(key_tuple)
        sql2 = ','.join(value_tuple)
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, sql1, sql2)
        print(sql)

        self.__edit(sql)

    def delete(self, table: str, data_dict: dict = {}):
        key_tuple = tuple(data_dict)
        value_tuple = tuple(data_dict.values())
        sql_limit = "Where "
        sql = "DELETE FROM %s " % table
        i = 0

        if data_dict == {}:
            print(sql)
            self.__edit(sql)
            return

        for key in key_tuple:
            sql_limit_add = key + " = %s " % value_tuple[i]
            i += 1
            sql_limit += sql_limit_add
        sql += sql_limit

        print(sql)

        print(self.__edit(sql))


def to_str_format(word):
    return '{1}{0}{1}'.format(word, "'")
