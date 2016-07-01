#-*-coding:utf-8-*-

from selenium import webdriver
import time,sys,os,xlrd
from selenium.webdriver.support.wait import WebDriverWait

class Action:
    driver = None
    def __init__(self,url=None):
        self.url = url

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        assert(self.driver.title,u'页面打开错误')


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print '%s元素没有找到'%loc

    def find_elements(self,*loc):
        if len(self.find_elements(*loc)):
            return self.driver.find_elements(*loc)
        else:
            print '%s元素没有找到'%loc

    def switch_to_frame(self,loc):
        self.driver.switch_to_frame(loc)

    def script(self,js):
        self.driver.execute_script(js)
    def send_keys(self,loc,key,first_click=True,first_clear=True):
        try:
            #if first_click:
                #self.driver.find_element(loc).click()
            if first_clear:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(key)

        except:
            print '%s元素没有找到'%loc

    @staticmethod
    def read(file,sheetno):
        data = xlrd.open_workbook(file)
        table = data.sheet_by_name(sheetno)
        return table
    @staticmethod
    def readline(file,sheetno):
        table = Action.read(file,sheetno)
        for i in range(1,table.nrows):
            yield table.row_values(i)

    @staticmethod
    def locate(index,file='K_f_s\\dataEngine\\erpdata.xls',sheetno='element'):
        table = Action.read(file,sheetno)
        for i in range(1,table.nrows):
            if index in table.row_values(i):
                return table.row_values(i)[1:3]

    def pngName(self,name):
        day = time.strftime('%Y%m%d',time.localtime(time.time()))
        now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        fp = '.\\result' + day + 'img'
        if os.path.exists(fp):
            filename = fp + '\\' + now + '_' + name + '.png'
            return  filename
        else:
            os.mkdir(fp)
            filename = fp + '\\' + now + '_' + name + '.png'
            return  filename

    def savePng(self,name):
        image = self.driver.save_screenshot(self.pngName(name))
        return image