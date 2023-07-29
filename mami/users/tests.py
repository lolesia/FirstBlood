from django.test import TestCase
from rest_framework import serializers
from .serializer import UserSerializer


class UserSerializerTest(TestCase):
    data_positve = {
        'email': 'test@example.com',
        'name': 'John',
        'last_name': 'Doe',
        'phone': '+380634002895',
        'password1': 'password123',
        'password2': 'password123',
    }

    def test_serializer(self):

        serializer = UserSerializer(data=UserSerializerTest.data_positve)
        self.assertTrue(serializer.is_valid())

    def test_validate_phone(self):
        valid_phone = '0634002895'
        serializer = UserSerializer()
        try:
            validated_phone = serializer.validate_phone(valid_phone)
            self.assertEquals(validated_phone, valid_phone)
        except serializers.ValidationError:
            self.fail("Валідація номеру телефона не повинаа викликати виключення")


    def test_validate_password(self):
        valid_password = {'password1': 'password123',
                          'password2': 'password123'}
        serializer = UserSerializer()
        try:
            validated_data = serializer.validate(valid_password)
            self.assertEqual(validated_data, valid_password)
        except serializers.ValidationError:
            self.fail("Валідація паролю не повинаа викликати виключення")





