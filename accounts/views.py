import random
import string

from accounts.serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import UserPermission
from rest_framework.decorators import action
from clients.models import Profile


from . import forms


class UserViewSet(viewsets.ModelViewSet):

	authentication_classes = []
	permission_classes = []
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	User = get_user_model()
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserInfoViewSet(APIView):
	def get(self, request):
		serializer = UserInfoSerializer(request.user)
		if request.user.pos == 'client':
			try:
				Profile.objects.get(client_id=request.user.id)
			except ObjectDoesNotExist:
				new_data={'profile':"none"}
				new_data.update(serializer.data)
				return Response(new_data)
		return Response(serializer.data)