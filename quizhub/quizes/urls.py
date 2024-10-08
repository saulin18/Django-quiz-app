from django.urls import path
from .views import quiz_list, quiz_create, quiz_winner_update

urlpatterns = [
    path('', quiz_list),
    path('create/', quiz_create),
    path('update/<int:pk>/', quiz_winner_update),
]