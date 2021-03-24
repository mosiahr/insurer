import logging

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

logger = logging.getLogger(__name__)


class CreateMessage:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def create(self, to, from_, body_message):
        try:
            message = self.client.messages.create(
                from_=from_,
                to=to,
                body=body_message)
            return message.sid
        except TwilioRestException as e:
            logger.error(e)
