from rest_framework import serializers
from clients.models import Mast, Profile, ClassesClient
from django.contrib.auth import get_user_model
from consul.models import Counselor
from consul.serializers import Course2Serializer
 # If used custom user model

class MastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mast
		fields = (
			'q1', 
			'q2', 
			'q3', 
			'q3', 
			'q4', 
			'q5', 
			'q6', 
			'q7', 
			'q8', 
			'q9', 
			'q10', 
			'q11', 
			'q12',
			'q13',
			'q14',
			'q15',
			'q16',
			'q17',
			'q18',
			'q19',
			'q20',
			'q21',
			'q21Yes',
			'q22',
			'q22Yes',
			'mastScore')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = (
			'client',
			'streetAddress',
			'streetAddress2',
			'city',
			'zipCode',
			'state',
			'primePhone',
			'workPhone',
			'dob',
			'idType',
			'ethnicity',
			'gender',
			'martial',
			'emp'
			'emergencyContact',
			'emergencyRelationship',
			'emergencyPhone',
			'emergencyEmail',
			'income',
			'idNumber',
			'collegeGrad',
			'hsGrad',
			'interpreter',
			'edLevel',
			'familySize',
			'occupation',
			'collegeGrad'
			)

class ClassesClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClassesClient
		fields = (
			'client',
			'course',
			'course_date'
		)

class ClassesClient2Serializer(serializers.ModelSerializer):
	course = Course2Serializer()
	class Meta:
		model = ClassesClient
		fields = (
			'course',
			'course_date'
		)
		depth = 1