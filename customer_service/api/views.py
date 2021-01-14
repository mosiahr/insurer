from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from .serializers import InsurancePolicySerializer, MessageSmsSerializer

from customer_service.models import InsurancePolicy, \
    MessageSmsInsurancePolicyExpires


class InsurancePolicyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()


class MessageSmsInsurancePolicyExpiresListCreateAPIView(ListCreateAPIView):
    serializer_class = MessageSmsSerializer
    queryset = MessageSmsInsurancePolicyExpires.objects.all()
