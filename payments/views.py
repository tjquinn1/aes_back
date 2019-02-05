from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import stripe
# Create your views here.


class PaymentsView(APIView):
	def post(self, request):
		stripe.api_key = "sk_test_CDbMqNBvMp6tRymefsj6c2O0"
		charge = stripe.Charge.create(
			amount=999,
			currency='usd',
			description='Example charge',
			source=request.data['token']['id'],
		)
		print(charge)
		return Response(status=status.HTTP_201_CREATED)

	# def get(self, request):
	# 	course = Course.objects.all()
	# 	serializer = CourseCounselorSerializer(course, many=True)
	# 	return Response(serializer.data)