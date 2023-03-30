from django.urls import path
from . import views

app_name = 'devicezk'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('biomconf/', views.biomconf, name='biomconf'),
    path('biomconf/result', views.connDev, name='result'),
    path('biomconf/device_connection_data/', views.device_connection_data, name = 'device_connection_data')
]