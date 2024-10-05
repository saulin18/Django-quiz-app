from django.contrib import admin
from quizhub.quizes.models import Quiz
from .models import Solution

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Solution)
