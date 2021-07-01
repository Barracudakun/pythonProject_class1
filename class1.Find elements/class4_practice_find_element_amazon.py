# -*- coding = utf-8 -*-
# @Time: 6/12/21 1:59 PM
# @Author: YAO
# @File: class4_practice_find_element_amazon.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
driver.get('http://www.amazon.com')
driver.find_element_by_id('twotabsearchtextbox').send_keys('shoes')
sleep(2)
driver.find_element_by_id('nav-search-submit-button').click()
sleep(2)
driver.quit()