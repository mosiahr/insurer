from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires
from .tables import InsurancePolicyTable, MessageSmsInsurancePolicyExpiresTable
from .filters import InsurancePolicyFilter, \
    MessageSmsInsurancePolicyExpiresFilter


class InsurancePolicyView(LoginRequiredMixin, SingleTableMixin, FilterView):
    """
    Render list of insurance polices. The view has the ability to edit the
    result after calling the customer. Also, the view allows use Django Rest
    Framework and Twilio.com for send SMS messages to customers to notify them
    that insurance policy is ending.
    """
    model = InsurancePolicy
    table_class = InsurancePolicyTable
    template_name = 'customer_service/policies.html'
    context_object_name = 'policies'
    filterset_class = InsurancePolicyFilter


class InsurancePolicyDetailView(LoginRequiredMixin, DetailView):
    """
    Render a "detail" view of an insurance policy. The view includes:
        - policy information;
        - customer information;
        - car information;
        - sms messages those were sent to customer to notify them that insurance
          policy is ending.
    The view has the ability to edit the result after colling the customer.
    """
    model = InsurancePolicy
    template_name = 'customer_service/policy_detail.html'
    context_object_name = 'policy'

    def get_context_data(self, **kwargs):
        context = super(InsurancePolicyDetailView, self).get_context_data()
        insurance_policy = self.get_object()
        if insurance_policy:
            context.update(
                {
                    'sms_messages': MessageSmsInsurancePolicyExpires.objects.filter(
                        insurance_policy=insurance_policy.id)})
        return context


class MessageSmsInsurancePolicyExpiresView(LoginRequiredMixin, SingleTableMixin,
                                           FilterView):
    """
    Render list of sms messages those were sent to customers to notify them that
    insurance policy is ending.
    """
    model = MessageSmsInsurancePolicyExpires
    table_class = MessageSmsInsurancePolicyExpiresTable
    template_name = 'customer_service/message_sms_policy_expire_list.html'
    context_object_name = 'sms_messages'
    filterset_class = MessageSmsInsurancePolicyExpiresFilter


class MessageSmsInsurancePolicyExpiresDetailView(LoginRequiredMixin,
                                                 DetailView):
    model = MessageSmsInsurancePolicyExpires
    template_name = 'customer_service/message_sms_policy_expire_datail.html'
    context_object_name = 'message'
