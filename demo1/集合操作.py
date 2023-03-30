# 切片
list = ['1','a',2,'b',3,'c']
# 1位取到索引3 不好含索引3
print(list[1:3])
print(list[-3:-1])
# 前两个
print(list[:2])
# 前5个 每两个取一个
print(list[:5:2])
# 每个数,每3个取一个
print(list[::3])
# 复制数组
copy = list[:]
list.append('4')
print(copy)

