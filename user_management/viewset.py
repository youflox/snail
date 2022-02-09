from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

from django.contrib.auth.models import User

from .serializer import UserSignupSerializer


class UserLoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print(login(request, user))
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)



class UserSignupView(APIView):
    def post(self, request, format=None):
        serializer = UserSignupSerializer(data = request.data)

        if serializer.is_valid(serializer):
            serializer.create(validated_data= serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)




# {
# "username": "nt_admin",
# "first_name": "nanda",
# "last_name": "mnasdf",
# "email": "asdf@gam.com",
# "password": "admin"
# }