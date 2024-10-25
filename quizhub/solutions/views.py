from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from quizhub.quizes.models import Quiz, Solution
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from quizhub.quizes.models import Quiz, Solution
from .serializers import SolutionSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_solutions(request, pk):

   quiz = Quiz.objects.get(pk=pk)
   solutions = Solution.objects.filter(quiz=quiz)
   serializer = SolutionSerializer(solutions, many=True)
   return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_solution(request, pk):
  try:
    quiz = Quiz.objects.get(pk=pk)
  except Quiz.DoesNotExist:
    return Response({"error": "Quiz no encontrado."}, status=status.HTTP_404_NOT_FOUND)

  try:
    if quiz.owner == request.user:
      raise ValueError("No puedes agregar una solución a tu propio quiz.")

    if Solution.objects.filter(quiz=quiz, user=request.user).exists():
      raise ValueError("No puedes publicar otra solución en este quiz.")

    content = request.data.get('content')
    if not content:
      raise ValueError("El contenido es obligatorio.")

    solution = Solution.objects.create(quiz=quiz, user=request.user, content=content)
    quiz.solutions.add(solution)
    quiz.save()
    return Response({"detail": "Solución creada exitosamente."}, status=status.HTTP_201_CREATED)

  except ValueError as e:
    return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
  except Exception as e:
    return Response({"error": "Ha ocurrido un error interno"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_solution(request, pk):
  try:
    solution = Solution.objects.get(pk=pk)
  except Solution.DoesNotExist:
    return Response({"error": "Solución no encontrada."}, status=status.HTTP_404_NOT_FOUND)

  quiz = solution.quiz

  try:
    if solution.user != request.user:
      raise ValueError("No puedes eliminar esta solución, no eres el creador de la misma.")

    solution.delete()
    quiz.solutions.remove(solution)
    quiz.save()

    if Solution.objects.filter(quiz=quiz, user=request.user).exists():
      raise ValueError("Solución eliminada. No puedes publicar otra solución en este quiz.")

    return Response({"detail": "Solución eliminada."}, status=status.HTTP_204_NO_CONTENT)

  except ValueError as e:
    return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)
  except Exception as e:
    return Response({"error": "Ha ocurrido un error interno"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   
