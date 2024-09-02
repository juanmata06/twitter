from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from user.api.serializers import UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data='ok')
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
