
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

from quizhub.quizes.models import Quiz, Solution
from .serializers import SolutionSerializer

@api_view(['GET'])
def get_solutions(request, pk):

   quiz = Quiz.objects.get(pk=pk)
   solutions = Solution.objects.filter(quiz=quiz)
   serializer = SolutionSerializer(solutions, many=True)
   return Response(serializer.data)
   

