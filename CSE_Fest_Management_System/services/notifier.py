from interfaces.notification_Interface import NotificationInterface

class Notifier(NotificationInterface):
    """
    The Notifier class is responsible for sending notifications to participants.
    It implements the NotificationInterface to ensure a standardized notify_participant method.
    """

    def notify_participant(self, participant, message):
        """
        Sends a notification to a specified participant.
        
        Parameters:
        - participant: The participant to be notified. It is expected to have a 'name' attribute.
        - message: The notification message to be sent.
        
        This method prints a message to simulate sending a notification.
        """
        print(f"Notification to {participant.name}: {message}")  # Simulate sending a notification to the participant
