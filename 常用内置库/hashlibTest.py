#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScriptName: hashlibTest
Project: python-test
Author: yangyufan.
Create Date: 2023-04-04 10:39:12
Description:
"""
import hashlib
import hmac

md5 = hashlib.md5()
md5.update('hellow word'.encode('utf-8'))
md5.update('yes'.encode('utf-8'))
print(md5.hexdigest())

# 需要二进制
message = b'hello word Hi!'
key = b'paas'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())