# -*- coding:utf-8 -*-
__author__ = 'tsbc'

#import pymssql    此模块暂时不支持64位系统
import pyodbc

class MSSQL:
	"""
	连接执行SQL
	"""

	def __init__(self, host, user, passwd, db):

		self.host = host
		self.user = user
		self.passwd = passwd
		self.db = db

	def __GetConnect(self):

		if not self.db:
			raise (NameError, "没有设置数据库信息！")
        #连接数据库
		self.coxn = pyodbc.connect('DRIVER={SQL Server};'
                                   'server=self.host;'
                                   'user=self.user;'
                                   'password=self.passwd;'
                                   'database=self.db')

		cur = self.coxn.cursor()

		if not cur:
			raise (NameError, "连接数据库失败")
		else:
			return cur

	def ExecQuery(self, sql):
		cur = self.__GetConnect()    #获取游标
		cur.execute(sql)             #执行sql语句
		row = cur.fetchone()         #获取所有记录列表
		return row[0]                #根据需要返回某字段的值
# sql= "SELECT UserAccount FROM SystemUser WHERE UserAccount = 'sss';"
# ms = MSSQL('192.168.1.7','testerp','111aa~','TERP20151116')
# rs = ms.ExecQuery("SELECT UserAccount FROM SystemUser WHERE UserAccount = 'testadd'")
# print rs
#
# ms.coxn.close()