#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

map = {'a': 1, 'B': 2}

map = json.dumps(map)
print(map)
map = json.loads(map)
print(map)

class TestSeria(object):
  def __init__(self, **kwargs):
    self.id = kwargs['id']
    self.name = kwargs['name']

  def say(self):
    print('id:%s,name:%s' % (self.id, self.name))


test = TestSeria(id=1, name='tom')
test.say()
# 序列化
test = json.dumps(test, default=lambda obj: obj.__dict__)
print(test)

# 反序列化
def changeTestSeria(obj):
  return TestSeria(id=obj['id'],name=obj['name'])
test = json.loads(test,object_hook=changeTestSeria)
test.say()
