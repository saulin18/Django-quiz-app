from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from quizhub.users.models import RegisterUser
from .serializers import MyTokenObtainPairSerializer, RegisterUserSerializer
from .models import RegisterUser as CustomUser
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(['POST'])
def register(request):
  username = request.data.get('username')
  password = request.data.get('password')
  
  if not username or not password:
    return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

  user = CustomUser.objects.create_user(username=username, password=password)

  refresh = RefreshToken.for_user(user)
  token = {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

  return Response(token, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_user(request):
    username = request.query_params.get('username')
    user = RegisterUser.objects.get(username=username)
    serializer = RegisterUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class get_users(generics.ListAPIView):
    serializer_class = RegisterUserSerializer
    queryset = RegisterUser.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshView.serializer_class