from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


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
            print(e)
