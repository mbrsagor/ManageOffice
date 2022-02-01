from django.urls import path
from .views import UserRegistrationAPIView, LoginAPIView

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
