#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import pickle

logging.basicConfig(level=logging.INFO)

file = open('test.txt', 'r')
print(file.read())
file.close()

try:
  file = open('test.txt', 'r')
  for line in file.readlines():
    print(line)
except BaseException as e:
  logging.info("测试")
  logging.exception(e)
finally:
  if file:
    file.close()

# 二进制文件
# 写文件
file = open('test.txt', 'wb')
map = {'name':'tom','age':18}
# 文本写入
# file.write("测试写入")
# 序列化写入
pickle.dump(map,file)
file.close()
# 序列化读取
file = open('test.txt', 'rb')
# print(file.read())
print(pickle.load(file))
file.close()



# 文件系统
print(os.name)
# 环境变量
print(os.environ)

# 创建目录
os.mkdir('./test')
# 删除目录
os.rmdir('./test')

# 创建文件
file = open('./test1.txt', 'w')
file.close()
# 重命名
os.rename('./test1.txt', './test2.txt')
# 删除文件
os.remove('./test2.txt')
