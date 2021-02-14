from rest_framework import serializers
from django.utils.translation import ugettext as _

from customer_service.models import InsurancePolicy, \
    MessageSmsInsurancePolicyExpires
from insurer.conf import MESSAGE_FOOTER, MANAGER_PHONE


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = ('is_reinsured', 'is_reinsured_another_company',
                  'is_impossible_to_call', 'is_called_will_insure',
                  'is_called_will_not_insure')


class MessageSmsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['body'] += ('.\n' + _('Info') + ': ' + MANAGER_PHONE + '\n' + MESSAGE_FOOTER)
        return super(MessageSmsSerializer, self).create(validated_data)

    class Meta:
        model = MessageSmsInsurancePolicyExpires
        fields = ('sid', 'body', 'from_phone_number', 'to_phone_number',
                  'insurance_policy')
