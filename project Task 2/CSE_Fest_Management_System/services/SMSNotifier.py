from interfaces.notification_Interface import NotificationInterface

# SMSNotifier class implements the NotificationInterface
# This adheres to the Interface Segregation Principle (ISP) because it implements only the methods relevant to SMS notifications
class SMSNotifier(NotificationInterface):
    def notify_participant(self, participant, message):
        # The method sends an SMS notification to the participant
        # This implements the notify_participant method from the NotificationInterface
        print(f"SMS to {participant.name}: {message}")
