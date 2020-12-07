from django.contrib import admin
from bug.models import Bug


# Register your models here.

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname', 'bugdetail', 'bugstatus', 'buglevel',
                    'bugcreater', 'bugassign', 'created_time','id']
