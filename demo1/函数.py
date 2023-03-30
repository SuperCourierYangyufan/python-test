print(abs(-3))

print(str(-1.3))

a = abs
print(a(-3))

def maxNumber(list,number):
  if not isinstance(number,(int,float)):
    raise TypeError('必须为数字类型')
  if list == None or len(list) < 5:
    raise TypeError('参数不能为空,且位数不小于5位')
  return max(list),number

list = [3,7,2,9,3,2]
print(maxNumber(list,20))

def todoFun(obj1):
  # paas用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
  pass
print(todoFun(1))