from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'last_name', 'phone')

