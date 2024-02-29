from django.urls import path
from .views import UserRegistrationAPIView

urlpatterns = [
    path('', UserRegistrationAPIView.as_view())
]