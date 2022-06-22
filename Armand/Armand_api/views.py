import json
import time

from django.shortcuts import render
from Armand_api.models import *
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required  # 登录态验证装饰器
from django.shortcuts import get_object_or_404
# from django.core.serializers.json import DjangoJSONEncoder
from utils.dataFormat import CJsonEncoder

# Create your views here.
def v_help(request):
    return render(request,'help.html')

# purple logon page
def v_login_purple(request):
    return render(request, 'login_purple.html')

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



def login(request, message=''):
    res ={}
    res['notices'] = list(DB_notify.objects.all().values('content'))[::-1][0:2]
    res['message'] = message
    print(res)
    return render(request, 'login.html', res)

# 登录功能
def login_action(request):
    # 让用户体验到平台的安全，是花了时间比对的，心理暗示。类似取款机的取钱声音，是录音，让用户觉得安全。
    time.sleep(0.3)
    # 获取用户名密码
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    print(username,":",password)
    # 去数据库进行比对
    user = auth.authenticate(username=username, password=password)
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

# 退出功能
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")  # 重定向到登录页面

# 进入vue的首页
@login_required
def index(request):
    return render(request, 'index.html')



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
    # 获取用户ID
    userID = request.user.id  # 具体实现（获取请求头里的cookie携带的sessionID,反解析获取到用户的id、name等信息）
    tj_datas = {}
    tj_datas['notices'] =list(DB_notify.objects.all().values('content'))[::-1]
    tj_datas['news']=list(DB_news.objects.filter(to_user_id=userID).values())[::-1]
    for i in tj_datas['news']:
        from_user_name = get_object_or_404(User, pk=i['from_user_id']).username
        i['from_user_name']= from_user_name
        i['content'] = i['content'][:10] + '...' if len(i['content']) > 10 else i['content'] # 三元运算符
    print(tj_datas['news'])
    tj_datas['overview'] = {
        "project_count": 80,
        "api_count": 20,
        "case_count": 220,
        "env_count": 40,
        "user_count": 20
    }
    tj_datas['monitors'] = {
        "case_pass": 98,
        "api_pass": 99,
        "case_fail": 10,
    }
    tj_datas['contributions'] = {
        "project":10,
        "case": 1110,
        "api": 10,
        "monitor":90
    }
    return HttpResponse(json.dumps(tj_datas), content_type='application/json')

# 获取实时数据
def get_real_time_datas(request):
    real_time_datas={
        "ApiShop_count": 10,
        "UnReadNews_count": 110,
        "RunCase_count": 68,
        "Import_count": 34
    }
    return HttpResponse(json.dumps(real_time_datas),content_type='application/json')

# 获取项目列表
def proj_list(request):
    # 需兼容未输入关键字 和输入关键字查询两种情况
    keys = request.GET.get('keys', None)  # 注意这里与必定存在参数的 获取方法不同, 对比request.GET['proj_id']
    if keys:
        proj_list_data = list((DB_proj_list.objects.filter(proj_name__contains=keys)|DB_proj_list.objects.filter(des__contains=keys)).values())[::-1]
    else:
        proj_list_data = list(DB_proj_list.objects.all().values())[::-1]

    # 增加创建者姓名，通过创建者id获取创建者姓名
    for i in proj_list_data:
        try:
            creator_name = get_object_or_404(User, pk=i['creator']).username
        except:
            creator_name = '无名'
        i['creator_name'] = creator_name

        try:
            updator_name = get_object_or_404(User, pk=i['updator']).username
        except:
            updator_name = '无名'
        i['updator_name'] = updator_name

    # DjangoJSONEncoder将datetime序列化为json
    return HttpResponse(json.dumps(proj_list_data, cls=CJsonEncoder), content_type='application/json')

# 新增项目
def add_proj(request):
    # 防止用户由于cookie失效导致获取不到用户id
    creator_id = request.user.id if request.user.id else 0
    DB_proj_list.objects.create(creator=creator_id)
    return proj_list(request)

# 删除项目
def delete_proj(request):
    proj_id = request.GET['proj_id']
    DB_proj_list.objects.filter(id=proj_id).delete()
    return proj_list(request)

# 获取项目配置信息
def get_proj_config(request):
    proj_id = request.GET['proj_id']
    proj_config = DB_proj_list.objects.filter(id=proj_id).values()[0]
    print(proj_config)
    print(type(proj_config))
    return HttpResponse(json.dumps(str(proj_config,encoding='utf-8'), cls=CJsonEncoder), content_type='application/json') # 这里报错，需改

# 更新项目配置信息
def update_proj_config(request):
    new_proj_config = request.body
    print(new_proj_config)
    # new_proj_config = DB_proj_list.objects.filter(id=proj_id)
    return HttpResponse('', content_type='application/json')