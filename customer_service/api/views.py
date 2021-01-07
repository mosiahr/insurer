from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView, \
    CreateAPIView, ListCreateAPIView

from .serializers import InsurancePolicySerializer, MessageSmsSerializer

from customer_service.models import InsurancePolicy, MessageSmsInsurancePolicyExpires
from customer_service.services import CreateMessage
from insurer.conf import ACCOUNT_SID, AUTH_TOKEN, TO, FROM_


class InsurancePolicyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()

    def get(self, request, *args, **kwargs):
        print('get')
        print(request.data)
        print(self.get_object())
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print('PUT')
        print(request.data)

        instance = self.get_object()
        body_message = f'Your policy expires on {instance.end_date}'
        print(body_message)
        # message = CreateMessage(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
        # message.create(from_=FROM_, to=TO, body_message=body_message)

        # return
        return self.update(request, *args, **kwargs)


# class InsurancePolicyUpdateAPIView(UpdateAPIView):
#     ''' Concrete view for updating a model instance. '''
#     serializer_class = InsurancePolicySerializer
#     queryset = InsurancePolicy.objects.all()
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# class MessageSmsCreateAPIView(CreateAPIView):
#     serializer_class = MessageSmsSerializer
#     queryset = MessageSms.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         print(request)
#         # instance = self.get_object()
#         # body_message = f'Your policy expires on {instance.end_date}'
#         # print(body_message)
#         # message = CreateMessage(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
#         # message.create(from_=FROM_, to=TO, body_message=body_message)
#         return self.create(request, *args, **kwargs)


class MessageSmsInsurancePolicyExpiresListCreateAPIView(ListCreateAPIView):
    serializer_class = MessageSmsSerializer
    queryset = MessageSmsInsurancePolicyExpires.objects.all()

    def post(self, request, *args, **kwargs):
        print(request)
        # instance = self.get_object()
        # body_message = f'Your policy expires on {instance.end_date}'
        # print(body_message)
        # message = CreateMessage(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
        # message.create(from_=FROM_, to=TO, body_message=body_message)
        return self.create(request, *args, **kwargs)