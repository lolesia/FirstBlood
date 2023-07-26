from rest_framework import serializers
from .models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reviews
        fields = '__all__'


