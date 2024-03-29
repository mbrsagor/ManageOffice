from django.urls import path
from user import views


urlpatterns = [
    path('registration/', views.UserRegistrationAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<pk>/', views.ProfileUpdateAPIView.as_view()),
    path('password-change/<pk>/', views.ChangePasswordView.as_view()),
]
