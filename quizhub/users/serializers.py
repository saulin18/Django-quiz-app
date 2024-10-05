
from rest_framework import serializers
from .models import RegisterUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  


class RegisterUserSerializer(serializers.ModelSerializer):    
    class Meta:
      model = RegisterUser
      fields = ['username', 'is_admin', 'is_active']
      REQUIRED_FIELDS = ['username', 'password']
      extra_kwargs = {
        'password': {'write_only': True},
        'Quiz': {'read_only': True},
      }
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token    