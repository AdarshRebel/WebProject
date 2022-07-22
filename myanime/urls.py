from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='blog-register'),
]
