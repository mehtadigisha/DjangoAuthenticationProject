from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/',views.signupaccount,name='signupaccount'),
    path('logoutaccount/',views.logoutaccount,name='logoutaccount'),
    path('loginaccount/',views.loginaccount,name='loginaccount'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('forgot-password-success/', views.forgot_password_success, name='forgot_password_success'),
    path('reset-password/<str:token>/', views.reset_password, name='reset_password'),
]