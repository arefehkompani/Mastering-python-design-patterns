# Here MessageService is loosly coupled with EmailSender and SMSSender through dependency injection

class MessageService:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message: str):
        self.sender.send(message)

class EmailSender:
    def send(self, message):
        print("Email Message: ", message)

class SMSSender:
    def send(self, message):
        print(f"SMS Message: {message}")

if __name__ == "__main__":
    email_message = MessageService(EmailSender())
    email_message.send_message("Hello via Email")

    sms_message = MessageService(SMSSender())
    sms_message.send_message("Hello via sms")