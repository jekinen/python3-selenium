# encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCf = ParseConfigFile()
        self.addContactsOptions = self.parseCf.getItemsSection("163mail_addContactsPage")
        print(self.addContactsOptions)

    def createContactPersonButton(self):
        # 获取新建联系人按钮
        try:
            # 从定位表达式配置文件中读取定位新建联系人按钮的定位方式和表达式
            locateType,locatorExpression = self.addContactsOptions[\
                "addContactsPage.createContactctsBtn".lower()].split(">")
            # 获取新建联系人按钮并返还给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        # 获取新建联系人界面中的姓名输入框
        try:
            locateType,locatorExpression = self.addContactsOptions[\
                "addContactsPage.contactPersonName".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        # 获取新建联系人界面中的邮箱输入框
        try:
            locateType,locatorExpression = self.addContactsOptions[\
                "addContactsPage.contactPersonEmail".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        # 获取新建联系人界面中的星标选择框
        try:
            locateType, locatorExpression = self.addContactsOptions[ \
                "addContactsPage.starContacts".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def conttactPersonMobile(self):
        # 获取新建联系人界面中的手机输入框
        try:
            locateType, locatorExpression = self.addContactsOptions[\
                "addContactsPage.conttactPersonMobile".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        # 获取新建联系人界面中的联系人备注输入框
        try:
            locateType, locatorExpression = self.addContactsOptions[\
                "addContactsPage.contactPersonComment".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def savecontacePerson(self):
        # 获取新建联系人界面中的保存联系人按钮
        try:
            locateType, locatorExpression = self.addContactsOptions[ \
                "addContactsPage.savecontacePerson".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
