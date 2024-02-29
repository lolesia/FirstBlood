from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError
from phonenumbers import parse, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException


def password_validation(value):
    try:
        validate_password(value)
    except ValidationError as e:
        raise serializers.ValidationError(", ".join(e.messages))


def phone_numer_validation(value):
    try:
        parsed_number = parse(value)
        if not is_valid_number(parsed_number):
            raise ValidationError("Invalid phone number")
    except NumberParseException:
        raise ValidationError("Phone number recognition error")



