# -*- coding = utf-8 -*-
# @Time: 6/19/21 6:28 PM
# @Author: YAO
# @File: 2. For loop.py
# @Software: PyCharm

'''
for 循环
语法：
for 临时变量 in 序列：
    重复执行的代码 1
    重复执行的代码 2
    ... ...

str1 = "hello world"
for i in str1:
    print(i)
'''
# # break
# str1 = "hello world"
# for i in str1:
#     if i == 'o':
#         break
#     print(i)

# continue
# str1 = "hello world"
# for i in str1:
#     if i == 'o':
#         continue
#     print(i)

'''    
for...else

'''


for i in range(10):
    if i == 5:
        print('hello world')
        continue
else:
    print('hello world')