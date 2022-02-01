from django.urls import path
from .views import UserRegistrationAPIView, LoginAPIView

urlpatterns = [
    path('create-user/', UserRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
