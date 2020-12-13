from django.views import View
from django.views.generic.detail import SingleObjectMixin, \
    SingleObjectTemplateResponseMixin, DetailView

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

    # def get_context_data(self, **kwargs):
    #     return super(InsurancePolicyView, self).get_context_data(**kwargs)


class InsurancePolicyDetailView(DetailView):
    model = InsurancePolicy
    template_name = 'customer_service/policy_detail.html'
    context_object_name = 'policy'

