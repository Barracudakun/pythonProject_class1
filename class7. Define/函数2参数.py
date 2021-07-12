#1 函数：固定数据1 ，2 加法
def add_num1():
    result = 1+2  # 1， 2 是是时参
    print(result)

add_num1()

# 参数形式 掺入真实数据 1 +2 ,10 +20做加法运算
def add_num2(a,b): # a , b 是形参
    result = a + b
    print(result)
add_num2(1,2)

add_num2(10,20)

#add_num2 报错 ， 定义2个参数， 传入数据也要2个

