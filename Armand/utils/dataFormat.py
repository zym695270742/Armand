import datetime
from django.utils.timezone import get_default_timezone  # 获取settings中配置的timezone
import json


class TimeFormat():
    @classmethod
    def dateTimeFromUTCToDefault(self, awareTime):
        # 将models里定义的DateTimeField字段的值转换为项目指定时区时间
        default_zn_t = awareTime.astimezone(get_default_timezone())
        return default_zn_t


class CJsonEncoder(json.JSONEncoder):
    '''
        重写json.JsonEncoder将datetime序列化为json
    '''
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            obj = TimeFormat.dateTimeFromUTCToDefault(obj)
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            obj = TimeFormat.dateTimeFromUTCToDefault(obj)
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)