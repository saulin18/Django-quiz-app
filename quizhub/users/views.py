from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from quizhub.users.models import RegisterUser
from .serializers import MyTokenObtainPairSerializer, RegisterUserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = RegisterUser.objects.all()
    
    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


class get_users(generics.ListAPIView):
    serializer_class = RegisterUserSerializer
    queryset = RegisterUser.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshView.serializer_class