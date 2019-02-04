from rest_framework import serializers
from consul.models import Counselor, Course, Contact
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
			'sat',
			'numPpl',
			'name'
			)

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = (
			'name',
			'email',
			'phone',
			'message',
			'title',
			'q1',
			'dui',
			'famCounseling',
			'domViolence',
			'empAssistance',
			'partnership',
			'teenHelp',
			'athCounseling',
			'submitted',
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
			'sat',
			'name'
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