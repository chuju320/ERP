#-*-coding:utf-8-*-

from selenium import webdriver
import time

driver = webdriver.Ie()
driver.get('https://cbss.10010.com/essframe')
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id('STAFF_ID').clear()#清空用户名输入框
driver.find_element_by_id('STAFF_ID').send_keys('1234')#输入用户名
time.sleep(1)
driver.find_element_by_id('LOGIN_PASSWORD').send_keys('1234')#输入密码
m = driver.find_element_by_id('LOGIN_PROVINCE_CODE')
m.find_element_by_xpath('//option[@value="76"]').click()#选择省份
time.sleep(1)
driver.find_element_by_id('VERIFY_CODE').send_keys('1234')#输入验证码
time.sleep(1)
driver.find_element_by_xpath('//div[@class="submit clear"]/input').click()#点击登录
time.sleep(1)
driver.quit()