from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .models import User
from .serializers import UserSerializer


class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignin(APIView):
    def post(self, request):
        user_email = request.data.get("user_email")
        user_password = request.data.get("user_password")

        try:
            user = User.objects.get(user_email=user_email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email"}, status=400)

        if not check_password(user_password, user.user_password):
            return Response({"error": "Invalid password"}, status=400)

        serializer = UserSerializer(user)
        return Response({"message": "Login successful", "data": serializer.data})


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)