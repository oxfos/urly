from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('<pk>/stats', views.ShortcodeDetailView.as_view(), name='api_stats'),
]