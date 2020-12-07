from django.contrib import admin
from .models import Apitest, Apistep, Apis


# Register your models here.

# @admin.register(Apistep)
class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult',
                    'apistatus','create_time','id','apitest']
    model=Apistep
    extra=1


@admin.register(Apitest)
class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname','apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]


@admin.register(Apis)
class ApisAdmin(admin.ModelAdmin):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apiresult',
                    'apistatus','create_time','id','Product']

# admin.site.register(Apis)