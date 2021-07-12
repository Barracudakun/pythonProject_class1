'''
目标：unittest 框架-- TestCast 使用 （大驼峰）
步骤：
    1 导包 import unittest
    2 新建类 （class） 并继承unittest.TestCase
    3 测试方法必须以test 字母开头
'''


import unittest

def add(x, y):
    return x+y

class Test01(unittest.TestCase):
    def test_add(self):
        result = add(1, 1)
        print(result)

    def test_add002(self):
        result = add(1, 2)
        print(result)

    def add003(self):  # 必须以test开头 否运行不了
        result = add(1, 3)
        print(result)

if __name__=='__main__':
    unittest.main()