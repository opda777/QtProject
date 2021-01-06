#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import Connect
from connect import to_str_format


class CourseMessage:
    def __init__(self, row: tuple):
        self.id = row[0]
        self.course_id = row[1]
        self.employee_id = row[2]
        self.mem_id = row[3]
        self.message_info = row[4]
        self.message_time = row[5]
        self.reply_info = row[6]
        self.reply_time = row[7]


class CourseMessageTable(Connect):
    def __init__(self):
        super().__init__()

    def make_course_message_list(self, c_tuple):
        message_list = super().make_result_list(CourseMessage, c_tuple)
        return message_list

    def post_message(self, course_id, mem_id, message_info):
        course_id = to_str_format(course_id)
        mem_id = to_str_format(mem_id)
        message_info = to_str_format(message_info)
        self.insert('courses_messages', {"course_id": course_id, "mem_id": mem_id, "message_info": message_info})

    def reply_message(self, messages_id, employee_id , reply_info):
        messages_id = to_str_format(messages_id)
        employee_id = to_str_format(employee_id)
        reply_info = to_str_format(reply_info)
        self.update('courses_messages', "message_id", messages_id, {"employee_id": employee_id, "reply_info": reply_info})
