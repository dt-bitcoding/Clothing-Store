from django.urls import path
from . import views
from .views import success_view



urlpatterns = [
    
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/success/', success_view, name='success'),
    path('loginuser', views.Userlogin , name='login'),
    path('logout/', views.logout, name='logout'),
    path('reset_password/', views.pass_reset_form, name='reset_password'),
    path('password_reset_confirm/', views.pass_reset_confirm, name='pass_reset_confirm'),
    path('password_reset_done/', views.pass_reset_done, name='password_reset_done'),
    path('password_reset_complete/', views.pass_reset_complete, name='password_reset_complete'),
    path('product_detail/', views.product_detail, name='product_detail'),

]

