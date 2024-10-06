from django.db import models
from quizhub.quizes.models import Quiz
from quizhub.users.models import RegisterUser
# Create your models here.

class Solution(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='solution')
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, related_name='solutions')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('quiz', 'user')  

    def __str__(self):
        return f'Solution by {self.user.username} for {self.quiz.title}'       