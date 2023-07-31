from rest_framework import serializers
from .models import User

from phonenumbers import parse, is_valid_number


class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'name', 'last_name', 'phone', 'password1', 'password2')

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError('Паролі не співпадають')
        return data

    def validate_phone(self, phone):
        parsed_number = parse(phone, "UA")
        if not is_valid_number(parsed_number):
            raise serializers.ValidationError("Invalid phone number")
        return phone

    def create(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        last_name = validated_data.get('last_name')
        phone = validated_data.get('phone')
        password1 = validated_data.get('password1')

        user = User.objects.create_user(email=email, name=name, last_name=last_name, phone=phone, password=password1)
        return user



