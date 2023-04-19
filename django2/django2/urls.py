"""
URL configuration for django2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views ...단순작업
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf ...작업량이 많을때, 어플리케이션이 많을때
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import시 주의가 필요하다. 
# /   루트 (가장 최상의 디렉토리로 이동 / Web root)
# ./   현재 위치 (파일의 현재 디렉토리를 의미)
# ../  현재 위치의 상단 폴더 (상위 디렉토리로 이동)

from django.contrib import admin
from django.urls import path
from gpapp import views
from gpapp.views import CallView
from django.urls.conf import include 

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # 사용자 요청에 대한 컨트롤러 연결 방법 3가지가 있다.
    path('',views.MainFunc, name='MainFunc'),  # 1. Function views
    path('gpapp/callget',CallView.as_view()),  # 2. Class-based views
    path('myapp/', include('gpapp.urls')),     # 3. Including another URLconf , main urls외 별도의 urls 생성함 즉 권한을 위임한다.
    
]
