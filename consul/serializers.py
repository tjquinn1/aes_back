from rest_framework import serializers
from consul.models import Counselor, Course, Contact
from django.contrib.auth import get_user_model
 # If used custom user model

class CounselorSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField(many=False)
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
			'counselor1',
			'counselor2',
			'counselor3',
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