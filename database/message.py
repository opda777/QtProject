#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 留言
from connect import Connect


class Message:
    def __init__(self, row):
        message_id = row[0]
        course_id = row[1]
        employee_id = row[2]
        mem_id = row[3]
        message_info = row[4]
        message_time = row[5]
        reply_info = row[6]
        reply_time = row[7]


class MessageTable(Connect):
    def __init__(self):
        super().__init__()

    def postMessage(self, mem_id, course_id, message_info):
        conn = self.conn
        cursor = self.cursor

        sql = "INSERT INTO courses_messages(mem_id,course_id,message_info) VALUES ('%s', '%s','%s');" % (
            mem_id, course_id, message_info)
        try:
            result = cursor.execute(sql)
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

    def replyMessage(self, message_id, employee_id, reply_info):
        conn = self.conn
        cursor = self.cursor

        sql = "UPDATE courses_messages SET employee_id='%s' , reply_info='%s' WHERE message_id='%s'" % (
            employee_id, reply_info, message_id)
        try:
            result = cursor.execute(sql)
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('111')

    def getCourseMessages():
        pass
