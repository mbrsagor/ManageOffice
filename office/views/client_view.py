from rest_framework import viewsets, generics, permissions
from django_filters import rest_framework as filters

from office.models import Client
from office.serializers.client_serializer import ClientSerializer
from pagination.default_pagination import StandardResultsSetPagination


class ClientFilter(filters.FilterSet):
    """
    Client filter class
    """

    name = filters.CharFilter(field_name='name')
    phn_num = filters.CharFilter(field_name='phn_num')
    email = filters.CharFilter(field_name='email')

    class Meta:
        model = Client
        fields = ['name', 'phn_num', 'email']


class ClientViewSet(viewsets.ModelViewSet):
    """
    Create user. The client only can create by superuser
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class ClientFilterView(generics.ListAPIView):
    """
    List of client by search filter
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter
