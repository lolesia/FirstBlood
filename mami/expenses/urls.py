from django.urls import path
from .views import ExpensesApiView, ExpensesDetailApiView, TypeApiView, TypeDetailApiView

urlpatterns = [
    path('', ExpensesApiView.as_view()),
    path('<int:id>/', ExpensesDetailApiView.as_view()),
    path('type/', TypeApiView.as_view()),
    path('type/<int:id>/', TypeDetailApiView.as_view())
]