from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from core.containers import ProjectContainer

from .dto import ExpensesCreateDTO, TypeCreateDTO
from .serializer import ExpensesSerializer, TypeSerializer, ExpensesCreateSerializer, TypeCreateSerializer


class ExpensesDetailApiView(APIView):
    def __init__(self):
        super().__init__()
        self.expenses_interactor = ProjectContainer.expenses_interactor()

    def get(self, request, id):
        try:
            expenses = self.expenses_interactor.get_expenses_by_id(id)
        except NotFound:
            return Response({"detail": f"Expenses with {id} not found"}, status=status.HTTP_404_NOT_FOUND)
        expenses_serializer = ExpensesSerializer(expenses)
        return Response(
            data=expenses_serializer.data,
            status=status.HTTP_200_OK
        )


class ExpensesApiView(APIView):
    def __init__(self):
        super().__init__()
        self.expenses_interactor = ProjectContainer.expenses_interactor()

    def post(self, request):

        create_expenses = ExpensesCreateSerializer(data=request.data)
        if not create_expenses.is_valid():
            return Response(create_expenses.errors, status=status.HTTP_400_BAD_REQUEST)

        # create_expenses_interactor = ProjectContainer.expenses_interactor()
        create_expenses_dto = ExpensesCreateDTO(**create_expenses.validated_data)
        create_expenses = self.expenses_interactor.create_expenses(create_expenses_dto)
        expenses_serializer = ExpensesSerializer(create_expenses)

        return Response(
            data=expenses_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        try:
            expenses = self.expenses_interactor.get_expenses_by_groomer_id(request.user.id)
        except NotFound:
            return Response({"detail": f"This groomer {request.user.first_name} {request.user.last_name} not has no expenses yet"}, status=status.HTTP_404_NOT_FOUND)
        expenses_serializer = ExpensesSerializer(expenses)
        return Response(
            data=expenses_serializer.data,
            status=status.HTTP_200_OK
        )


class TypeDetailApiView(APIView):

    def __init__(self):
        super().__init__()
        self.type_interactor = ProjectContainer.expenses_interactor()

    def get(self, request, id):

        try:
            type = self.type_interactor.get_type_by_id(id)
        except NotFound:
            return Response({"detail": f"Type with id {id} not found"}, status=status.HTTP_404_NOT_FOUND)
        type_serializer = TypeSerializer(type)
        return Response(
            data=type_serializer.data,
            status=status.HTTP_200_OK
        )


class TypeApiView(APIView):

    def __init__(self):
        super().__init__()
        self.type_interactor = ProjectContainer.expenses_interactor()

    def post(self, request):

        create_type = TypeCreateSerializer(data=request.data)
        if not create_type.is_valid():
            return Response(create_type.errors, status=status.HTTP_400_BAD_REQUEST)

        create_type_interactor = ProjectContainer.expenses_interactor()
        create_type_dto = TypeCreateDTO(**create_type.validated_data)
        create_type = create_type_interactor.create_type(create_type_dto)
        type_serializer = TypeSerializer(create_type)

        return Response(
            data=type_serializer.data,
            status=status.HTTP_200_OK
        )






