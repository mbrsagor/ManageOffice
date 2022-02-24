from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from office.models import Department, Designation, Bank, Payment
from utils.employee_info import Pay


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


class PaymentFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(field_name='user', queryset=User.objects.all())
    bank_name = filters.ModelChoiceFilter(field_name='bank_name', queryset=Bank.objects.all())
    pay_purpose = filters.ChoiceFilter(field_name='pay_purpose', choices=Pay.payment_types())
    amount = filters.NumberFilter(field_name='amount')

    class Meta:
        model = Payment
        fields = ['user', 'bank_name', 'pay_purpose', 'amount']
