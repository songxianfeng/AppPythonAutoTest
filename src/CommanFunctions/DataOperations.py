#-*- coding: UTF-8 -*-
'''
Created on 2018-11-26
@author: growingio
'''
import sys
import os
from xml.dom import minidom
global DOC,CONN

class DataOperations(object):   
    '''
    数据读取相关操作
    '''
    def __init__(self,filename):

        '''
        初始化xml文档
        '''

        global DOC,CONN
        #个人调试读取路径
        #DOC = minidom.parse("../TestData/"+filename)

        #jenkins读取数据路径

        DOC = minidom.parse(os.getcwd()+"/src/TestData/"+filename)   

    def readxml(self,tagnamefirst,tagNamesecond):
        '''
        从指定的文件中中读取指定节点的值
        @param tagnamefirst:起始节点的名称，如：project
        @param tagNamesecond: 起始节点下的二级节点
        @return: 返回二级节点的值
        '''          

        root = DOC.documentElement
        message=root.getElementsByTagName(tagnamefirst)[0]
        return message.getElementsByTagName(tagNamesecond)[0].childNodes[0].nodeValue
    
    
    
    