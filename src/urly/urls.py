from django.urls import path
from . import views


app_name = 'urly'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten/', views.get_shortcode, name='shorten'),
    path('400/', views.error_400, name='error_400'),
    path('404/', views.error_404, name='error_404'),
    path('409/', views.error_409, name='error_409'),
    path('412/', views.error_412, name='error_412'),
    path('<str:shortcode_2>/', views.check_shortcode, name='check_shortcode'),
]