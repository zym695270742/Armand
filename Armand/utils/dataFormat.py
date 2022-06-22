import datetime

# from django.core.serializers import json
import json

class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            res = obj.strftime('%Y-%M-%D %H:%M:%S')
        elif isinstance(obj, datetime.date):
            res = obj.strftime('%Y-%M-%D')
        else:
            res = {'result_code':'999','result_message':'time data error,please check the value'}
        return json.JSONEncoder.default(self, res)