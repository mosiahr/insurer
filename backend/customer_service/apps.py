from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomerServiceConfig(AppConfig):
    name = 'customer_service'
    verbose_name = _('Customer service')

    def ready(self):
        import customer_service.signals
