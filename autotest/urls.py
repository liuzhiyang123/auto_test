"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apitest import views
from product import views as proviews
from bug import views as bugviews
from set import views as setviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',views.test),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('product_manage/',proviews.product_manager,name='product_manage'),
    path('apitest_manage/',views.apitest_manage,name='apitest_manage'),
    path('apistep_manage/',views.apistep_manage,name='apistep_manage'),
    path('apis_manage/',views.apis_manage,name='apis_manage'),
    path('bug_manage/',bugviews.bug_manage,name='bug_manage'),
    path('set_manage/',setviews.set_manage,name='set_manage'),
    path('user/',setviews.set_user,name='set_user')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)