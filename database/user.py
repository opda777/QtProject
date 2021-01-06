#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import Connect


class User:
    def __init__(self, row: tuple):
        self.id = row[0]
        self.password = row[1]
        self.idc = row[2]
        self.name = row[3]
        self.sex = row[4]
        self.birthday = row[5]
        self.telephone = row[6]
        self.icon = row[7]
        self.vip_level = row[8]
        self.balance = row[9]


class UserTable(Connect):
    def __init__(self):
        super().__init__()

    # 用户登录 输入账号密码 返回用户对象
    def user_login(self, user_id, user_pwd):
        user_id = '{1}{0}{1}'.format(user_id, "'")
        user_pwd = '{1}{0}{1}'.format(user_pwd, "'")

        result = self.select('MEMBERS', {'mem_id': user_id, 'mem_password': user_pwd})
        if result == ():
            print("错误的用户名或密码")
            return False
        print(result)
        user = User(result[0])
        return user

    # 用户注册 输入账号密码昵称 成功返回True 失败返回False
    def user_reg(self, user_id, user_pwd, user_name):
        user_id = '{1}{0}{1}'.format(user_id, "'")
        user_pwd = '{1}{0}{1}'.format(user_pwd, "'")
        user_name = '{1}{0}{1}'.format(user_name, "'")
        result = self.select('MEMBERS', {'mem_id': user_id})
        if result == ():
            self.insert('MEMBERS', {'mem_id': user_id, 'mem_password': user_pwd, 'mem_name': user_name})
            return user_name
        else:
            err = u"已经注册过的用户名"
            print(err)
            return False

    # 获取用户数据
    def get_user_info(self, user_id):
        user_id = "'" + user_id + "'"
        result = self.select('MEMBERS', {'mem_id': user_id})
        if result == ():
            print("不存在的用户")
            return 0
        print(result)
        user = User(result[0])
        return user

    def update_user_info(self, user_id, new_dict: dict = {}):
        user_id = "'" + user_id + "'"
        result = self.select('MEMBERS', {'mem_id': user_id})
        self.update('MEMBERS', 'mem_id', user_id, new_dict)
