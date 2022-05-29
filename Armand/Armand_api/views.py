import time

from django.shortcuts import render
from Armand_api.models import *
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def v_help(request):
    return render(request,'help.html')

def v_login_purple(request):
    return render(request, 'login_purple.html')

def login(request, message=''):
    res ={}
    res['notices'] = list(DB_notify.objects.all().values('content'))[::-1][0:2]
    res['message'] = message
    print(res)
    return render(request, 'login.html', res)

# 登录功能
def login_action(request):
    # 让用户体验到平台的安全，是花了时间比对的，心理暗示。类似取款机的取钱声音，是录音，让用户觉得安全。
    time.sleep(1)
    # 获取用户名密码
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    print(username,":",password)
    # 去数据库进行比对
    user =  auth.authenticate(username=username, password=password)
    if user is None: # 用户名/密码错误
        return login(request, 'username or password error')
    else: # 验证成功
        # 登录
        auth.login(request, user)
        request.session['user'] = username
        # 跳转至首页
        return HttpResponseRedirect('/index/')

# 注册功能
def register_action(request):
    time.sleep(1)
    # 获取用户名密码
    username = request.GET['username']
    password = request.GET['password']
    print(username,":",password)
    #去数据库注册
    try: # 注册成功
        user = User.objects.create_user(username=username,password=password)
        user.save()
        # 登录
        auth.login(request, user)
        request.session['user'] = username
        # 跳转至首页
        return HttpResponseRedirect('/index/')
    except: # 注册失败，用户名已存在
        return login(request, 'username exists')
