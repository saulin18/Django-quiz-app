from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from quizhub.users.models import RegisterUser
from .serializers import MyTokenObtainPairSerializer, RegisterUserSerializer

# Create your views here.

@api_view(['POST'])
def register(request):
    user = RegisterUser.objects.create_user(username=request.data['username'], password=request.data['password'])
    serializer = RegisterUserSerializer(user, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_users(generics.ListAPIView):
    serializer_class = RegisterUserSerializer
    queryset = RegisterUser.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshView.serializer_class