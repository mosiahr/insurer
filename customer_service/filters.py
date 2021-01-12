from django.db import models

import django_filters
from django_filters.widgets import DateRangeWidget
from bootstrap_datepicker_plus import DatePickerInput

from insurer.settings import DATE_INPUT_FORMAT
from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires


class InsurancePolicyFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name='customer',
                                         method='filter_customer')

    car = django_filters.CharFilter(field_name='car',
                                    method='filter_car')

    end_date = django_filters.DateFromToRangeFilter(
        widget=DateRangeWidget(attrs={'type': 'date'})
    )

    def filter_customer(self, queryset, name, value):
        return queryset.filter(customer__name__icontains=value)

    def filter_car(self, queryset, name, value):
        return queryset.filter(car__registration_number__icontains=value)

    class Meta:
        model = InsurancePolicy
        fields = ['number', 'registration_date', 'begin_date', 'end_date',
                  'customer', 'car', 'insurance_code']

        filter_overrides = {
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': DatePickerInput(format=DATE_INPUT_FORMAT),
                },
            },
        }


class MessageSmsInsurancePolicyExpiresFilter(django_filters.FilterSet):
    insurance_policy = django_filters.CharFilter(field_name='insurance_policy',
                                                 method='filter_insurance_policy')

    created = django_filters.DateFromToRangeFilter(
        widget=DateRangeWidget(attrs={'type': 'date'})
    )

    class Meta:
        model = MessageSmsInsurancePolicyExpires
        fields = ['created', 'sid', 'body', 'insurance_policy']

    def filter_insurance_policy(self, queryset, name, value):
        return queryset.filter(insurance_policy__number__icontains=value)
