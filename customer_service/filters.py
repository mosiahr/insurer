import django_filters

from .models import InsurancePolicy


class InsurancePolicyFilter(django_filters.FilterSet):
    class Meta:
        model = InsurancePolicy
        fields = ['number', 'registration_date', 'begin_date', 'end_date',
                  'insurance_code']

