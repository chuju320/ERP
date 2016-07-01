#-*-coding:utf-8-*-

'''学习如何读写excel中的数据，使用到的模块有xrld、xlwt、xlutis'''
import xlrd,xlwt
from xlutils.copy import copy


def passOrNot(nrow,num):
    '''封装函数，在框架中调用，作用是将最终是否通过的结果写入excel中的case data表中'''
    #font = xlwt.easyxf('font:color-index red ,bold on')    #定义字体
    #headerStyle = font     #定义标头字体
    oldwb = xlrd.open_workbook('dataEngine\\erpdata.xls',formatting_info=True)  #保持原excel文档格式不变
    newwb = copy(oldwb)   #copy从打开的xlrd的book变量中，拷贝出一份成为新的xlwt的WorkBook变量
    newws = newwb.get_sheet(2)   #通过get_sheet去获得对应的sheet
    if num == 1:
        print 'PASS'
        newws.write(nrow,10,'PASS')    #写入新数据，注意此处中文必须解码
    else:
        print 'NOT PASS'
        newws.write(nrow,10,'NOT PASS')
    #写入完成后，需要保存
    newwb.save('dataEngine\\erpdata.xls')
