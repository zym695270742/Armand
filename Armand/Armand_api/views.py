import json
import time

from django.shortcuts import render
from Armand_api.models import *
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def v_help(request):
    return render(request,'help.html')

# purple logon page
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


# red logon page
def v_login_red(request, message=''):
    res ={}
    res['notices'] = list(DB_notify.objects.all().values('content'))[::-1][0:2]
    res['message_sign_in'] = message
    print(res)
    return render(request, 'login_red.html', res)

# 登录
def sign_in_action(request):
    time.sleep(1)
    # 通过name属性获取请求数据
    username = request.POST.get('username_sign_in', None)  # 对应属性名称必须是name, 如 name='username_sign_in'
    password = request.POST.get('password_sign_in', None)
    print(username, password)
    # 去DB获取该用户信息，进行比对
    user = auth.authenticate(username=username, password=password)
    if user is None:
        return v_login_red(request, 'username or password error')
    else: # 用户信息验证成功
        # 登录
        auth.login(request, user)
        request.session['user'] = username
        # 跳转至首页
        return HttpResponseRedirect('/index/')

# 注册
def sign_up_action(request):
    time.sleep(1)
    # 通过name属性获取请求数据
    username = request.GET['username_sign_up']
    email = request.GET['email_sign_up']
    password = request.GET['password_sign_up']
    print(username, email, password)
    # 去DB注册新用户：
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # 登录
        user.v_login_red(request, user)
        request.session['user'] = username
        # 跳转至首页
        return HttpResponseRedirect('/index/')
    except: # 注册失败，用户名已存在
        return v_login_red(request, 'username exists')



# 忘记密码
def forgot_pwd(request, message=''):
    res ={}
    res['notices'] = list(DB_notify.objects.all().values('content'))[::-1][0:2]
    res['message_password_reset'] = message
    print(res)
    return render(request, 'pwd_reset.html', res)

def password_reset(request):
    username = request.POST.get('username', None)
    new_pwd = request.POST.get('new_password', None)
    new_pwd_cf = request.POST.get('new_password_confirm', None)

    # 如果用户不存在，则使跳转首页，创建用户
    isExisting = User.objects.filter(username=username).exists()
    if not isExisting:
        return forgot_pwd(request, 'user does not exists, please create new user' )

    if new_pwd != new_pwd_cf:
        return forgot_pwd(request, "password not same")

    # 去DB修改密码
    try:
        pwd = User.objects.filter(username=username).update(password=make_password(new_pwd))
        print(pwd)
        return v_login_red(request,  'password reset success, please sign in')
    except:
        return forgot_pwd(request,  "Internal error")

# 获取统计信息
def get_tj_datas(request):
    tj_datas = {}
    tj_datas['notices'] =list(DB_notify.objects.all().values('content'))[::-1]
    return HttpResponse(json.dumps(tj_datas), content_type='application/json')