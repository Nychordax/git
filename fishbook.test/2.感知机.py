'''感知机：多个输入，一个输出，输出为0或1
主要的逻辑运算：与门、或门、非门、异或门、与非门……'''
2.3 感知机的实现
2.3.1 简单的实现
# 先定义一个接受x1，x2两个输入AND函数
def AND(x1,x2)
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp > theta:
        return 0
    else:
        return 1

print(AND(1,1))
print(AND(0,1))
print(AND(1,0))
print(AND(0,0))

2.3.2 导入权重和偏执
# 把刚才的theta换成-b，w1,w2称为权重，b称为偏执
import numpy as np
x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7
w*x # 输出：[0. 0.5]
np.sum(w*x) # 输出：0.5
np.sum(w*x) + b # 输出：-0.2

2.3.2 使用权重金额偏执的实现
# 使用权重和偏执，可以实现与门
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp > 0 :
        return 1
    elif tmp<=0:
        return 0

# 接着，我们可以实现与非么和或门：
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp > 0:
        return 1
    else:
        return 0
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp> 0:
        return 1
    else:
        return 0
    
'''感知机的局限性：感知机只能实现逻辑门，不能实现其他运算；只能实现线性运算，不能实现非线性运算
异或门：输入相同为0 不同为1
感知机无法实现异或门，因为异或门是线性不可分的
'''
#但是可以通过组合与门，与非门，或门来实现异或门：
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y
'''叠加了多层的感知自己也成为多层感知机'''

# 我自己有一个idea 我想把这个异或门画出来
 #1.生成网格
import matplotlib.pyplot as plt
x1 = np.arange(-0.5,1.5,0.01)
x2 = np.arange(-0.5,1.5,0.01)
X1,X2 = np.meshgrid(x1,x2)  # 生成网格
 #2.对每个点计算XOR输出
Z = np.zeros_like(X1) # 生成与x1相同大小的矩阵，全为0
for i in range(X1.shape[0]): # 遍历x1 #shape[0]表示行数 #shape[1]表示列数 #shape[2]表示第三维 #x1.shape[0]表示行数
    for j in range(X1.shape[1]):
        Z[i,j] = XOR(X1[i,j],X2[i,j])
 #3.画图
plt.figure(figsize = (6,6)) # 设置图片大小
plt.contourf(X1, X2, Z, levels=[-0.5, 0.5, 1.5], colors=['#cce5ff','#ffcccc'])
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('XOR gata (multi-layer perceptron)')

 #4.把四个关键点标出来
points = [(0,0),(0,1),(1,0),(1,1)]
for px,py in points:
    plt.scatter(px,py,c = 'black',s = 80,zorder = 3)
    plt.text(px + 0.03,py + 0.03,f'({px},{py})',fontsize = 10)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()
