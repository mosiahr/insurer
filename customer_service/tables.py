import django_tables2 as tables
from django.utils.html import format_html

from .models import InsurancePolicy


class InsurancePolicyTable(tables.Table):
    class Meta:
        model = InsurancePolicy
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'number', 'registration_date', 'begin_date', 'end_date',
                  'car', 'insurance_code', 'price', 'territory')

    def render_price(self, value):
        return f'{value} грн.'
