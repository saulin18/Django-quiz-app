from django.urls import path
from .views import delete_solution, get_solutions

urlpatterns = [
    path('get-solutions/<int:pk>', get_solutions),
    path('quizes/solutions/delete/<int:pk>', delete_solution),
]