#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Month import month,Weekday
class Base(object):
  def sayHello(self):
    print("hello!%s"%(Weekday.Sun))

class Super(Base):
  pass

super = Super()
super.sayHello()
# 返回所有属性和方法
print(dir(super))

