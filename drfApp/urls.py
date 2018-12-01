from django.urls import path
from django.views.generic import TemplateView
from .views import CategoryAPIView, DeleteCategory

urlpatterns = [
     path('', TemplateView.as_view(template_name='index.html'), name='view-data'),
     path('api/category/', CategoryAPIView.as_view(), name='category'),
     path('api/category/<int:pk>', DeleteCategory.as_view()),
]
