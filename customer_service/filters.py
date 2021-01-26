from datetime import datetime

from django.utils.translation import ugettext as _
from django.forms.widgets import TextInput

import django_filters
from bootstrap_datepicker_plus import DatePickerInput

from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires
from insurer.settings import DATE_INPUT_FORMAT_UA


class BaseFilter(django_filters.FilterSet):
    insurance_policy = django_filters.CharFilter(
        label=_('Number insurance policy'),
        method='filter_insurance_policy',
        widget=TextInput(
            attrs={'placeholder': 'AM-0000000', 'autocomplete': 'off'})
    )

    date_after = django_filters.DateFilter(
        label=_('Date from'),
        method='filter_date_after',
        widget=DatePickerInput(
            format=DATE_INPUT_FORMAT_UA,
            attrs={'placeholder': _('Date from'), 'autocomplete': 'off'}),
    )

    date_before = django_filters.DateFilter(
        label=_('Date to'),
        method='filter_date_before',
        widget=DatePickerInput(
            format=DATE_INPUT_FORMAT_UA,
            attrs={'placeholder': _('Date to'), 'autocomplete': 'off'})
    )

    @classmethod
    def filter_for_field(cls, field, field_name, lookup_expr=None):
        _filter = super(BaseFilter, cls).filter_for_field(field, field_name,
                                                         lookup_expr)
        _filter.field.widget.attrs.update({'autocomplete': 'off'})
        return _filter


class InsurancePolicyFilter(BaseFilter):
    customer = django_filters.CharFilter(
        method='filter_customer',
        widget=TextInput(
            attrs={'placeholder': _('Customer'), 'autocomplete': 'off'}))

    car = django_filters.CharFilter(
        method='filter_car',
        widget=TextInput(attrs={'placeholder': _('Number of the car'),
                                'autocomplete': 'off'}))

    class Meta:
        model = InsurancePolicy
        fields = ['id', 'insurance_policy', 'date_after', 'date_before',
                  'customer', 'car']

    def filter_insurance_policy(self, queryset, name, value):
        """
        Filter by number of insurance policy.
        __icontains: Case-insensitive containment test.
        """
        return queryset.filter(number__icontains=value)

    def filter_customer(self, queryset, name, value):
        """
        Filter by customer name.
        __icontains: Case-insensitive containment test.
        """
        return queryset.filter(customer__name__icontains=value)

    def filter_car(self, queryset, name, value):
        """
        Filter by car number.
        __icontains: Case-insensitive containment test.
        """
        return queryset.filter(car__registration_number__icontains=value)

    def filter_date_after(self, queryset, name, value):
        """
        __gte: Greater than or equal to.
        """
        return queryset.filter(end_date__gte=value)

    def filter_date_before(self, queryset, name, value):
        """
        __lte: Less than or equal to.
        """
        return queryset.filter(end_date__lte=value)


class MessageSmsInsurancePolicyExpiresFilter(BaseFilter):
    class Meta:
        model = MessageSmsInsurancePolicyExpires
        fields = ['id', 'date_after', 'date_before', 'sid', 'insurance_policy']

    def filter_insurance_policy(self, queryset, name, value):
        """
        __icontains: Case-insensitive containment test.
        """
        return queryset.filter(insurance_policy__number__icontains=value)

    def filter_date_after(self, queryset, name, value):
        """
        __gte: Greater than or equal to.
        """
        return queryset.filter(created__gte=value)

    def filter_date_before(self, queryset, name, value):
        """
        __lte: Less than or equal to.
        """
        return queryset.filter(created__lte=value)
