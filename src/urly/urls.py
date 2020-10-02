from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten', views.get_shortcode, name='shorten'),
    path('<str:shortcode_2>', views.check_shortcode, name='check_shortcode'),
    path('<str:shortcode>/stats', views.get_stats, name='stats')
]