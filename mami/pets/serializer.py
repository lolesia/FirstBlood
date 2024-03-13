from rest_framework import serializers


class BreedDTOSerializer(serializers.Serializer):
    id = serializers.Serializer(read_only=True)
    breed = serializers.CharField()


class BreedCreateDTOSerializer(serializers.Serializer):
    breed = serializers.CharField()


class PetDTOSerializer(serializers.Serializer):
    owner = serializers.CharField(read_only=True)
    owner_id = serializers.IntegerField(read_only=True)
    pet_name = serializers.ImageField(required=False)
    breed = serializers.CharField(read_only=True, allow_blank=True, allow_null=True)
    weight = serializers.FloatField()
    description = serializers.CharField(allow_blank=True, allow_null=True)


class PetCreateDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.CharField(read_only=True)
    owner_id = serializers.IntegerField(read_only=True)
    pet_name = serializers.ImageField(required=False)
    breed = serializers.CharField(read_only=True, allow_blank=True, allow_null=True)
    weight = serializers.FloatField()
    description = serializers.CharField(allow_blank=True, allow_null=True)
