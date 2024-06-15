from .views import index, register
from django.contrib.auth import views as auth_views
from django.urls import path 

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name= 'login'),
]
