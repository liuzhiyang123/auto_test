from django.shortcuts import render
from .models import Product
# Create your views here.


def product_manager(request):
    user=request.session.get('user','')
    product_list=Product.objects.all()
    return render(request,'product_manage.html',{'user':user,'products':product_list})