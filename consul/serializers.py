from rest_framework import serializers
from consul.models import Counselor, Course
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer, UserInfoSerializer
 # If used custom user model

class CounselorSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	class Meta:
		model = Counselor
		fields = (
			'sunStart',
			'sunEnd',
			'monStart',
			'monEnd',
			'tueStart',
			'tueEnd',
			'wedStart',
			'wedEnd',
			'thurStart',
			'thurEnd',
			'friStart',
			'friEnd',
			'satStart',
			'satEnd',
			'user'
			)
		depth = 1
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = (
			'counselors',
			'startTime',
			'endTime',
			'sun',
			'mon',
			'tue',
			'wed',
			'thur',
			'fri',
			'sat'
			)
		
class CourseCounselorSerializer(serializers.ModelSerializer):
	counselors = CounselorSerializer(many=True)
	class Meta:
		model = Course
		fields = (
			'id',
			'counselors',
			'startTime',
			'endTime',
			'sun',
			'mon',
			'tue',
			'wed',
			'thur',
			'fri',
			'sat'
			)

class CounselorInfoSerializer(serializers.ModelSerializer):
	user = UserInfoSerializer()
	class Meta:
		model = Counselor
		fields = (
			'user',
			)


class Course2Serializer(serializers.ModelSerializer):
	counselors = CounselorInfoSerializer(many=True)
	class Meta:
		model = Course
		fields = (
			'counselors',
			'startTime',
			'endTime',
			'name',
			)