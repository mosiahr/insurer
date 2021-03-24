import os

from django.db.models.signals import pre_save
from django.dispatch import receiver

from customer_service.models import MessageSmsInsurancePolicyExpires
from customer_service.services import CreateMessage
from insurer.conf import TO, FROM_
from insurer.settings import SEND_SMS_MESSAGE


@receiver(pre_save, sender=MessageSmsInsurancePolicyExpires)
def pre_save_sms_message(sender, instance, **kwargs):
    """
    Receiver which will be connected to this signal.
    """
    message = CreateMessage(account_sid=os.environ.get('ACCOUNT_SID'),
                            auth_token=os.environ.get('AUTH_TOKEN'))

    if SEND_SMS_MESSAGE:
        instance.sid = message.create(from_=FROM_, to=TO,
                                      body_message=instance.body)
