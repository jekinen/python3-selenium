# encoding = utf-8
from selenium import webdriver
from appModules.LoginAction import loginAction
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.AddContactPersonAction import AddContactPerson
import time
import traceback
from util.Log import Log

# 创建解析Excel对象
print(dataFilePath)
excelObj = ParseExcel()
# 将Excel文件加载到内存
excelObj.loadWorkBook(dataFilePath)
log = Log()
def LaunchBrowser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 访问163邮箱地址
    driver.get("https://mail.163.com/")
    time.sleep(3)
    return driver
def test163MailAddCntacts():
    try:
        # 根据Excel文件中的sheet名获取此sheet对象
        userSheet = excelObj.getSheetByName("163账号")
        # 获取163账号sheet中是否执行列
        isExecuteUser = excelObj.getColumn(userSheet,account_isExecute)
        # 获取163账号sheet中的数据列表
        dataBookColumn = excelObj.getColumn(userSheet,account_dataBook)
        log.info('测试为163邮箱添加正式开始。。。。。')
        for idx,i in enumerate(isExecuteUser[1:]):
            # 遍历163表中的账号，为需要执行的账号添加联系人
            if i.value == "y":#表示要执行
                # 获取第i行的数据
                userRow = excelObj.getRow(userSheet,idx+2)
                # 获取第i行的用户名
                userName = userRow[account_username - 1].value
                # 获取i行的密码
                passWord = str(userRow[account_password -1].value)
                print(userName,passWord)
                # 创建浏览器实例
                driver = LaunchBrowser()
                # 登录163邮箱
                loginAction.login(driver,userName,passWord)
                time.sleep(3)
                # 获取为第i行中用户添加的联系人数据表sheet名
                dataBookName = dataBookColumn[idx +1].value
                log.info('执行'+dataBookName+'表中内容')
                # 获取相对应的数据表
                dataSheet = excelObj.getSheetByName(dataBookName)
                # 获取联系人数据表中是否执行列对象
                isExecuteData = excelObj.getColumn(dataSheet,contacts_isExecute)
                contactNum = 0 #记录添加成功联系人个数
                isExecuteNum = 0 #记录需要记录联系人个数
                for id,data in enumerate(isExecuteData[1:]):
                    # 循环遍历是否执行添加联系人
                    # 如果被设置为添加，则进行联系人添加操作
                    if data.value == "y":
                        # 如果第id行的联系人被设置为执行，则isExecuteNum自增1
                        isExecuteNum+=1
                        # 获取联系人表第id+2行对象
                        rowContent = excelObj.getRow(dataSheet,id +2)
                        # 获取联系人姓名
                        contactPersonName = rowContent[\
                            contacts_contactPersonName -1].value
                        # 获取联系人邮箱
                        contactEmail = rowContent[\
                            contacts_contactPersonEmail -1].value
                        # 是否标记为星标联系人
                        isStar = rowContent[contacts_isStar-1].value
                        # 获取手机号
                        contactPersonPhone = rowContent[contacts_contactPersonMobile-1].value
                        # 获取联系人备注信息
                        contactsPersonComment = rowContent[contacts_contactPersonComment - 1].value
                        # 添加联系人成功后，断言的关键字
                        assertKeyWord = rowContent[\
                            contacts_assertKeyWords -1].value
                        log.info('联系人姓名：'+contactPersonName+'联系人邮箱：'+contactEmail+\
                              '是否标记为星标联系人：'+isStar+"手机号："+str(contactPersonPhone)+'联系人备注信息：'+contactsPersonComment)
                        # 执行添加联系人操作
                        AddContactPerson.add(driver, \
                                             contactPersonName,\
                                             contactEmail,\
                                             isStar,\
                                             contactPersonPhone,\
                                             contactsPersonComment)
                        time.sleep(3)
                        # 在联系人工作表中写入添加联系人执行时间
                        excelObj.writeCellCurrentTime(dataSheet,rowNo= id+2,colsNo=contacts_runTime)
                        try:
                            # 断言给定的关键字是否出现在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            excelObj.writeCell(dataSheet,"faild",rowNo= id+2,\
                                               colsNo =contacts_textResult,style="red" )
                        else:
                            # 断言成功，写入添加联系人成功信息
                            excelObj.writeCell(dataSheet,"pass",rowNo= id+2,\
                                               colsNo=contacts_textResult,style="green")
                            contactNum+=1
                    print("contactNum = %s,isExecuteNum=%s"\
                        %(contactNum,isExecuteNum))
                if contactNum == isExecuteNum:
                        # 如果成功添加的联系人数与需要添加的联系人数相等，
                        # 说明给第i个用户添加联系人测试用例执行成功
                        # 在163账号工作表中写入成功信息，否则写入失败信息
                    excelObj.writeCell(userSheet,"pass",rowNo= idx+2,\
                                           colsNo=account_testResult,style="green")
                    print(u'为用户%s添加%d个联系人，测试通过！'\
                        %(userName,contactNum))
                else:
                    excelObj.writeCell(userSheet,"faild",rowNo= idx+2,\
                                        colsNo=account_testResult,style="read")
            else:
                print(u'用户%s被设置为忽略执行！'%excelObj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username))
                # driver.quit()
    except Exception as e:
        log.info(u'数据驱动框架主程序发生异常，异常信息为：')
        log.error(traceback.print_exc())


if __name__=="__main__":
   test163MailAddCntacts()