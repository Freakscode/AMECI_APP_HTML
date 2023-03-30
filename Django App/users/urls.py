from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/', views.user, name='users'),
    path('users/usuariosactivos', views.usuarios_activos, name='users'),
]