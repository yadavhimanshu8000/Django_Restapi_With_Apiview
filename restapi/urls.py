"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    path('createuser/', views.userapi.as_view()),
    path('userdetail/<int:pk>/', views.userview.as_view()),
    path('createpost/', views.postapi.as_view()),
    path('postdetail/<int:pk>/', views.postview.as_view()),
    path('checkfollows/', views.followsapi.as_view()),
    path('followsdetail/<int:pk>/', views.followsview.as_view()),
    
    
    
   
]
urlpatterns = format_suffix_patterns(urlpatterns)
