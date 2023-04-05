import json
from datetime import datetime

from django.core import serializers
from django.db import connection
from django.db.models import Max, Q, F
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_GET

from app01.models import UserInfo


def sayHello(request):
  return HttpResponse("你好,我的宝!")


# 根据app注册顺序,逐一去templates里面去找
def test01(request):
  map = {
    'title': '超级请求头',
    'names': ['tom', 'jacy'],
    'info': {'a': 1, 'b': 2, 'c': 3}
  }
  return render(request, 'test01.html', map)


def test02(request):
  # 获取请求方式
  print(request.method)
  # 获取GET请求参数 <QueryDict: {'age': ['18'], 'name': ['tom']}>
  print(request.GET.get('age'))
  map = {'code': 200, 'message': '返回json1112'}
  # 重定向
  # return redirect('https://www.baidu.com')
  # json_dumps_params={'ensure_ascii': False} 是让页面中文显示正确
  return JsonResponse(map, json_dumps_params={'ensure_ascii': False})


@require_GET
def test03(request):
  list = UserInfo.objects.all()
  list = serializers.serialize('python',list)
  return JsonResponse({'code': 200, 'message': 'ok','data':list})
