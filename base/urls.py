from rest_framework import routers
from base.views.office_view import OfficeViewSet

router = routers.DefaultRouter()

router.register('office', OfficeViewSet)

urlpatterns = router.urls
