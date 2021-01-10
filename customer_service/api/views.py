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
        # message = CreateMessage(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
        # sid = message.create(from_=FROM_, to=TO, body_message=request.data['body'])
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        # request.data.update({'sid': sid})
        request.data.update({'sid': 'asdfasdfasdfasdfadfasdf'})
        return self.create(request, *args, **kwargs)
