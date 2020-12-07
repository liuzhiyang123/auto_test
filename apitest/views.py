from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from apitest.models import Apitest, Apistep, Apis


def test(request):
    return HttpResponse('test view')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(request,username=username,password=password)
        print('user',user)
        if user and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            return redirect('/home/')
        return render(request,'login.html',{'error':'用户名或密码错误'})
    return render(request, 'login.html')


def home(request):
    return render(request,'home.html')


def logout(request):
    auth.logout(request)
    return render(request,'login.html')


@login_required
def apitest_manage(request):
    apitest_list=Apitest.objects.all()
    username=request.session.get('user','')
    return render(request,"apitest_manage.html",{'user':username,'apitests':apitest_list})


@login_required
def apistep_manage(request):
    username=request.session.get('user','')
    apistep_list=Apistep.objects.all()
    return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list})


@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, 'apis_manage.html', {'user': username, 'apis_list': apis_list})
