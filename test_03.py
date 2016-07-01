#-*-coding:utf-8-*-
# from selenium import webdriver
import time,unittest
import test_01
import test_02
from test import test_support

class ExecutionEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filepath = 'K_f_s\\dataEngine\\erpdata.xls'

    def action(self,*txt):
        exeKeyword = test_02.actionKey()
        base = test_01.Action()
        Summary = txt[3]
        print '[' + Summary + ']'
        k = 4
        stepdata = base.readline(self.filepath,'Test Steps')
        for i in stepdata:
            if txt[1] == i[0]:
                if i[3] == 'openBrowser':
                    print i[2]
                    self.driver = exeKeyword.openBrowser()
                elif i[3] == 'InputText':
                    print i[2]
                    loc = base.locate(i[4])
                    exeKeyword.inputText(loc,txt[k])
                elif i[3] == 'submit':
                    print i[2]
                    loc = base.locate(i[4])
                    exeKeyword.Submit(loc)
                elif i[3] == 'closeBrowser':
                    print i[2]
                    time.sleep(3)
                    exeKeyword.closeBrowser()
                elif i[3] == 'navigate':
                    print i[2]
                    url = i[4]
                    exeKeyword.navigate(url)
                elif i[3] == 'click':
                    print i[2]
                    loc = base.locate(i[4])
                    print loc
                    exeKeyword.clickElemnet(loc)
                elif i[3] == 'swichframe':
                    print i[2]
                    frame = i[4]
                    exeKeyword.switch_frame(frame)
                elif i[3] == 'defaultframe':
                    print i[2]
                    exeKeyword.switch_frame_default()
                elif i[3] == 'assert':
                    print i[2]
                    expect_loc = base.locate(i[4])
                    exeKeyword.DBassert(expect_loc,i[5])
                elif i[3] == 'sleep':
                    print i[2]
                    a = int(i[4])
                    time.sleep(a)
                elif i[3] == 'login':
                    print i[2]
                    name = i[4]
                    psw = i[5]
                    img = i[6]
                    name_loc = exeKeyword.locate(i[7])
                    psw_loc = exeKeyword.locate(i[8])
                    img_loc = exeKeyword.locate(i[9])
                    button = exeKeyword.locate(i[10])
                    exeKeyword.login(name,psw,img,name_loc,psw_loc,img_loc,button)

    @staticmethod
    def getTestFunc(*txt):
        def test(self):
            self.action(*txt)
        return test

    @classmethod
    def tearDownClass(cls):
        print 'End'

def testCase():
    base = test_01.Action()
    data = base.readline('K_f_s\\dataEngine\\erpdata.xls','Test Cases')
    for i in data:
        TCid = i[1]
        if i[4] == 'Y':
            print '[RUN]' + i[2] + ':'
            print '*'*8
            table = base.readline('K_f_s\\dataEngine\\erpdata.xls','case data')
            for j in table:
                if j[2] == 'Y' and j[1] == TCid:
                    print j
                    setattr(ExecutionEngine,'test_%s_%s'%(j[0],i[1]),ExecutionEngine.getTestFunc(*j))

testCase()

if __name__ == 'main':
    unittest.main()

