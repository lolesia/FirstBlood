from rest_framework import viewsets
from .serializer import PortfolioSerializer
from .models import Portfolio
from .permission import PortfolioPermission


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [PortfolioPermission]



