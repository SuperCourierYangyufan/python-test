#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScriptName: collections
Project: python-test
Author: yangyufan.
Create Date: 2023-04-04 09:51:02
Description:
"""
from collections import deque, defaultdict, namedtuple, OrderedDict

# 定义一个不可变的set,但是有类型
Point = namedtuple('Point', ['x', 'y'])
p = Point(3,4)

# 双向列表
linkList = deque(['a','b','c'])

map = defaultdict(lambda:None)
map['a'] = 1
print(map['a'])
print(map['b'])

# 顺序map
linkHashMap = OrderedDict([('b',2),('a',1)])
print(linkHashMap)
