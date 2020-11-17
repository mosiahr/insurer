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
    template_name = 'customer_service/polices.html'
    context_object_name = 'polices'

    filterset_class = InsurancePolicyFilter
