from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ejecutar/', views.ejecutar_codigo, name='ejecutar_codigo'),
]