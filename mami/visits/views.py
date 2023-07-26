from rest_framework import viewsets
from .serializer import VisitsSerializer
from .models import Visits
from rest_framework.permissions import IsAuthenticated


class VisitsViewSet(viewsets.ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
    permission_classes = [IsAuthenticated]
