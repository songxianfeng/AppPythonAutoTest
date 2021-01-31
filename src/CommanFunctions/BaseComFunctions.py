#-*- coding: UTF-8 -*-
'''
Created on 2018-11-26

@author: SXF
'''
import os,time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)

global driver

class BaseComFunctions(object):
    '''
    App自动化测试基础类
    '''


    def __init__(self):
        '''
        设置App自动化测试
        '''
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='8.1.0'
        desired_caps['deviceName']='e316685a'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['automationName']='Appium'
        
        desired_caps['appPackage'] = 'com.taobao.taobao'
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'

        #输入中文
        desired_caps['unicodeKeyboard'] = True  #使用Unicode编码方式发送字符串
        desired_caps['resetKeyboard'] = True #隐藏键盘
        
        desired_caps['app'] = PATH('../Apps/shoujitaobao.apk')#被测试的App在电脑上的位
        
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        
    def QuitApp(self):
        '''
        退出app
        '''
        self.driver.quit()
        
    def AllowPhoneCall(self):
        '''
        允许天猫访问电话
        '''
        time.sleep(3)
        #单击允许按钮
        loc1=("xpath","//*[@text='允许']")
        #第一次
        ae = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc1))
        ae.click()
        
    def CheckElemPresent(self,lmathod,loc):
        '''
        判断元素 否存在
        @param lmathod: 元素定位方法
        @param loc:元素定位地址
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
#         time.sleep(3)
#         loc=("xpath","//*[@text='同意']")
#         #单击“同意”按钮
#         ce = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
#         ce.click()
        #单击允许按钮
        loc1=("xpath","//*[@text='允许']")
        #第一次
        ae = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc1))
        ae.click()
        
        loc2=("xpath","//*[@text='同意']")
        #单击“同意”按钮
        ces = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc2))
        ces.click()
        
        #单击允许按钮，位置
#         time.sleep(5)
#         loc3=("xpath","//*[@text='允许']")
#         #第一次
#         ael = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc3))
#         ael.click()
        #从登录页返回
        time.sleep(5)
        if  not self.CheckElemPresent("Xpath", "//android.widget.TextView[@content-desc='天猫']"):
            #如果进入了登录页面，则返回
            self.driver.back()
        
        
            time.sleep(5)
            loc4=("xpath","//*[@text='允许']")
            #允许app获取地址
            aell = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc4))
            aell.click()
        
    def ElemClick(self,locmethods,location):
        '''
        单击元素
        @param locmethods:定位方法 
        @param location:定位数据 
        '''
        if locmethods=="ID":
            felem=self.driver.find_element_by_id(location)
        if locmethods=="Xpath":
            felem=self.driver.find_element_by_xpath(location)
            
        felem.click()
        
    
    def GetText(self,locmethods,location):
        '''
        获取元素内容
        @param locmethods:定位方法 
        @param location:定位数据 
        '''
        if locmethods=="ID":
            felem=self.driver.find_element_by_id(location)
        if locmethods=="Xpath":
            felem=self.driver.find_element_by_xpath(location)
            
        return felem.text
    
    def SendTextToElem(self,locmethods,location,content):
        '''
        向输入框输入内容
        @param locmethods:定位方法 
        @param location:定位数据 
        @param content:要输入的内容
        '''
        if locmethods=="ID":
            felem=self.driver.find_element_by_id(location)
        if locmethods=="Xpath":
            felem=self.driver.find_element_by_xpath(location)
            
        felem.send_keys(content)
        
    def GetElemes(self,locmethods,location):
        '''
        获取相同定位方法的元素
        @param locmethods:定位方法 
        @param location:定位数据 
        '''
        if locmethods=="ID":
            elems=self.driver.find_elements_by_id(location)
        if locmethods=="Xpath":
            elems=self.driver.find_elements_by_xpath(location)
            
        return elems
    
    
    def GetEleme(self,locmethods,location):
        '''
        获取定位方法的元素
        @param locmethods:定位方法 
        @param location:定位数据 
        '''
        if locmethods=="ID":
            elems=self.driver.find_element_by_id(location)
        if locmethods=="Xpath":
            elems=self.driver.find_element_by_xpath(location)
            
        return elems
            
    def NavBack(self):
        '''
        返回按钮
        '''
        self.driver.back()
        
    def PressEnterBtn(self):
        '''
        输入回车按钮
        '''
        self.driver.press_keycode(66)