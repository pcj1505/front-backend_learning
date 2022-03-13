
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),  #아무것도 없는 경로로 들어왔다.
    path('create/',views.index), #create 경로로 들어왔다.
    path('read/1/',views.index)
]
