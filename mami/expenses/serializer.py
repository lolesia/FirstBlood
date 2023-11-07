from rest_framework import serializers


class ExpensesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    name = serializers.CharField()
    cost = serializers.IntegerField()
    date = serializers.DateField()
    comment = serializers.CharField()


class ExpensesCreateSerializer(serializers.Serializer):
    type = serializers.CharField()
    name = serializers.CharField()
    cost = serializers.IntegerField()
    date = serializers.DateField()
    comment = serializers.CharField()


class TypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
