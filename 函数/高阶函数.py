#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def fun(x):
  return x * x


# 循环调用方法
result = map(fun, [1, 2, 3, 4, 5])
print(list(result))


def add(x, y):
  print(str(x) + ":" + str(y))
  return x + y


# reduce把结果继续和序列的下一个元素做累积计算
result = reduce(add, [1, 3, 5, 7, 9])
print(result)


# 过滤数据
def gtNumber(data):
  return data > 10


print(list(filter(gtNumber, [2, 5, 11, 45, 3])))


# 排序
def fun2(data):
  return data % 10


print(list(sorted([1, 2, 11, 456, 2, 3], key=fun2)))

# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))


"""
@函数名
def XXX(参数):
  paas
  
便会自动执行函数名(XXX),并将结果赋值给XXX  
XXX = 函数名(XXX)
"""
# 装饰器 ！！！！ AOP
def log(func):
  # 本质上 log() 返回wrapper() 而 XXX = 函数名(XXX) 所以 wrapper() = message()
  # 所有wrapper入参用*args, **kw 可接受所有参数 *args为数组参数,**kw为多个带变量名的参数[key:value]
  def wrapper(*args, **kw):
    print('call %s"' % func.__name__)
    return func(*args, **kw)

  return wrapper


@log
def message(data):
  print('message' + data)


message("测试日志")

# 带参数的装饰器,需要多包一层

def log(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print('%s %s():' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator

@log('execute')
def now():
  print('2015-3-25')

now()