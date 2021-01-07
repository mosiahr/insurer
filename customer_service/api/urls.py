from django.urls import path

# from .views import InsurancePolicyView, InsurancePolicyDetailView
from .views import InsurancePolicyRetrieveUpdateAPIView, \
    MessageSmsInsurancePolicyExpiresListCreateAPIView

app_name = 'customer_service'

urlpatterns = [
    path('policies/<int:pk>/', InsurancePolicyRetrieveUpdateAPIView.as_view(),
         name='api-insurance-policy-update'),
    path('policies/message/sms/create/',
         MessageSmsInsurancePolicyExpiresListCreateAPIView.as_view(),
         name='api-message-sms-create'),
]
