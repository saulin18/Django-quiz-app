from django.urls import path
from .views import delete_solution, get_solutions, create_solution

urlpatterns = [
    path('get-solutions/<int:pk>', get_solutions),
    path('quizes/solutions/delete/<int:pk>', delete_solution),
    path('quizes/solutions/<int:pk>', create_solution)
    
]