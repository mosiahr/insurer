from django.http import QueryDict
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InsurancePolicySerializer, MessageSmsSerializer

from customer_service.models import InsurancePolicy, \
    MessageSmsInsurancePolicyExpires
from customer_service.services import CreateMessage
from insurer.conf import ACCOUNT_SID, AUTH_TOKEN, TO, FROM_


class InsurancePolicyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()

    # def get(self, request, *args, **kwargs):
    #     print('get')
    #     print(request.data)
    #     print(self.get_object())
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     print('PUT')
    #     print(request.data)
    #     return self.update(request, *args, **kwargs)


class MessageSmsInsurancePolicyExpiresListCreateAPIView(ListCreateAPIView):
    serializer_class = MessageSmsSerializer
    queryset = MessageSmsInsurancePolicyExpires.objects.all()

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        insurance_policy = InsurancePolicy.objects.get(
            pk=request.data['insurance_policy'])

        try:
            customer = insurance_policy.customer
        except:
            customer = None

        body_message = f'{customer.name}, your policy {insurance_policy.number} expires on {insurance_policy.end_date}'
        message = CreateMessage(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
        sid = message.create(from_=FROM_, to=TO, body_message=body_message)

        request.data.update({'sid': sid,
                             'body': body_message})
        print(request.data)
        return self.create(request, *args, **kwargs)
