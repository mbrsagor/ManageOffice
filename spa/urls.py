from django.contrib import admin
from django.urls import path, include

from drfApp.views import PostViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('post',PostViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('drfApp.urls')),
]
