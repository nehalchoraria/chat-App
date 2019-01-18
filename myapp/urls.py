"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
#from django.conf.urls import include, url
from django.conf.urls import url
from login import views
from django.contrib.auth.views import login

urlpatterns = [
 path('admin/', admin.site.urls),
 url(r'^$', login),
 url(r'^logout/$', views.logout_page, name='logout_page'),
 url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
 url(r'^register/$', views.register, name='register' ),
 url(r'^register/success/$', views.register_success, name='register_success' ),
 url(r'^onlineUsers/$', views.onlineUsers, name='onlineUsers' ),
 url(r'^home/$', views.home, name='home' ),
]
