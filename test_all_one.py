import os
import unittest
from abd_test import *
from sort_test import *
import HTMLTestRunner

#设置文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)


#构造测试套件
suit=unittest.TestSuite
suit.addTest(unittest.makeSuite(Abs_test))
suit.addTest(unittest.makeSuite(Sort_test))

if __name__=="__main__":
    #打开一个文件，将result写入
    html_report=report_path+r"/resuult.html"
    fp=open(html_report,"wb")