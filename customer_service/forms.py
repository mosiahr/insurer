from django import forms

from insurer.settings import DATE_INPUT_FORMATS
from .models import InsurancePolicy


class InsurancePolicyForm(forms.ModelForm):
    registration_date = forms.DateField(input_formats=DATE_INPUT_FORMATS)

    class Meta:
        model = InsurancePolicy
        fields = ('number', 'sticker', 'registration_date',
                    'begin_date', 'end_date',
                    'car', 'insurance_code', 'sum_insured', 'price',
                    'bonus', 'territory')