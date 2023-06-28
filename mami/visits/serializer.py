from rest_framework import serializers
from .models import Visits


class VisitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visits
        fields = '__all__'