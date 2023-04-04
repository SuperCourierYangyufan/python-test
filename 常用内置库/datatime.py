#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

print(datetime.now())

dataInfo = datetime(2022, 3, 4, 21, 12, 42)
print(dataInfo)
# 时间转字符串
print(dataInfo.strftime('%Y-%m-%d %H:%M:%S'))

timestampInfo = dataInfo.timestamp()
print(timestampInfo)

print(datetime.utcfromtimestamp(timestampInfo))

# 字符串转时间
dataInfo = datetime.strptime('2023-04-04 09:33:21', '%Y-%m-%d %H:%M:%S')
print(dataInfo)

# 时间加减
dataInfo = dataInfo+timedelta(hours=1,days=-1,seconds=+3)
print(dataInfo)

#时区转换
dataInfo = dataInfo.utcnow().replace(tzinfo=timezone.utc)
print(dataInfo)