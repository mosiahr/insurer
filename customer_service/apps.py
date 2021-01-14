from django.apps import AppConfig


class CustomerServiceConfig(AppConfig):
    name = 'customer_service'

    def ready(self):
        import customer_service.signals
