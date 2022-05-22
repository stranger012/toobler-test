"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page,name='index'), 
    path('index/',index_page,name='index1'),
    path('register_page/',register_page,name='register_page'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('add_message/',add_message,name='add_message'),
    path('view_messages/',view_messages,name='view_messages'),
    path('delete_msg/',delete_msg,name='delete_msg'),
    path('edit_msg/',edit_msg,name='edit_msg'),
    path('view_activities/',view_activities,name='view_activities'),
    path('activity/',activity,name='activity'),
     path('logout/',logout,name='logout'),
     path('edit_msg_page/',edit_msg_page,name='edit_msg_page')
    

]
