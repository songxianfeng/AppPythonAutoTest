#-*- coding: UTF-8 -*-
'''
Created on 2018-11-26

@author: growingio
'''
import logging,time
import os


global LoggerOpr
class LogOperations(object):
    '''
    日志操作类
    '''


    def __init__(self):
        '''
        设置日志格式
        '''
        self.LoggerOpr=logging.getLogger(__name__)
        self.LoggerOpr.setLevel(level=logging.INFO)
        #Jenkins目录
        handler=logging.FileHandler(os.getcwd()+"/src/logs/RddTestLog"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) +".log")
        #本地执行
       # handler=logging.FileHandler("../logs/RddTestLog"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) +".log")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.LoggerOpr.addHandler(handler)
        
    def setInfo(self,msg):
        '''
        记录info级别日志
        '''
        self.LoggerOpr.info(msg)

    def setError(self,msg):
        '''
        记录error级别日志
        '''
        self.LoggerOpr.error(msg)
        
    def setWarning(self,msg):
        '''
        记录warning级别日志
        '''
        self.LoggerOpr.warning(msg)