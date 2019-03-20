# encoding = utf-8
import os

# 获取当前文在所在目录父级的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取页面存放元素定位表达式的绝对路径
pageElementLocatorPath = parentDirPath+u'\\config\\PageElementLocator.ini'

# 获取数据文件存放的绝对路径
dataFilePath = parentDirPath + u'\\testDate\\163邮箱联系人.xlsx'

# Log文件存放路径
LogPath = parentDirPath+u'\\Log'
# 163账号工作表中，每列所对应的数字序号
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 联系人工作表中，每列对应的数字序号
contacts_contactPersonName = 2
contacts_contactPersonEmail = 3
contacts_isStar = 4
contacts_contactPersonMobile = 5
contacts_contactPersonComment = 6
contacts_assertKeyWords = 7
contacts_isExecute = 8
contacts_runTime = 9
contacts_textResult = 10


if __name__ == "__main__":
    print(parentDirPath)
    print(pageElementLocatorPath)
    print(dataFilePath)