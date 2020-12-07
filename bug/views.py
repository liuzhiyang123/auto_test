from django.shortcuts import render
from .models import Bug

# Create your views here.

def bug_manage(request):
    bug_list=Bug.objects.all()
    return render(request,'bug_manage.html',{'bugs':bug_list})