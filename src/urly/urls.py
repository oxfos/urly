from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten/', views.shorten, name='shorten'),
]