from django.test import TestCase
from rest_framework import serializers
from .serializer import UserSerializer
from .views import UserViewSet
from rest_framework import permissions
from .permission import IsOwnerOrReadOnly

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


class UserViewSetTest(TestCase):

    def test_get_permission_create(self):
        view = UserViewSet()
        view.action = 'create'
        permissions_list = view.get_permissions()
        expected_permissions = [permissions.AllowAny]
        actual_permissions = [permission.__class__ for permission in permissions_list]
        self.assertEqual(actual_permissions, expected_permissions)

    def test_get_permission_update(self):
        view = UserViewSet()
        view.action = ('update', 'partial_update')
        permissions_list = view.get_permissions()
        expected_permissions = [IsOwnerOrReadOnly]
        actual_permissions = [permission.__class__ for permission in permissions_list]
        self.assertEqual(actual_permissions, expected_permissions)

    def test_get_permission_destroy(self):
        view = UserViewSet()
        view.action = 'destroy'
        permissions_list = view.get_permissions()
        expected_permissions = [permissions.IsAdminUser]
        actual_permissions = [permission.__class__ for permission in permissions_list]
        self.assertEqual(actual_permissions, expected_permissions)

    def test_get_permission_else(self):
        view = UserViewSet()
        view.action = 'some_other_action'
        permissions_list = view.get_permissions()
        expected_permissions = [permissions.IsAuthenticatedOrReadOnly]
        actual_permissions = [permission.__class__ for permission in permissions_list]
        self.assertEqual(actual_permissions, expected_permissions)
