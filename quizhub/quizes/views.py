from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from quizhub.quizes.models import Quiz  
from .serializers import QuizSerializer 

# Create your views here.


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        return Quiz.objects.all()


class QuizDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer   


class QuizCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer   
    

class QuizUpdateView(generics.UpdateAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
   
    def put(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    