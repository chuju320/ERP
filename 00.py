#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class b(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.maximize_window()
        time.sleep(1)
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        time.sleep(1)
        driver.find_element_by_id('kw').send_keys('shit')
        time.sleep(1)

        driver.find_element_by_link_text('登录').click()
        time.sleep(2)
        driver.find_element_by_id('TANGRAM__PSP_8__userName').clear()
        driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('123')
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('123')
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
