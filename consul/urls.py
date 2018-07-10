from django.conf.urls import url, include
from . import views
from aes_back.urls import common_router as router




#router.register(r'masts', views.MastViewSet) 

app_name = 'consul'

urlpatterns = [
	#url(r"mast/$", views.MastView.as_view(), name="Mast")
	url(r"counselor/$", views.CounselorView.as_view(), name="Counselor"),
	url(r"course/$", views.CourseView.as_view(), name="Course")

]
