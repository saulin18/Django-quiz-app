from django.urls import path
from .views import get_solutions

urlpatterns = [
    path('/get-solutions/<int:pk>', get_solutions),
]