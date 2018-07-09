from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from clients.serializers import MastSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from clients.models import Mast
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

# class MastViewSet(viewsets.ModelViewSet):
# 	queryset = Mast.objects.all()
# 	serializer_class = MastSerializer

class MastView(APIView):
	serializer_class = MastSerializer
	def post(self, request):
		print(request.user.first_name)
		return Response(status=status.HTTP_201_CREATED)
