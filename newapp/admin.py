from django.contrib import admin
# Register your models here.
from .models import Visitor,Message
class VisitorAdmin(admin.ModelAdmin):
    list_display = [
        'name','gender','age','number','password'
    ]#显示字段
    list_filter = ['name']#过滤字段
    search_fields = ['name']
    list_per_page = 2#分页
    # actions_on_bottom = True #设置执行动作的位置 bottom 和 top 只能存在一个
    actions_on_top = True
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(Message)

