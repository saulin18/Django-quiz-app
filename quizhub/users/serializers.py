
from rest_framework import serializers
from .models import RegisterUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  


class RegisterUserSerializer(serializers.ModelSerializer):    
    class Meta:
      model = RegisterUser
      fields = ['username', 'email', 'password', 'password2']
      extra_kwargs = {
        'password': {'write_only': True},
        'Quiz': {'read_only': True},
      }
    
    def create(self, validated_data):
      password = validated_data.pop('password')
      password2 = validated_data.pop('password2')
      if password != password2:
        raise serializers.ValidationError({'password': 'Passwords must match'})
      user = RegisterUser(email=validated_data['email'], username=validated_data['username'])
      user.set_password(password)
      user.save()
      return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token    