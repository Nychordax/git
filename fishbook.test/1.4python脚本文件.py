'''到目前为止，我们看到的都是基于Python解释器的例子,python解释器能够以对话模式执行程序,也可以从文件中读取程序并执行。Python解释器可以从标准输入读取程序,也可以从文件中读取程序。
我们可以使用命令行参数来指定要执行的文件名,也可以使用交互模式来输入程序'''
1.4.1 保存为文件
#将终端移动到运行文件所在位置
    cd D:\git.test\fishook.test
#运行文件
    python test鱼书.py
1.4.2 类
#前面了解到 int和str都是“内置”的数据类型，是python自带的类。我们也可以自己定义类，可以创建数据类型
class 类名：
    def __init__(self,参数1,参数2):#构造函数
        self.属性1 = 参数1
        self.属性2 = 参数2
    def 方法名1(self,参数1,参数2):#方法1
        #方法体
    def 方法名2(self,参数1,参数2):#方法2
        #方法体
下面是一个简单的类的例子：
class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized!")
    def hello(self):
        print("Hello "+self.name+"!")
    def goodbye(self):
        print("Goodbye"+self.name+"!")
m = Man("Nychordax")
m.hello()
m.goodbye()
#运行结果
#Initialized!
#Hello Nychordax!
#Goodbye Nychordax!
