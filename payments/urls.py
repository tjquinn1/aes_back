from django.conf.urls import url, include
from . import views
from aes_back.urls import common_router as router




#router.register(r'masts', views.MastViewSet) 

app_name = 'payments'

urlpatterns = [
	#url(r"mast/$", views.MastView.as_view(), name="Mast")
	url(r"charge/$", views.PaymentsView.as_view(), name="Payments"),
]
