from rest_framework import serializers
from .models import Pet, Breed


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'

