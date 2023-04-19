"""
URL configuration for django3session project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from sessionapp import views # 어플리케이션 이름 사용할 것 

urlpatterns = [ # 클라이언트 요청에 의해 urls.py를 만난다.
    path("admin/", admin.site.urls),
    
    path('',views.mainFunc), # 요청명이 없으면..
    path('setos',views.setOsFunc),  
    path('showos',views.showOsFunc),      
]