# -*- coding = utf-8 -*-
# @Time: 6/16/21 10:01 PM
# @Author: YAO
# @File: 1 元素运算符.py
# @Software: PyCharm
'''
运算符
1.
算数运算符: +, -, *(乘)， / (除)， // (取整数), % (求余数), ** (某数的几次幂)
print(4 + 3, 4 / 3, 4 // 3, 4 % 3, 4 ** 3)

2.
比较运算符： == (等于 =), != (不等于), >, <, >=, <=

3.赋值运算符： = ， += ， -= ， *= ， %= ， **= ， //=
a = 10
b = 20
b += a
b = b + a
print(b)
b -= a
b = b - a
print(b)
b *= a
b = b * a
print(b)
b %= a
b = b % a
print(b)
b **= a
b = b ** a
print(b)
b //= a
b = b // a
print(b)

4
逻辑运算符： and, or, not
and 同时为True, 则返回False
or 其中一个为真，则返回False
not 非

5.
位运算符
&, |, ^, ~, <<, >>

6.
成员运算符: in, not
strl = "helloworld"
if "h" in strl:
    print("in")
else:
    print("not in")

7.
身份运算符： is, is not
# is 判断两个对象是否属于同一个对象，判断两个对象内存地址是否一致    id(a) = id(b)  id 是存放地址
# is not 判断两个对象是否不属于同一个对象
a1 = 10
b1 = 10
print(a1 is b1)
print(id(a1), id(b1))

'''