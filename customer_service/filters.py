import django_filters

from .models import InsurancePolicy, Customer


class InsurancePolicyFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name='customer',
                                         method='filter_customer')

    car = django_filters.CharFilter(field_name='car',
                                    method='filter_car')

    def filter_customer(self, queryset, name, value):
        return queryset.filter(customer__name__icontains=value)

    def filter_car(self, queryset, name, value):
        return queryset.filter(car__registration_number__icontains=value)

    class Meta:
        model = InsurancePolicy
        fields = ['number', 'registration_date', 'begin_date', 'end_date',
                  'customer', 'car', 'insurance_code']
