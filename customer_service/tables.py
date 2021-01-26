from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import ugettext as _

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires


class InsurancePolicyTable(tables.Table):
    number = tables.LinkColumn('customer-service:policy_detail', args=[A('pk')],
                               attrs={'td': {'class': 'number'}},
                               verbose_name=_('Policy'))
    end_date = tables.DateColumn(attrs={'td': {'class': 'end_date'}})
    customer = tables.Column(attrs={'td': {'class': 'customer'}})
    is_reinsured = tables.Column(attrs={'td': {'class': 'is_reinsured'}})
    is_reinsured_another_company = tables.Column(
        verbose_name=_('Another comp.'),
        attrs={'td': {'class': 'is_reinsured_another_company'}})
    is_impossible_to_call = tables.Column(
        verbose_name=_('Impossible'),
        attrs={'td': {'class': 'is_impossible_to_call'}})
    is_called_will_insure = tables.Column(
        verbose_name=_('Will insure'),
        attrs={'td': {'class': 'is_called_will_insure'}})
    is_called_will_not_insure = tables.Column(
        verbose_name=_('Will not insure'),
        attrs={'td': {'class': 'is_called_will_not_insure'}})
    send_sms = tables.TemplateColumn(
        verbose_name=_('Send SMS'),
        template_code=f"<button type='button' class='btn btn-outline-primary btn-sm send_sms '>{_('Send SMS')}</button>",
        orderable=False)  # orderable not sortable

    class Meta:
        attrs = {'class': 'table table-hover table-sm'}
        model = InsurancePolicy
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'number', 'end_date', 'customer', 'car', 'price',
                  'is_reinsured', 'is_reinsured_another_company',
                  'is_impossible_to_call', 'is_called_will_insure',
                  'is_called_will_not_insure')

        row_attrs = {
            'data-id': lambda record: record.pk,
            'data-url': lambda record: reverse(
                'api-customer-service:api-insurance-policy-update',
                kwargs={'pk': record.pk}),
        }
        order_by = ('end_date',)


    def render_price(self, value):
        return value

    def render_territory(self, value):
        return str(value)[:15]

    def result_after_the_call(self, value, yes='✔', no='❌'):
        """ Result after the call to the customer """
        return format_html('<a href="#"><span class={}>{}</span></a>',
                           str(value).casefold(), yes if value else no)

    def render_is_reinsured(self, value):
        return self.result_after_the_call(value)

    def render_is_reinsured_another_company(self, value):
        return self.result_after_the_call(value)

    def render_is_impossible_to_call(self, value):
        return self.result_after_the_call(value)

    def render_is_called_will_insure(self, value):
        return self.result_after_the_call(value)

    def render_is_called_will_not_insure(self, value):
        return self.result_after_the_call(value)


class MessageSmsInsurancePolicyExpiresTable(tables.Table):
    created = tables.DateColumn(verbose_name=_('Sent'))
    body = tables.Column(verbose_name=_('SMS text'))

    class Meta:
        attrs = {'class': 'table table-hover table-sm'}
        model = MessageSmsInsurancePolicyExpires
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'created', 'sid', 'insurance_policy', 'body')
        order_by = ('-id',)
