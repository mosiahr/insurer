from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import InsurancePolicySerializer

from customer_service.models import InsurancePolicy


class InsurancePolicyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()


