from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    """
    The NotificationInterface defines the method that any notification system must implement.
    This allows various ways of notifying participants (such as email, SMS, etc.).
    """

    @abstractmethod
    def notify_participant(self, participant, message):
        """
        Abstract method to notify a participant with a message.
        
        Parameters:
        - participant: The participant object who will receive the notification.
        - message: The message that needs to be sent to the participant.
        
        This method must be implemented by any class that inherits from NotificationInterface.
        It is expected that the inheriting class will define the way the notification is sent 
        (e.g., via email, SMS, etc.).
        """
        pass
