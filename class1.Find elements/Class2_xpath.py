'''
实战经验中，必须要写！！！！！
from selenium import webdriver
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')  #括号内为webdriver地址
driver.maximize_window()
driver.implicitly_wait(10)
'''

'''
为什么使用Xpath和css定位？
1 ID,name, class; 依赖于元素定位这三个对应的属性， 如果元素没有以上三个属性，定位方法不能使用
2 ling_text, partial_link_text 只适合超链接
3. tag_name:只能找到页面唯一元素，或者页面中多个想同元素的第一个元素
什么是Xpath 定位？
基于元素的路径定位
Xpath是XML Path 简称（xml 是一种标记语言，焦点：数据存储与传递（皮质文件） 后缀 .XML
Xpath定位策略 (xpath 与css 一定能定位到元素）
1. 路径定位
    1). 绝对路径 /html/body/.../...
        语法： 以'/' 开头，逐级开始缩写，不能调级。 如 /html/body/div/p[1]/input
    2）. 相对路径
        语法： 以 '//' 开头，后面根元素名称 比如 p,div,id. 不知道元素名称可以使用'*'代替 ， '*'表示查找所有元素。
            如：//input 'input'表示元素 如果不知道'input' 可以使用 '//*'

2. 路径结合属性
        语法：在Xpath中，所有的元素属性必须使用 '@' 符号修饰 如： //*[@id=id值']
3. 属性与逻辑结合(and)定位 (多个属性定位)
        语法： //*[@id='id 值' and @属性 = '属性值']
4. 层级与属性结合定位 ***重要 /input or /input[1], /input[2];   or /a or /a[1], /a[2]  任意标签名 [1],[2] 表示第几个标签名
        语法； //*[@id='父级id属性值']/input  （提示：想对路径只有开头使用'//' 之后子集元素都使用'/'）
5. 如果要基于text 来定位元素
        //*[text()='文本内容']   进行查找

提示：
    1. 一般建议使用指定标签名 如 'input','name','a','div' . 不实用 '*' 代替。 '*'查找所有标签名，效率较慢
    2. 无论绝对路径还是相对路径, '/' ，'//'后面必须为元素的名称或 '*'
    3. 在工作中，建议使用相对路径 '//' , 不建议使用 绝对路径 '/'
    4. 相对路径匹配任意集元素，不限制元素的位置 格式 '//input' or '//*'

XPath 定位方法
driver.find_element_by_xpath(xpath) or
dirver.find_element(By.xpath)

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
driver.get('http://www.amazon.com')
#id 定位
# driver.find_element_by_id('twotabsearchtextbox').send_keys('shoes')
# sleep(2)
# driver.find_element_by_id('nav-search-submit-button').click()
# sleep(2)
# driver.quit()
#xpath 定位 据对路径
# driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys('shoes')
# sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
# sleep(2)
# driver.quit()
#xpath 定位 相对路径
# driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]').send_keys('shoes')
# sleep(2)
# driver.find_element_by_xpath('//input[@id="nav-search-submit-button"]').click()
# sleep(2)
# driver.quit()
driver.find_element_by_xpath('//*[@id="nav-xshop"]/a[2]').click()
# sleep(2)
# driver.find_element_by_xpath('').click()
# sleep(2)
# driver.quit()