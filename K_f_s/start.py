#-*-coding:utf-8-*-
import ExecutionEngine
import xlrd
from public import BasePage

login_page = BasePage.Action()
#casedata = login_page.getTabledata("dataEngine\\erpdata.xls", "settings")

run = login_page.getcelldata("dataEngine\\erpdata.xls","settings", 1, 1)
print 'run:%s' %run
result = login_page.getcelldata("dataEngine\\erpdata.xls","settings", 2, 1)
print 'result:%s' %result
open = login_page.getcelldata("dataEngine\\erpdata.xls","settings", 3, 1)
print 'open:%s' %open
if __name__ == '__main__':
    ExecutionEngine.generateTestCases(run,result,open)



