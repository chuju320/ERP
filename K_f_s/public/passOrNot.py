#-*-coding:utf-8-*-

'''ѧϰ��ζ�дexcel�е����ݣ�ʹ�õ���ģ����xrld��xlwt��xlutis'''
import xlrd,xlwt
from xlutils.copy import copy


def passOrNot(nrow,num):
    '''��װ�������ڿ���е��ã������ǽ������Ƿ�ͨ���Ľ��д��excel�е�case data����'''
    #font = xlwt.easyxf('font:color-index red ,bold on')    #��������
    #headerStyle = font     #�����ͷ����
    oldwb = xlrd.open_workbook('dataEngine\\erpdata.xls',formatting_info=True)  #����ԭexcel�ĵ���ʽ����
    newwb = copy(oldwb)   #copy�Ӵ򿪵�xlrd��book�����У�������һ�ݳ�Ϊ�µ�xlwt��WorkBook����
    newws = newwb.get_sheet(2)   #ͨ��get_sheetȥ��ö�Ӧ��sheet
    if num == 1:
        print 'PASS'
        newws.write(nrow,10,'PASS')    #д�������ݣ�ע��˴����ı������
    else:
        print 'NOT PASS'
        newws.write(nrow,10,'NOT PASS')
    #д����ɺ���Ҫ����
    newwb.save('dataEngine\\erpdata.xls')
