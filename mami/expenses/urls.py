from django.urls import path
from .views import ExpensesApiView

urlpatterns = [
    path('', ExpensesApiView.as_view())
]