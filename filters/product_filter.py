import django_filters
from django.db.models import Q
from office.models import Project


class ProjectFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_filter', label='Cerca')

    class Meta:
        model = Project
        fields = ['q']

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(sku__iexact=value))
