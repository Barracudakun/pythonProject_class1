'''
实战经验中，必须要写！！！！！
from selenium import webdriver
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')  #括号内为webdriver地址
driver.maximize_window()
driver.implicitly_wait(10)
'''
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
driver.get("http://www.amazon.com")
'''
id 定位
driver.find_element(By.ID,"kw").send_keys("尚马学院")
name 定位
driver.find_element(By.NAME,"wd").send_keys("尚马学院")   推荐 利于封装
driver.find_element_by_id("we").send_keys("尚马学院") 不推荐，不利于封装
Link_text 定位
driver.find_element(By.LINK_TEXT,"新闻").click()
Partial link_text 定位
driver.find_element(By.PARTIAL_LINK_TEXT,"新").click()
sleep(2)
Class_name 定位
driver.find_element(By.CLASS_NAME,"class name").click()  class_name 定位不推荐， 不利于定位
driver.find_elements_by_class_name("class name").click()
Tag name 定位
driver.find_element(By.TAG_NAME,"tag name").send_keys()  tag name 也不利于定位， 不推荐
driver.find_element_by_tag_name("tag name").send_keys()
Css selector 定位
driver.find_element(By.CSS_SELECTOR,"cssselector").click()  链接比较冗长
driver.find_element_by_css_selector("cssselector").send_keys() 链接比较冗长
Xpath 定位
driver.find_element_by_xpath("").click()  最常使用 如果ID与Name定位不到元素
driver.find_element(By.XPATH,"").send_keys()
css 定位
driver.find_element_by_css_selector().send_keys() 在实战项目里，强烈推荐使用 一般和 partial_link text 一起使用 查找元素 
'''
'''
Xpath：目前应用最多的一种行为，基于页面结构来进行的定位  $$$$非常重要  
copy 与手写 xpath 路径 区别， copy 不一定100% 准确，不一定能定位到元素。 手写一定可以定位到元素 
据对路径：从html 跟路径下一层一层往下数，找到对应的层级，从而找到元素
想对路径：基于匹配制度来查找元素，一句Xpath语法结构来走
例如： //*[@id="kw"]   百度input id值
// 表示从根路径下开始查找
* 表示任意元素
[] 表示筛选条件 （查找函数）
@ 表示给予是醒来筛选， 例如 @id="kw" 表示基于id属性值为kw 的条件来进行筛选
确认xpath 路径是否正确
    1. 在Chrome developer tool 页面使用command+f 查找，进行判断
    2. 在Chrome developer too 中输入$x() 进行校验
如果要基于text来定位元素
在[]中添加text()="文本内容" 进行查找。 例如： //a[text()="登录"]
'''
'''
CSS 定位
说明：
    1. css 是一种标记语言，焦点: 数据的样式，控制元素的显示样式，就必须先找到元素，在css标记语言中找打元素使用css选择器
    2. css 定位就是通过css选择器工具进行定位
    3. css 定位 极力推荐 使用，查找元素效率比xpath 高语法比xpath 更简单
'''
'''
xpath 与css 类似功能对比
定位方式            xpath                                                           css
元素定位            //input                                                       input
id                //input[@id='kw']                                              #kw
class             //*[@class='telA']                                             .telA   
属性              1. //*[text()="XXX"]                                           1. input[type^='p']  （p字母开头的元素)
                 2. //input[starts_with(@atrribute,'xxx')]                      2. input[type$='d']   (d字母结束的元素)
                 3. //input[contains(@attribute,'xxx')]                         3. input[type*="w"]   (包含w字母的元素)
'''
'''
定位一组元素
方法： driver.find_elements by xxx()
返回结果： 类型为列表，要对列表进行访问和操作必须指定下标或进行遍历[下标从0开始]
'''
'''
扩展8种元素定位的底层实现
方式： driver.find_element(By.XXX,'value')   注：XXX一定为大写
参数说明：
By.XXX: 为By类的类型 如： By.ID
value: 元素的定位值 如： 'userA'
By 类 ： 需要导包 位置 from selenium.webdriver.common.by import By
'''