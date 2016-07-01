# -*- coding:utf-8 -*-
__author__ = 'tsbc'

from selenium import webdriver
import time,selenium
import connmssql,xlrd
import sys
from K_f_s.public import BasePage
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("E:\\ERP\\Release01\\K_f_s\\public")
from selenium.webdriver.common.action_chains import ActionChains
import robot

class Actionkeywords(BasePage.Action):
	"""定义关键字方法"""

	def openBrowser(self, browser):
		"""打开浏览器方法"""
		# self.driver = webdriver.Firefox()
		# self.driver.maximize_window()
		# self.driver.implicitly_wait(30)
		# return  self.driver
		# 通过传参选择启动浏览器
		self.browser = browser  # 传入浏览器对象

		if self.driver == None:
			if self.browser.upper() == 'IE':
				self.driver = webdriver.Ie()
			elif self.browser.upper() == 'CHROME':
				self.driver = webdriver.Chrome()
			elif self.browser.upper() == 'FIREFOX':
				self.driver = webdriver.Firefox(timeout=10)
			elif self.browser.upper() == 'SAFARI':
				self.driver = webdriver.Safari()
			elif self.browser.upper() == 'PHANTOMJS':
				self.driver = webdriver.PhantomJS()
			else:
				#self.options = webdriver.ChromeOptions()

				#self.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

				#self.driver = webdriver.Chrome(chrome_options=self.options)
				self.driver = webdriver.Chrome()
				#self.driver = webdriver.Firefox()
		# pass
		#print u"加载浏览器驱动失败!"
		self.verificationErrors = []

	# return self.driver

	def navigate(self, url, title):
		"""
		跳转Url地址
		"""
		self.open(url, title)

	def closeBrowser(self,num):
		"""关闭浏览器"""

		self.close(num)

	# 调用send_keys
	def input_Text(self, loc, text):
		"""文本框输入内容"""
		print loc, text
		# print("aaaa")
		self.send_keys(loc, text)

	#
	def Submit(self, submit_loc):
		"""提交表单"""
		self.saveScreenshot(self.driver, "submit")
		self.find_element(*submit_loc).click()

	def clickElement(self,button_loc):
		"""点击按钮"""
		# print self.find_element(*button_loc).text
		print 'find_element()',button_loc
		self.find_element(button_loc).click()

	def find_elements_i(self,index,element_loc):
		"""点击元素"""
		# print self.find_elements_i(i, *element_loc)
		self.find_elements_i(index,*element_loc)

	def switch_frame(self, loc):
		"""
		切换iframe
		"""
		self.switch_to_frame(loc)
	def switch_to_alert(self,loc):
		'''处理alert弹窗'''
		if loc == 'Sure':
			self.switch_to_alert().accept()
		else:
			self.switch_to_alert().dismiss()


	def switch_frame_default(self):
		"""还原默认frame"""
		self.driver.switch_to_default_content()

	def DataAssert(self, expected_loc, actual):
		"""通用断言关键字
		:param
		expected_loc  预期结果元素标识 driver.find_element(*expected_loc).text 获取预期值
		actual  实际结果
		"""
		expected = self.find_element(expected_loc).text
		print u'预期结果：' + actual
		print u'实际结果：' + expected
		if actual not in expected:
			self.saveScreenshot(self.driver, "error")
		assert actual in expected

	def MSQuery(self, host, user, passwd, db, sql):
		"""MSSQL QUERY 关键字
		:param
		host 主机名名称或IP
		user 登录用户
		passwd 登录密码
		db  连接数据库
		sql 执行的SQL
		"""
		ms = connmssql.MSSQL(host, user, passwd, db)
		return ms.ExecQuery(sql)


	def DBAssert(self,expected, actual):
		"""通用断言关键字
		:param expected  预期结果
		:param actual    实际结果
		"""
		print u'预期结果：' + actual
		print u'实际结果：' + expected
		if actual not in expected:
			self.saveScreenshot(self.driver, "error")
		assert actual in expected


	def login(self, username, password, userinput, passinput,btnsubmit):
		"""
		构造登录使用的公用方法
		"""
		# self.driver.implicitly_wait(30)
		self.find_element(userinput).send_keys(username)
		self.find_element(passinput).send_keys(password)
		#self.find_element(*VerifyImg).send_keys(VerifyNo)
		self.find_element(btnsubmit).click()
		time.sleep(1)


	def verifyLogin(self, span_loc, userid_loc):
		"""登录校验"""
		spanTF = True
		try:
			# 通过捕获异常，判断是否显示的出了Tip文本，显示为 True 否则为False
			self.find_element(*span_loc).text
			spanTF = True
		except:
			spanTF = False

		if spanTF:
			print self.find_element(*span_loc).text
		else:
			print self.driver.title
			self.checkTrue(self.find_element(*userid_loc).text, u"登录失败")