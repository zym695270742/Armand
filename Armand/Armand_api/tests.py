from django.test import TestCase

# Create your tests here.

# def update_proj_config(request):
#     body  = request.body
#     # 将从web服务器接收到的json格式的bytes类型转换成str
#     str_new_proj_config = str(body, encoding='utf-8')
#     print('str-----',str_new_proj_config)
#     print(type(str_new_proj_config))
#     dict_new_proj_config = json.loads(str_new_proj_config)
#     print('dict-----',dict_new_proj_config)
#     print(type(dict_new_proj_config))
#     print(dict_new_proj_config["id"])
#     json_new_proj_config = json.dumps(str_new_proj_config)
#     print('json-----',json_new_proj_config)
#     print(type(json_new_proj_config))


# str----- {"id":1,"proj_name":"cmd","des":"-","creator":0,"updator":0,"create_time":"2022-06-23 16:27:03","update_time":"2022-06-23 16:27:03","mock_type":"mock_data","private":false,"Group":"","Logon_var":"","Public_var":"","Permission":"[]","sign":"","hide_flag":false}
# <class 'str'>
# dict----- {'id': 1, 'proj_name': 'cmd', 'des': '-', 'creator': 0, 'updator': 0, 'create_time': '2022-06-23 16:27:03', 'update_time': '2022-06-23 16:27:03', 'mock_type': 'mock_data', 'private': False, 'Group': '', 'Logon_var': '', 'Public_var': '', 'Permission': '[]', 'sign': '', 'hide_flag': False}
# <class 'dict'>
# 1
# json----- "{\"id\":1,\"proj_name\":\"cmd\",\"des\":\"-\",\"creator\":0,\"updator\":0,\"create_time\":\"2022-06-23 16:27:03\",\"update_time\":\"2022-06-23 16:27:03\",\"mock_type\":\"mock_data\",\"private\":false,\"Group\":\"\",\"Logon_var\":\"\",\"Public_var\":\"\",\"Permission\":\"[]\",\"sign\":\"\",\"hide_flag\":false}"
# <class 'str'>