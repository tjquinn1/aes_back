from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from consul.serializers import CounselorSerializer, CourseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
from .models import Counselor, CounselorCourse, Course

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
		data = request.data
		course = CourseSerializer(data=request.data)
		print(request.data)
		if course.is_valid():
			course_saved = course.save(
				startTime = datetime.strptime(data.get('startTime'), '%H:%M').time(),
				endTime = datetime.strptime(data.get('endTime'), '%H:%M').time(),
				sun = data.get('sun'),
				mon = data.get('mon'),
				tue = data.get('tue'),
				wed = data.get('wed'),
				thur = data.get('thur'),
				fri = data.get('fri'),
				sat = data.get('sat'),
				numPpl = data.get('sumPpl'),
				name = data.get('name')
			)
			counselor = Counselor.objects.get(id=data.get('counselors'))
			CounselorCourse.objects.create(
				counselor = counselor,
				course = course_saved,
				priority = 1
			)
			return Response(status=status.HTTP_201_CREATED)
		return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		courses = Course.objects.all()
		days = {'sun':[], 'mon': [], 'tue': [], 'wed': [], 'thur': [], 'fri': [], 'sat':[]}
		for course in courses:
			if course.sun:
				course_serializer = CourseSerializer(course)
				days['sun'].append(course_serializer.data)
			if course.mon:
				course_serializer = CourseSerializer(course)
				days['mon'].append(course_serializer.data)
			if course.tue:
				course_serializer = CourseSerializer(course)
				days['tue'].append(course_serializer.data)
			if course.wed:
				course_serializer = CourseSerializer(course)
				days['wed'].append(course_serializer.data)
			if course.thur:
				course_serializer = CourseSerializer(course)
				days['thur'].append(course_serializer.data)
			if course.fri:
				course_serializer = CourseSerializer(course)
				days['fri'].append(course_serializer.data)
			if course.sat:
				course_serializer = CourseSerializer(course)
				days['sat'].append(course_serializer.data)
		print(days)
		#serializer = CourseSerializer(days, many=True)
		return Response(days)