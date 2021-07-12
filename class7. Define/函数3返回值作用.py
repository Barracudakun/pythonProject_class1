#在函数中 ， 如果需要返回结果给用户，需要使用函数返回值

#定义一个函数，返回"烟"
def buy():
    return '烟'

goods = buy()  #返回值在函数调用的地方
print(goods)

'''
return 作用：
1 负责函数返回值
2 退出当前函数，导致return 下方的所有代码（函数体内部）不执行
'''


# 需求： 制作计算器：计算人意连个数字的加法结果，并返回结果
'''
1 定义函数： 2 个参数 和 return 返回值
2 调用函数，传入 2 个真是数据 ， 这里既有返回结果，打印这个结果
'''

def sum_num(a, b):
    return a + b

#用result 变量保存函数的返回值
result = sum_num(1,2)
print(result)