from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserRegistrationAPIView

urlpatterns = [
    path('create-user/', UserRegistrationAPIView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),
]
