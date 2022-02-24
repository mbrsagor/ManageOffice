from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from office.models import Payment
from office.serializers.payment_serializer import PaymentSerializer
from office.pagination import StandardResultsSetPagination
from office.filter import PaymentFilter


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = PaymentFilter
    filter_backends = (filters.DjangoFilterBackend,)
