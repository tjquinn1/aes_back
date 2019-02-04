from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from clients.serializers import MastSerializer, ProfileSerializer, ClassesClientSerializer, ClassesClient2Serializer, PsychSocSerializer  
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ClassesClient, Mast

# Create your views here.

class MastView(APIView):
	def post(self, request):
		mast = MastSerializer(data=request.data)
		print(request.user.id)
		if mast.is_valid():
			mast.save(client=self.request.user)
			return Response(status=status.HTTP_201_CREATED)
		return Response(mast.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def get(self, request):
		mast = Mast.objects.get(client_id=request.user.id)
		serializer = MastSerializer(mast)
		return Response(serializer.data)


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

class ClientClassesView(APIView):
	def post(self, request):
		data = request.data
		print(data)
		for key, course in enumerate(data['selected']):
			d = {'client':request.user.id, 'course': course[1], 'course_date': course[2]}
			client_classes = ClassesClientSerializer(data=d)
			print(client_classes)
			if client_classes.is_valid():
				client_classes.save()
		if client_classes.errors:
			return Response(client_classes.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status=status.HTTP_201_CREATED)

	def get(self, request):
		client_classes = ClassesClient.objects.filter(client_id=request.user)
		serializer = ClassesClient2Serializer(client_classes, many=True)
		return Response(serializer.data)


