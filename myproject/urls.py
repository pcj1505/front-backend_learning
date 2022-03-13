"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
# http://127.0.0.1/
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/
urlpatterns = [
    path('admin/', admin.site.urls),  #라우팅과 관련된 정보가 들어있어야함 admin/ : 장고가 기본적으로 가지고 있는 관리자 화면으로 이동하기 위한 라우팅 설정 
    path('', include('myapp.urls'))
]
