# encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()

    def addressLink(self):
        try:
            # 从定位表达式配置文件中读取定位通讯录按钮的定位方式和表达式
            locateType,locatorExpression = self.parseCF.getOptionValue(\
                "163mail_homePage","homePage.addressbook").split(">")
            # 获取登录成功页面通讯录页面元素，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
