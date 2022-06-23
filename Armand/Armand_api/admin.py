from django.contrib import admin

# Register your models here.
from Armand_api.models import *
from Armand_api import models

admin.site.register(DB_notify)
admin.site.register(DB_news)

class ControllerDBProjLst(admin.ModelAdmin):
    list_display = ("proj_name","des","creator","updator","create_time","update_time", "mock_type", "private", "Group",
                    "Logon_var", "Public_var", "Permission", "sign", "hide_flag")

admin.site.register(models.DB_proj_list, ControllerDBProjLst)
