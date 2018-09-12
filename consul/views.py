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
from rest_framework.decorators import action

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

class ScheduleClassView(APIView):
	@action(detail=False)
	def get(self, request):
		user_id = request.user.id
		counselor = Counselor.objects.get(user_id=2)
		#courses_counselor = CounselorCourse(counselor_id=counselor)
		course_counselor = counselor.course_set.all()
		print(course_counselor)
		print(dir(course_counselor))
		#schedule_course = ScheduleCourseSerializer(data=request.data)
		return Response("Innercept")

#	@action(detail=False)
#	def class_dates_get(self, request):
#		if counselor_courses.isNull == False:
#			sun_courses = Course.objects.filter(sun=True, mon=False, tues=False, wed=False, thur=False, fri=False, sat=False)
#			mon_courses = Course.objects.filter(sun=False, mon=True, tues=False, wed=False, thur=False, fri=False, sat=False)
#			tues_courses = Course.objects.filter(sun=False, mon=False, tues=True, wed=False, thur=False, fri=False, sat=False)
#			wed_courses = Course.objects.filter(sun=False, mon=False, tues=False, wed=True, thur=False, fri=False, sat=False)
#			thur_courses = Course.objects.filter(sun=False, mon=False, tues=False, wed=False, thur=True, fri=False, sat=False)
#			fri_courses = Course.objects.filter(sun=False, mon=False, tues=False, wed=False, thur=False, fri=True sat=False)
#			sat_courses = Course.objects.filter(sun=False, mon=False, tues=False, wed=False, thur=False, fri=False, sat=True)
#		else:
#			print("The selected counselor does not have any courses")
#		schedule_course = ScheduleCourseSerializer(data=request.data)
#		return Response(schedule_course.data)

	def post(self, request):
		schedule_class = ScheduleClassSerializer(data=request.data)
		print(request.user.id)
		if schedule_class.is_valid():
			schedule_class.save(client=self.request.user)
			return Response(status=status.HTTP_201_CREATED)
		return Response(schedule_class.errors, status=status.HTTP_400_BAD_REQUEST)