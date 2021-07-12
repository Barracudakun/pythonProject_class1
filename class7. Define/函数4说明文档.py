'''
语法
1.定义函数的说明文档
def 函数名（）
    """说明文档的位置"""
    代码
    ......

2. 查看函数的说明文档
help(函数名)
'''

def sum_num(a, b):
    """求和函数"""
    return a + b

help(sum_num)
result = sum_num(10, 20)
print(result)

#函数的说明文档高级使用
def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return:  返回值
    """
    return a + b
help(sum_num1)