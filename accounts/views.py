import random
import string

from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import UserPermission

from . import forms


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	User = get_user_model()
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (UserPermission,)


# class CreateUserView(CreateAPIView):

#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = UserSerializer
import random
import string

from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import UserPermission

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
	permission_classes = (UserPermission,)
