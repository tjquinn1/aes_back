from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from aes_back.urls import common_router as router
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



router.register(r'users', views.UserViewSet) 

app_name = 'accounts'

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    #url(r'^register', views.CreateUserView.as_view(), name="reg"),
	url(r'^verify/', verify_jwt_token),
	url(r"userinfo/$", views.UserInfoViewSet.as_view(), name="Userinfo")
	]
