from rest_framework import viewsets
from .serializer import ExpensesSerializer, TypeSerializer
from .models import Expenses, Type
from rest_framework.permissions import IsAdminUser


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAdminUser]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAdminUser]