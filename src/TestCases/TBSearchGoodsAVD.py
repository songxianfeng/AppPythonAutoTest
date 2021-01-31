#-*- coding: UTF-8 -*-
'''
Created on 2019-3-18

@author: growingio
'''
import unittest
import os,time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)

global driver
class TBSearchGoodsAVD(unittest.TestCase):


    def setUp(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='8.1.0'
        #模拟器
        desired_caps['deviceName']='127.0.0.1:62001'
        desired_caps['automationName']='Appium'
        #输入中文
        desired_caps['unicodeKeyboard'] = True  #使用Unicode编码方式发送字符串
        desired_caps['resetKeyboard'] = True   #隐藏键盘
        desired_caps['app'] = PATH('../Apps/shoujitaobao.apk')#被测试的App在电脑上的位
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        print "Start to run testcase...."

    def tearDown(self):
        self.driver.quit()
        print "The testcase finished!!!"
    
    def CheckElemPresent(self,lmathod,loc):
        '''
        判断元素 否存在
        '''  
        try:   
            if lmathod=="Xpath":
                self.driver.find_element_by_xpath(loc)
                return True
        except NoSuchElementException:
            return False
            
    def AllowAllRequest(self):
        '''
        允许所有打开时的授权操作
        '''
        time.sleep(3)
        loc=("xpath","//*[@text='同意']")
        #单击“同意”按钮
        ce = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
        ce.click()
       
        #单击“同意”按钮,第二次
#         loc2=("xpath","//*[@text='同意']")
#         ces = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc2))
#         ces.click()
        
        time.sleep(15)
        
            
        
    def testSearchGoods(self):
        
        #允许授权
        self.AllowAllRequest()
        #time.sleep(15)
        #1,单击搜索按钮
        self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='搜索']").click()
        #2，输入搜索关键字
        elem=self.driver.find_element_by_id("com.taobao.taobao:id/searchEdit")
        
        elem.send_keys("python")
        #3，单击搜索按钮
        #self.driver.press_keycode(84)
        self.driver.press_keycode(66)
        time.sleep(5)
        #4，检测搜索结果
        itemtitle=self.driver.find_element_by_id("com.taobao.taobao:id/title").text
        print itemtitle
        
        
        
             
        if "python" in itemtitle.lower():
            self.assertEqual(1, 1)
            print u"测试搜索功能-----passed"
        else:
            print  u"测试搜索功能失败，搜索结果为："+itemtitle
            self.assertEqual(1, 0)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()