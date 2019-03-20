# encoding = utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import HomePage as Page
import traceback
import time
class AddContactPerson(object):
    def __init__(self):
        print("add contact person")

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            # 点击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人页实例对象
            apb = Page(driver)
            apb.createContactPersonButton().click()
            if contactName:
                #非必填项
                apb.contactPersonName().send_keys(contactName)
                #必填项
                apb.contactPersonEmail().send_keys(contactEmail)
            if isStar == u'是':
                #非必填项
                apb.starContacts().click()
            if contactPhone:
                # 非必填项
                apb.conttactPersonMobile().send_keys(contactPhone)
            if contactComment:
                apb.contactPersonComment().send_keys(contactComment)
            apb.savecontacePerson().click()
        except Exception as e:
            # 打印异常堆栈信息
            print(traceback.print_exc())
            raise e

if __name__ == "__main__":
    from selenium import webdriver
    from appModules.LoginAction import loginAction
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com")
    time.sleep(3)
    loginAction.login(driver,"用户名","密码")
    time.sleep(3)
    AddContactPerson.add(driver,u"张三","602208333@qq.com",u"是","","")
    time.sleep(10)
    driver.quit()






