from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializer import UserRegistrationSerializer
from .dto import UserRegistrationDTO

from core.containers import ProjectContainer
from core.permissions import NotAuthenticated


class UserRegistrationAPIView(APIView):

    permission_classes = [NotAuthenticated]

    def post(self, request):
        create_user = UserRegistrationSerializer(data=request.data)
        if not create_user.is_valid():
            return Response(create_user.errors, status=status.HTTP_400_BAD_REQUEST)

        create_user_interactor = ProjectContainer.user_interactor()
        create_user_dto = UserRegistrationDTO(**create_user.validated_data)
        create_user = create_user_interactor.user_registration(create_user_dto)
        create_user_serializer = UserRegistrationSerializer(create_user)

        return Response(
            data=create_user_serializer.data,
            status=status.HTTP_201_CREATED,
        )





    
