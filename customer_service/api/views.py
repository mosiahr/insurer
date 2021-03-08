from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import InsurancePolicySerializer, MessageSmsSerializer

from customer_service.models import InsurancePolicy, \
    MessageSmsInsurancePolicyExpires


class InsurancePolicyRetrieveUpdateAPIView(LoginRequiredMixin,
                                           RetrieveUpdateAPIView):
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()


class MessageSmsInsurancePolicyExpiresListCreateAPIView(LoginRequiredMixin,
                                                        ListCreateAPIView):
    serializer_class = MessageSmsSerializer
    queryset = MessageSmsInsurancePolicyExpires.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
