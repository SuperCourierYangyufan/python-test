from 模块.utils import _say

print(abs(-3))

print(str(-1.3))

a = abs
print(a(-3))


# 默认参数 定义默认参数要牢记一点：默认参数必须指向不变对象！ 要不然每次调用都会容易改变
# 参数前带* 代表传入数组,调用时可以随便传几个参数
# 参数前带** 代表可变参数,传入时可传入0-n个变量 传入已 传入名:传入值
# def person(name, age, *, city, job): * 后面位规定名字的入参
# 参数顺序位 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def maxNumber(*list, number=11, **other):
  if not isinstance(number, (int, float)):
    # 抛出异常
    raise TypeError('必须为数字类型')
  if list == None or len(list) < 5:
    raise TypeError('参数不能为空,且位数不小于5位')
  # 可返回多个,本质上是个数组
  return max(list), number, other


list = [3, 7, 2, 9, 3, 2]
print(maxNumber(*list, 20, hello='word'))


def todoFun(obj1):
  # paas用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
  pass


print(todoFun(1))

# 引入模块
_say('HELLO WORLD')