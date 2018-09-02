from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from clients.serializers import MastSerializer, ProfileSerializer, PsychSocSerializer 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.



class MastView(APIView):
	def post(self, request):
		mast = MastSerializer(data=request.data)
		print(request.user.id)
		if mast.is_valid():
			mast.save(client=self.request.user)
			return Response(status=status.HTTP_201_CREATED)
		return Response(mast.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
	def post(self, request):
		profile = MastSerializer(data=request.data)
		print(request.user.id)
		if profile.is_valid():
			profile.save(client=self.request.user)
			return Response(status=status.HTTP_201_CREATED)
		return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)

class PsychSocView(APIView):
	def post(self, request):
		psychSoc = PsychSocSerializer(data=request.data)
		print(request.user.id)
		if psychSoc.is_valid():
			psychSoc.save(client=self.request.user)
			return Response(status=status.HTTP_201_CREATED)
		return Response(psychSoc.errors, status=status.HTTP_400_BAD_REQUEST)
