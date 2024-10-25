
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from quizhub.quizes.models import Solution
from quizhub.quizes.models import Quiz
from .serializers import QuizSerializer
from quizhub.solutions.serializers import SolutionSerializer

# Create your views here.

@api_view(['GET'])
def quiz_list(request):
    quiz_list = Quiz.objects.all()
    serializer = QuizSerializer(quiz_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def quiz_create(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        quiz = serializer.save(owner=request.user, solutions=[])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def quiz_winner_update(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    if quiz.owner != request.user:
        return Response({'error': 'You are not the owner of this quiz'},status=status.HTTP_403_FORBIDDEN)

    solution_id = request.data.get('solution_id')
    if not solution_id:
        return Response({'error': 'Missing solution_id'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        solution = Solution.objects.get(pk=solution_id, quiz=quiz)
    except Solution.DoesNotExist:
        return Response({'error': 'Solution not found'}, status=status.HTTP_404_NOT_FOUND)

    if quiz.winner_solution:  
        quiz.winner_solution = solution
    else:  
        quiz.winner_solution = solution
    quiz.save()

    serializer = SolutionSerializer(solution)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    

   
    