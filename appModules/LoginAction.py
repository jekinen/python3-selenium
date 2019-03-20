# encoding = utf-8
from pageObjects import LoginPage
import time
class loginAction(object):
    def __init__(self):
        print("login..........")

    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage.loginPage(driver)
            # 将当前焦点切换到登录模块的frame中，以便能进行后续登录操作
            login.switchToFrame()
            # 输入登录用户名
            login.userNameObj().send_keys(username)
            # 输入密码
            login.passwordObj().send_keys(password)
            time.sleep(3)
            # 点击登录按钮
            login.loginButton().click()
            time.sleep(3)
            # 切换回主窗口
            login.switchToDefaultFrame()
        except Exception as e:
            raise e

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    time.sleep(3)
    loginAction.login(driver,"shzygdst","zihuijiayou")
    time.sleep(3)
    driver.quit()



