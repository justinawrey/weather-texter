from twilio.rest import Client

class Twilio:
    def __init__(self):
        self.api_key = ""
        self.acc_sid = ""
        self.recipients = []

    def set_acc_sid(self, sid):
        self.acc_sid = sid
    
    def set_api_key(self, key):
        self.api_key = key
    
    def register_recipient(self, phone_number):
        self.recipients.append(phone_number)
    
    def send_data(self, data):
        client = Client(self.acc_sid, self.api_key)
        for recipient in self.recipients:
            client.messages.create(
                to=recipient, 
                from_="+17788607371",
                body=data
            )
