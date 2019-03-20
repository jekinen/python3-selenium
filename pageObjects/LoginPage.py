# encoding = utf-8
from util.ObjectMap import *
import time
from util.ParseConfigurationFile import ParseConfigFile
class loginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCf = ParseConfigFile()
        self.loginOptions = self.parseCf.getItemsSection("163mail_login")
        print(self.loginOptions)
    # 进入frame框
    def switchToFrame(self):
        try:
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(locatorExpression))
            # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]"))
        except Exception as e:
            raise e


    # 回到默认界面
    def switchToDefaultFrame(self):

        self.driver.switch_to.default_content()

    def userNameObj(self):
        try:
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.usrename".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            # elementObj = getElement(self.driver,"name","email")
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            # elementObj = getElement(self.driver,"name","password")
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExpression)
            # elementObj = getElement(self.driver,"id","dologin")
            return elementObj
        except Exception as e:
            raise e

if __name__ == "__main__":
    from selenium import webdriver
    driver  = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    login = loginPage(driver)
    time.sleep(5)
    login.switchToFrame()
    login.userNameObj().send_keys("shzygdst")
    login.passwordObj().send_keys("zihuijiayou1")
    login.loginButton().click
    time.sleep(5)
    login.switchToDefaultFrame()
    driver.quit()



