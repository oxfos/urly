from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten', views.make_shortcode, name='shorten'),
    path('<str:shortcode>', views.check_shortcode, name='check_shortcode'),
    path('<str:shortcode>/stats', views.get_stats, name='stats')
]