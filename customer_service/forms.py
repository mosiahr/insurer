from django import forms

from .models import InsurancePolicy, MessageSmsInsurancePolicyExpires


# class InsurancePolicyForm(forms.ModelForm):
#     class Meta:
#         model = InsurancePolicy
#         fields = ('number', 'sticker', 'registration_date',
#                   'begin_date', 'end_date',
#                   'car', 'insurance_code', 'sum_insured', 'price',
#                   'bonus', 'territory')
#
#
# class MessageSmsInsurancePolicyExpiresForm(forms.ModelForm):
#     class Meta:
#         model = MessageSmsInsurancePolicyExpires
#         fields = ('created', 'sid', 'body', 'insurance_policy')
