from quizhub.users.models import RegisterUser
from django.db import models
# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    owner = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, null=True, blank=True, related_name='quizzes')
    winner_solution = models.OneToOneField(
        'Solution',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='winning_quiz'
    )
    solutions = models.ManyToManyField(
        'Solution',
        blank=True,
        related_name='quizzes'  # Este es correcto
    )

    class Meta:
        app_label = 'quizes' 

    def __str__(self):
        return self.title


class Solution(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='solutions_list'  # Cambié esto para evitar conflictos
    )
    user = models.ForeignKey(
        RegisterUser,
        on_delete=models.CASCADE,
        related_name='user_solutions'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('quiz', 'user')  

    def __str__(self):
        return f'Solution by {self.user.username} for {self.quiz.title}'
