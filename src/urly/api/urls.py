from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('<shortcode>/stats', views.shortcode_stats, name='api_stats'),
]