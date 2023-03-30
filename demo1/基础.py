print('hello word')

print(123_456)

print(-1.3_5)

a = 1.3e-6
a = 'I\'m  \nhappy'
print(a)

b = True

print(not b)
print(b and not b)
print(b or not b)

a = 'ABC'
b = a
a = '你好'
print(len(a))
print(b)
a = a.replace('你','D')
# byte字节
c = a.encode('utf-8')
print(c)
# byte字节转回来
print(c.decode('utf-8',errors='ignore'))

print(9/3)
print(9//3)
print(10//3)
print(10%3)


print('今天 是%d月 一共%s 温度是%f度 来一个特殊字符 %%' % (5,'31天',18.6))