from django.urls import  path
from .views import register, MyTokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('auth/register/', register),
    path('auth/login/', MyTokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]