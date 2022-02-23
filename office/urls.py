from django.urls import path
from rest_framework import routers
from office.views.department_view import DepartmentViewSet

router = routers.DefaultRouter()

router.register('department', DepartmentViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
] + router.urls
