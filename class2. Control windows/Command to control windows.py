# -*- coding = utf-8 -*-
# @Time: 6/13/21 3:00 PM
# @Author: YAO
# @File: Command to control windows.py
# @Software: PyCharm

'''
2.1 操作浏览器的常用方法
    1. driver.maximize_windows()                                   窗口最大化
    2. driver.set_window_size(width,height)                        设置浏览器大小
    3. driver.set_window_position(x,y)                             设置浏览器位置
    4. driver.back()                                               后退
    5. driver.forward()                                            前进
    6. driver.refresh()                                            刷新
    7. driver.close()                                              关闭当前窗口
    8. driver.quit()                                               关闭所有程序启动窗口
    9. driver.title                                                获取页面title
    10.driver.current_url                                          获取当前页面url
'''
'''
2.2 提示
    1.driver.title 和 diver.current url   没有() 应用场景: 一般为判断上步操作事后执行成功
    2. driver.maximize_window()          一般为前置代码，获取driver后，直接编写最大化浏览器
    3. driver.refresh()                  在后面cookie 章节会使用到
    4. driver.close() 与 driver.quit() 区别
        close() :关闭当前主窗口
        quit(): 关闭由driver对象启动的所有窗口
'''

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
url = 'http://www.amazon.com'
driver.get(url)
driver.maximize_window()
sleep(2)
driver.set_window_size(300,200)
sleep(2)
driver.set_window_position(400,200)
sleep(2)
driver.maximize_window()
driver.find_element_by_partial_link_text('Best Sellers').click()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.quit()