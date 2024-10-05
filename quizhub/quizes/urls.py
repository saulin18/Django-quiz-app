from django.urls import path
from .views import quiz_list, quiz_create, quiz_winner_update, create_solution

urlpatterns = [
    path('', quiz_list),
    path('', quiz_create),
    path('update/<int:pk>', quiz_winner_update),
    path('solutions/<int:pk>', create_solution),
]