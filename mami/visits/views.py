from rest_framework import viewsets
from .serializer import VisitsSerializer
from .models import Visits


class VisitsViewSet(viewsets.ModelViewSet):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
