# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os, HTMLTestRunner

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.base_url = "http://192.168.1.8/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        time.sleep(1)
        driver.get(self.base_url + "/SystemManager/Account")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_id("UserAccount").clear()
        driver.find_element_by_id("UserAccount").send_keys("admin")
        time.sleep(1)
        driver.find_element_by_id("UserPassword").clear()
        driver.find_element_by_id("UserPassword").send_keys("123")
        time.sleep(1)

        now = driver.current_window_handle
        print now

        driver.find_element_by_id("btnLogin").click()
        driver.implicitly_wait(10)

        all = driver.window_handles

        for i in all:
            print i
            driver.switch_to_window(i)
            print driver.title


            if driver.title.__contains__('ErpLayout'):

                driver.find_element_by_xpath('//div[text()="录入管理"]').click()
                driver.implicitly_wait(10)
                time.sleep(1)
                driver.find_element_by_xpath('//span[text()="商品品牌列表"]').click()
                time.sleep(1)
                driver.switch_to_frame("bda76498-586a-4c9a-b307-8808600e8a1c")
                time.sleep(1)
                driver.find_element_by_id('btnAdd').click()
                time.sleep(1)
                driver.switch_to_frame('framedialog')
                driver.find_element_by_xpath('//td[text()="品牌的Logo:"]/following-sibling::td//input').send_keys('E:\ERP\\Release01\Keyword-for-selenium-erp\2.png')

                time.sleep(1)
                driver.switch_to_default_content()
                driver.switch_to_frame('bda76498-586a-4c9a-b307-8808600e8a1c')

                time.sleep(1)
                a = driver.find_element_by_xpath('//div[text()="111"]').text
                print a


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    testunit=unittest.TestSuite()
    testunit.addTest(Login("test_1"))


    a = open('./result.html', 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=a,
        title=u'页面登录测试报告',
        description=u'用例执行情况：')

    runner.run(testunit)

    try:
        url = 'file:///' + os.path.abspath('./result.html')
        driver = webdriver.Firefox()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        driver.get(url)
        driver.refresh()

    except:
        print '没有生成测试报告'

