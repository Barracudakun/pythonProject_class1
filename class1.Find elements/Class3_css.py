# -*- coding = utf-8 -*-
# @Time: 6/12/21 12:34 PM
# @Author: YAO
# @File: Class3_css.py
# @Software: PyCharm

'''
CSS 定位
说明：
    1. css 是一种标记语言，焦点: 数据的样式，控制元素的显示样式，就必须先找到元素，在css标记语言中找打元素使用css选择器
    2. css 定位就是通过css选择器工具进行定位
    3. css 定位 极力推荐 使用，查找元素效率比xpath 高语法比xpath 更简单
方法:
   1 driver.find_element_by_css_selector()
   2  To test CSS selector in a browser , use $$() command in your browser console
常用测试：
    1. id 选择器
        前提：元素里必须有id属性    #id
        语法： #id 如 #kw   (baidu search id)
    2. class 选择器              .class
        前提： 元素里必须有class 属性
        语法： .class 如 .telA
    3. 元素选择器
        语法： element 如 input
    4. 属性选择器  [attribute=value]
        语法： [属性名=属性值]
    5. 层级选择器
        语法：
            1. p>input
            2. p input (prefer)
        提示： > 与空格的区别，大于号必须为子元素，空格则不用


CSS is faster, it is recommended to use CSS over XPath, but
1. CSS does not support text, you can't locate by text() with CSS,
you will have to use XPath for this

2. CSS can't be linked to a child element , for example,  $x("//div[./a]") is impossible to do with CSS


'''





from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#amazon home page search for table