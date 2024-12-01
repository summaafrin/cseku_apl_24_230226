from abc import ABC, abstractmethod

# Interface for notification services
# Following the Interface Segregation Principle (ISP): 
# This interface ensures that any class implementing it only handles notifications, 
# providing a clear and specific contract for notification-related functionality.
class NotificationInterface(ABC):
    @abstractmethod
    def notify_participant(self, participant, message):
        """
        Sends a notification to a participant with the specified message.
        Classes implementing this interface must define this method.
        """
        pass
