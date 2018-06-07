from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from aes_back.urls import common_router as router
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



router.register(r'users', views.UserViewSet) 

app_name = 'accounts'

urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login"),
    url(r'^login/', obtain_jwt_token),
    url(r"^logout/$", views.logout_view, name="logout"),
    url(r'^register', views.CreateUserView.as_view(), name="reg"),
    #url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r'edit/$', views.Edit, name='edit'),
    url(r'^login/$', views.custom_login, name='login'),
     url(r'^verify/', verify_jwt_token),
]
