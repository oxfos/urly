"""urly_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400


handler400 = 'urly.views.error_400'
handler404 = 'urly.views.error_404'
handler409 = 'urly.views.error_409'
handler412 = 'urly.views.error_412'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urly.urls', namespace = 'urly')),
]
