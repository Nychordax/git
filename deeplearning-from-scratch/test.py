# ============================================================
# 《深度学习入门》第3章 - 手写数字识别（推理与准确率计算）
# ============================================================

import sys, os
sys.path.append(os.pardir)  # 把上一级目录加入模块搜索路径（书里的写法）
import numpy as np           # NumPy，用于数组运算
import pickle                # pickle，用于读取训练好的权重文件
from dataset.mnist import load_mnist          # 加载 MNIST 数据的函数
from common.functions import sigmoid, softmax  # 从 common 文件夹导入激活函数


# ---------- 1. 获取测试数据 ----------
def get_data():
    # 调用 load_mnist 加载数据
    # normalize=True：把像素值归一化到 0.0-1.0 之间
    # flatten=True：把 28×28 的图片拉平成 784 个数字
    # one_hot_label=False：标签保持为数字（如 5），而不是 one-hot 向量
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    # 只返回测试集，因为我们要评估模型在没见过的数据上的表现
    return x_test, t_test


# ---------- 2. 加载训练好的权重 ----------
def init_network():
    # 打开 sample_weight.pkl 文件，'rb' 表示以二进制只读方式打开
    with open(r"D:\git.test\deeplearning-from-scratch\ch03\sample_weight.pkl", 'rb') as f:
        # pickle.load 把文件里的权重字典读出来
        # 这个字典里存着 W1、W2、W3（权重）和 b1、b2、b3（偏置）
        network = pickle.load(f)
    return network


# ---------- 3. 前向传播（推理） ----------
def predict(network, x):
    # 从字典里取出三层的权重和偏置
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 第一层：输入 × 权重 + 偏置，然后过 sigmoid 激活函数
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    # 第二层：第一层输出 × 权重 + 偏置，再过 sigmoid
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    # 第三层（输出层）：第二层输出 × 权重 + 偏置，过 softmax
    # softmax 把输出变成概率分布，所有类别概率加起来等于 1
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y  # 返回 10 个类别的概率


# ---------- 4. 主流程：批量推理并计算准确率 ----------
x, t = get_data()          # 获取测试图片和标签
network = init_network()   # 加载权重

accuracy_cnt = 0           # 计数器，记录预测正确的数量
for i in range(len(x)):    # 遍历每一张测试图片
    y = predict(network, x[i])   # 对第 i 张图做推理，得到 10 个概率
    p = np.argmax(y)             # 取出概率最高的那个类别的索引（即预测数字）
    if p == t[i]:                # 如果预测结果等于真实标签
        accuracy_cnt += 1        # 计数器加 1

# 准确率 = 预测正确数量 / 总图片数
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))