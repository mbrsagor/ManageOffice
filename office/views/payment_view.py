from rest_framework import viewsets, generics, permissions
from django_filters import rest_framework as filters

from office.models import Payment
from office.serializers.payment_serializer import PaymentSerializer
from pagination.default_pagination import StandardResultsSetPagination
from office.filter import PaymentFilter


class PaymentViewSet(viewsets.ModelViewSet):
    """
    Payment CRUD API endpoint
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class PaymentSearchFilterView(generics.ListAPIView):
    """
    Payment filter API endpoint
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = PaymentFilter
    filter_backends = (filters.DjangoFilterBackend,)
