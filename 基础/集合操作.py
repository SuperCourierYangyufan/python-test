# 切片
from typing import Iterable

list = ['1', 'a', 2, 'b', 3, 'c']
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

# 迭代
map = {'a': 1, 'b': 2, "c": 3}
for key, value in map.items():
  print(key)
  print(value)
# 判断是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
# 下标循环
for index, key in enumerate(map):
  print(index)
  print(key)
# 来源循环后的每个值,可做操作 [if 正向条件] [else 反向条件] for 变量值 in 来源 [if 过滤条件]
# [] 代表可选
list = [x*x if x % 2 == 0 else -x for x in range(1, 20) if x % 10 != 0];
print(list)
