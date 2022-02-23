from django_filters import rest_framework as filters

from office.models import Department, Designation, Bank


class DepartmentFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Department
        fields = ['name', 'is_active']


class DesignationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Designation
        fields = ['name', 'is_active']


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Bank
        fields = ['name', 'is_active']
