from django.contrib import admin

# Register your models here.
from .models import Product
from apitest.models import Apis

class ApisAdmin(admin.TabularInline):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apiresult',
                    'apistatus','create_time','id','product']
    model = Apis
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdesc','producter','create_time']
    inlines = [ApisAdmin]