'''
1.UnitTest 断言 (assert) 自动化脚本不写断言assert，相当于没有执行测试一个效果
    1.1 什么是断言？
    概念： 让程序替代人为判断测试程序执行结果是否符合预期结果的过程

    1.2 为什么要学习断言
    自动化脚本在执行的时候一般都是无人值守状态，我们不知道执行结果是否符合预期结果，所以我们需要让程序替代人为检测程序执行的结果是否符合预期结果，
    这就是需要使用断言

    1.3 常用断言 在unittest 里面
    self.assertEqual(ex1, ex2) #判断 ex1 == ex2
    self.assertIn(exq, ex2) #判断ex2 是否包含ex1 注意：所谓的包含不能跳字符
    self.assertTrue(ex) #判断ex是否为True

    1.4断言联系
    目标： 'cancel orders' in page "https://www.amazon.com/gp/help/customer/display.html"
    方法：
        def setup(self):
            #get driver
            #打开url
            #最大化浏览器
            #隐式等待
        def teardown(self):
            #关闭浏览器驱动
        def textInPage():
            #testcase
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')
#Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
# driver.maximize_window()
# driver.implicitly_wait(10)

class CancelOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Desktop/chromedriver')

    def CancelOrder(self):
        driver = self.driver
        self.driver.get("https://www.amazon.com/gp/help/customer/display.html")
        self.driver.find_element(By.ID, 'helpsearch')
        self.send_keys("Cancel order")
        self.send_keys(Keys.RETURN)
        self.assertIn("Cancel Items or Orders", )
        # result =

        # assert "Cancel Items or Orders" in


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()