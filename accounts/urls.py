from django.urls import path

from .views import UserRegistrationAPIView, LoginAPIView, ProfileAPIView, ChangePasswordAPI

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('change-password/<pk>/', ChangePasswordAPI.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]
