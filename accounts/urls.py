from django.urls import path
from .views import UserRegistrationAPIView, LoginAPIView, ProfileAPIView

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]
