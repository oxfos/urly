from django.urls import path
from .views import api_shortcode_stats
from .. import views


app_name = 'urly'

urlpatterns = [
    path('<str:shortcode>', views.check_shortcode, name='check_shortcode'),
    path('<str:shortcode>/stats', api_shortcode_stats, name='api_stats'),
]