from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from consul.serializers import CounselorSerializer, CourseSerializer, ContactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
from .models import Counselor

# Create your views here.

class CounselorView(APIView):
	def post(self, request):
		data = request.data 
		counselor = CounselorSerializer(data=request.data)
		if counselor.is_valid():
			counselor.save(user=self.request.user,
							sunStart = datetime.strptime(data.get('sunStart'), '%H:%M').time(),
							sunEnd = datetime.strptime(data.get('sunEnd'), '%H:%M').time(),
							monStart = datetime.strptime(data.get('monStart'), '%H:%M').time(),
							monEnd = datetime.strptime(data.get('monEnd'), '%H:%M').time(),
							tueStart = datetime.strptime(data.get('tueStart'), '%H:%M').time(),
							tueEnd = datetime.strptime(data.get('tueEnd'), '%H:%M').time(),
							wedStart = datetime.strptime(data.get('wedStart'), '%H:%M').time(),
							wedEnd = datetime.strptime(data.get('wedEnd'), '%H:%M').time(),
							thurStart = datetime.strptime(data.get('thurStart'), '%H:%M').time(),
							thurEnd = datetime.strptime(data.get('thurEnd'), '%H:%M').time(),
							friStart = datetime.strptime(data.get('friStart'), '%H:%M').time(),
							friEnd = datetime.strptime(data.get('friEnd'), '%H:%M').time(),
							satStart = datetime.strptime(data.get('satStart'), '%H:%M').time(),
							satEnd = datetime.strptime(data.get('satEnd'), '%H:%M').time(),
			)
			return Response(status=status.HTTP_201_CREATED)
		return Response(counselor.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		counselor = Counselor.objects.all()
		serializer = CounselorSerializer(counselor, many=True)
		return Response(serializer.data)

class CourseView(APIView):
	def post(self, request):
		course = CourseSerializer(data=request.data)
		if course.is_valid():
			course.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		course = Course.objects.all()
		serializer = CourseSerializer(course, many=True)
		return Response(serializer.data)

class ContactView(APIView):
	def post(self, request):
		contact = ContactSerializer(data=request.data)
		if contact.is_valid():
			contact.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(contact.errors, status=status.HTTP_400_BAD_REQUEST)