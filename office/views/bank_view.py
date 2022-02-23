from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from office.models import Bank
from office.serializers.bank_serailizer import BankSerializer
from office.pagination import StandardResultsSetPagination
from office.filter import BankFilter


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = BankFilter
    filter_backends = (filters.DjangoFilterBackend,)

    # API URL: /api/v1/bank/
    """
        {
            "name": "Bank Name",
            "is_active": true
        }
    """
