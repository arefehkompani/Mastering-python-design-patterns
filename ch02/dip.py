from typing import Protocol

class MessageSender(Protocol):
    def send(self, message: str):
        ...

class Email:
    def send(self, message: str):
        print(f"The content of email: {message}")

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender
    
    def send(self, message: str):
        self.sender.send(message)

if __name__ == "__main__":
    email = Email()
    notif = Notification(sender=email)
    notif.send("I saw your email.")