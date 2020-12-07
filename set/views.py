from django.shortcuts import render
from .models import Set
from django.contrib.auth.models import User
# Create your views here.


def set_manage(request):
    set_list=Set.objects.all()

    return render(request,'set_manage.html',{'sets':set_list})


def set_user(request):
    user_list=User.objects.all()

    return render(request,'set_user.html',{'users':user_list})