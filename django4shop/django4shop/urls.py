"""
URL configuration for django4shop project.

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
from shopapp import views

urlpatterns = [ # 클라이언트의 요청을 뷰와 매핑 진행함. 
    path("admin/", admin.site.urls), 
    
    path("", views.mainFunc), # 요청명이 없을때
    path("page1", views.page1Func), # 요청명이 page1일때
    path("page2", views.page2Func), # 요청명이 page2일떄
    path("cart", views.cartFunc),
    path("buy", views.buyFunc),
    
]
