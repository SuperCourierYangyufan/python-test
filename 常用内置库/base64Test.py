#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScriptName: base64Test
Project: python-test
Author: yangyufan.
Create Date: 2023-04-04 10:08:52
Description:
"""
import base64

# 编码 需要对字符串前加b 表示字节
string = b'hello word'
string = base64.b64encode(string)
print(string)

string = base64.b64decode(string)
print(string)

string = base64.b64encode(string)
print(string)