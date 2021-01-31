#-*- coding: UTF-8 -*-
'''
Created on 2019-3-19

@author: growingio
'''
import unittest,time
#添加对公用函数的引用
from CommanFunctions.BaseComFunctions import BaseComFunctions
from CommanFunctions.DataOperations import DataOperations
from CommanFunctions.LogOperations import LogOperations

global bcfun
class TianMaoShopTest(unittest.TestCase):


    def setUp(self):
        print "Run SetUp"
        self.bcfun=BaseComFunctions()
        self.bcfun.AllowAllRequest()



    def tearDown(self):
        self.bcfun.QuitApp()
        print "Quit App Test"  


    def testSearchGoods(self):
        '''
        测试淘宝的搜索功能
        '''
        dr=DataOperations("TianMaoShopTest.xml")
        logopr=LogOperations()
        time.sleep(3)
        #1,单击搜索按钮
        self.bcfun.ElemClick("Xpath", dr.readxml("vtmshop", "sxpath"))
        #2，输入搜索关键字
        self.bcfun.SendTextToElem("ID", dr.readxml("vtmshop", "sedit"), dr.readxml("vtmshop", "scont"))
        #3，单击搜索按钮
        self.bcfun.PressEnterBtn()
        time.sleep(5)
        #4，检测搜索结果
        itemtitle=self.bcfun.GetText("ID", dr.readxml("vtmshop", "sresult"))
        print itemtitle
        
        if dr.readxml("vtmshop", "scont") in itemtitle.lower():
            self.assertEqual(1, 1)
            print u"测试搜索功能-----passed"
        else:
            print  u"测试搜索功能失败，搜索结果为："+itemtitle
            logopr.setError("testSearchGoods run failed,the search result is:"+itemtitle)
            self.assertEqual(1, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()