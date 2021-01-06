#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","Lcy7814","study_platform" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()


def connectMySQL():
    # 打开数据库连接
    db = pymysql.connect("localhost","root","Lcy7814","study_platform" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return db,cursor

global db,cursor
db,cursor = connectMySQL()

def queryTest():
    # SQL 查询语句
    sql = "SELECT * FROM Administrators"
    try:
    # 执行SQL语句
        cursor = connectMySQL()
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            admin_id = row[0]
            admin_password = row[1]
            power = row[2]

            # 打印结果
            print ("admin_id=%s,admin_password=%s,power=%s" % \
                    (admin_id, admin_password, power))
    except:
        print ("Error: unable to fetch data")
    
    # 关闭数据库连接
def insertTest():
    # SQL 插入语句
    sql = """INSERT INTO MEMBERS(member_id,
            mem_password, idc , mem_name)
            VALUES ('U00000003', '654321', 440000000000000000, 'hhgnb')"""
    try:
    # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

def deleteTest():
    sql = "DELETE FROM MEMBERS WHERE member_id ='U00000003'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    

def updateTest():
    sql = "UPDATE MEMBERS SET mem_name = 'hhg' WHERE member_id ='U00000002'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def main():
    updateTest()
    
if __name__ == '__main__':
    main()

