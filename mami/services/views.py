from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ServicesSerializer
from .models import Services
from .permission import ServicesPermission


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [ServicesPermission]

