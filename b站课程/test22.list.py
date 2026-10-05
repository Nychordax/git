a = [1,2,3,4,2,3,1,1,]
a.append(0) # 添加元素到列表末尾
print(a)
a.insert(1,0) # 在指定位置插入元素
print(a)
a.remove(1) # 删除指定元素
print(a)
a.pop() # 删除列表末尾元素
print(a)
a = [1,2,3,4,2,3,1,-1,]
print(a[-1]) # 取列表最后一个元素
print(a[0:3]) # 取列表前3个元素
print(a[:3]) # 取列表前3个元素
print(a[2:5]) # 取列表第3到第5个元素
print(a[-3:]) # 取列表倒数第3个元素到最后一个元素

print(a.index(2))    # 查找指定元素在列表中的位置
print(a.count(1))    # 统计指定元素在列表中出现的次数
print(a.sort())    # 对列表进行排序
print(a.sort(reverse=True))    # 对列表进行倒序排序