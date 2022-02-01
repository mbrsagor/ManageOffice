from django.urls import path
from .views import UserRegistrationAPIView

urlpatterns = [
    path('create-user/', UserRegistrationAPIView.as_view()),
]
