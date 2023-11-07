from rest_framework import status
from rest_framework.views import APIView
from .serializer import ExpensesSerializer, TypeSerializer, ExpensesCreateSerializer
from rest_framework.response import Response
from core.containers import ProjectContainer
from .dto import ExpensesCreateDTO


class ExpensesApiView(APIView):

    def post(self, request):
        create_expenses = ExpensesCreateSerializer(data=request)
        if not create_expenses.is_valid():
            return Response(create_expenses.errors, status=status.HTTP_400_BAD_REQUEST)

        create_expenses_interactor = ProjectContainer.expenses_interactor()
        create_expenses_dto = ExpensesCreateDTO(**create_expenses.validated_data)
        create_expenses = create_expenses_interactor.create_expenses(create_expenses_dto)
        create_expenses_serializer = ExpensesSerializer(create_expenses)

        return Response(
            data=create_expenses_serializer.data,
            status=status.HTTP_201_CREATED,
        )


class TypeApiView(APIView):

    def post(self, request):
        pass




