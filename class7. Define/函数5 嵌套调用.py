'''
函数的嵌套调用
所谓的函数嵌套调用是指一个函数里面有调用了另外一个函数
'''

#两个函数testA 和 testB --- 在A里面嵌套调用B函数
def testB():
    print('B函数开始----')
    print('这是B函数')
    print('B函数的结束')

def testA():
    print('A函数的开始----')
    #调用嵌套B
    testB()
    print('A函数的结束----')

testA()