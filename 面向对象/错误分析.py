#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

class RuntimeException(ValueError):
  logging.info('进入自定义异常')


def tryError():
  try:
    a = 1/0
  except RuntimeException as e:
    logging.exception(e)
    raise RuntimeException("出错了")
  else:
    logging.info("没有错误,执行我")
  finally:
    logging.info("最终执行")

try:
  tryError()
except BaseException as e:
  logging.info("总的异常")
  logging.exception(e)
