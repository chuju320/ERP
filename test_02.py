#-*-coding:utf-8-*-

from selenium import webdriver
import sys,time
import test_01

class actionKey(test_01.Action):

    def openBrowser(self):
        self.driver = webdriver.Firefox(timeout=10)

    def navigate(self,url):
        self.open(url)

    def closeBrowser(self):
        self.driver.quit()

    def inputText(self,loc,txt):
        self.send_keys(loc,txt)

    def Submit(self,loc):
        self.savePng(self.driver,'Submit')
        self.find_element(*loc).click()

    def clickElemnet(self,loc):
        self.find_element(*loc).click()

    def clickElements_i(self,loc,index):
        self.find_elements(*loc,index=index).click()

    def switch_frame(self,frame):
        self.switch_to_frame(frame)

    def switch_frame_default(self):
        self.driver.switch_to_default_content()

    def DBassert(self,loc,actual):
        exepect = self.find_element(*loc).text
        print '实际结果',actual
        print '期望结果',exepect
        if actual in exepect:
            print '匹配成功'
        else:
            print '匹配失败'

    def login(self,username,password,img,nameloc,passwordloc,imgloc,button):
        self.find_element(*nameloc).clear()
        self.find_element(*nameloc).send_keys(username)
        self.find_element(*passwordloc).send_keys(password)
        self.find_element(*imgloc).send_keys(img)
        self.find_element(*button).click()
