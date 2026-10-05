1.3.1 Arithmetic calculation 
1.3.2 Data type
    type(10) # int
    type(2.718) # float
    type('Hello') # str
    type([1,2,3]) # list
    type((1,2,3)) # tuple
    type({1,2,3}) # set
    type({'name':'Tom','age':18}) # dict
    type(True) # bool
    type(None) # NoneType
1.3.3 variable
1.3.4 list
    a = [1,2,3,4,5] # generate a list
    print(a) # print the content of the list
    len(a) #get the length pf the list
    a[0] #get the first element of the list
    a[4] = 99 #change the fifth element of the list
    print(a)
1.3.5 dictionary
    me = {'height':180,'weight':75,'age':18} # generate a dictionary
    me['height'] # get the value of the key 'height'
    me['weight'] = 80 # change the value of the key 'weight'
    print(me)
1.3.6 布尔型（Bool）
    hungry = True
    sleepy = False
    type (hungry) # bool
    not hungry # False
    hungrty and sleepy # False
    hungry or sleepy # True
1.3.7 if语句
    hungry = True
    if hungry:
        print("I'm hungry")
    hungry = False
    if hungry:
        print("I'm hungry")
    else:
        print("I'm not hungry")
        print("I'm sleepy")
1.3.8 for语句
    for i in[1,2,3]:
        print(i) #使用for循环遍历列表
    for i in range(5):
        print(i) #使用for循环遍历数字
1.3.9 函数
    def hello():
        print('Hello World!')
    hello() #调用函数
    #此外，函数还可以有参数和返回值
    def hello(object):
        print("Hello" + object + "!") #字符串的拼接可以用加号
    hello("World")


