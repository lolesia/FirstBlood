from rest_framework import serializers
from .validators import password_validation


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, validators=[password_validation])
    profile_type = serializers.ChoiceField(choices=['owner', 'groomer'])
    first_name = serializers.CharField()

