#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from typing import NamedTuple

class Course(NamedTuple):
    # course_id,employee_id,course_name,tags,info,totaltime,pic_path,price,member_num=range(9)
    course_id : int
    employee_id : str
    course_name : str
    tags : str
    info : str
    totaltime :float
    pic_path : str
    price : float
    member_num :int




