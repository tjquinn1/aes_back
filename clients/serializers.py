from rest_framework import serializers
from clients.models import Mast, Profile
from django.contrib.auth import get_user_model
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