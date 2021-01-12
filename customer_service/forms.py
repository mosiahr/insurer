from django import forms

from insurer.settings import DATE_INPUT_FORMAT, DATE_TIME_INPUT_FORMAT
from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires


class InsurancePolicyForm(forms.ModelForm):
    registration_date = forms.DateField(input_formats=DATE_INPUT_FORMAT)

    class Meta:
        model = InsurancePolicy
        fields = ('number', 'sticker', 'registration_date',
                  'begin_date', 'end_date',
                  'car', 'insurance_code', 'sum_insured', 'price',
                  'bonus', 'territory')


class MessageSmsInsurancePolicyExpiresForm(forms.ModelForm):
    created = forms.DateTimeField(input_formats=DATE_TIME_INPUT_FORMAT)

    class Meta:
        model = MessageSmsInsurancePolicyExpires
        fields = ('created', 'sid', 'body', 'insurance_policy')
