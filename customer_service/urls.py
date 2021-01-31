from django.urls import path


from .views import (InsurancePolicyView, InsurancePolicyDetailView,
                    MessageSmsInsurancePolicyExpiresView)

app_name = 'customer_service'
urlpatterns = [
    path('policies/', InsurancePolicyView.as_view(), name='policies'),
    path('policies/<int:pk>/',
         InsurancePolicyDetailView.as_view(), name='policy_detail'),
    path('messages/', MessageSmsInsurancePolicyExpiresView.as_view(),
         name='messages'),
]
