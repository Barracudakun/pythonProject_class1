# -*- coding = utf-8 -*-
# @Time: 6/19/21 4:41 PM
# @Author: YAO
# @File: 1. While loop.py
# @Software: PyCharm
'''
初始条件设置 - 通常是重复执行的 计数器
i = 1 计数器

while 基本语法
        i <= 5
while 条件(判断 计时器是否达到 目标次数):
     条件满足时， 做的事情1
     条件满足时， 做的事情2
     条件满足时， 做的事情3
     ...
    处理条件(计数器 + 1) i = i + 1
'''
'''
#打印5遍 hello world
#1 定义一个整数变量，记录所有循环次数
i = 0 
#2 开始循环
while i <= 5:
    #1.希望在循环内执行代码
    print("hello world")
    # 2. 处理器
    i += 1
'''

'''
# 计算 0 ~ 100 之间的所有数的求和
# 定义最终结果变量
result = 0
#定义一个整数的变量记录循环的次数
i = 0
while i <= 100:
    print(i)
# 每一次循环，都让result 这个变量和i 这个计数器相加
    result += i
#处理器
    i += 1
print("0~100 total result = %d" % result)
'''

'''
计算0~100 之间所有偶数的累计求和结果
开始步骤
# 0. 最终结果
result = 0 
# 1. 计数器
i = 0 

while i <= 100:
    #偶数 i % 2 == 0
    #奇数 i % 2 != 0
    if i % 2 == 0:
    if i % 2 != 0: 
        print(i)
        result += i 
    
    i += 1 
print("result")
'''
'''
# 计算0~100之间所有偶数的累计求和结果

# 开始步骤
# 0. 最终结果
result = 0
# 1. 计数器
i = 0

while i <= 100:

    if i % 2 == 0:
        print(i)
        result += i

    i += 1
print("Total 0~100 even number = %d" %result)
'''
'''
循环可以和else 配合使用
while...else 
需求： 女朋友生气了，要惩罚： 连续说五遍 "媳妇，我错了" 如果道歉完毕， 女朋友就原谅我， 这个程序怎么写

语法：
while 条件：
    条件成立重复执行代码
else:
    循环结束之后要执行的代码
'''
# 需求： 女朋友生气了，要惩罚： 连续说五遍 "媳妇，我错了" 如果道歉完毕， 女朋友就原谅我
'''
1. 书写道歉循环
2. 循环正常结束要执行代码 ---- else
'''

i = 0
while i <= 5:
    print('媳妇， 我错了')
    i += 1
else:
    print('媳妇原谅我，真开心，哈哈哈')
