from django.conf.urls import url, include
from . import views
from aes_back.urls import common_router as router




#router.register(r'masts', views.MastViewSet) 

app_name = 'clients'

urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login"),
	url(r"mast/$", views.MastView.as_view(), name="Mast"),
    url(r"psychsoc/$", views.PsychSocView.as_view(), name="PsychSoc"),
    url(r"client_classes/$", views.ClientClassesView.as_view(), name="ClientClasses"),
	url(r"program/$", views.ProgramView.as_view(), name="Program"),
	url(r"profile/$", views.ProfileView.as_view(), name="Profile")
]
