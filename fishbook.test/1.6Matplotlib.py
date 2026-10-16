'''在深度学习的实验中，图形的绘制和数据的可视化非常重要。Matplotlib是用于绘制图形的库
使用matplotlib可以轻松的绘制图形和实现数据的可视化。'''
1.6.1 绘制简单的图形
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0,6,0.1) # 创建一个从0到6的数组，步长为0.1
y = np.sin(x)

# 绘制图形
plt.plot(x,y) # 绘制x和y的曲线
plt.show() # 显示图形
1.6.2 pyplot 的功能
'''在刚才的sin函数的图形中，我们尝试追加cos函数的图形，并尝试使用pyplot的添加标题和x轴标签等其他功能。'''
import numpy as np
import matplotlib.pyplot as plt
# 生成数据
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 绘制图形
plt.plot(x,y1,label = "sin")
plt.plot(x,y2,linestyle = "--",label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend() # 显示图例
plt.show() # 显示图形
1.6.3 显示图像
'''pyplot中还提供了用于显示图像的方法imshow（）。另外，也可以是同matplotlib.image模块的imread（）方法读取图像。'''
import matplotlib.pyplot as plt
from matplotlib.image import imread # 导入imread方法
img = imread('lena.png') # 读取图像(选取合适的路径)
plt.imshow(img)
plt.show