'''
fixture
    说明： 装置函数 (setUp, tearDown) 这两个函数可以一起使用， 也可以单独使用
        1 初始化函数： def setUp():
        2 结束函数：  def tearDown():
    级别：
        1. 函数级别: def setUp(): / def tearDown():     # 常用
            特性： 几个测试函数，执行几次，每个测试函数执行之前都会执行setUp, 执行之后都会执行tearDown
        2. 类级别: def setUpClass(): / def tearDownClass():     #常用
            特性： 测试 "类"(class)运行之前运行一次setUpClass "类" 运行之后执行一次tearDownClass
            注意： 类方法必须使用 @classmethod 修饰
        3. 模块级别：def setUpModule(): / def tearDownModule():     #不常用
            特殊：模块运行之前执行一次， setUpModule ， 运行之后执行一次 tearDownModule

    提示：
        无论使用函数级别还是类级别，之后常用的场景为：
         初始化： def setup(self): or def setUpClass(cls):
            1 获取浏览器实例化对象
            2 最大化浏览器
            3 隐式等待
         结束：  def tearDown(): or def tearDownClass():
            关闭浏览器驱动对象
'''
import unittest
#1. 函数级别: def setUp(): / def tearDown():
          #  特性： 几个测试函数，执行几次，每个测试函数执行之前都会执行setUp, 执行之后都会执行tearDown
        # 缺点：如果每次一测试用例执行一次， 都要打开和关闭一次浏览器， 会使进度变慢
class Test03(unittest.TestCase):
    def setUp(self):
        print('setup 被执行')


    def tearDown(self):
        print('tearDown 被执行')

    def test01(self):
        print('test01 被执行')

    def test02(self):
        print('test02 被执行')

#2. 类级别: def setUpClass(): / def tearDownClass():
         #   特性： 测试 "类"(class)运行之前运行一次setUpClass "类" 运行之后执行一次tearDownClass
            #  注意： 类方法必须使用 @classmethod 修饰

class Test04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass 被执行')
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass 被执行')

    def test01(self):
        print('test01 被执行')

    def test02(self):
        print('test02 被执行')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass 被执行')