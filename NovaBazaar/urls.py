from django.urls import path
from . import views
from .views import success_view



urlpatterns = [
    path('', views.user, name='index'),
    
    path('success/', success_view, name='success'),
    path('login/', views.signup, name='userlogin'),
    path('login', views.Userlogin , name='login'),
]

