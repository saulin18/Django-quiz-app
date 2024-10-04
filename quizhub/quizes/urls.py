from django.urls import path
from .views import QuizListView, QuizDetailView, QuizCreateView, QuizUpdateView 

\

urlpatterns = [
    path('', QuizListView.as_view()),
    path('<int:pk>/', QuizDetailView.as_view()),
    path('create/', QuizCreateView.as_view()),
    path('update/<int:pk>/', QuizUpdateView.as_view()),
]