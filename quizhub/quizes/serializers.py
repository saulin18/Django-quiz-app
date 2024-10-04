
from quizhub.quizes.models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        