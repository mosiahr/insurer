from django.urls import path, include


from .views import InsurancePolicyView

urlpatterns = [
    path('polices/', InsurancePolicyView.as_view(), name='polices'),
]