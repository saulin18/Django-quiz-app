from .models import Solution
from rest_framework import serializers

class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = '__all__'