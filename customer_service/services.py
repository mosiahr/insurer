from twilio.rest import Client


class CreateMessage:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def create(self, to, from_, body_message):
        message = self.client.messages.create(
            from_=from_,
            to=to,
            body=body_message)
        print(message.sid)
