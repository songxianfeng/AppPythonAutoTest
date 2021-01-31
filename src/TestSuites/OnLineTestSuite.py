#-*- coding: UTF-8 -*-
'''
Created on 2018-11-26

@author: growingio
'''
import unittest
import sys
import HTMLTestRunner
import os,time

sys.path.append("..")

sys.path.append(os.getcwd()+"/src/")

#from src.TestCases.FirstTestNav import FirstTestNav

from TestCases.TianMaoShopTest import TianMaoShopTest

class OnlineTestSuite():
    '''
    线上回归测试用例集
    '''

    def testReg(self):
        #构造测试集             
        suite = unittest.TestSuite() 
        suite.addTest(TianMaoShopTest("testSearchGoods"))

        '''
        runner = unittest.TextTestRunner() 
        #不生成测试报告，直接运行测试用例
        result=runner.run(suite)
        #如果有测试用例执行失败，则返回1
        if (not result.wasSuccessful()):
                exit(1)
        '''
        
        #利用HTMLTestRunner生成测试报告
        
        #创建测试报告目录，使用网上的HTMLTestRunner
#         reportfile=os.getcwd()+"/src/reports/"+str(int(round(time.time() * 1000)))
#         os.mkdir(reportfile)
#         filename=reportfile+'/report.html'
#         fp=file(filename,'wb')
#         runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Pdd App AutoTest Report',description=u'App AutoTest onLine!')

        #使用优化后的HTMLTestRunner
        repath=os.getcwd()+'\src\\reports\\report'+str(int(time.time()))
        os.mkdir(repath)
        runner=HTMLTestRunner.HTMLTestRunner(repath,title=u'淘宝App自动化测试报告',description=u'淘宝App自动化回归测试报告，回归线上环境！')
        result=runner.run(suite) #自动进行测试
        if (not result.wasSuccessful()):
            exit(1)     

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    OnlineTestSuite().testReg()