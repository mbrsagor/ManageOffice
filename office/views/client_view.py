from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from office.models import Client
from office.serializers.client_serializer import ClientSerializer
from office.pagination import StandardResultsSetPagination


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    phn_num = filters.CharFilter(field_name='phn_num')
    email = filters.CharFilter(field_name='email')

    class Meta:
        model = Client
        fields = ['name', 'phn_num', 'email']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
