from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from django_tables2 import SingleTableView

from .models import InsurancePolicy
from .tables import InsurancePolicyTable
from .forms import InsurancePolicyForm


class InsurancePolicyView(SingleTableView):
    form_class = InsurancePolicyForm
    model = InsurancePolicy
    table_class = InsurancePolicyTable
    template_name = 'customer_service/polices.html'
    context_object_name = 'polices'
