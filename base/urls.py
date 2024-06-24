from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_alarms, name="home"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('hello/', views.say_hello, name="hello"),
  path('create/', views.create_alarm, name="create")
]