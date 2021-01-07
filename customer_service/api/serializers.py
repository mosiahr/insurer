from rest_framework import serializers

from customer_service.models import InsurancePolicy, \
    MessageSmsInsurancePolicyExpires


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = ('is_reinsured', 'is_reinsured_another_company',
                  'is_impossible_to_call', 'is_called_will_insure',
                  'is_called_will_not_insure')


class MessageSmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSmsInsurancePolicyExpires
        fields = ('sid', 'body', 'from_phone_number', 'to_phone_number',
                  'customer', 'car', 'insurance_policy')
