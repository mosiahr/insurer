from django.views.generic.detail import DetailView
from django.urls import reverse

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import InsurancePolicy
from .tables import InsurancePolicyTable
from .forms import InsurancePolicyForm
from .filters import InsurancePolicyFilter


class InsurancePolicyView(SingleTableMixin, FilterView):
    form_class = InsurancePolicyForm
    model = InsurancePolicy
    table_class = InsurancePolicyTable
    template_name = 'customer_service/policies.html'
    context_object_name = 'policies'
    filterset_class = InsurancePolicyFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_sms_url = reverse('api-customer-service:api-message-sms-create')
        context.update({'message_sms_url': message_sms_url})
        return context


class InsurancePolicyDetailView(DetailView):
    model = InsurancePolicy
    template_name = 'customer_service/policy_detail.html'
    context_object_name = 'policy'
