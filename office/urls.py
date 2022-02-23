from django.urls import path
from rest_framework import routers
from office.views.department_view import DepartmentViewSet
from office.views.designation_view import DesignationViewSet

router = routers.DefaultRouter()

router.register('department', DepartmentViewSet)
router.register('designation', DesignationViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
] + router.urls
