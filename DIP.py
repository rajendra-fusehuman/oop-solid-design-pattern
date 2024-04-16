from abc import ABC, abstractmethod


class MessageSender:
    @abstractmethod
    def send_message(self, recipient, subject, message):
        pass


class EmailMessageSender(MessageSender):
    def send_message(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")


class TextMessageSender(MessageSender):
    def send_message(self, recipient, subject, message):
        print(f"Sending text to {recipient}: {subject} - {message}")


class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender

    def send_notification(self, recipient, subject, message):
        self.message_sender.send_message(recipient, subject, message)


def main():
    message_sender = EmailMessageSender()
    notification_service = NotificationService(message_sender)
    notification_service.send_notification("user@example.com", "Hello", "this is an email notification!")

    message_sender = TextMessageSender()
    notification_service = NotificationService(message_sender)
    notification_service.send_notification("9841222222", "Hello", "this is a text notification!")

if __name__ == '__main__':
    main()
