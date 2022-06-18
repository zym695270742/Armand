"""Armand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Armand_api.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help/', v_help),
    path('login_purple/', v_login_purple),

    path('', login),
    path('login_action/', login_action),
    path('register_action/', register_action),
    path('accounts/login/', login),
    path('logout/', logout),

    path('login_red/', v_login_red),
    path('sign_in_action/', sign_in_action),
    path('sign_up_action/', sign_up_action),

    path('forgot_pwd/', forgot_pwd),
    path('password_reset/', password_reset),
    # path('index/', TemplateView.as_view(template_name='index.html')), # 不经过后台views.py
    path('index/', index),  # 经过后台views.py index函数，渲染首页
    path('get_tj_datas/', get_tj_datas),
    path('get_real_time_datas/', get_real_time_datas),
    path('proj_list/', proj_list),  # 获取项目列表
    path('add_proj/', add_proj),  # 新增项目
]
