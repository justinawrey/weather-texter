class Twilio:
    def __init__(self):
        self.api_key = ""
        self.recipients = []
    
    def set_api_key(self, key):
        self.api_key = key

    def register_recipient(self, phone_number):
        self.recipients.append(phone_number)
    
    def send_data(self, data):
        pass
