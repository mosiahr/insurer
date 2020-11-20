from django.urls import path, include


from .views import InsurancePolicyView

app_name = 'customer_service'
urlpatterns = [
    path('policies/', InsurancePolicyView.as_view(), name='policies'),
]