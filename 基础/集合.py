#!/usr/bin/env python3
# -*- coding: utf-8 -*-
nameList = ['b','c','a']
print(nameList)

nameList.sort()
print(nameList)

print(len(nameList))
print(nameList[0])
print(nameList[-1])
print(nameList[-2])

nameList.append('d')
print(nameList)

nameList.insert(1,'h')
print(nameList)

nameList.pop(1)
print(nameList)

nameList[3] = [1,2,3]
print(nameList)
print(nameList[3][1])

constNameList = ('x','y','z')
# ()为元组不可修改
# constNameList[1] = 1
print(constNameList)
