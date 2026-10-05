def fun():
    a = 10
    print(a)
    return a+100
print(fun())
'''全局变量与局部变量
1.全局变量：在函数外定义的变量，作用范围在整个文件中
2.局部变量：在函数内定义的变量，作用范围在函数内
3.如果在函数内想要修改全局变量的值，需要使用global关键字'''

def fun1():
    global a
    a = 20
    print(a)
    return a
print(fun1())

b = 30
def fun2():
    global b
    b = 40
    return b
print('b past:',b)
fun2()
print('b now:',b)