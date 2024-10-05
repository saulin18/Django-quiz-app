
from .models import Quiz, Solution  
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        
        
class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = '__all__'