from rest_framework import serializers
from clients.models import Mast, Profile, ClassesClient, PsychSoc
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

class PsychSocSerializer(serializers.ModelSerializer):
	class Meta:
		model = PsychSoc
		fields = (
			'ls1',
			'ls2',
			'ls3',
			'ls4',
			'ls5',
			'ls6',
			'ss1',
			'ss2',
			'ss3',
			'ss4',
			'ss5',
			'fs1',
			'fs2',
			'fs3',
			'fs4',
			'fs5',
			'hs1',
			'hs2',
			'hs3',
			'hs4',
			'hs5',
			'ms1',
			'ms2',
			'ms2Yes',
			'ms3',
			'ms3Yes',
			'ms4',
			'ms4',
			'ms5',
			'ms5Yes',
			'em1',
			'em2',
			'em3',
			'em4',
			'em5',
			'em6',
			'em7',
			'em7Yes',
			'fd1',
			'fd2',
			'fd3',
			'fd4',
			'fd5',
			'fd6',
			'fd7',
			'fd8',
			'fd9',
			'su1',
			'alcFirst',
			'alcLast',
			'alcFreq',
			'su2',
			'ampAmount',
			'su3',
			'barbFirst',
			'barbLast',
			'barbFreq',
    		'barbAmount',
    		'su4',
    		'cafFirst',
    		'cafLast',
    		'cafFreq',
    		'cafAmount',
    		'su5',
    		'cocFirst',
    		'cocLast',
    		'cocFreq',
    		'cocAmount',
    		'su6',
    		'crcFirst',
    		'crcLast',
    		'crcFreq',
    		'crcAmount',
    		'su7',
    		'lsdFirst',
    		'lsdLast',
    		'lsdFreq',
    		'lsdAmount',
    		'su8',
    		'inhFirst',
    		'inhLast',
    		'inhFreq',
    		'inhAmount',
    		'su9',
    		'thcFirst',
    		'thcLast',
    		'thcFreq',
    		'thcAmount',
    		'su10',
    		'nicFirst',
			'nicLast',
    		'nicFreq',
			'nicAmount',
			'su11',
			'pcpFirst',
			'pcpLast',
    		'pcpFreq',
			'pcpAmount',
			'su12',
			'preFirst',
			'preLast',
			'preFreq',
			'preAmount',
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
