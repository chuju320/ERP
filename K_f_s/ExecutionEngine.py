# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from public import BasePage
from config import actionKeyword
from test import test_support
import HTML_Result


testunit = unittest.TestSuite()

class ExecutionEngin(unittest.TestCase):
	"""用例描述信息"""
	#脚本初始化
	@classmethod
	def setUpClass(cls):
		# cls.self.driver = None
		# cls.self.driver = webself.driver.Firefox()
		# cls.self.driver.maximize_window()
		cls.filepath = "dataEngine\\erpdata.xls"

	#测试用例
	def action(self,*txt):
		"""
		测试Demo
		"""
		exeKeyword = actionKeyword.Actionkeywords()
		base = BasePage.Action()
		Summary = txt[3]		#txt是case data表中的行数据
		print "["+Summary+"]"
		k =4
		stepdata = base.getTabledata(self.filepath, "Test Steps")
		for j in stepdata:   #遍历每行用例步骤
			if txt[1] == j[0]:
				# print j[3]
				if j[3] == "openBrowser":
					print j[2]
					global  num
					num = 0
					self.driver = exeKeyword.openBrowser(j[4])

				elif j[3] == "InputText":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.input_Text(loc, txt[k])
					k += 1
				elif j[3] == "submit":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.Submit(loc)
				# elif j[3] == "verifyLogin":
				# 	print j[2]
				# 	loc_1 = base.locate(j[4])
				# 	loc_2 = base.locate(j[5])
				# 	exeKeyword.verifyLogin(loc_1, loc_2)
				elif j[3] == "closeBrowser":
					print j[2]
					time.sleep(5)
					num += 1
					print 'num=%d'%num
					exeKeyword.closeBrowser(num)
				elif j[3] == "navigate":
					print j[2]
					url = j[4]
					title = j[5]
					exeKeyword.navigate(url,title)
				elif j[3] == "click":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.clickElement(loc)
				elif j[3] == "switchframe":  #重点问题
					print j[2]
					# loc = base.Locatetext(j[4])
					loc = base.locate(j[4])
					print loc
					loc = exeKeyword.find_element(loc)   #为什么需要加*
					exeKeyword.switch_frame(loc)
					print u'跳转成功'
				elif j[3] == "defaultframe":
					print j[2]
					exeKeyword.switch_frame_default()
				elif j[3] == "assert":
					print j[2]
					expected_loc = base.locate(j[4])
					print 'expected_loc:%s' % expected_loc
					actual = j[5]
					exeKeyword.DataAssert(expected_loc,actual)
				elif j[3] == "sleep":
					print j[2]
					s = int(j[4])
					time.sleep(s)
				elif j[3] == "login":
					print j[2]
					username = j[4]
					password = j[5]
					#VerifyNo = j[6]
					userinput = base.locate(j[6])
					passinput = base.locate(j[7])
					#Verifyimg = base.locate(j[9])
					btnsubmit = base.locate(j[8])
					self.driver = self.driver
					exeKeyword.login(username,password,userinput,passinput,btnsubmit)
				elif j[3] == "DBAssert":
					print j[2]
					host = '192.168.1.7'
					user = 'testerp'
					password = '111aa~'
					db = 'TERP20151116'
					sql = j[4]
					actual = j[5]
					expected = exeKeyword.MSQuery(host,user,password,db,sql)
					exeKeyword.DBAssert(expected,actual)

	@staticmethod
	def getTestFunc(*txt):
		def func(self):
			self.action(*txt)
		return func


	#脚本退出
	@classmethod
	def tearDownClass(cls):
		print "End"
		# cls.self.driver.quit()

def generateTestCases(run,result='Yes',open='No'):
	login_page = BasePage.Action()
	casedata = login_page.getTabledata("dataEngine\\erpdata.xls", "Test Cases")
	for i in casedata:
		TCid = i[1]   #Login
		if i[4] == "Y":
			print "【Run】"+i[2]+"："
			print " + -"*8
			table = login_page.getTabledata("dataEngine\\erpdata.xls", "case data")
			for txt in table:
				if (txt[2] == "Y") & (txt[1] == TCid):  #Login==Login
					print txt
					setattr(ExecutionEngin, 'test_%s_%s' % (txt[0], i[1]), ExecutionEngin.getTestFunc(*txt))
					#添加测试用例到测试套件
					testunit.addTest(ExecutionEngin('test_%s_%s' % (txt[0], i[1])))
	if run == 'Debug':
		print '■■■■Debug模式■■■■'
		test_support.run_unittest(ExecutionEngin)
	else:
		#调用测试生成报告
		HTML_Result.Result(result,open,testunit)

#if __name__ == '__main__':
#generateTestCases()

#def test_main():
#	test_support.run_unittest(ExecutionEngin)


