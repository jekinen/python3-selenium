# encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElement(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,30).until(\
            lambda x:x.find_element(by = locateType,value= locateExpression))
        return element
    except Exception as e:
        raise e

# 获取多个相同页面元素对象，并已Lost返回
def getElements(driver,locateType,locateExpression):
    try:
        elements = WebDriverWait(driver,30).until(\
            lambda x:x.find_elements(by=locateType,value=locateExpression))
        return elements
    except Exception as e:
        raise e

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    searchBox = getElement(driver,"id","kw")
    print(searchBox.tag_name)
    aList = getElements(driver,"tag name",'a')
    print(len(aList))
    driver.quit()