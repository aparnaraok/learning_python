"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls.defaults import *
#from django.urls import include, path
from myapp.views import *

urlpatterns = [
    #path('',say_hello),
    #path('hello/$',say_hello), #http://127.0.0.1:8000/hello/$
    path('hello/',say_hello), #http://127.0.0.1:8000/hello
    path('curdate/',current_time_stamp), #http://127.0.0.1:8000/curdate
    path('admin/', admin.site.urls),
]