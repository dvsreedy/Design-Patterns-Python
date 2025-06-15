from abc import ABC, abstractmethod

class NotificationFactory(ABC):


    @abstractmethod
    def create_email_notification(self):
        pass
    
    @abstractmethod
    def create_sms_notification(self):
        pass    

    @abstractmethod
    def push_nofication(self):
        pass

class AmazonNotificationFactory(NotificationFactory):

    def create_email_notification(self):
        return AmazonEmailNotification()

    def create_sms_notification(self):
        return AmazonSMSNotification()

    def push_nofication(self):
        return AmazonPushNotification()
    
class GoogleNotificationFactory(NotificationFactory):
    def create_email_notification(self):
        return GoogleEmailNotification()

    def create_sms_notification(self):
        return GoogleSMSNotification()

    def push_nofication(self):
        return GooglePushNotification()


class AbstractEmailNotification(ABC):
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def formated(self):
        pass


class AbstractSMSNotification(ABC):
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def formated(self):
        pass

class AbstractPushNotification(ABC):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def formated(self):
        pass

class AmazonEmailNotification(AbstractEmailNotification):
    def send(self):
        return "Amazon Email Notification Sent"

    def formated(self):
        return "Amazon Email Notification Formatted"

class AmazonSMSNotification(AbstractSMSNotification):
    def send(self):
        return "Amazon SMS Notification Sent"
    def formated(self):
        return "Amazon SMS Notification Formatted"


class AmazonPushNotification(AbstractPushNotification):
    def send(self):
        return "Amazon Push Notification Sent"

    def formated(self):
        return "Amazon Push Notification Formatted"

class GoogleEmailNotification(AbstractEmailNotification):
    def send(self):
        return "Google Email Notification Sent"
    def formated(self):
        return "Google Email Notification Formatted"
    

class GoogleSMSNotification(AbstractSMSNotification):
    def send(self):
        return "Google SMS Notification Sent"
    def formated(self):
        return "Google SMS Notification Formatted"
    
class GooglePushNotification(AbstractPushNotification):
    def send(self):
        return "Google Push Notification Sent"

    def formated(self):
        return "Google Push Notification Formatted"


def send_notification(factory: NotificationFactory):
    email = factory.create_email_notification()
    sms = factory.create_sms_notification()
    push = factory.push_nofication()

    print(email.send())
    print(email.formated())
    print(sms.send())
    print(sms.formated())
    print(push.send())
    print(push.formated())

factory_mapping = {
     "Amazon": AmazonNotificationFactory(),
     "Google":  GoogleNotificationFactory(),
}


def send_notification_by_factory(factory_type: str) -> NotificationFactory:
    factory_instance = factory_mapping[factory_type]
    print(f"Sending notifications using {factory_instance} Factory:")
    # factory_instance = factory_class()  # Create an instance of the factory class
    send_notification(factory_instance)

if __name__ == "__main__":
    provider = input("Enter the provider (Amazon or Google): ")
    notification_factory = send_notification_by_factory(provider)
    # send_notification(notification_factory)

