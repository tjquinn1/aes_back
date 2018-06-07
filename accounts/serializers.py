from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import get_user_model
 # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    def create(self, validated_data):

        user = UserModel.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            pos='clit'

        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'first_name', 'last_name', 'pos')