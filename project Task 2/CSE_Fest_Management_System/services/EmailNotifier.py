from interfaces.notification_Interface import NotificationInterface

# EmailNotifier is a concrete implementation of the NotificationInterface.
# This class follows the Interface Segregation Principle (ISP) by providing 
# a specific method (notify_participant) for sending notifications, in this 
# case via email, instead of a general-purpose notification method.

class EmailNotifier(NotificationInterface):
    # Implements the 'notify_participant' method from NotificationInterface.
    def notify_participant(self, participant, message):
        # Sends a notification to the participant via email.
        print(f"Email to {participant.name}: {message}")
