"""aes_back URL Configuration

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
from django.urls import path, include, re_path
from django.conf.urls import url, include
from rest_framework import routers
from aes_back.router import common_router 
import accounts.urls
import clients.urls
import payments.urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



urlpatterns = [
	re_path(r'^', include(common_router.urls)),
	re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
	re_path(r'^clients/', include('clients.urls', namespace='clients')),
	re_path(r'^admin/', include('consul.urls', namespace='consul')),
	re_path(r'^payments/', include('payments.urls', namespace='payments')),
	re_path(r'^auth/obtain_token/', obtain_jwt_token),
	re_path(r'^auth/refresh_token/', refresh_jwt_token),
	re_path(r'^auth/api-token-verify', verify_jwt_token)
]
