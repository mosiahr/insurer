from django.urls import path, include

from .views import (InsurancePolicyView, InsurancePolicyDetailView,
                    MessageSmsInsurancePolicyExpiresView,
                    MessageSmsInsurancePolicyExpiresDetailView)

app_name = 'customer_service'
urlpatterns = [
    path('policies/', InsurancePolicyView.as_view(), name='policies'),
    path('policies/<int:pk>/',
         InsurancePolicyDetailView.as_view(), name='policy_detail'),
    path('messages/', MessageSmsInsurancePolicyExpiresView.as_view(),
         name='messages'),
]
