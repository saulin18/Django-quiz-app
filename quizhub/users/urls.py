from django.urls import  path
from .views import RegisterView, MyTokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', MyTokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]