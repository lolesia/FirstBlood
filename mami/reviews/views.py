from .serializer import ReviewsSerializer
from rest_framework import viewsets
from .models import Reviews
from .permission import CustomPermission


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [CustomPermission]

