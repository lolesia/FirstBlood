from rest_framework import serializers
from .models import Expenses, Type


class ExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
