# -*- coding = utf-8 -*-
# @Time: 6/14/21 9:21 PM
# @Author: YAO
# @File: sleep.py
# @Software: PyCharm
''''
实战经验中，必须要写！！！！！
from selenium import webdriver
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')  #括号内为webdriver地址
driver.maximize_window()
driver.implicitly_wait(10)
'''
from selenium.webdriver.support.wait import WebDriverWait

'''
元素等待
1.为什么设置元素等待
由于电脑配置或网络原因，在查找元素时， 元素代码为在第一时间被加载出来，而跑出来找到元素异常
2.什么事元素等待
元素都在第一次未找到时，元素等待设置的时长被激活，如果在设置的有效时长内找到元素，继续执行代码，如果超出设置的时长未找到元素，抛出元素异常
3.元素的等待分类
    1。隐式等待
    2。显示等待
3.1 隐式等待实现方式：
    方法： driver.implicitly_wait(timeout)
    (timeout 为最大等待时长，单位：秒)
    说明：隐式等待为全局设置，只需设置一次，就会作用于所有元素
    
3.2 显示等待：
    概念：指定元素时，如果能定位到元素这直接返回该元素，不触发等待：如果不能定位到该元素，则间隔一段时间再去定位元素：如果在达到最大时长时还没有找到
元素，则抛出超时异常 TimeoutException  
    实现放式:
        1 导报等待类 ---> from selenium webdriver.support.wait import WebDriverWait
        2 WebDriverWait(driver,timeout,poll_frequency=0.5)
            1). driver:浏览器对象
            2）. timeout: 超时的时长，单位：秒
            3）. poll_frequency: 检测间隔时长，默认为0。5秒
        3 调用方法 until（method）：直到。。。时
            1). method: 函数名称，该函数用来实现对元素的定位
            2). 一般使用匿名函数来实现： lamba x: x.find_element_by_id("kw")
        4 element = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id('kw'))

'''


